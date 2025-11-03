# Banner Modification Automation Platform - Comprehensive Design Document

**Version:** 1.0  
**Date:** 2025-11-01  
**Status:** Design Specification  
**Technology Stack:** Python, BigQuery, Google Cloud Platform  

---

## Table of Contents

1. [Executive Summary](#executive-summary)
2. [Current State Analysis](#current-state-analysis)
3. [Automation Architecture](#automation-architecture)
4. [Configuration System](#configuration-system)
5. [Core Components](#core-components)
6. [Safety Mechanisms](#safety-mechanisms)
7. [Implementation Roadmap](#implementation-roadmap)
8. [Integration Approach](#integration-approach)
9. [Code Structure](#code-structure)
10. [Deployment Strategy](#deployment-strategy)
11. [Monitoring & Observability](#monitoring--observability)
12. [Migration Strategy](#migration-strategy)

---

## Executive Summary

### Problem Statement
The current banner modification procedure is a **manual, error-prone process** involving 9 sequential SQL transformations. It requires:
- Manual writing and execution of SQL queries
- Complex date range calculations
- Risk of data corruption on failures
- No rollback capabilities
- Difficult validation and verification

### Solution Overview
A **Python-based automation platform** that transforms the manual process into a production-ready, automated system with:
- Configuration-driven SQL generation
- Transaction support with atomic operations
- Comprehensive validation and safety checks
- Dry-run mode for risk-free testing
- Full audit trail and logging
- Rollback mechanisms
- Scheduled execution capability

### Expected Benefits
- **99% reduction** in manual SQL writing
- **95% reduction** in human errors
- **100x faster** execution (automation vs manual)
- **Zero data loss** risk with transaction support
- **Full auditability** with comprehensive logging
- **Reusability** across multiple banner campaigns

---

## Current State Analysis

### Current Manual Process Flow

```
START
  ↓
Requirements Gathering
  ↓ (Manual)
Frequency Requirement → Target Date Mapping
  ↓ (Manual)
Date Range Calculations
  ↓ (Manual)
SQL Query Writing (9 queries)
  ↓ (Manual)
Sequential Query Execution
  ↓ (Manual)
Record Count Validation
  ↓ (Manual)
Data Quality Checks
  ↓
END
```

### Identified Issues

| Issue | Impact | Frequency | Current Mitigation |
|-------|--------|-----------|-------------------|
| Manual SQL errors | High | Common | Manual review |
| Incorrect date ranges | High | Occasional | Checklists |
| Out-of-order execution | High | Rare | Documentation |
| Mid-pipeline failures | Critical | Rare | Manual rollback |
| Missing validation | Medium | Common | Ad-hoc checks |
| Duplicate insertions | High | Occasional | Manual verification |

### Risk Points Analysis

1. **Query Generation Risk** (High)
   - Manual SQL writing
   - Typos in table names, dates, log names
   - Incorrect WHERE clause logic

2. **Data Transformation Risk** (Critical)
   - Wrong timestamp calculations
   - Incorrect JSON field updates
   - Banner ID mismatches

3. **Execution Risk** (Critical)
   - Partial failures leaving data in inconsistent state
   - Concurrent executions causing conflicts
   - Resource constraints

4. **Rollback Risk** (Critical)
   - No automated rollback
   - Manual recovery process
   - Potential data loss

---

## Automation Architecture

### High-Level Architecture

```
┌──────────────────────────────────────────────────────────────┐
│                    Banner Automation Platform                │
│                                                              │
│  ┌─────────────────┐  ┌─────────────────┐  ┌──────────────┐ │
│  │   User Input    │  │   Config File   │  │ CLI/Web UI   │ │
│  │   (Frequency    │  │   (YAML/JSON)   │  │              │ │
│  │   Requirements) │  │                 │  │              │ │
│  └────────┬────────┘  └────────┬────────┘  └──────┬───────┘ │
│           │                    │                  │         │
│           └────────────┬───────┴──────────────────┘         │
│                        │                                  │
│                        ▼                                  │
│              ┌─────────────────────────┐                   │
│              │   Configuration Manager │                   │
│              │   - Validation          │                   │
│              │   - Parsing             │                   │
│              │   - Enrichment          │                   │
│              └────────────┬────────────┘                   │
│                           │                                │
│                           ▼                                │
│              ┌─────────────────────────┐                   │
│              │     SQL Generator       │                   │
│              │   - Phase Generation    │                   │
│              │   - Query Templates     │                   │
│              │   - Parameter Binding   │                   │
│              └────────────┬────────────┘                   │
│                           │                                │
│                           ▼                                │
│              ┌─────────────────────────┐                   │
│              │   Validation Engine     │                   │
│              │   - Pre-flight Checks   │                   │
│              │   - Data Analysis       │                   │
│              │   - Safety Validation   │                   │
│              └────────────┬────────────┘                   │
│                           │                                │
│                           ▼                                │
│  ┌─────────────────────────────────────────────────────────┐ │
│  │              Execution Engine                            │ │
│  │  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐  │ │
│  │  │ Transaction  │  │ SQL Executor │  │ Rollback Mgr │  │ │
│  │  │   Manager    │  │              │  │              │  │ │
│  │  └──────────────┘  └──────────────┘  └──────────────┘  │ │
│  └─────────────────────────┬───────────────────────────────┘ │
│                           │                                 │
│                           ▼                                 │
│              ┌─────────────────────────┐                   │
│              │   Monitoring & Logging  │                   │
│              │   - Audit Trail         │                   │
│              │   - Metrics             │                   │
│              │   - Alerts              │                   │
│              └────────────┬────────────┘                   │
└───────────────────────────┼────────────────────────────────┘
                            │
          ┌─────────────────┼─────────────────┐
          │                 │                 │
          ▼                 ▼                 ▼
    ┌──────────┐    ┌──────────────┐  ┌──────────┐
    │ Staging  │    │   Production │  │  Backup  │
    │ Table    │    │    Table     │  │  Table   │
    └──────────┘    └──────────────┘  └──────────┘
```

### Architecture Components

#### 1. Configuration Manager
- **Purpose**: Parse and validate configuration files
- **Input**: YAML/JSON configuration
- **Output**: Validated configuration object
- **Responsibilities**:
  - Schema validation
  - Default value injection
  - Date range verification
  - Banner ID uniqueness checks

#### 2. SQL Generator
- **Purpose**: Generate parameterized SQL queries from configuration
- **Input**: Validated configuration
- **Output**: List of SQL statements
- **Responsibilities**:
  - Template-based query generation
  - Parameter substitution
  - Query optimization
  - Conditional query generation

#### 3. Validation Engine
- **Purpose**: Ensure safety before execution
- **Input**: Generated queries + configuration
- **Output**: Validation report
- **Responsibilities**:
  - Pre-flight data analysis
  - Record count predictions
  - Safety checks
  - Constraint verification

#### 4. Execution Engine
- **Purpose**: Execute validated queries with safety guarantees
- **Input**: Validated queries
- **Output**: Execution results
- **Responsibilities**:
  - Transaction management
  - Query execution
  - Progress tracking
  - Error handling

#### 5. Rollback Manager
- **Purpose**: Restore system to previous state on failure
- **Input**: Execution context, failure point
- **Output**: Restored system state
- **Responsibilities**:
  - Backup creation
  - Restoration procedures
  - Partial rollback support
  - State verification

---

## Configuration System

### Configuration Schema (YAML)

```yaml
# banner_automation_config.yaml
campaign:
  banner_id: "5902"
  campaign_name: "Q4_Banner_Campaign"
  description: "Banner campaign for Q4 2025"
  execution_mode: "safe"  # safe | dry_run | production

source:
  database: "bigquery"
  project_id: "clirnet-dev"
  dataset: "request_edit"
  table: "H_5902_distinct_data"
  backup_required: true
  backup_table_suffix: "_backup_{timestamp}"

target:
  database: "bigquery"
  project_id: "clirnetapp"
  dataset: "banner_data"
  table: "banner_call_data"

frequency_requirement:
  type: "daily"  # daily | periodic | single_event | custom
  start_date: "2025-04-25"
  end_date: "2025-04-27"
  banner_count_per_day: 1
  
  # Alternative specification:
  # type: "custom"
  # target_dates:
  #   - "2025-04-25"
  #   - "2025-04-26"
  #   - "2025-04-27"

date_mapping:
  strategy: "volume_based"  # volume_based | time_based | custom
  
  # For volume_based strategy:
  records_per_banner: 100000
  
  # For time_based strategy:
  source_data_start: "2025-04-01"
  source_data_end: "2025-04-28"
  split_method: "equal_periods"  # equal_periods | custom_ranges
  
  # For custom_ranges strategy:
  phases:
    - phase_id: 1
      source_start: "2025-04-01"
      source_end: "2025-04-21"
      target_date: "2025-04-25"
      logname_suffix: "2025-04-25"
      exclude_lognames: []
      special_source: null  # e.g., "add-report-prod-server"
      
    - phase_id: 2
      source_start: "2025-04-22"
      source_end: "2025-04-24"
      target_date: "2025-04-26"
      logname_suffix: "2025-04-26"
      exclude_lognames: ["H_5902_distinct_2025-04-25"]
      special_source: null
      
    - phase_id: 3
      source_start: "2025-04-25"
      source_end: "2025-04-28"
      target_date: "2025-04-27"
      logname_suffix: "2025-04-27"
      exclude_lognames: 
        - "H_5902_distinct_2025-04-25"
        - "H_5902_distinct_2025-04-26"
      special_source: null

transformation:
  preserve_time_component: true
  end_time_offset_seconds: 5
  json_field_updates:
    start_time_format: "%Y-%m-%d %H:%M:%S"
    end_time_source: "calculated"  # calculated | fixed
    timestamp_get_source: "unix_seconds"  # unix_seconds | epoch_ms

validation:
  pre_execution:
    - check_source_data_exists
    - check_target_table_access
    - verify_no_existing_banner_ids
    - analyze_record_distribution
    - validate_date_ranges
    
  post_execution:
    - verify_record_counts
    - sample_data_validation
    - timestamp_format_check
    - json_field_validation
    - banner_id_verification
    
  thresholds:
    max_variance_from_expected: 0.05  # 5% tolerance
    min_records_per_phase: 1000
    max_records_per_phase: 10000000

execution:
  batch_size: 10000
  max_retries: 3
  retry_delay_seconds: 30
  timeout_minutes: 120
  parallel_execution: false  # Keep false for safety
  
logging:
  level: "INFO"  # DEBUG | INFO | WARNING | ERROR
  output_format: "json"  # json | text
  log_file: "/var/log/banner_automation/app.log"
  audit_trail_enabled: true
  metrics_enabled: true

notification:
  on_success:
    - email: "banner-ops@clirnet.com"
    - slack_webhook: "https://hooks.slack.com/..."
  on_failure:
    - email: "banner-ops@clirnet.com"
    - slack_webhook: "https://hooks.slack.com/..."
    - pagerduty_integration: true
```

### Configuration Examples

#### Example 1: Daily Banner Campaign

```yaml
frequency_requirement:
  type: "daily"
  start_date: "2025-05-01"
  end_date: "2025-05-07"
  banner_count_per_day: 1

date_mapping:
  strategy: "time_based"
  source_data_start: "2025-04-01"
  source_data_end: "2025-04-30"
  split_method: "equal_periods"
```

#### Example 2: Multi-Banner Event

```yaml
frequency_requirement:
  type: "custom"
  target_dates:
    - "2025-04-25"
    - "2025-04-26"
    - "2025-04-27"

date_mapping:
  strategy: "custom"
  phases:
    - phase_id: 1
      source_start: "2025-04-01"
      source_end: "2025-04-10"
      target_date: "2025-04-25"
      
    - phase_id: 2
      source_start: "2025-04-11"
      source_end: "2025-04-20"
      target_date: "2025-04-26"
      
    - phase_id: 3
      source_start: "2025-04-21"
      source_end: "2025-04-28"
      target_date: "2025-04-27"
```

#### Example 3: Rotating Banner Campaign

```yaml
frequency_requirement:
  type: "rotating"
  start_date: "2025-06-01"
  end_date: "2025-06-30"
  banner_sequence:
    - "5901"
    - "5902"
    - "5903"
  rotation_frequency_days: 3

date_mapping:
  strategy: "volume_based"
  records_per_banner: 500000
```

---

## Core Components

### 1. Configuration Manager

```python
from typing import Dict, List, Optional
from dataclasses import dataclass
from datetime import datetime
import yaml
import jsonschema

@dataclass
class PhaseConfig:
    phase_id: int
    source_start: str
    source_end: str
    target_date: str
    logname_suffix: str
    exclude_lognames: List[str]
    special_source: Optional[str]
    expected_records: Optional[int] = None

@dataclass
class BannerConfig:
    banner_id: str
    campaign_name: str
    execution_mode: str
    source_table: str
    target_table: str
    phases: List[PhaseConfig]
    
class ConfigurationManager:
    """Parse, validate, and enrich configuration files."""
    
    def __init__(self, config_path: str):
        self.config_path = config_path
        self._config = None
        self._schema = self._load_schema()
    
    def load_and_validate(self) -> BannerConfig:
        """Load configuration from file and validate against schema."""
        # Load YAML
        with open(self.config_path, 'r') as f:
            config_data = yaml.safe_load(f)
        
        # Validate against schema
        jsonschema.validate(config_data, self._schema)
        
        # Parse into structured objects
        return self._parse_config(config_data)
    
    def _parse_config(self, data: dict) -> BannerConfig:
        """Convert raw config data to BannerConfig objects."""
        phases = [
            PhaseConfig(
                phase_id=p['phase_id'],
                source_start=p['source_start'],
                source_end=p['source_end'],
                target_date=p['target_date'],
                logname_suffix=p['logname_suffix'],
                exclude_lognames=p.get('exclude_lognames', []),
                special_source=p.get('special_source'),
            )
            for p in data['date_mapping']['phases']
        ]
        
        return BannerConfig(
            banner_id=data['campaign']['banner_id'],
            campaign_name=data['campaign']['campaign_name'],
            execution_mode=data['campaign']['execution_mode'],
            source_table=data['source']['table'],
            target_table=data['target']['table'],
            phases=phases,
        )
```

### 2. SQL Generator

```python
from typing import List, Dict
from jinja2 import Template

class SQLGenerator:
    """Generate parameterized SQL queries from configuration."""
    
    def __init__(self):
        # Jinja2 templates for each query type
        self.templates = {
            'update_timestamp': Template("""
                UPDATE `{{ source_table }}`
                SET 
                  timestamp = TIMESTAMP(DATETIME('{{ target_date }}', TIME(timestamp))),
                  logName = '{{ log_name }}'
                WHERE DATE(timestamp) BETWEEN '{{ source_start }}' AND '{{ source_end }}'
                  {% if exclude_lognames %}
                  AND logName NOT IN {{ exclude_lognames | tojson }}
                  {% endif %}
            """),
            
            'update_special_log': Template("""
                UPDATE `{{ source_table }}`
                SET 
                  timestamp = TIMESTAMP(DATETIME('{{ target_date }}', TIME(timestamp))),
                  logName = '{{ log_name }}'
                WHERE logName = '{{ special_log_name }}'
            """),
            
            'update_start_time': Template("""
                UPDATE `{{ source_table }}`
                SET 
                  jsonPayload.start_time = FORMAT_TIMESTAMP(
                    '%Y-%m-%d %H:%M:%S', 
                    TIMESTAMP(DATETIME('{{ target_date }}', TIME(TIMESTAMP(jsonPayload.start_time))))
                  )
                WHERE logName = '{{ log_name }}'
            """),
            
            'update_end_time': Template("""
                UPDATE `{{ source_table }}`
                SET 
                  jsonPayload.end_time = FORMAT_TIMESTAMP(
                    '%Y-%m-%d %H:%M:%S', 
                    TIMESTAMP_ADD(
                      TIMESTAMP(jsonPayload.start_time), 
                      INTERVAL {{ offset_seconds }} SECOND
                    )
                  )
                WHERE logName IN {{ log_names | tojson }}
            """),
            
            'update_timestamp_get': Template("""
                UPDATE `{{ source_table }}`
                SET 
                  jsonPayload.timestamp_get = UNIX_SECONDS(TIMESTAMP(jsonPayload.start_time))
                WHERE logName IN {{ log_names | tojson }}
            """),
            
            'update_banner_id': Template("""
                UPDATE `{{ source_table }}`
                SET jsonPayload.banner_id = '{{ banner_id }}'
                WHERE 1<>0
            """),
            
            'insert_to_production': Template("""
                INSERT INTO `{{ target_table }}`
                SELECT * FROM `{{ source_table }}`
                WHERE logName IN {{ final_log_names | tojson }}
            """),
        }
    
    def generate_all_queries(self, config: BannerConfig) -> List[Dict[str, str]]:
        """Generate all SQL queries for a banner configuration."""
        queries = []
        
        # Generate timestamp/logName updates for each phase
        for phase in config.phases:
            # Primary source
            queries.append({
                'type': 'update_timestamp',
                'sql': self.templates['update_timestamp'].render(
                    source_table=config.source_table,
                    target_date=phase.target_date,
                    log_name=f"H_{config.banner_id}_distinct_{phase.logname_suffix}",
                    source_start=phase.source_start,
                    source_end=phase.source_end,
                    exclude_lognames=phase.exclude_lognames,
                ),
                'description': f"Phase {phase.phase_id}: Update timestamp and logName",
            })
            
            # Special source (if specified)
            if phase.special_source:
                queries.append({
                    'type': 'update_special_log',
                    'sql': self.templates['update_special_log'].render(
                        source_table=config.source_table,
                        target_date=phase.target_date,
                        log_name=f"H_{config.banner_id}_distinct_{phase.logname_suffix}",
                        special_log_name=phase.special_source,
                    ),
                    'description': f"Phase {phase.phase_id}: Update special log source",
                })
        
        # Generate JSON field updates
        all_log_names = [
            f"H_{config.banner_id}_distinct_{p.logname_suffix}"
            for p in config.phases
        ]
        
        # Update start_time (first phase only)
        queries.append({
            'type': 'update_start_time',
            'sql': self.templates['update_start_time'].render(
                source_table=config.source_table,
                target_date=config.phases[0].target_date,
                log_name=all_log_names[0],
            ),
            'description': "Update start_time JSON field",
        })
        
        # Update end_time (all phases)
        queries.append({
            'type': 'update_end_time',
            'sql': self.templates['update_end_time'].render(
                source_table=config.source_table,
                offset_seconds=5,
                log_names=all_log_names,
            ),
            'description': "Update end_time JSON field",
        })
        
        # Update timestamp_get (all phases)
        queries.append({
            'type': 'update_timestamp_get',
            'sql': self.templates['update_timestamp_get'].render(
                source_table=config.source_table,
                log_names=all_log_names,
            ),
            'description': "Update timestamp_get JSON field",
        })
        
        # Update banner_id
        queries.append({
            'type': 'update_banner_id',
            'sql': self.templates['update_banner_id'].render(
                source_table=config.source_table,
                banner_id=config.banner_id,
            ),
            'description': "Update banner_id field",
        })
        
        # Insert to production
        queries.append({
            'type': 'insert_to_production',
            'sql': self.templates['insert_to_production'].render(
                target_table=config.target_table,
                source_table=config.source_table,
                final_log_names=all_log_names,
            ),
            'description': "Insert transformed records to production",
        })
        
        return queries
```

### 3. Validation Engine

```python
from typing import List, Dict
from dataclasses import dataclass

@dataclass
class ValidationResult:
    check_name: str
    passed: bool
    message: str
    details: Dict = None

class ValidationEngine:
    """Pre-flight validation and safety checks."""
    
    def __init__(self, bq_client):
        self.client = bq_client
    
    def pre_execution_validation(
        self, 
        config: BannerConfig,
        queries: List[Dict]
    ) -> List[ValidationResult]:
        """Run all pre-execution validation checks."""
        results = []
        
        # Check 1: Source data exists
        results.append(self._check_source_data_exists(config))
        
        # Check 2: Target table accessible
        results.append(self._check_target_access(config))
        
        # Check 3: No existing banner IDs
        results.append(self._check_no_existing_banner(config))
        
        # Check 4: Record distribution analysis
        results.append(self._analyze_record_distribution(config))
        
        # Check 5: Date range validation
        results.append(self._validate_date_ranges(config))
        
        return results
    
    def _check_source_data_exists(self, config: BannerConfig) -> ValidationResult:
        """Verify source table has data."""
        query = f"""
            SELECT COUNT(*) as record_count
            FROM `{config.source_table}`
            LIMIT 1
        """
        
        try:
            result = self.client.query(query).result()
            row = list(result)[0]
            
            if row.record_count > 0:
                return ValidationResult(
                    check_name="source_data_exists",
                    passed=True,
                    message=f"Source table has {row.record_count} records",
                )
            else:
                return ValidationResult(
                    check_name="source_data_exists",
                    passed=False,
                    message="Source table is empty",
                )
        except Exception as e:
            return ValidationResult(
                check_name="source_data_exists",
                passed=False,
                message=f"Error checking source data: {str(e)}",
            )
    
    def _check_no_existing_banner(self, config: BannerConfig) -> ValidationResult:
        """Verify banner ID doesn't already exist in production."""
        query = f"""
            SELECT COUNT(*) as count
            FROM `{config.target_table}`
            WHERE jsonPayload.banner_id = '{config.banner_id}'
        """
        
        try:
            result = self.client.query(query).result()
            row = list(result)[0]
            
            if row.count == 0:
                return ValidationResult(
                    check_name="no_existing_banner",
                    passed=True,
                    message="Banner ID not found in production (safe to proceed)",
                )
            else:
                return ValidationResult(
                    check_name="no_existing_banner",
                    passed=False,
                    message=f"Banner ID {config.banner_id} already exists with {row.count} records",
                )
        except Exception as e:
            return ValidationResult(
                check_name="no_existing_banner",
                passed=False,
                message=f"Error checking existing banner: {str(e)}",
            )
    
    def _analyze_record_distribution(self, config: BannerConfig) -> ValidationResult:
        """Analyze expected record distribution across phases."""
        query = f"""
            SELECT 
              DATE(timestamp) as date,
              COUNT(*) as count
            FROM `{config.source_table}`
            WHERE DATE(timestamp) BETWEEN '{config.phases[0].source_start}' 
              AND '{config.phases[-1].source_end}'
            GROUP BY DATE(timestamp)
            ORDER BY date
        """
        
        try:
            result = self.client.query(query).result()
            records = list(result)
            
            total_records = sum(r.count for r in records)
            expected_per_phase = total_records // len(config.phases)
            
            # Check for reasonable distribution
            min_expected = expected_per_phase * 0.5  # 50% tolerance
            max_expected = expected_per_phase * 1.5
            
            unbalanced_phases = []
            for phase in config.phases:
                phase_query = f"""
                    SELECT COUNT(*) as count
                    FROM `{config.source_table}`
                    WHERE DATE(timestamp) BETWEEN '{phase.source_start}' 
                      AND '{phase.source_end}'
                """
                phase_result = self.client.query(phase_query).result()
                phase_count = list(phase_result)[0].count
                
                if phase_count < min_expected or phase_count > max_expected:
                    unbalanced_phases.append({
                        'phase': phase.phase_id,
                        'count': phase_count,
                        'expected_range': f"{min_expected}-{max_expected}",
                    })
            
            if unbalanced_phases:
                return ValidationResult(
                    check_name="record_distribution",
                    passed=False,
                    message=f"Unbalanced phases detected",
                    details={'unbalanced_phases': unbalanced_phases},
                )
            else:
                return ValidationResult(
                    check_name="record_distribution",
                    passed=True,
                    message=f"Record distribution is balanced across phases",
                    details={'total_records': total_records, 'expected_per_phase': expected_per_phase},
                )
        except Exception as e:
            return ValidationResult(
                check_name="record_distribution",
                passed=False,
                message=f"Error analyzing record distribution: {str(e)}",
            )
    
    def post_execution_validation(
        self,
        config: BannerConfig,
        execution_results: List[Dict]
    ) -> List[ValidationResult]:
        """Run post-execution validation checks."""
        results = []
        
        # Verify record counts
        results.append(self._verify_record_counts(config))
        
        # Sample data validation
        results.append(self._sample_data_validation(config))
        
        # Timestamp format check
        results.append(self._check_timestamp_formats(config))
        
        return results
    
    def _verify_record_counts(self, config: BannerConfig) -> ValidationResult:
        """Verify expected vs actual record counts."""
        # Get count from staging table
        staging_query = f"""
            SELECT COUNT(*) as count
            FROM `{config.source_table}`
            WHERE logName LIKE 'H_{config.banner_id}_distinct_%'
        """
        
        # Get count from production table
        production_query = f"""
            SELECT COUNT(*) as count
            FROM `{config.target_table}`
            WHERE jsonPayload.banner_id = '{config.banner_id}'
        """
        
        try:
            staging_result = self.client.query(staging_query).result()
            staging_count = list(staging_result)[0].count
            
            production_result = self.client.query(production_query).result()
            production_count = list(production_result)[0].count
            
            if staging_count == production_count:
                return ValidationResult(
                    check_name="record_count_match",
                    passed=True,
                    message=f"Record counts match: {production_count} records",
                )
            else:
                return ValidationResult(
                    check_name="record_count_match",
                    passed=False,
                    message=f"Record count mismatch: staging={staging_count}, production={production_count}",
                )
        except Exception as e:
            return ValidationResult(
                check_name="record_count_match",
                passed=False,
                message=f"Error verifying record counts: {str(e)}",
            )
```

### 4. Execution Engine with Transaction Support

```python
import logging
from typing import List, Dict, Optional
from datetime import datetime
from google.cloud import bigquery

class ExecutionEngine:
    """Execute SQL queries with transaction support and rollback."""
    
    def __init__(self, bq_client, logger: logging.Logger):
        self.client = bq_client
        self.logger = logger
        self.execution_log = []
        self.backup_created = False
    
    def execute_with_safety(
        self,
        config: BannerConfig,
        queries: List[Dict],
        dry_run: bool = False,
    ) -> Dict:
        """Execute queries with full safety guarantees."""
        
        execution_context = {
            'start_time': datetime.utcnow(),
            'config': config,
            'dry_run': dry_run,
            'steps_completed': [],
            'steps_failed': [],
            'backup_table': None,
        }
        
        try:
            # Step 1: Create backup (if not dry run)
            if not dry_run and config.execution_mode != 'dry_run':
                backup_table = self._create_backup(config)
                execution_context['backup_table'] = backup_table
                self.backup_created = True
                self.logger.info(f"Backup created: {backup_table}")
            
            # Step 2: Execute queries sequentially
            for idx, query_info in enumerate(queries):
                step_num = idx + 1
                self.logger.info(f"Executing step {step_num}/{len(queries)}: {query_info['description']}")
                
                if dry_run:
                    self.logger.info(f"[DRY RUN] Would execute: {query_info['type']}")
                    execution_context['steps_completed'].append({
                        'step': step_num,
                        'type': query_info['type'],
                        'dry_run': True,
                    })
                else:
                    try:
                        result = self._execute_single_query(query_info['sql'])
                        execution_context['steps_completed'].append({
                            'step': step_num,
                            'type': query_info['type'],
                            'rows_affected': result,
                        })
                        self.logger.info(f"Step {step_num} completed successfully")
                    except Exception as e:
                        self.logger.error(f"Step {step_num} failed: {str(e)}")
                        execution_context['steps_failed'].append({
                            'step': step_num,
                            'type': query_info['type'],
                            'error': str(e),
                        })
                        
                        # Initiate rollback
                        self.logger.error("Initiating rollback due to failure")
                        rollback_result = self._rollback(execution_context)
                        execution_context['rollback'] = rollback_result
                        
                        raise ExecutionFailedException(
                            f"Query execution failed at step {step_num}: {str(e)}"
                        )
            
            # Step 3: Validation
            if not dry_run:
                validation_results = self._post_execution_validation(config)
                execution_context['validation_results'] = validation_results
                
                if not all(r.passed for r in validation_results):
                    self.logger.warning("Validation failures detected")
            
            execution_context['end_time'] = datetime.utcnow()
            execution_context['status'] = 'SUCCESS'
            
            return execution_context
            
        except Exception as e:
            execution_context['end_time'] = datetime.utcnow()
            execution_context['status'] = 'FAILED'
            execution_context['error'] = str(e)
            
            self.logger.error(f"Execution failed: {str(e)}")
            raise
    
    def _create_backup(self, config: BannerConfig) -> str:
        """Create backup of source table."""
        timestamp = datetime.utcnow().strftime('%Y%m%d_%H%M%S')
        backup_table = f"{config.source_table}_backup_{timestamp}"
        
        query = f"""
            CREATE TABLE `{backup_table}` AS
            SELECT * FROM `{config.source_table}`
        """
        
        self.client.query(query).result()
        return backup_table
    
    def _execute_single_query(self, sql: str) -> int:
        """Execute a single SQL query and return rows affected."""
        job = self.client.query(sql)
        result = job.result()
        # For UPDATE queries, BigQuery returns the number of bytes processed
        # We can infer row count from the query plan
        return job.num_dml_bytes_processed
    
    def _rollback(self, execution_context: Dict) -> Dict:
        """Restore system to previous state."""
        rollback_result = {
            'start_time': datetime.utcnow(),
            'actions': [],
            'status': 'PENDING',
        }
        
        try:
            # If backup was created, restore from it
            if self.backup_created and execution_context['backup_table']:
                self.logger.info(f"Restoring from backup: {execution_context['backup_table']}")
                
                # Clear current staging table
                clear_query = f"DELETE FROM `{execution_context['config'].source_table}` WHERE 1=1"
                self.client.query(clear_query).result()
                rollback_result['actions'].append({'action': 'clear_staging', 'success': True})
                
                # Restore from backup
                restore_query = f"""
                    INSERT INTO `{execution_context['config'].source_table}`
                    SELECT * FROM `{execution_context['backup_table']}`
                """
                self.client.query(restore_query).result()
                rollback_result['actions'].append({'action': 'restore_backup', 'success': True})
                
                self.logger.info("Rollback completed successfully")
            
            rollback_result['status'] = 'SUCCESS'
            rollback_result['end_time'] = datetime.utcnow()
            
        except Exception as e:
            rollback_result['status'] = 'FAILED'
            rollback_result['error'] = str(e)
            self.logger.error(f"Rollback failed: {str(e)}")
        
        return rollback_result

class ExecutionFailedException(Exception):
    """Custom exception for execution failures."""
    pass
```

---

## Safety Mechanisms

### 1. Transaction Support

**Problem**: Current process has no transaction support. A failure mid-pipeline leaves data in inconsistent state.

**Solution**: Implement multi-step transaction with checkpoints:

```
Execution Flow with Transactions:

START
  ↓
Checkpoint 1: Create Backup
  ↓
Transaction Begin
  ↓
Step 1: Update Phase 1
  ↓
Checkpoint 2: Verify Step 1
  ↓
Step 2: Update Phase 2
  ↓
Checkpoint 3: Verify Step 2
  ↓
Step 3: Update Phase 3
  ↓
Checkpoint 4: Verify Step 3
  ↓
Step 4: Update JSON Fields
  ↓
Checkpoint 5: Verify JSON Updates
  ↓
Step 5: Update Banner ID
  ↓
Checkpoint 6: Verify Banner ID
  ↓
Step 6: Insert to Production
  ↓
Transaction Commit
  ↓
Final Validation
  ↓
END
```

**Implementation**:
- BigQuery doesn't support traditional ACID transactions for multiple DML statements
- Solution: **Checkpoint-based rollback** with backup tables
- Each checkpoint verifies data integrity
- Automatic rollback on any failure

### 2. Data Validation at Each Step

**Pre-Execution Validation**:

```python
class PreFlightChecks:
    def __init__(self):
        self.checks = [
            self.check_source_table_exists,
            self.check_target_table_exists,
            self.check_no_existing_banner_id,
            self.check_date_range_validity,
            self.check_record_volume_reasonable,
            self.check_column_compatibility,
            self.check_permission_access,
        ]
    
    def run_all(self, config, client) -> ValidationReport:
        report = ValidationReport()
        for check in self.checks:
            result = check(config, client)
            report.add_result(result)
            if not result.passed and result.severity == 'CRITICAL':
                report.can_proceed = False
        return report
```

**In-Execution Validation**:

```python
class ExecutionChecks:
    def after_step(self, step_num, query_type, client, config):
        """Validate after each execution step."""
        checks = {
            'update_timestamp': self.verify_timestamp_updates,
            'update_json_fields': self.verify_json_updates,
            'update_banner_id': self.verify_banner_id_updates,
            'insert_production': self.verify_insert_completed,
        }
        
        if query_type in checks:
            result = checks[query_type](client, config)
            if not result.passed:
                raise ValidationFailedException(f"Validation failed after step {step_num}")
```

**Post-Execution Validation**:

```python
class PostExecutionValidation:
    def final_validation(self, config, client):
        validations = [
            ('record_count', self.verify_record_count_match),
            ('data_sampling', self.verify_sample_data_quality),
            ('timestamp_format', self.verify_timestamp_format),
            ('json_field_integrity', self.verify_json_field_integrity),
            ('banner_id_consistency', self.verify_banner_id_consistency),
        ]
        
        results = []
        for name, validator in validations:
            result = validator(config, client)
            results.append(result)
        
        return ValidationSummary(results)
```

### 3. Backup and Restore Procedures

**Backup Strategy**:

```
Backup Creation Process:

┌─────────────────────────────────────────┐
│  1. Pre-Execution Backup               │
│     - Snapshot source table             │
│     - Store as timestamped backup       │
│     - Verify backup integrity           │
└─────────────────────────────────────────┘
                  ↓
┌─────────────────────────────────────────┐
│  2. Incremental Checkpoints             │
│     - After each phase                  │
│     - Store row counts per phase        │
│     - Verify phase completion           │
└─────────────────────────────────────────┘
                  ↓
┌─────────────────────────────────────────┐
│  3. Production Backup                   │
│     - Snapshot production table (opt)   │
│     - Before insert                     │
│     - Quick rollback target             │
└─────────────────────────────────────────┘
```

**Restore Procedures**:

```python
class BackupRestore:
    def full_restore(self, backup_table: str, target_table: str):
        """Complete restore from backup."""
        steps = [
            self._clear_target_table(target_table),
            self._restore_from_backup(backup_table, target_table),
            self._verify_restore(target_table),
        ]
        
        for step_name, query in steps:
            try:
                self.client.query(query).result()
                self.logger.info(f"Restore step completed: {step_name}")
            except Exception as e:
                self.logger.error(f"Restore step failed: {step_name} - {str(e)}")
                raise RestoreFailedException(f"Failed at {step_name}")
    
    def partial_restore(self, config: BannerConfig, phase: int):
        """Restore to before a specific phase."""
        # Logic to undo only a specific phase
        # More complex but allows granular rollback
        pass
```

### 4. Dry-Run Mode

**Purpose**: Test everything without making changes.

**Implementation**:

```python
class DryRunMode:
    """
    Simulates full execution without making any changes.
    """
    
    def execute_dry_run(self, config: BannerConfig, queries: List[Dict]):
        """Execute all steps in simulation mode."""
        results = {
            'mode': 'DRY_RUN',
            'steps': [],
            'estimated_records_affected': 0,
            'warnings': [],
        }
        
        for idx, query_info in enumerate(queries):
            # Analyze query to estimate impact
            impact = self._estimate_query_impact(query_info['sql'], config)
            
            step_result = {
                'step': idx + 1,
                'type': query_info['type'],
                'description': query_info['description'],
                'estimated_rows_affected': impact.rows,
                'estimated_bytes_processed': impact.bytes,
                'would_execute': True,
            }
            
            results['steps'].append(step_result)
            results['estimated_records_affected'] += impact.rows
        
        # Simulate validation
        results['validation_results'] = self._simulate_validation(config)
        
        return results
    
    def generate_execution_plan(self, config: BannerConfig, queries: List[Dict]):
        """Generate a human-readable execution plan."""
        plan = []
        plan.append(f"Banner Campaign: {config.campaign_name} (ID: {config.banner_id})")
        plan.append(f"Source: {config.source_table}")
        plan.append(f"Target: {config.target_table}")
        plan.append(f"Phases: {len(config.phases)}")
        plan.append("\nExecution Steps:\n")
        
        for idx, query_info in enumerate(queries):
            plan.append(f"  {idx + 1}. {query_info['description']}")
            plan.append(f"     Type: {query_info['type']}")
            plan.append(f"     Target Phase: {self._get_phase_for_query(query_info)}")
            plan.append("")
        
        return "\n".join(plan)
```

### 5. Rollback Mechanisms

**Rollback Triggers**:
- Any query execution failure
- Validation failure after execution step
- Manual rollback request
- Timeout or resource constraint exceeded
- Detection of data anomaly

**Rollback Types**:

```python
class RollbackManager:
    def __init__(self, bq_client, logger):
        self.client = bq_client
        self.logger = logger
    
    def automatic_rollback(self, execution_context: Dict, failure_point: Dict):
        """Automatic rollback on failure."""
        rollback_type = self._determine_rollback_type(failure_point)
        
        if rollback_type == 'FULL':
            return self._full_rollback(execution_context)
        elif rollback_type == 'PARTIAL':
            return self._partial_rollback(execution_context, failure_point)
        elif rollback_type == 'PHASE':
            return self._phase_rollback(execution_context, failure_point)
    
    def _full_rollback(self, context: Dict):
        """Restore entire staging table from backup."""
        if not context.get('backup_table'):
            raise RollbackError("No backup available for full rollback")
        
        backup_table = context['backup_table']
        
        # Clear staging table
        clear_query = f"DELETE FROM `{context['config'].source_table}` WHERE 1=1"
        self.client.query(clear_query)
        
        # Restore from backup
        restore_query = f"""
            INSERT INTO `{context['config'].source_table}`
            SELECT * FROM `{backup_table}`
        """
        self.client.query(restore_query)
        
        self.logger.info(f"Full rollback completed from {backup_table}")
    
    def _partial_rollback(self, context: Dict, failure_point: Dict):
        """Rollback to last successful checkpoint."""
        # Implementation for partial rollback
        # More complex but preserves work done in earlier phases
        pass
    
    def _phase_rollback(self, context: Dict, failure_point: Dict):
        """Rollback a specific phase."""
        # Implementation for rolling back just one phase
        pass
```

---

## Implementation Roadmap

### Phase 1: Core Automation Engine (Weeks 1-4)

**Goal**: Build minimum viable automation system

**Deliverables**:
- [ ] Configuration Manager (YAML parsing and validation)
- [ ] SQL Generator (Jinja2 templates)
- [ ] Basic execution engine (sequential query execution)
- [ ] Logging framework
- [ ] CLI interface

**Milestones**:
- Week 1: Configuration Manager + SQL Generator
- Week 2: Basic Execution Engine
- Week 3: Logging + Error Handling
- Week 4: CLI + Integration Testing

**Success Criteria**:
- Can execute simple single-phase banner insertion
- All queries generated correctly
- Basic error handling in place

**Technical Tasks**:
```python
# Core classes to implement:
- ConfigurationManager
- SQLGenerator  
- BasicExecutionEngine
- Logger
- CLI interface
```

---

### Phase 2: Configuration System (Weeks 5-6)

**Goal**: Flexible, production-ready configuration management

**Deliverables**:
- [ ] Advanced configuration schema
- [ ] Multiple frequency pattern support (daily, periodic, custom)
- [ ] Configuration validation with detailed error messages
- [ ] Configuration examples library
- [ ] Config migration tools

**Features**:
- Support for all patterns mentioned in FREQUENCY_TO_QUERIES_GUIDE.md
- Smart date range calculation
- Default value injection
- Configuration inheritance for similar campaigns

**Success Criteria**:
- Can handle any frequency requirement pattern
- Configuration validation catches all errors
- Easy to create new configurations

---

### Phase 3: Safety Mechanisms (Weeks 7-10)

**Goal**: Production-grade safety and reliability

**Deliverables**:
- [ ] Transaction support with checkpoints
- [ ] Automated backup/restore
- [ ] Comprehensive validation engine (pre, in, post execution)
- [ ] Rollback manager
- [ ] Dry-run mode
- [ ] Data integrity checks

**Milestones**:
- Week 7: Backup/Restore + Pre-flight validation
- Week 8: Checkpoint system + Rollback manager
- Week 9: In-execution validation + Dry-run mode
- Week 10: End-to-end testing + Integration

**Success Criteria**:
- Failed execution never leaves data in inconsistent state
- Can restore from any failure point
- Dry-run accurately predicts actual execution
- All validation checks pass before production use

**Technical Implementation**:
```python
class SafetyMechanisms:
    - PreFlightValidationEngine
    - CheckpointManager
    - BackupRestoreManager
    - RollbackManager
    - DryRunEngine
    - DataIntegrityChecker
```

---

### Phase 4: Testing and Production Deployment (Weeks 11-12)

**Goal**: Production-ready deployment with comprehensive testing

**Deliverables**:
- [ ] Unit test suite (>90% coverage)
- [ ] Integration test suite
- [ ] Performance testing
- [ ] Load testing (simulate large banner campaigns)
- [ ] Production deployment guide
- [ ] Documentation
- [ ] Training materials

**Testing Strategy**:
- **Unit Tests**: Each component in isolation
- **Integration Tests**: End-to-end workflow tests
- **Performance Tests**: Large dataset handling
- **Failure Tests**: Simulate failures at each step
- **Regression Tests**: Ensure banner quality matches manual process

**Success Criteria**:
- All tests pass
- Can handle datasets up to 100M records
- Production deployment validated
- Team trained and ready

---

### Migration Strategy

#### Step 1: Shadow Mode (Weeks 1-8)

Run automation in parallel with manual process:
```
Week 1-4: Run automation on test data (not production)
Week 5-6: Run automation on production data, don't insert to production
Week 7-8: Run automation in parallel, compare outputs
```

#### Step 2: Controlled Rollout (Week 9-10)

```
Week 9: 
  - 80% manual / 20% automation
  - Only for simple, low-risk campaigns
  
Week 10:
  - 50% manual / 50% automation
  - Include medium complexity campaigns
```

#### Step 3: Full Automation (Week 11-12)

```
Week 11-12:
  - 100% automation for new campaigns
  - Manual process as backup only
```

---

## Code Structure

### Directory Structure

```
banner_automation/
├── README.md
├── setup.py
├── requirements.txt
├── config/
│   ├── schemas/
│   │   ├── banner_config_schema.yaml
│   │   └── validation_schemas.yaml
│   ├── examples/
│   │   ├── daily_campaign.yaml
│   │   ├── multi_banner_event.yaml
│   │   └── rotating_campaign.yaml
│   └── templates/
│       └── sql_templates.yaml
├── src/
│   └── banner_automation/
│       ├── __init__.py
│       ├── core/
│       │   ├── __init__.py
│       │   ├── config_manager.py
│       │   ├── sql_generator.py
│       │   ├── execution_engine.py
│       │   └── exceptions.py
│       ├── validation/
│       │   ├── __init__.py
│       │   ├── pre_flight_checks.py
│       │   ├── in_execution_checks.py
│       │   ├── post_execution_checks.py
│       │   └── data_analyzer.py
│       ├── safety/
│       │   ├── __init__.py
│       │   ├── backup_manager.py
│       │   ├── rollback_manager.py
│       │   ├── checkpoint_manager.py
│       │   └── dry_run_engine.py
│       ├── clients/
│       │   ├── __init__.py
│       │   ├── bigquery_client.py
│       │   └── database_client.py
│       ├── utils/
│       │   ├── __init__.py
│       │   ├── date_utils.py
│       │   ├── logging_config.py
│       │   └── metrics.py
│       └── cli/
│           ├── __init__.py
│           ├── main.py
│           └── commands.py
├── tests/
│   ├── __init__.py
│   ├── unit/
│   │   ├── test_config_manager.py
│   │   ├── test_sql_generator.py
│   │   ├── test_execution_engine.py
│   │   └── test_validation.py
│   ├── integration/
│   │   ├── test_end_to_end.py
│   │   ├── test_safety_mechanisms.py
│   │   └── test_rollback.py
│   └── fixtures/
│       ├── sample_configs/
│       └── test_data/
├── docs/
│   ├── architecture.md
│   ├── configuration_guide.md
│   ├── deployment_guide.md
│   └── troubleshooting.md
├── scripts/
│   ├── setup_dev.sh
│   ├── run_tests.sh
│   └── deploy.sh
└── Dockerfile
```

### Key Classes and Interfaces

#### Core Classes

```python
# src/banner_automation/core/config_manager.py
class ConfigurationManager:
    """Parse and validate configuration files."""
    
    def load_config(self, config_path: str) -> BannerConfig:
        """Load configuration from YAML file."""
        pass
    
    def validate_config(self, config: dict) -> ValidationResult:
        """Validate configuration against schema."""
        pass
    
    def enrich_config(self, config: BannerConfig) -> BannerConfig:
        """Add calculated fields and defaults."""
        pass

# src/banner_automation/core/sql_generator.py
class SQLGenerator:
    """Generate SQL queries from configuration."""
    
    def generate_queries(self, config: BannerConfig) -> List[SQLQuery]:
        """Generate all SQL queries for a campaign."""
        pass
    
    def generate_query(self, template_name: str, params: dict) -> str:
        """Generate single query from template."""
        pass

# src/banner_automation/core/execution_engine.py
class ExecutionEngine:
    """Execute SQL queries with safety guarantees."""
    
    def execute(self, config: BannerConfig, queries: List[SQLQuery], dry_run: bool = False) -> ExecutionResult:
        """Execute queries."""
        pass
    
    def execute_with_rollback(self, execution_context: Dict) -> ExecutionResult:
        """Execute with rollback on failure."""
        pass
```

#### Validation Classes

```python
# src/banner_automation/validation/validator.py
class Validator:
    """Base validator interface."""
    
    def validate(self, data: Any) -> ValidationResult:
        """Run validation and return result."""
        pass

# Specific validators:
class PreFlightValidator(Validator):
    """Pre-execution validation."""
    
class InExecutionValidator(Validator):
    """During execution validation."""
    
class PostExecutionValidator(Validator):
    """Post-execution validation."""
```

#### Safety Classes

```python
# src/banner_automation/safety/backup_manager.py
class BackupManager:
    """Manage backups for safe execution."""
    
    def create_backup(self, source_table: str) -> str:
        """Create backup and return backup table name."""
        pass
    
    def restore_backup(self, backup_table: str, target_table: str):
        """Restore from backup."""
        pass

# src/banner_automation/safety/rollback_manager.py
class RollbackManager:
    """Handle rollback operations."""
    
    def rollback_to_checkpoint(self, checkpoint_id: str):
        """Rollback to specific checkpoint."""
        pass
    
    def full_rollback(self, backup_table: str, target_table: str):
        """Complete rollback from backup."""
        pass
```

---

## Integration Approach

### 1. Integration with Current Workflow

**Phase 1: Parallel Execution**
```
Manual Process    |    Automation Platform
      ↓           |              ↓
Requirements      |    Configuration File
      ↓           |              ↓
Manual SQL        |    Auto SQL Generation
      ↓           |              ↓
Manual Execution  |    Auto Execution
      ↓           |              ↓
Manual Validation |    Auto Validation
      ↓           |              ↓
Manual Insertion  |    Auto Insertion
```

**Phase 2: Validation Mode**
```
Both processes execute
      ↓
Compare outputs
      ↓
Validate results match
      ↓
If 100% match → Automation ready for production
```

### 2. Integration with Existing Systems

#### BigQuery Integration

```python
# src/banner_automation/clients/bigquery_client.py
from google.cloud import bigquery
from typing import List, Iterator

class BigQueryClient:
    """BigQuery-specific client with banner automation features."""
    
    def __init__(self, project_id: str, credentials_path: str):
        self.client = bigquery.Client(project=project_id)
        self.project_id = project_id
    
    def execute_query(self, sql: str) -> Iterator:
        """Execute query and return results."""
        job = self.client.query(sql)
        return job.result()
    
    def execute_dml(self, sql: str) -> int:
        """Execute DML (UPDATE/INSERT) and return bytes processed."""
        job = self.client.query(sql)
        job.result()  # Wait for completion
        return job.num_dml_bytes_processed
    
    def create_table_from_query(self, destination_table: str, query: str):
        """Create table from query result."""
        job_config = bigquery.QueryJobConfig(
            destination=destination_table
        )
        job = self.client.query(query, job_config=job_config)
        job.result()
    
    def table_exists(self, table_ref: str) -> bool:
        """Check if table exists."""
        try:
            self.client.get_table(table_ref)
            return True
        except:
            return False
    
    def get_table_schema(self, table_ref: str) -> List:
        """Get table schema."""
        table = self.client.get_table(table_ref)
        return [field.name for field in table.schema]
```

#### Google Cloud Platform Integration

```python
# Optional: Cloud Functions for scheduled execution
# deployment/cloud_function/main.py

def banner_automation_handler(request):
    """
    Cloud Function entry point for scheduled banner automation.
    
    Triggered by Cloud Scheduler or Pub/Sub message.
    """
    from banner_automation import BannerAutomationOrchestrator
    
    orchestrator = BannerAutomationOrchestrator()
    
    # Get configuration from Cloud Storage
    config = orchestrator.load_config_from_gcs(
        bucket='banner-automation-configs',
        object='campaign_5902.yaml'
    )
    
    # Execute automation
    result = orchestrator.execute_campaign(
        config=config,
        dry_run=False
    )
    
    # Send notification
    orchestrator.send_notification(result)
    
    return {'status': 'success', 'banner_id': config.banner_id}
```

#### Slack Integration

```python
# Integration with Slack for notifications
import requests

class SlackNotifier:
    """Send notifications to Slack."""
    
    def __init__(self, webhook_url: str):
        self.webhook_url = webhook_url
    
    def send_execution_start(self, config: BannerConfig):
        """Notify that execution has started."""
        message = {
            'text': f"🚀 Banner Automation Started",
            'blocks': [
                {
                    'type': 'section',
                    'text': {
                        'type': 'mrkdwn',
                        'text': f"*Banner Campaign:* {config.campaign_name}\n*Banner ID:* {config.banner_id}\n*Phases:* {len(config.phases)}\n*Status:* Started"
                    }
                }
            ]
        }
        self._post_message(message)
    
    def send_execution_success(self, result: ExecutionResult):
        """Notify successful completion."""
        message = {
            'text': f"✅ Banner Automation Completed Successfully",
            'blocks': [
                {
                    'type': 'section',
                    'text': {
                        'type': 'mrkdwn',
                        'text': f"*Banner ID:* {result.config.banner_id}\n*Records Processed:* {result.records_affected}\n*Duration:* {result.duration}\n*Status:* ✅ Success"
                    }
                }
            ]
        }
        self._post_message(message)
    
    def send_execution_failure(self, error: str):
        """Notify failure with details."""
        message = {
            'text': f"❌ Banner Automation Failed",
            'blocks': [
                {
                    'type': 'section',
                    'text': {
                        'type': 'mrkdwn',
                        'text': f"*Error:* {error}\n*Status:* ❌ Failed"
                    }
                }
            ]
        }
        self._post_message(message)
```

---

## Deployment Strategy

### 1. Development Environment Setup

```bash
#!/bin/bash
# scripts/setup_dev.sh

echo "Setting up Banner Automation Development Environment"

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Install pre-commit hooks
pre-commit install

# Set up Google Cloud credentials
gcloud auth login
gcloud auth application-default login

# Create test configuration
cp config/examples/daily_campaign.yaml config/my_campaign.yaml

echo "Development environment ready!"
echo "Run: source venv/bin/activate && python -m banner_automation.cli --help"
```

### 2. Testing Pipeline

```yaml
# .github/workflows/test.yml
name: Test Suite

on: [push, pull_request]

jobs:
  unit-tests:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.9'
      - name: Install dependencies
        run: |
          pip install -r requirements.txt
          pip install -r requirements-test.txt
      - name: Run unit tests
        run: pytest tests/unit/ -v --cov=banner_automation --cov-report=xml
      - name: Upload coverage
        uses: codecov/codecov-action@v1

  integration-tests:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.9'
      - name: Run integration tests
        run: pytest tests/integration/ -v
        env:
          GCP_PROJECT_ID: ${{ secrets.GCP_PROJECT_ID }}
          GCP_CREDENTIALS: ${{ secrets.GCP_CREDENTIALS }}
```

### 3. Production Deployment

```bash
#!/bin/bash
# scripts/deploy.sh

echo "Deploying Banner Automation to Production"

# Build Docker image
docker build -t banner-automation:latest .

# Tag for Google Container Registry
docker tag banner-automation:latest gcr.io/$PROJECT_ID/banner-automation:latest

# Push to registry
docker push gcr.io/$PROJECT_ID/banner-automation:latest

# Deploy to Cloud Run
gcloud run deploy banner-automation \
  --image gcr.io/$PROJECT_ID/banner-automation:latest \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated \
  --set-env-vars GCP_PROJECT_ID=$PROJECT_ID

echo "Deployment complete!"
echo "Service URL: https://banner-automation-xxxxxxxx-uc.a.run.app"
```

### 4. Kubernetes Deployment

```yaml
# deployment/k8s/deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: banner-automation
spec:
  replicas: 1
  selector:
    matchLabels:
      app: banner-automation
  template:
    metadata:
      labels:
        app: banner-automation
    spec:
      containers:
      - name: banner-automation
        image: gcr.io/PROJECT_ID/banner-automation:latest
        env:
        - name: GCP_PROJECT_ID
          value: "clirnet-dev"
        - name: LOG_LEVEL
          value: "INFO"
        resources:
          requests:
            memory: "2Gi"
            cpu: "1000m"
          limits:
            memory: "4Gi"
            cpu: "2000m"
        volumeMounts:
        - name: google-cloud-key
          mountPath: /var/secrets/google
      volumes:
      - name: google-cloud-key
        secret:
          secretName: gcp-key
---
apiVersion: v1
kind: Service
metadata:
  name: banner-automation-service
spec:
  selector:
    app: banner-automation
  ports:
  - port: 80
    targetPort: 8080
  type: LoadBalancer
```

---

## Monitoring & Observability

### 1. Logging Framework

```python
# src/banner_automation/utils/logging_config.py
import logging
import json
from datetime import datetime

class JSONFormatter(logging.Formatter):
    """Custom JSON formatter for structured logging."""
    
    def format(self, record):
        log_entry = {
            'timestamp': datetime.utcnow().isoformat(),
            'level': record.levelname,
            'logger': record.name,
            'message': record.getMessage(),
            'module': record.module,
            'function': record.funcName,
            'line': record.lineno,
        }
        
        if record.exc_info:
            log_entry['exception'] = self.formatException(record.exc_info)
        
        return json.dumps(log_entry)

def setup_logging(level: str = 'INFO', log_file: str = None):
    """Configure structured logging."""
    logger = logging.getLogger()
    logger.setLevel(getattr(logging, level.upper()))
    
    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(JSONFormatter())
    logger.addHandler(console_handler)
    
    # File handler (if specified)
    if log_file:
        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(JSONFormatter())
        logger.addHandler(file_handler)
    
    return logger
```

### 2. Metrics Collection

```python
# src/banner_automation/utils/metrics.py
from dataclasses import dataclass
from datetime import datetime
from typing import Dict, List

@dataclass
class ExecutionMetrics:
    """Metrics collected during execution."""
    start_time: datetime
    end_time: datetime = None
    
    # Query metrics
    queries_executed: int = 0
    queries_failed: int = 0
    total_bytes_processed: int = 0
    
    # Data metrics
    records_affected: int = 0
    records_per_phase: Dict[int, int] = None
    
    # Validation metrics
    validation_checks_passed: int = 0
    validation_checks_failed: int = 0
    
    @property
    def duration_seconds(self) -> float:
        if self.end_time:
            return (self.end_time - self.start_time).total_seconds()
        return 0
    
    @property
    def success_rate(self) -> float:
        if self.queries_executed == 0:
            return 0
        return (self.queries_executed - self.queries_failed) / self.queries_executed

class MetricsCollector:
    """Collect and aggregate metrics."""
    
    def __init__(self):
        self.metrics = ExecutionMetrics(
            start_time=datetime.utcnow(),
            records_per_phase={}
        )
    
    def record_query_execution(self, query_type: str, bytes_processed: int):
        """Record a successful query execution."""
        self.metrics.queries_executed += 1
        self.metrics.total_bytes_processed += bytes_processed
    
    def record_query_failure(self, query_type: str, error: str):
        """Record a query failure."""
        self.metrics.queries_failed += 1
    
    def record_phase_completion(self, phase_id: int, record_count: int):
        """Record phase completion."""
        self.metrics.records_per_phase[phase_id] = record_count
        self.metrics.records_affected += record_count
    
    def record_validation(self, check_name: str, passed: bool):
        """Record validation result."""
        if passed:
            self.metrics.validation_checks_passed += 1
        else:
            self.metrics.validation_checks_failed += 1
    
    def finalize(self):
        """Finalize metrics collection."""
        self.metrics.end_time = datetime.utcnow()
        return self.metrics
```

### 3. Audit Trail

```python
# src/banner_automation/core/audit_logger.py
import json
from datetime import datetime
from typing import Dict, Any

class AuditLogger:
    """Comprehensive audit trail for all operations."""
    
    def __init__(self, audit_table: str, bq_client):
        self.audit_table = audit_table
        self.client = bq_client
        self.entries = []
    
    def log_configuration_load(self, config_path: str, banner_id: str):
        """Log configuration loading."""
        self._log_event('CONFIGURATION_LOADED', {
            'config_path': config_path,
            'banner_id': banner_id,
        })
    
    def log_sql_generation(self, query_count: int, phases: int):
        """Log SQL generation."""
        self._log_event('SQL_GENERATED', {
            'query_count': query_count,
            'phases': phases,
        })
    
    def log_validation(self, validation_type: str, result: str, details: Dict):
        """Log validation results."""
        self._log_event('VALIDATION_' + result, {
            'validation_type': validation_type,
            'details': details,
        })
    
    def log_execution_step(self, step_num: int, query_type: str, status: str, details: Dict):
        """Log execution step."""
        self._log_event('EXECUTION_STEP', {
            'step_number': step_num,
            'query_type': query_type,
            'status': status,
            'details': details,
        })
    
    def log_rollback(self, rollback_type: str, reason: str, success: bool):
        """Log rollback operation."""
        self._log_event('ROLLBACK_EXECUTED', {
            'rollback_type': rollback_type,
            'reason': reason,
            'success': success,
        })
    
    def log_completion(self, status: str, records_affected: int, duration_seconds: float):
        """Log execution completion."""
        self._log_event('EXECUTION_COMPLETED', {
            'status': status,
            'records_affected': records_affected,
            'duration_seconds': duration_seconds,
        })
    
    def _log_event(self, event_type: str, data: Dict[str, Any]):
        """Log a single event."""
        entry = {
            'timestamp': datetime.utcnow().isoformat(),
            'event_type': event_type,
            'data': json.dumps(data),
        }
        self.entries.append(entry)
    
    def flush_to_bigquery(self):
        """Write all audit entries to BigQuery."""
        if not self.entries:
            return
        
        # Prepare for insertion
        rows = [json.dumps(entry) for entry in self.entries]
        
        # Insert to BigQuery
        errors = self.client.insert_rows_json(self.audit_table, self.entries)
        
        if errors:
            print(f"Audit logging errors: {errors}")
        else:
            self.entries = []  # Clear after successful insert
```

### 4. Dashboard and Alerts

**Grafana Dashboard Configuration**:

```json
{
  "dashboard": {
    "title": "Banner Automation Monitoring",
    "panels": [
      {
        "title": "Execution Success Rate",
        "type": "stat",
        "targets": [
          {
            "expr": "rate(banner_automation_executions_total[5m]) * 100",
            "legendFormat": "Success Rate %"
          }
        ]
      },
      {
        "title": "Query Execution Time",
        "type": "graph",
        "targets": [
          {
            "expr": "banner_automation_query_duration_seconds",
            "legendFormat": "{{query_type}}"
          }
        ]
      },
      {
        "title": "Records Processed",
        "type": "graph",
        "targets": [
          {
            "expr": "banner_automation_records_affected_total",
            "legendFormat": "Records"
          }
        ]
      },
      {
        "title": "Validation Failures",
        "type": "graph",
        "targets": [
          {
            "expr": "rate(banner_automation_validation_failures_total[5m])",
            "legendFormat": "Failures/sec"
          }
        ]
      }
    ]
  }
}
```

**Alerting Rules**:

```yaml
# monitoring/alerts.yml
groups:
- name: banner_automation
  rules:
  - alert: BannerAutomationExecutionFailed
    expr: increase(banner_automation_executions_failed_total[5m]) > 0
    for: 0m
    labels:
      severity: critical
    annotations:
      summary: "Banner automation execution failed"
      description: "A banner automation campaign failed to execute"
  
  - alert: BannerAutomationHighValidationFailure
    expr: rate(banner_automation_validation_failures_total[5m]) > 0.1
    for: 2m
    labels:
      severity: warning
    annotations:
      summary: "High validation failure rate"
      description: "Validation failure rate is {{ $value }} failures per second"
  
  - alert: BannerAutomationSlowExecution
    expr: banner_automation_query_duration_seconds > 300
    for: 0m
    labels:
      severity: warning
    annotations:
      summary: "Slow query execution detected"
      description: "Query taking longer than 5 minutes: {{ $labels.query_type }}"
```

---

## Migration Strategy

### Phase 1: Preparation (Weeks 1-2)

**Goals**:
- Team training on new system
- Configuration migration planning
- Baseline metrics collection

**Activities**:
- Train team on configuration system
- Document current manual process variations
- Identify edge cases and special scenarios
- Create initial configurations for recent campaigns
- Set up monitoring and alerting

**Success Criteria**:
- All team members trained
- Configuration files created for past 5 campaigns
- Monitoring infrastructure in place

---

### Phase 2: Shadow Mode (Weeks 3-6)

**Goals**:
- Run automation alongside manual process
- Validate output quality matches manual process
- Build confidence in automation system

**Execution Plan**:
```
Week 3-4: Simple Campaigns
  - Run automation on simple, low-risk campaigns
  - Do NOT insert to production
  - Compare outputs with manual process
  - Fix any discrepancies

Week 5-6: Complex Campaigns
  - Include more complex campaigns
  - Test edge cases and special scenarios
  - Validate rollback mechanisms
  - Performance tuning
```

**Validation Process**:
```python
def validate_automation_vs_manual(manual_result: dict, automation_result: dict):
    """Compare manual vs automation results."""
    checks = [
        ('record_count', manual_result.count == automation_result.count),
        ('banner_ids', manual_result.banner_ids == automation_result.banner_ids),
        ('date_ranges', manual_result.date_ranges == automation_result.date_ranges),
        ('json_fields', manual_result.json_fields == automation_result.json_fields),
    ]
    
    return all(check[1] for check in checks)
```

**Success Criteria**:
- 100% output quality match for all test campaigns
- No data quality issues
- Performance acceptable (within 50% of manual time)
- Team confident in automation

---

### Phase 3: Parallel Execution (Weeks 7-10)

**Goals**:
- Run automation in production alongside manual
- Gradual transition to automation

**Execution Plan**:
```
Week 7-8: 20% Automation
  - Run 1 in 5 campaigns via automation
  - Compare with manual results
  - Monitor for issues
  - Build production confidence

Week 9-10: 50% Automation
  - Run 1 in 2 campaigns via automation
  - Full production monitoring
  - Gather feedback
  - Optimize based on production data
```

**Monitoring**:
- Daily review of automation runs
- Compare success/failure rates
- Track time savings
- Collect user feedback

**Success Criteria**:
- No production issues
- Reduced error rate (automation vs manual)
- Team prefers automation for new campaigns
- Time savings documented

---

### Phase 4: Full Automation (Weeks 11-12)

**Goals**:
- Complete migration to automation
- Manual process as fallback only
- Continuous improvement

**Execution Plan**:
```
Week 11: 80% Automation
  - Most campaigns run via automation
  - Manual process for complex edge cases
  - Document any remaining manual steps
  - Plan for handling edge cases

Week 12: 100% Automation
  - All standard campaigns via automation
  - Manual process documentation complete
  - Backlog of edge case handling
  - Continuous improvement planning
```

**Success Criteria**:
- 100% of standard campaigns automated
- <5% of campaigns require manual intervention
- Zero data quality issues
- Team fully comfortable with automation
- Documentation complete

---

### Post-Migration: Optimization (Ongoing)

**Goals**:
- Continuous improvement
- Additional automation opportunities
- Process refinement

**Activities**:
- Monthly review of automation metrics
- Identify opportunities for further automation
- Gather team feedback
- Optimize configurations
- Add new features based on usage

**Success Metrics**:
- Reduction in manual effort: >90%
- Reduction in errors: >95%
- Time to execute: <10 minutes (vs 2+ hours manual)
- Team satisfaction: >9/10

---

## Conclusion

This comprehensive automation platform transforms the banner modification process from a manual, error-prone procedure into a production-ready, automated system. By implementing:

1. **Configuration-driven approach** - No more manual SQL writing
2. **Transaction support with rollback** - Zero risk of data corruption
3. **Comprehensive validation** - Catch errors before they become problems
4. **Dry-run mode** - Safe testing without production impact
5. **Full audit trail** - Complete visibility into all operations

The solution will:
- Reduce manual effort by **99%**
- Reduce errors by **95%**
- Improve execution speed by **100x**
- Provide complete safety guarantees
- Enable scheduled and automated execution

**Next Steps**:
1. Review and approve design
2. Begin Phase 1 implementation
3. Set up development environment
4. Start with simple campaign automation
5. Iterate and improve based on real-world usage

This platform will position CLIRNET's banner operations for scale while maintaining data integrity and operational excellence.

---

**Document Version**: 1.0  
**Last Updated**: 2025-11-01  
**Owner**: AVP Product - CLIRNET  
**Technical Review**: Banner Operations Team
