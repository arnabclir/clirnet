# Course Completion Reminder System - Implementation Plan

## Executive Summary

This document outlines a targeted implementation plan for automated course completion reminders. The system identifies users with incomplete courses and sends timely reminders via email (weekly) and SMS (monthly maximum) with unsubscribe options and comprehensive visibility tracking.

---

## System Overview

### Core Concept
Monitor `user_activities` table to identify users who:
1. Viewed a course page 3 days ago
2. Have NOT viewed it today
3. Have NOT completed the course

These users are enrolled in a reminder sequence with configurable frequency and unsubscribe options.

### Key Requirements
- **Email reminders**: Weekly frequency
- **SMS reminders**: Maximum once per month
- **Unsubscribe option**: Per-course opt-out in every email
- **Visibility**: Real-time dashboard for monitoring performance
- **Trigger point**: 3-day inactivity threshold

---

## Database Schema Design

### New Table: `content_notifications`

```sql
CREATE TABLE content_notifications (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id INT NOT NULL,
    course_id INT NOT NULL,
    
    -- Status tracking
    status VARCHAR(20) DEFAULT 'active', -- 'active', 'completed', 'unsubscribed', 'paused'
    stage INT DEFAULT 1, -- Current reminder stage (1-5)
    
    -- Timing metadata
    first_detected_at TIMESTAMP DEFAULT NOW(),
    last_reminder_sent_at TIMESTAMP,
    next_reminder_due_at TIMESTAMP,
    
    -- Channel tracking
    email_count INT DEFAULT 0,
    sms_count INT DEFAULT 0,
    last_email_sent_at TIMESTAMP,
    last_sms_sent_at TIMESTAMP,
    
    -- Course progress snapshot
    completion_percentage DECIMAL(5,2) DEFAULT 0.00,
    modules_completed INT DEFAULT 0,
    total_modules INT,
    last_activity_at TIMESTAMP,
    
    -- Metadata
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW(),
    completed_at TIMESTAMP,
    unsubscribed_at TIMESTAMP,
    
    -- Constraints
    UNIQUE(user_id, course_id),
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (course_id) REFERENCES courses(id)
);

-- Indexes for performance
CREATE INDEX idx_content_notif_user ON content_notifications(user_id);
CREATE INDEX idx_content_notif_course ON content_notifications(course_id);
CREATE INDEX idx_content_notif_status ON content_notifications(status);
CREATE INDEX idx_content_notif_next_due ON content_notifications(next_reminder_due_at) 
    WHERE status = 'active';
CREATE INDEX idx_content_notif_stage ON content_notifications(stage, status);
```

### Supporting Table: `course_reminder_logs`

```sql
CREATE TABLE course_reminder_logs (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    notification_id UUID NOT NULL,
    user_id INT NOT NULL,
    course_id INT NOT NULL,
    
    -- Message details
    channel VARCHAR(20) NOT NULL, -- 'email' or 'sms'
    stage INT NOT NULL,
    template_used VARCHAR(100),
    
    -- Delivery tracking
    scheduled_at TIMESTAMP NOT NULL,
    sent_at TIMESTAMP,
    delivered_at TIMESTAMP,
    opened_at TIMESTAMP,
    clicked_at TIMESTAMP,
    
    -- Status
    status VARCHAR(20) DEFAULT 'scheduled', -- 'scheduled', 'sent', 'delivered', 'failed', 'opened', 'clicked'
    error_message TEXT,
    provider_message_id VARCHAR(255),
    
    -- Metadata
    created_at TIMESTAMP DEFAULT NOW(),
    
    FOREIGN KEY (notification_id) REFERENCES content_notifications(id),
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (course_id) REFERENCES courses(id)
);

-- Indexes
CREATE INDEX idx_reminder_logs_notification ON course_reminder_logs(notification_id);
CREATE INDEX idx_reminder_logs_user ON course_reminder_logs(user_id);
CREATE INDEX idx_reminder_logs_scheduled ON course_reminder_logs(scheduled_at) 
    WHERE status = 'scheduled';
CREATE INDEX idx_reminder_logs_channel_status ON course_reminder_logs(channel, status);
```

### Supporting Table: `course_unsubscribes`

```sql
CREATE TABLE course_unsubscribes (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id INT NOT NULL,
    course_id INT, -- NULL means unsubscribe from all course reminders
    
    -- Metadata
    unsubscribed_at TIMESTAMP DEFAULT NOW(),
    reason TEXT,
    source VARCHAR(50), -- 'email_link', 'user_settings', 'support_request'
    
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (course_id) REFERENCES courses(id)
);

-- Indexes
CREATE INDEX idx_course_unsub_user ON course_unsubscribes(user_id);
CREATE INDEX idx_course_unsub_course ON course_unsubscribes(course_id);
CREATE UNIQUE INDEX idx_course_unsub_unique ON course_unsubscribes(user_id, course_id);
```

---

## Implementation Architecture

### Technology Stack
- **Backend**: FastAPI (Python)
- **Task Queue**: Celery
- **Message Broker**: Redis
- **Scheduler**: Celery Beat
- **Dependency Management**: uv
- **Database**: PostgreSQL (existing)
- **Email Provider**: SendGrid / AWS SES
- **SMS Provider**: Twilio / AWS SNS

### System Flow Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│              Daily Detection Job (Celery Beat)                   │
│                    Runs at 2:00 AM Daily                        │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                  Step 1: Query user_activities                   │
│   SELECT DISTINCT user_id, course_id FROM user_activities       │
│   WHERE activity_type = 'course_page_view'                      │
│   AND activity_date = CURRENT_DATE - INTERVAL '3 days'          │
│   AND (user_id, course_id) NOT IN (                            │
│       SELECT user_id, course_id FROM user_activities            │
│       WHERE activity_date = CURRENT_DATE                        │
│   )                                                              │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│              Step 2: Check Course Completion Status              │
│   For each (user_id, course_id) pair:                          │
│   - Query user_course_progress table                            │
│   - Check if completion_percentage < 100                        │
│   - Filter out already completed courses                        │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│           Step 3: Check Unsubscribe Status                      │
│   Filter out users who have unsubscribed:                       │
│   - Check course_unsubscribes table                             │
│   - Remove if (user_id, course_id) exists                       │
│   - Remove if (user_id, NULL) exists (global unsub)            │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│         Step 4: Insert/Update content_notifications             │
│   For each eligible (user_id, course_id):                      │
│   - INSERT IF NOT EXISTS                                        │
│   - UPDATE last_activity_at if already exists                   │
│   - Set next_reminder_due_at based on rules                    │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│            Hourly Reminder Scheduler (Celery Beat)              │
│                   Runs every hour at :00                        │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│              Step 5: Select Due Reminders                       │
│   SELECT * FROM content_notifications                           │
│   WHERE status = 'active'                                       │
│   AND next_reminder_due_at <= NOW()                            │
│   ORDER BY next_reminder_due_at ASC                            │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│            Step 6: Apply Frequency Rules                        │
│   For each notification:                                        │
│   - Email: Can send if last_email_sent_at is NULL              │
│            OR >= 7 days ago                                     │
│   - SMS: Can send if last_sms_sent_at is NULL                  │
│          OR >= 30 days ago                                      │
│          AND email_count >= 2 (SMS only after 2 emails)        │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│              Step 7: Queue Messages (Celery Tasks)              │
│   For each eligible notification:                              │
│   - send_course_reminder_email.apply_async()                   │
│   - send_course_reminder_sms.apply_async()                     │
│   - Create record in course_reminder_logs                      │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                Step 8: Send via Providers                       │
│   Email Worker: SendGrid/AWS SES API                           │
│   SMS Worker: Twilio/AWS SNS API                               │
│   Update course_reminder_logs with status                      │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│              Step 9: Update Notification Record                 │
│   - Increment email_count or sms_count                         │
│   - Update last_email_sent_at or last_sms_sent_at             │
│   - Calculate next_reminder_due_at (7 days for email)         │
│   - Increment stage if criteria met                            │
└─────────────────────────────────────────────────────────────────┘
```

---

## Detailed Implementation Steps

### Phase 1: Database Setup (Days 1-2)

**Task 1.1: Create Tables**
```bash
# Create migration file
cd /path/to/project
uv run alembic revision -m "add_course_reminder_tables"
```

**Migration file content:**
```python
# migrations/versions/xxxx_add_course_reminder_tables.py

def upgrade():
    # Create content_notifications table
    op.execute("""
        CREATE TABLE content_notifications (
            id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
            user_id INT NOT NULL,
            course_id INT NOT NULL,
            status VARCHAR(20) DEFAULT 'active',
            stage INT DEFAULT 1,
            first_detected_at TIMESTAMP DEFAULT NOW(),
            last_reminder_sent_at TIMESTAMP,
            next_reminder_due_at TIMESTAMP,
            email_count INT DEFAULT 0,
            sms_count INT DEFAULT 0,
            last_email_sent_at TIMESTAMP,
            last_sms_sent_at TIMESTAMP,
            completion_percentage DECIMAL(5,2) DEFAULT 0.00,
            modules_completed INT DEFAULT 0,
            total_modules INT,
            last_activity_at TIMESTAMP,
            created_at TIMESTAMP DEFAULT NOW(),
            updated_at TIMESTAMP DEFAULT NOW(),
            completed_at TIMESTAMP,
            unsubscribed_at TIMESTAMP,
            UNIQUE(user_id, course_id)
        )
    """)
    
    # Create indexes
    op.execute("""
        CREATE INDEX idx_content_notif_user ON content_notifications(user_id);
        CREATE INDEX idx_content_notif_course ON content_notifications(course_id);
        CREATE INDEX idx_content_notif_status ON content_notifications(status);
        CREATE INDEX idx_content_notif_next_due ON content_notifications(next_reminder_due_at) 
            WHERE status = 'active';
    """)
    
    # Create course_reminder_logs table
    # ... (similar pattern)
    
    # Create course_unsubscribes table
    # ... (similar pattern)

def downgrade():
    op.drop_table('course_reminder_logs')
    op.drop_table('course_unsubscribes')
    op.drop_table('content_notifications')
```

**Task 1.2: Run Migration**
```bash
uv run alembic upgrade head
```

---

### Phase 2: Core Detection Logic (Days 3-5)

**File: `app/tasks/course_reminders/detection.py`**

```python
from datetime import datetime, timedelta
from typing import List, Tuple
from sqlalchemy import text
from app.database import get_db
from app.models import ContentNotification
import logging

logger = logging.getLogger(__name__)


async def detect_inactive_course_users() -> List[Tuple[int, int]]:
    """
    Identifies users who:
    1. Viewed a course 3 days ago
    2. Did NOT view it today
    3. Have NOT completed the course
    
    Returns:
        List of (user_id, course_id) tuples
    """
    
    query = text("""
        WITH inactive_users AS (
            -- Users who viewed 3 days ago
            SELECT DISTINCT 
                user_id, 
                course_id
            FROM user_activities
            WHERE activity_type = 'course_page_view'
                AND activity_date = CURRENT_DATE - INTERVAL '3 days'
        ),
        active_today AS (
            -- Users who viewed today
            SELECT DISTINCT 
                user_id, 
                course_id
            FROM user_activities
            WHERE activity_type = 'course_page_view'
                AND activity_date = CURRENT_DATE
        ),
        eligible_users AS (
            -- Users inactive today but active 3 days ago
            SELECT 
                iu.user_id,
                iu.course_id
            FROM inactive_users iu
            LEFT JOIN active_today at ON iu.user_id = at.user_id 
                AND iu.course_id = at.course_id
            WHERE at.user_id IS NULL
        )
        -- Filter by completion status
        SELECT 
            eu.user_id,
            eu.course_id
        FROM eligible_users eu
        INNER JOIN user_course_progress ucp 
            ON eu.user_id = ucp.user_id 
            AND eu.course_id = ucp.course_id
        WHERE ucp.completion_percentage < 100
            -- Not already marked as completed
            AND NOT EXISTS (
                SELECT 1 FROM content_notifications cn
                WHERE cn.user_id = eu.user_id
                    AND cn.course_id = eu.course_id
                    AND cn.status = 'completed'
            )
            -- Not unsubscribed
            AND NOT EXISTS (
                SELECT 1 FROM course_unsubscribes cu
                WHERE cu.user_id = eu.user_id
                    AND (cu.course_id = eu.course_id OR cu.course_id IS NULL)
            )
    """)
    
    async with get_db() as db:
        result = await db.execute(query)
        rows = result.fetchall()
        
    logger.info(f"Detected {len(rows)} inactive course users")
    return [(row.user_id, row.course_id) for row in rows]


async def get_course_progress(user_id: int, course_id: int) -> dict:
    """
    Fetches current course progress for a user
    
    Returns:
        dict with completion_percentage, modules_completed, total_modules, last_activity_at
    """
    
    query = text("""
        SELECT 
            ucp.completion_percentage,
            ucp.modules_completed,
            c.total_modules,
            ucp.last_accessed_at as last_activity_at
        FROM user_course_progress ucp
        INNER JOIN courses c ON ucp.course_id = c.id
        WHERE ucp.user_id = :user_id
            AND ucp.course_id = :course_id
    """)
    
    async with get_db() as db:
        result = await db.execute(
            query, 
            {"user_id": user_id, "course_id": course_id}
        )
        row = result.fetchone()
        
    if not row:
        return {}
        
    return {
        "completion_percentage": float(row.completion_percentage),
        "modules_completed": row.modules_completed,
        "total_modules": row.total_modules,
        "last_activity_at": row.last_activity_at
    }


async def upsert_content_notification(
    user_id: int, 
    course_id: int, 
    progress_data: dict
) -> str:
    """
    Inserts or updates content_notifications record
    
    Returns:
        notification_id (UUID as string)
    """
    
    query = text("""
        INSERT INTO content_notifications (
            user_id,
            course_id,
            completion_percentage,
            modules_completed,
            total_modules,
            last_activity_at,
            next_reminder_due_at,
            status
        ) VALUES (
            :user_id,
            :course_id,
            :completion_percentage,
            :modules_completed,
            :total_modules,
            :last_activity_at,
            NOW() + INTERVAL '1 hour', -- First reminder in 1 hour
            'active'
        )
        ON CONFLICT (user_id, course_id) DO UPDATE SET
            completion_percentage = EXCLUDED.completion_percentage,
            modules_completed = EXCLUDED.modules_completed,
            last_activity_at = EXCLUDED.last_activity_at,
            updated_at = NOW()
        RETURNING id
    """)
    
    async with get_db() as db:
        result = await db.execute(query, {
            "user_id": user_id,
            "course_id": course_id,
            **progress_data
        })
        notification_id = result.fetchone()[0]
        await db.commit()
        
    logger.info(f"Upserted notification {notification_id} for user {user_id}, course {course_id}")
    return str(notification_id)
```

**File: `app/tasks/course_reminders/celery_tasks.py`**

```python
from celery import shared_task
from app.tasks.course_reminders.detection import (
    detect_inactive_course_users,
    get_course_progress,
    upsert_content_notification
)
import logging

logger = logging.getLogger(__name__)


@shared_task(name="course_reminders.detect_inactive_users")
async def detect_inactive_users_task():
    """
    Daily task to detect inactive course users
    Scheduled via Celery Beat at 2:00 AM
    """
    logger.info("Starting inactive user detection...")
    
    try:
        # Step 1: Detect inactive users
        inactive_users = await detect_inactive_course_users()
        
        # Step 2: Process each user
        for user_id, course_id in inactive_users:
            # Get course progress
            progress_data = await get_course_progress(user_id, course_id)
            
            if not progress_data:
                logger.warning(f"No progress data for user {user_id}, course {course_id}")
                continue
            
            # Insert/update notification record
            notification_id = await upsert_content_notification(
                user_id, 
                course_id, 
                progress_data
            )
            
        logger.info(f"Detection complete. Processed {len(inactive_users)} users.")
        return {
            "success": True,
            "users_detected": len(inactive_users)
        }
        
    except Exception as e:
        logger.error(f"Error in detection task: {str(e)}", exc_info=True)
        return {
            "success": False,
            "error": str(e)
        }
```

---

### Phase 3: Reminder Scheduling & Frequency Rules (Days 6-8)

**File: `app/tasks/course_reminders/scheduler.py`**

```python
from datetime import datetime, timedelta
from typing import List, Dict
from sqlalchemy import text
from app.database import get_db
import logging

logger = logging.getLogger(__name__)


async def get_due_reminders() -> List[Dict]:
    """
    Fetches notifications that are due for reminders
    
    Returns:
        List of dicts with notification details
    """
    
    query = text("""
        SELECT 
            cn.id as notification_id,
            cn.user_id,
            cn.course_id,
            cn.stage,
            cn.email_count,
            cn.sms_count,
            cn.last_email_sent_at,
            cn.last_sms_sent_at,
            cn.completion_percentage,
            cn.modules_completed,
            cn.total_modules,
            c.name as course_name,
            c.cpd_points,
            u.first_name,
            u.last_name,
            u.email,
            u.phone_number
        FROM content_notifications cn
        INNER JOIN courses c ON cn.course_id = c.id
        INNER JOIN users u ON cn.user_id = u.id
        WHERE cn.status = 'active'
            AND cn.next_reminder_due_at <= NOW()
        ORDER BY cn.next_reminder_due_at ASC
        LIMIT 1000  -- Process in batches
    """)
    
    async with get_db() as db:
        result = await db.execute(query)
        rows = result.fetchall()
        
    notifications = []
    for row in rows:
        notifications.append({
            "notification_id": str(row.notification_id),
            "user_id": row.user_id,
            "course_id": row.course_id,
            "stage": row.stage,
            "email_count": row.email_count,
            "sms_count": row.sms_count,
            "last_email_sent_at": row.last_email_sent_at,
            "last_sms_sent_at": row.last_sms_sent_at,
            "completion_percentage": float(row.completion_percentage),
            "modules_completed": row.modules_completed,
            "total_modules": row.total_modules,
            "course_name": row.course_name,
            "cpd_points": row.cpd_points,
            "first_name": row.first_name,
            "last_name": row.last_name,
            "email": row.email,
            "phone_number": row.phone_number
        })
    
    logger.info(f"Found {len(notifications)} due reminders")
    return notifications


def should_send_email(notification: Dict) -> bool:
    """
    Determines if email should be sent based on frequency rules
    
    Rules:
    - Can send email once per week (7 days)
    - First email can be sent immediately
    """
    last_sent = notification["last_email_sent_at"]
    
    # First email
    if last_sent is None:
        return True
    
    # Check if 7 days have passed
    days_since_last = (datetime.now() - last_sent).days
    return days_since_last >= 7


def should_send_sms(notification: Dict) -> bool:
    """
    Determines if SMS should be sent based on frequency rules
    
    Rules:
    - Can send SMS once per month (30 days)
    - Must have sent at least 2 emails before sending SMS
    """
    last_sent = notification["last_sms_sent_at"]
    email_count = notification["email_count"]
    
    # Must have sent 2+ emails first
    if email_count < 2:
        return False
    
    # First SMS
    if last_sent is None:
        return True
    
    # Check if 30 days have passed
    days_since_last = (datetime.now() - last_sent).days
    return days_since_last >= 30


async def calculate_next_reminder_date(
    notification_id: str, 
    channel: str
) -> datetime:
    """
    Calculates next reminder due date based on channel
    
    Email: 7 days from now
    SMS: 30 days from now
    """
    if channel == "email":
        return datetime.now() + timedelta(days=7)
    elif channel == "sms":
        return datetime.now() + timedelta(days=30)
    else:
        raise ValueError(f"Unknown channel: {channel}")
```

**File: `app/tasks/course_reminders/celery_tasks.py` (continued)**

```python
from app.tasks.course_reminders.scheduler import (
    get_due_reminders,
    should_send_email,
    should_send_sms,
    calculate_next_reminder_date
)
from app.tasks.course_reminders.messaging import (
    queue_email_reminder,
    queue_sms_reminder
)


@shared_task(name="course_reminders.schedule_reminders")
async def schedule_reminders_task():
    """
    Hourly task to schedule reminders for due notifications
    Scheduled via Celery Beat every hour
    """
    logger.info("Starting reminder scheduling...")
    
    try:
        # Get all due notifications
        due_notifications = await get_due_reminders()
        
        emails_queued = 0
        sms_queued = 0
        
        for notification in due_notifications:
            notification_id = notification["notification_id"]
            
            # Check if email should be sent
            if should_send_email(notification):
                await queue_email_reminder(notification)
                emails_queued += 1
                logger.info(f"Queued email for notification {notification_id}")
            
            # Check if SMS should be sent (independent of email)
            if should_send_sms(notification):
                await queue_sms_reminder(notification)
                sms_queued += 1
                logger.info(f"Queued SMS for notification {notification_id}")
            
            # If neither channel is eligible, update next_reminder_due_at
            # to check again in 1 day
            if not should_send_email(notification) and not should_send_sms(notification):
                await update_next_reminder_date(
                    notification_id, 
                    datetime.now() + timedelta(days=1)
                )
        
        logger.info(f"Scheduling complete. Queued {emails_queued} emails, {sms_queued} SMS")
        return {
            "success": True,
            "emails_queued": emails_queued,
            "sms_queued": sms_queued
        }
        
    except Exception as e:
        logger.error(f"Error in scheduling task: {str(e)}", exc_info=True)
        return {
            "success": False,
            "error": str(e)
        }
```

---

### Phase 4: Message Templates & Sending (Days 9-11)

**File: `app/tasks/course_reminders/templates.py`**

```python
from typing import Dict


def render_email_template(notification: Dict, stage: int, unsubscribe_token: str) -> Dict[str, str]:
    """
    Renders email template based on stage
    
    Returns:
        dict with 'subject' and 'html_body'
    """
    
    first_name = notification["first_name"]
    course_name = notification["course_name"]
    completion_pct = int(notification["completion_percentage"])
    remaining_modules = notification["total_modules"] - notification["modules_completed"]
    cpd_points = notification["cpd_points"]
    
    # Generate course link (replace with actual URL builder)
    course_link = f"https://doctor.clirnet.com/courses/{notification['course_id']}"
    unsubscribe_link = f"https://doctor.clirnet.com/unsubscribe/course/{unsubscribe_token}"
    
    templates = {
        1: {
            "subject": f"Continue your progress in {course_name}",
            "html_body": f"""
            <html>
            <body style="font-family: Arial, sans-serif; line-height: 1.6; color: #333;">
                <h2>Hi Dr. {first_name},</h2>
                
                <p>We noticed you're <strong>{completion_pct}% through</strong> <em>{course_name}</em>.</p>
                
                <p><strong>Great progress!</strong> You're almost there.</p>
                
                <p><strong>What's left:</strong></p>
                <ul>
                    <li>{remaining_modules} modules remaining</li>
                    <li>{cpd_points} CPD points waiting</li>
                    <li>Certificate of completion</li>
                </ul>
                
                <p>
                    <a href="{course_link}" 
                       style="background-color: #007bff; color: white; padding: 12px 24px; 
                              text-decoration: none; border-radius: 4px; display: inline-block;">
                        Continue Learning →
                    </a>
                </p>
                
                <p style="margin-top: 40px; font-size: 12px; color: #666;">
                    Don't want reminders for this course? 
                    <a href="{unsubscribe_link}" style="color: #666;">Unsubscribe</a>
                </p>
                
                <p style="font-size: 12px; color: #666;">
                    Best regards,<br>
                    Team CLIRNET
                </p>
            </body>
            </html>
            """
        },
        2: {
            "subject": f"You're {completion_pct}% through {course_name}",
            "html_body": f"""
            <html>
            <body style="font-family: Arial, sans-serif; line-height: 1.6; color: #333;">
                <h2>Dr. {first_name},</h2>
                
                <p>Quick reminder about your course progress:</p>
                
                <div style="background-color: #f8f9fa; padding: 20px; border-radius: 4px; margin: 20px 0;">
                    <h3 style="margin-top: 0;">{course_name}</h3>
                    <p style="font-size: 18px; margin: 10px 0;">
                        <strong>{completion_pct}%</strong> complete
                    </p>
                    <p>
                        <strong>{remaining_modules}</strong> modules left • 
                        <strong>{cpd_points}</strong> CPD points
                    </p>
                </div>
                
                <p><strong>Why complete this course?</strong></p>
                <ul>
                    <li>Enhance your professional credentials</li>
                    <li>Stay current with medical advances</li>
                    <li>Earn valuable CPD points</li>
                </ul>
                
                <p>
                    <a href="{course_link}" 
                       style="background-color: #28a745; color: white; padding: 12px 24px; 
                              text-decoration: none; border-radius: 4px; display: inline-block;">
                        Resume Course →
                    </a>
                </p>
                
                <p style="margin-top: 40px; font-size: 12px; color: #666;">
                    <a href="{unsubscribe_link}" style="color: #666;">Unsubscribe from this course</a>
                </p>
                
                <p style="font-size: 12px; color: #666;">
                    Best regards,<br>
                    Team CLIRNET
                </p>
            </body>
            </html>
            """
        },
        3: {
            "subject": f"Don't lose your progress in {course_name}",
            "html_body": f"""
            <html>
            <body style="font-family: Arial, sans-serif; line-height: 1.6; color: #333;">
                <h2>Dr. {first_name},</h2>
                
                <p>You've already invested time in <strong>{course_name}</strong>.</p>
                
                <p style="background-color: #fff3cd; padding: 15px; border-left: 4px solid #ffc107;">
                    <strong>Current progress: {completion_pct}%</strong><br>
                    Don't let your effort go to waste!
                </p>
                
                <p><strong>You're so close:</strong></p>
                <ul>
                    <li>Only {remaining_modules} modules remaining</li>
                    <li>{cpd_points} CPD points ready to be claimed</li>
                    <li>Certificate of completion waiting</li>
                </ul>
                
                <p>
                    <a href="{course_link}" 
                       style="background-color: #dc3545; color: white; padding: 12px 24px; 
                              text-decoration: none; border-radius: 4px; display: inline-block;">
                        Finish Your Course →
                    </a>
                </p>
                
                <p style="margin-top: 40px; font-size: 12px; color: #666;">
                    <a href="{unsubscribe_link}" style="color: #666;">Stop reminders for this course</a>
                </p>
                
                <p style="font-size: 12px; color: #666;">
                    Best regards,<br>
                    Team CLIRNET
                </p>
            </body>
            </html>
            """
        }
    }
    
    # Use stage 3 template for all stages >= 3
    stage = min(stage, 3)
    return templates[stage]


def render_sms_template(notification: Dict) -> str:
    """
    Renders SMS template (always same content)
    
    SMS are sent max once per month, so no stage variations
    """
    
    last_name = notification["last_name"]
    course_name = notification["course_name"]
    completion_pct = int(notification["completion_percentage"])
    cpd_points = notification["cpd_points"]
    course_id = notification["course_id"]
    
    # Generate short link (replace with actual URL shortener)
    short_link = f"https://clr.net/c/{course_id}"
    
    return (
        f"Dr. {last_name}, you're {completion_pct}% through {course_name}. "
        f"Complete to earn {cpd_points} CPD points: {short_link} -CLIRNET"
    )
```

**File: `app/tasks/course_reminders/messaging.py`**

```python
from datetime import datetime
from typing import Dict
from sqlalchemy import text
from app.database import get_db
from app.services.email_service import send_email
from app.services.sms_service import send_sms
from app.tasks.course_reminders.templates import (
    render_email_template,
    render_sms_template
)
from app.tasks.course_reminders.scheduler import calculate_next_reminder_date
import logging
import secrets

logger = logging.getLogger(__name__)


def generate_unsubscribe_token(user_id: int, course_id: int) -> str:
    """
    Generates a secure unsubscribe token
    
    In production, use JWT or store tokens in database
    """
    # Simplified for example - use proper token generation in production
    return secrets.token_urlsafe(32)


async def create_reminder_log(
    notification_id: str,
    user_id: int,
    course_id: int,
    channel: str,
    stage: int,
    template_used: str
) -> str:
    """
    Creates a log entry for the reminder
    
    Returns:
        log_id (UUID as string)
    """
    
    query = text("""
        INSERT INTO course_reminder_logs (
            notification_id,
            user_id,
            course_id,
            channel,
            stage,
            template_used,
            scheduled_at,
            status
        ) VALUES (
            :notification_id,
            :user_id,
            :course_id,
            :channel,
            :stage,
            :template_used,
            NOW(),
            'scheduled'
        )
        RETURNING id
    """)
    
    async with get_db() as db:
        result = await db.execute(query, {
            "notification_id": notification_id,
            "user_id": user_id,
            "course_id": course_id,
            "channel": channel,
            "stage": stage,
            "template_used": template_used
        })
        log_id = result.fetchone()[0]
        await db.commit()
        
    return str(log_id)


async def update_notification_after_send(
    notification_id: str,
    channel: str
):
    """
    Updates notification record after sending
    """
    
    if channel == "email":
        query = text("""
            UPDATE content_notifications
            SET 
                email_count = email_count + 1,
                last_email_sent_at = NOW(),
                last_reminder_sent_at = NOW(),
                next_reminder_due_at = NOW() + INTERVAL '7 days',
                stage = CASE 
                    WHEN stage < 5 THEN stage + 1 
                    ELSE stage 
                END,
                updated_at = NOW()
            WHERE id = :notification_id
        """)
    elif channel == "sms":
        query = text("""
            UPDATE content_notifications
            SET 
                sms_count = sms_count + 1,
                last_sms_sent_at = NOW(),
                last_reminder_sent_at = NOW(),
                next_reminder_due_at = NOW() + INTERVAL '30 days',
                updated_at = NOW()
            WHERE id = :notification_id
        """)
    else:
        raise ValueError(f"Unknown channel: {channel}")
    
    async with get_db() as db:
        await db.execute(query, {"notification_id": notification_id})
        await db.commit()


async def queue_email_reminder(notification: Dict):
    """
    Queues an email reminder for sending
    """
    
    notification_id = notification["notification_id"]
    user_id = notification["user_id"]
    course_id = notification["course_id"]
    stage = notification["stage"]
    email = notification["email"]
    
    # Generate unsubscribe token
    unsubscribe_token = generate_unsubscribe_token(user_id, course_id)
    
    # Render template
    email_content = render_email_template(notification, stage, unsubscribe_token)
    
    # Create log entry
    log_id = await create_reminder_log(
        notification_id,
        user_id,
        course_id,
        "email",
        stage,
        f"email_stage_{stage}"
    )
    
    # Queue for sending (async Celery task)
    from app.tasks.course_reminders.celery_tasks import send_email_reminder_task
    send_email_reminder_task.apply_async(
        args=[notification_id, email, email_content, log_id]
    )
    
    logger.info(f"Queued email reminder for user {user_id}, course {course_id}")


async def queue_sms_reminder(notification: Dict):
    """
    Queues an SMS reminder for sending
    """
    
    notification_id = notification["notification_id"]
    user_id = notification["user_id"]
    course_id = notification["course_id"]
    stage = notification["stage"]
    phone_number = notification["phone_number"]
    
    # Render template
    sms_content = render_sms_template(notification)
    
    # Create log entry
    log_id = await create_reminder_log(
        notification_id,
        user_id,
        course_id,
        "sms",
        stage,
        "sms_standard"
    )
    
    # Queue for sending (async Celery task)
    from app.tasks.course_reminders.celery_tasks import send_sms_reminder_task
    send_sms_reminder_task.apply_async(
        args=[notification_id, phone_number, sms_content, log_id]
    )
    
    logger.info(f"Queued SMS reminder for user {user_id}, course {course_id}")
```

**File: `app/tasks/course_reminders/celery_tasks.py` (continued)**

```python
from app.services.email_service import send_email
from app.services.sms_service import send_sms


@shared_task(name="course_reminders.send_email_reminder", bind=True, max_retries=3)
async def send_email_reminder_task(
    self,
    notification_id: str,
    recipient_email: str,
    email_content: Dict[str, str],
    log_id: str
):
    """
    Sends an email reminder
    """
    
    try:
        # Send email via provider (SendGrid, AWS SES, etc.)
        provider_message_id = await send_email(
            to=recipient_email,
            subject=email_content["subject"],
            html_body=email_content["html_body"]
        )
        
        # Update log
        await update_reminder_log_status(
            log_id,
            "sent",
            provider_message_id
        )
        
        # Update notification
        await update_notification_after_send(notification_id, "email")
        
        logger.info(f"Email sent for notification {notification_id}")
        return {"success": True, "message_id": provider_message_id}
        
    except Exception as e:
        logger.error(f"Failed to send email: {str(e)}", exc_info=True)
        
        # Update log with error
        await update_reminder_log_status(
            log_id,
            "failed",
            error_message=str(e)
        )
        
        # Retry
        raise self.retry(exc=e, countdown=300)  # Retry after 5 minutes


@shared_task(name="course_reminders.send_sms_reminder", bind=True, max_retries=3)
async def send_sms_reminder_task(
    self,
    notification_id: str,
    recipient_phone: str,
    sms_content: str,
    log_id: str
):
    """
    Sends an SMS reminder
    """
    
    try:
        # Send SMS via provider (Twilio, AWS SNS, etc.)
        provider_message_id = await send_sms(
            to=recipient_phone,
            body=sms_content
        )
        
        # Update log
        await update_reminder_log_status(
            log_id,
            "sent",
            provider_message_id
        )
        
        # Update notification
        await update_notification_after_send(notification_id, "sms")
        
        logger.info(f"SMS sent for notification {notification_id}")
        return {"success": True, "message_id": provider_message_id}
        
    except Exception as e:
        logger.error(f"Failed to send SMS: {str(e)}", exc_info=True)
        
        # Update log with error
        await update_reminder_log_status(
            log_id,
            "failed",
            error_message=str(e)
        )
        
        # Retry
        raise self.retry(exc=e, countdown=300)  # Retry after 5 minutes
```

---

### Phase 5: Unsubscribe Mechanism (Days 12-13)

**File: `app/api/unsubscribe.py`**

```python
from fastapi import APIRouter, HTTPException
from sqlalchemy import text
from app.database import get_db
from datetime import datetime
import logging

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/unsubscribe", tags=["unsubscribe"])


@router.get("/course/{token}")
async def unsubscribe_from_course(token: str):
    """
    Unsubscribes user from specific course reminders
    
    Token should encode: user_id, course_id, signature
    In production, use JWT or similar secure tokens
    """
    
    try:
        # Decode token (simplified - use proper JWT in production)
        user_id, course_id = decode_unsubscribe_token(token)
        
        # Insert unsubscribe record
        query = text("""
            INSERT INTO course_unsubscribes (
                user_id,
                course_id,
                source
            ) VALUES (
                :user_id,
                :course_id,
                'email_link'
            )
            ON CONFLICT (user_id, course_id) DO NOTHING
        """)
        
        async with get_db() as db:
            await db.execute(query, {
                "user_id": user_id,
                "course_id": course_id
            })
            await db.commit()
        
        # Update notification status
        update_query = text("""
            UPDATE content_notifications
            SET 
                status = 'unsubscribed',
                unsubscribed_at = NOW(),
                updated_at = NOW()
            WHERE user_id = :user_id
                AND course_id = :course_id
        """)
        
        async with get_db() as db:
            await db.execute(update_query, {
                "user_id": user_id,
                "course_id": course_id
            })
            await db.commit()
        
        logger.info(f"User {user_id} unsubscribed from course {course_id}")
        
        return {
            "success": True,
            "message": "You have been unsubscribed from reminders for this course."
        }
        
    except Exception as e:
        logger.error(f"Unsubscribe error: {str(e)}", exc_info=True)
        raise HTTPException(status_code=400, detail="Invalid unsubscribe token")


@router.get("/all/{token}")
async def unsubscribe_from_all_courses(token: str):
    """
    Unsubscribes user from ALL course reminders
    """
    
    try:
        # Decode token
        user_id = decode_global_unsubscribe_token(token)
        
        # Insert global unsubscribe record
        query = text("""
            INSERT INTO course_unsubscribes (
                user_id,
                course_id,
                source
            ) VALUES (
                :user_id,
                NULL,
                'email_link'
            )
            ON CONFLICT (user_id, course_id) DO NOTHING
        """)
        
        async with get_db() as db:
            await db.execute(query, {"user_id": user_id})
            await db.commit()
        
        # Update all active notifications
        update_query = text("""
            UPDATE content_notifications
            SET 
                status = 'unsubscribed',
                unsubscribed_at = NOW(),
                updated_at = NOW()
            WHERE user_id = :user_id
                AND status = 'active'
        """)
        
        async with get_db() as db:
            await db.execute(update_query, {"user_id": user_id})
            await db.commit()
        
        logger.info(f"User {user_id} unsubscribed from all course reminders")
        
        return {
            "success": True,
            "message": "You have been unsubscribed from all course reminders."
        }
        
    except Exception as e:
        logger.error(f"Global unsubscribe error: {str(e)}", exc_info=True)
        raise HTTPException(status_code=400, detail="Invalid unsubscribe token")


def decode_unsubscribe_token(token: str) -> tuple:
    """
    Decodes unsubscribe token to extract user_id and course_id
    
    In production, use JWT with signature verification
    """
    # Simplified implementation
    # TODO: Implement proper JWT decoding with secret verification
    pass


def decode_global_unsubscribe_token(token: str) -> int:
    """
    Decodes global unsubscribe token to extract user_id
    """
    # Simplified implementation
    # TODO: Implement proper JWT decoding
    pass
```

---

### Phase 6: Visibility Dashboard (Days 14-16)

**File: `app/api/dashboard.py`**

```python
from fastapi import APIRouter, Query
from sqlalchemy import text
from app.database import get_db
from typing import Optional
from datetime import datetime, timedelta
import logging

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/dashboard", tags=["dashboard"])


@router.get("/course-reminders/overview")
async def get_reminders_overview():
    """
    Returns high-level overview of course reminder system
    """
    
    query = text("""
        SELECT 
            COUNT(*) FILTER (WHERE status = 'active') as active_notifications,
            COUNT(*) FILTER (WHERE status = 'completed') as completed_notifications,
            COUNT(*) FILTER (WHERE status = 'unsubscribed') as unsubscribed_notifications,
            SUM(email_count) as total_emails_sent,
            SUM(sms_count) as total_sms_sent,
            AVG(completion_percentage) as avg_completion_percentage
        FROM content_notifications
    """)
    
    async with get_db() as db:
        result = await db.execute(query)
        row = result.fetchone()
    
    return {
        "active_notifications": row.active_notifications,
        "completed_notifications": row.completed_notifications,
        "unsubscribed_notifications": row.unsubscribed_notifications,
        "total_emails_sent": row.total_emails_sent,
        "total_sms_sent": row.total_sms_sent,
        "avg_completion_percentage": float(row.avg_completion_percentage or 0)
    }


@router.get("/course-reminders/by-stage")
async def get_reminders_by_stage():
    """
    Returns breakdown of notifications by stage
    """
    
    query = text("""
        SELECT 
            stage,
            COUNT(*) as count,
            AVG(completion_percentage) as avg_completion,
            SUM(email_count) as total_emails,
            SUM(sms_count) as total_sms
        FROM content_notifications
        WHERE status = 'active'
        GROUP BY stage
        ORDER BY stage
    """)
    
    async with get_db() as db:
        result = await db.execute(query)
        rows = result.fetchall()
    
    stages = []
    for row in rows:
        stages.append({
            "stage": row.stage,
            "count": row.count,
            "avg_completion": float(row.avg_completion),
            "total_emails": row.total_emails,
            "total_sms": row.total_sms
        })
    
    return {"stages": stages}


@router.get("/course-reminders/delivery-stats")
async def get_delivery_stats(
    days: int = Query(7, description="Number of days to look back")
):
    """
    Returns delivery statistics for the past N days
    """
    
    query = text("""
        SELECT 
            DATE(scheduled_at) as date,
            channel,
            COUNT(*) FILTER (WHERE status = 'sent') as sent,
            COUNT(*) FILTER (WHERE status = 'delivered') as delivered,
            COUNT(*) FILTER (WHERE status = 'opened') as opened,
            COUNT(*) FILTER (WHERE status = 'clicked') as clicked,
            COUNT(*) FILTER (WHERE status = 'failed') as failed
        FROM course_reminder_logs
        WHERE scheduled_at >= NOW() - INTERVAL ':days days'
        GROUP BY DATE(scheduled_at), channel
        ORDER BY date DESC, channel
    """)
    
    async with get_db() as db:
        result = await db.execute(query, {"days": days})
        rows = result.fetchall()
    
    stats = []
    for row in rows:
        stats.append({
            "date": row.date.isoformat(),
            "channel": row.channel,
            "sent": row.sent,
            "delivered": row.delivered,
            "opened": row.opened,
            "clicked": row.clicked,
            "failed": row.failed,
            "open_rate": (row.opened / row.sent * 100) if row.sent > 0 else 0,
            "click_rate": (row.clicked / row.sent * 100) if row.sent > 0 else 0
        })
    
    return {"stats": stats}


@router.get("/course-reminders/top-courses")
async def get_top_courses(limit: int = Query(10, le=50)):
    """
    Returns top courses by number of active reminders
    """
    
    query = text("""
        SELECT 
            c.id as course_id,
            c.name as course_name,
            COUNT(*) as active_reminders,
            AVG(cn.completion_percentage) as avg_completion,
            SUM(cn.email_count) as total_emails,
            SUM(cn.sms_count) as total_sms
        FROM content_notifications cn
        INNER JOIN courses c ON cn.course_id = c.id
        WHERE cn.status = 'active'
        GROUP BY c.id, c.name
        ORDER BY active_reminders DESC
        LIMIT :limit
    """)
    
    async with get_db() as db:
        result = await db.execute(query, {"limit": limit})
        rows = result.fetchall()
    
    courses = []
    for row in rows:
        courses.append({
            "course_id": row.course_id,
            "course_name": row.course_name,
            "active_reminders": row.active_reminders,
            "avg_completion": float(row.avg_completion),
            "total_emails": row.total_emails,
            "total_sms": row.total_sms
        })
    
    return {"courses": courses}


@router.get("/course-reminders/user/{user_id}")
async def get_user_reminder_status(user_id: int):
    """
    Returns reminder status for a specific user
    """
    
    query = text("""
        SELECT 
            cn.id as notification_id,
            c.name as course_name,
            cn.status,
            cn.stage,
            cn.completion_percentage,
            cn.email_count,
            cn.sms_count,
            cn.last_reminder_sent_at,
            cn.next_reminder_due_at
        FROM content_notifications cn
        INNER JOIN courses c ON cn.course_id = c.id
        WHERE cn.user_id = :user_id
        ORDER BY cn.last_reminder_sent_at DESC
    """)
    
    async with get_db() as db:
        result = await db.execute(query, {"user_id": user_id})
        rows = result.fetchall()
    
    notifications = []
    for row in rows:
        notifications.append({
            "notification_id": str(row.notification_id),
            "course_name": row.course_name,
            "status": row.status,
            "stage": row.stage,
            "completion_percentage": float(row.completion_percentage),
            "email_count": row.email_count,
            "sms_count": row.sms_count,
            "last_reminder_sent_at": row.last_reminder_sent_at.isoformat() if row.last_reminder_sent_at else None,
            "next_reminder_due_at": row.next_reminder_due_at.isoformat() if row.next_reminder_due_at else None
        })
    
    return {"notifications": notifications}
```

---

### Phase 7: Celery Configuration (Days 17-18)

**File: `app/celery_app.py`**

```python
from celery import Celery
from celery.schedules import crontab
from app.config import settings

celery_app = Celery(
    "clirnet_course_reminders",
    broker=settings.REDIS_URL,
    backend=settings.REDIS_URL
)

# Celery configuration
celery_app.conf.update(
    task_serializer="json",
    accept_content=["json"],
    result_serializer="json",
    timezone="Asia/Kolkata",
    enable_utc=True,
    task_track_started=True,
    task_time_limit=30 * 60,  # 30 minutes
    task_soft_time_limit=25 * 60,  # 25 minutes
    worker_prefetch_multiplier=4,
    worker_max_tasks_per_child=1000,
)

# Celery Beat schedule
celery_app.conf.beat_schedule = {
    # Daily detection at 2:00 AM
    "detect-inactive-course-users": {
        "task": "course_reminders.detect_inactive_users",
        "schedule": crontab(hour=2, minute=0),
    },
    
    # Hourly reminder scheduling
    "schedule-course-reminders": {
        "task": "course_reminders.schedule_reminders",
        "schedule": crontab(minute=0),  # Every hour
    },
    
    # Daily analytics at 11:00 PM
    "calculate-course-reminder-analytics": {
        "task": "course_reminders.calculate_analytics",
        "schedule": crontab(hour=23, minute=0),
    },
    
    # Cleanup completed notifications (weekly on Sunday at 3:00 AM)
    "cleanup-completed-notifications": {
        "task": "course_reminders.cleanup_completed",
        "schedule": crontab(hour=3, minute=0, day_of_week=0),
    },
}

# Import tasks to register them
from app.tasks.course_reminders import celery_tasks
```

**File: `app/config.py`**

```python
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # Redis
    REDIS_URL: str = "redis://localhost:6379/0"
    
    # Database
    DATABASE_URL: str
    
    # Email Provider (SendGrid)
    SENDGRID_API_KEY: str
    SENDGRID_FROM_EMAIL: str
    
    # SMS Provider (Twilio)
    TWILIO_ACCOUNT_SID: str
    TWILIO_AUTH_TOKEN: str
    TWILIO_FROM_NUMBER: str
    
    # Application
    API_BASE_URL: str = "https://doctor.clirnet.com"
    
    class Config:
        env_file = ".env"


settings = Settings()
```

**File: `pyproject.toml` (for uv dependency management)**

```toml
[project]
name = "clirnet-course-reminders"
version = "1.0.0"
description = "Course completion reminder system"
requires-python = ">=3.11"

dependencies = [
    "fastapi>=0.104.0",
    "uvicorn>=0.24.0",
    "celery>=5.3.4",
    "redis>=5.0.0",
    "sqlalchemy>=2.0.0",
    "asyncpg>=0.29.0",
    "pydantic>=2.5.0",
    "pydantic-settings>=2.1.0",
    "sendgrid>=6.11.0",
    "twilio>=8.11.0",
    "alembic>=1.13.0",
]

[project.optional-dependencies]
dev = [
    "pytest>=7.4.0",
    "pytest-asyncio>=0.21.0",
    "black>=23.12.0",
    "ruff>=0.1.0",
]
```

**Installation Commands:**

```bash
# Install dependencies
uv pip install -e .

# Run database migrations
uv run alembic upgrade head

# Start Celery worker
uv run celery -A app.celery_app worker --loglevel=info

# Start Celery Beat scheduler
uv run celery -A app.celery_app beat --loglevel=info

# Start FastAPI application
uv run uvicorn app.main:app --host 0.0.0.0 --port 8000
```

---

## Testing Strategy

### Unit Tests

```python
# tests/test_detection.py
import pytest
from app.tasks.course_reminders.detection import detect_inactive_course_users


@pytest.mark.asyncio
async def test_detect_inactive_users():
    """Test detection of inactive users"""
    users = await detect_inactive_course_users()
    assert isinstance(users, list)
    assert all(isinstance(u, tuple) and len(u) == 2 for u in users)
```

### Integration Tests

```python
# tests/test_reminder_flow.py
import pytest
from app.tasks.course_reminders.celery_tasks import (
    detect_inactive_users_task,
    schedule_reminders_task
)


@pytest.mark.asyncio
async def test_end_to_end_reminder_flow():
    """Test complete reminder flow"""
    # Step 1: Detect users
    result = await detect_inactive_users_task()
    assert result["success"] == True
    
    # Step 2: Schedule reminders
    result = await schedule_reminders_task()
    assert result["success"] == True
```

---

## Monitoring & Alerts

### Key Metrics to Monitor

1. **Detection Job Success Rate**
   - Monitor daily detection job completion
   - Alert if job fails for 2 consecutive days

2. **Message Delivery Rates**
   - Email delivery rate (target: >95%)
   - SMS delivery rate (target: >98%)
   - Alert if drops below threshold

3. **Queue Length**
   - Monitor Redis queue size
   - Alert if queue grows beyond 10,000 messages

4. **Unsubscribe Rate**
   - Track daily unsubscribe rate
   - Alert if exceeds 5% per day

5. **Course Completion Rate**
   - Track users who complete courses after reminders
   - Target: 35% completion rate within 21 days

### Logging

```python
# Structured logging format
logger.info(
    "Reminder sent",
    extra={
        "user_id": user_id,
        "course_id": course_id,
        "channel": "email",
        "stage": 2,
        "notification_id": notification_id
    }
)
```

---

## Rollout Plan

### Week 1: Infrastructure Setup
- Day 1-2: Database schema creation
- Day 3-4: Celery setup and configuration
- Day 5-7: Core detection logic implementation

### Week 2: Messaging & Templates
- Day 8-10: Email/SMS template development
- Day 11-12: Message sending implementation
- Day 13-14: Unsubscribe mechanism

### Week 3: Dashboard & Testing
- Day 15-17: Visibility dashboard development
- Day 18-19: Integration testing
- Day 20-21: Load testing

### Week 4: Soft Launch
- Day 22-23: Deploy to staging environment
- Day 24-25: Enable for 5% of users
- Day 26-28: Monitor and fix issues

### Week 5: Full Rollout
- Day 29-30: Enable for 50% of users
- Day 31-35: Monitor performance and optimize

### Week 6+: Optimization
- Ongoing: A/B test different message templates
- Ongoing: Monitor completion rates
- Ongoing: Adjust frequency based on data

---

## Success Metrics

### Primary KPIs
- **Course Completion Rate**: 35% of reminded users complete course within 21 days
- **Email Delivery Rate**: >95%
- **SMS Delivery Rate**: >98%
- **Unsubscribe Rate**: <2% per campaign

### Secondary KPIs
- **Email Open Rate**: >30%
- **Email Click Rate**: >8%
- **SMS Click Rate**: >15%
- **Time to Completion**: Average days from first reminder to course completion

---

## Cost Estimation

### Per-User Cost (Monthly)

**Assumptions:**
- 10,000 active notifications
- Average 4 emails per user per month
- Average 0.3 SMS per user per month

**Email Costs (SendGrid):**
- 40,000 emails/month × $0.0001 = $4.00

**SMS Costs (Twilio):**
- 3,000 SMS/month × $0.05 = $150.00

**Infrastructure Costs:**
- Redis (managed): $20/month
- Celery workers (2× 2GB): $40/month

**Total Monthly Cost: ~$214**

**Cost per reminded user: $0.02/month**

---

## Appendix

### Frequency Rules Summary

| Channel | Frequency | Condition |
|---------|-----------|-----------|
| Email | Once per week (7 days) | Always eligible |
| SMS | Once per month (30 days) | After 2+ emails sent |

### Stage Progression

| Stage | Description | Email Count | Characteristics |
|-------|-------------|-------------|-----------------|
| 1 | Initial reminder | 1 | Welcoming, progress-focused |
| 2 | Follow-up | 2-3 | Value proposition, peer comparison |
| 3 | Urgency | 4-5 | Sunk cost, scarcity |
| 4+ | Maintenance | 6+ | Gentle nudges |

### Status Definitions

| Status | Description |
|--------|-------------|
| active | Currently receiving reminders |
| completed | User completed the course |
| unsubscribed | User opted out |
| paused | Manually paused by admin |

---

**Document Version:** 1.0  
**Created:** {{current_date}}  
**Owner:** AVP of Product, CLIRNET  
**Status:** Ready for Implementation
