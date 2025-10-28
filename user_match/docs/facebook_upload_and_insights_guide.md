# Facebook Custom Audiences: Complete Upload & Insights Guide

*Your comprehensive guide to enriching doctor demographics using Facebook Custom Audiences*

---

## Table of Contents
- [Overview](#overview)
- [Data Format Requirements](#data-format-requirements)
- [Upload Process](#upload-process)
- [Accessing Insights](#accessing-insights)
- [Facebook vs Google](#facebook-vs-google-comparison)
- [Best Practices](#best-practices)
- [Troubleshooting](#troubleshooting)

---

## Overview

### What are Facebook Custom Audiences?

Facebook Custom Audiences allow you to target your existing customers across Facebook, Instagram, Messenger, and WhatsApp using customer data like emails and phone numbers.

**Key Benefits:**
- **Higher match rates** than Google (60-70% vs 40-60%)
- Access to **social behavior** and interest data
- **Cross-platform** reach (Facebook + Instagram)
- **Lookalike modeling** for audience expansion

### Privacy Compliance

**GDPR (EU):**
- Explicit consent required for ad_user_data and ad_personalization
- You are the Controller, Meta is the Processor
- Privacy policy must disclose Facebook advertising

**CCPA (California):**
- Limited Data Use (LDU) automatically enabled
- "Do Not Sell" link required on website
- Honor opt-out requests

**HIPAA (Healthcare):**
⚠️ **Facebook does NOT sign BAAs**
- Cannot upload patient lists or PHI
- Use authorized marketing lists only
- No health condition data permitted

---

## Data Format Requirements

### Supported File Formats
- CSV (.csv) - **recommended**
- Text (.txt)
- Excel (.xlsx)
- MailChimp (direct integration)

### File Constraints

| Limit | Value |
|-------|-------|
| Records per upload | 10,000 max |
| Minimum audience size | 100 users (same country) |
| Minimum for ads | 20 matched users |
| Recommended size | 10,000+ for best performance |

### Required Column Headers

Facebook uses **abbreviated headers**:

| Header | Description | Format |
|--------|-------------|--------|
| **email** | Email address | Lowercase, trimmed |
| **phone** | Phone number | E.164: +14155552671 |
| **fn** | First name | Lowercase, trimmed |
| **ln** | Last name | Lowercase, trimmed |
| **zip** | Postal code | 5 digits (US) or local format |
| **ct** | City | Lowercase, no spaces |
| **st** | State/Province | 2-letter code (CA, NY) |
| **country** | Country | 2-letter ISO code (**required**) |
| **dob** | Date of birth | YYYYMMDD |
| **gen** | Gender | "m" or "f" |

### Data Formatting Rules

**Email:**
```
Before: "  Doctor.Smith@Example.COM  "
After:  "doctor.smith@example.com"
```

**Phone:**
```
Before: "(415) 555-1234"
After:  "+14155551234"  (E.164 with country code)
```

**Names:**
```
Before: "Dr. John Doe Jr."
After fn: "john"
After ln: "doe"
```

### Hashing (Optional)

Facebook accepts:
- **Unhashed data** (auto-hashed during upload) - **recommended for most users**
- **Pre-hashed** (SHA-256 lowercase hex)

**Pre-hash only if:**
- You have technical requirements
- Using API integration
- Need extra security layer

**Hashing rules:**
1. Normalize data (lowercase, trim)
2. Hash with SHA-256
3. Convert to lowercase hex
4. Do NOT hash country or zip

---

## Upload Process

### Step 1: Access Business Manager

Navigate to: **https://business.facebook.com/adsmanager/audiences**

### Step 2: Create Custom Audience

1. Click **"Create Audience"** button
2. Select **"Custom Audience"**
3. Choose **"Customer List"**

### Step 3: Upload Your File

**Option A: File Upload**
1. Click **"Choose File"** or drag-and-drop
2. Select your CSV file
3. Wait for validation

**Option B: Copy-Paste**
1. Click **"or copy and paste data"**
2. Paste comma-separated values
3. Good for quick tests

**Option C: MailChimp Integration**
1. Click **"Import from MailChimp"**
2. Authorize connection
3. Select your MailChimp list

### Step 4: Map Columns

Facebook will auto-detect column types, but verify:

| Your Column | Map To |
|-------------|--------|
| "Email" | → email |
| "Phone" or "Mobile" | → phone |
| "FirstName" | → fn (First Name) |
| "LastName" | → ln (Last Name) |
| "Country" | → country |
| "ZIP" | → zip |

**⚠️ Yellow warnings:** Fix data quality issues for better match rates

### Step 5: Accept Compliance Terms

Check all required boxes:
- ☑️ I have rights to use this customer data
- ☑️ Data collected in compliance with laws
- ☑️ Customers consented to this use
- ☑️ No special category data included

### Step 6: Name and Create

1. Name your audience: `Doctor_List_India_2025`
2. Optional description for your team
3. Click **"Create"** or **"Upload & Create"**

### Processing Time

| Stage | Duration |
|-------|----------|
| Upload | 1-5 minutes |
| Initial processing | 15-60 minutes |
| Matching | 1-6 hours |
| Full population | Up to 48 hours |

⏰ **Best practice:** Wait 72 hours for numbers to stabilize

---

## Accessing Insights

### ⚠️ Important Update: Audience Insights Deprecated

Facebook removed its standalone **Audience Insights tool in July 2021**.

### Current Method: Meta Business Suite

**Access:** https://business.facebook.com → **Insights**

**Available Demographics:**
- Age ranges (13-17, 18-24, 25-34, 35-44, 45-54, 55-64, 65+)
- Gender breakdown
- Top locations (countries, cities)
- Primary languages
- Online activity times

### What's NO LONGER Available

❌ Detailed page likes by category  
❌ Specific purchase behaviors  
❌ Detailed lifestyle data  
❌ Job titles and employers  
❌ Household demographics  
❌ Device usage breakdown  
❌ Custom audience comparison tools

### Get More Insights Through Campaigns

**Run ads to your Custom Audience to unlock:**
- Performance by age and gender
- Location-based engagement
- Device usage (mobile vs desktop)
- Placement performance (Feed, Stories, Reels)
- Conversion rates by demographic

**How to access:**
1. Ads Manager → Your Campaign
2. Click **"View Charts"**
3. Use **"Breakdown"** dropdown:
   - Age and Gender
   - Country/Region
   - Device
   - Placement

### Alternative Tools

Since Facebook removed detailed insights:

| Tool | Type | Best For |
|------|------|----------|
| **Meta Business Suite** | Free | Basic demographics |
| **Madgicx** | Paid | Advanced audience analysis |
| **AdTargeting.io** | Freemium | Interest research |
| **Google Analytics + Pixel** | Free | Cross-platform insights |

---

## Facebook vs Google Comparison

### Format Differences

| Aspect | Facebook | Google |
|--------|----------|--------|
| **Headers** | email, phone, fn, ln | Email, Phone, First Name, Last Name |
| **File Formats** | CSV, TXT, XLSX, MailChimp | CSV only |
| **Records/Upload** | 10,000 max | No limit |
| **Minimum Size** | 100 users | 100 users |
| **Hashing** | Optional (auto-hash available) | Optional (auto-hash available) |
| **Phone Format** | E.164 with + | E.164 |
| **Country** | Always required | Required for phone |

### Match Rate Comparison

| Scenario | Facebook | Google |
|----------|----------|--------|
| Personal email only | 40-50% | 30-40% |
| Email + Phone | 60-70% | 50-60% |
| Email + Phone + Name + Location | 70-80% | 60-70% |
| Business email (B2B) | 10-15% | 15-25% |

**Winner:** Facebook typically 10-15% higher for consumer data

### Insights Comparison

| Insight Type | Facebook | Google |
|--------------|----------|--------|
| **Demographics** | ✅ Basic (limited) | ⚠️ Very limited |
| **Interests** | ⚠️ Limited since 2021 | ❌ Not available |
| **Search Behavior** | ❌ Not available | ✅ Available |
| **Social Activity** | ✅ Page engagement | ❌ Not available |
| **Device Usage** | ✅ Via campaigns | ✅ Via campaigns |
| **Lookalike Quality** | ✅ Excellent | ✅ Good |

### When to Use Each

**Use Facebook for:**
- ✅ B2C visual products (fashion, food, lifestyle)
- ✅ Brand awareness and social proof
- ✅ Instagram/mobile-first targeting
- ✅ Impulse purchases
- ✅ Higher match rates needed

**Use Google for:**
- ✅ High-intent search targeting
- ✅ B2B with work emails
- ✅ Considered purchases (research phase)
- ✅ YouTube video marketing
- ✅ Gmail direct marketing

**Best Strategy:** Use BOTH platforms for maximum reach

---

## Best Practices

### Data Quality

**Before Upload:**
1. ✅ Validate emails (use verification service)
2. ✅ Format phones to E.164
3. ✅ Remove duplicates
4. ✅ Lowercase all text fields
5. ✅ Remove titles (Dr., Mr., Mrs.)
6. ✅ Include country for ALL records

**Match Rate Optimization:**
- Add phone numbers → +10-15% match rate
- Add first + last names → +5-10%
- Include city, state, zip → +3-5%
- Clean invalid emails → +5-15%

### Update Frequency

| Business Type | Frequency |
|---------------|-----------|
| E-commerce (high volume) | Weekly |
| B2B/SaaS | Monthly |
| Retail/Seasonal | Quarterly |
| Services | Quarterly |

**Automation options:**
- Facebook API for scheduled uploads
- Zapier for no-code automation
- CRM integrations (Salesforce, HubSpot)

### Segmentation Strategies

**RFM Segmentation:**
- **Champions:** Recent + High frequency + High value
- **At Risk:** Long ago + High frequency + High value
- **New Customers:** Very recent + Low frequency
- **Hibernating:** Long ago + Low frequency + Low value

**Lifecycle Stages:**
- New customers (0-30 days)
- Active customers (31-180 days)
- At-risk customers (181-365 days)
- Lapsed customers (365+ days)

### Healthcare-Specific Compliance

⚠️ **Critical for Medical Practices:**

**CANNOT Upload:**
- ❌ Patient lists without authorization
- ❌ Protected Health Information (PHI)
- ❌ Medical record numbers
- ❌ Health conditions or diagnoses
- ❌ Treatment information

**CAN Upload:**
- ✅ Marketing list (with explicit consent)
- ✅ Event registrants (consent obtained)
- ✅ Newsletter subscribers (opt-in)
- ✅ Non-patient community members

**Required Consent Language:**
> "I authorize [Practice Name] to use my contact information for marketing purposes, including advertising on social media platforms like Facebook and Instagram."

---

## Troubleshooting

### Common Upload Errors

**"Custom Audience Terms Not Accepted"**
- **Fix:** Create audience manually in Ads Manager to trigger terms acceptance

**"Insufficient Data" (<100 records)**
- **Fix:** Add more customer records or combine lists

**"Cannot Read File"**
- **Fix:** Save as CSV UTF-8, remove special characters

**Error #2654 "Several Weeks Required"**
- **Fix:** New account restriction - wait 2-4 weeks with compliant activity

**"Low Quality Data" Warning**
- **Fix:** Validate emails, format phones to E.164, remove test data

### Low Match Rates

**If <30% match rate:**

1. **Check data quality**
   - Business emails? → Add personal emails
   - Phone format? → E.164 with country code
   - Old data? → Validate and clean

2. **Add more identifiers**
   - Include phone + name + location
   - More fields = higher match rates

3. **Verify file format**
   - UTF-8 encoding
   - Correct column mapping
   - No mixed hashed/unhashed data

### Audience Too Small

**"Size: <1,000" Warning**

**Solutions:**
1. Wait 72 hours for processing
2. Upload more customer data
3. Improve match rate (see above)
4. Combine multiple small audiences
5. Use for exclusion (works with small sizes)

### Privacy Warnings

**"May Violate Privacy Policies"**

**Common causes:**
- Special category data detected
- Lack of proper consent
- Purchased or scraped data
- Data of minors

**Fix:**
- Remove sensitive data
- Document consent process
- Use only first-party data
- Contact Facebook support if needed

---

## Creating Lookalike Audiences

### Requirements
- Minimum 100 matched users (1,000+ recommended)
- Quality source audience (high-value customers)

### Steps

1. **Audiences → Create Audience → Lookalike Audience**
2. **Select source:** Your Custom Audience
3. **Choose location:** Countries to find similar people
4. **Select size:** 1% (narrow) to 10% (broad)
5. **Create audience**

### Size Recommendations

| Size | Similarity | Use Case |
|------|------------|----------|
| 1% | Highest | Quality lead generation |
| 2-5% | Balanced | Scaling campaigns |
| 6-10% | Broader | Awareness, maximum reach |

---

## Facebook Conversions API

### Why Use It?

**Benefits:**
- 95% event capture vs 60-70% with Pixel only
- Server-to-server (bypasses ad blockers)
- Better match rates with enhanced matching
- iOS 14+ privacy resilient

### Quick Setup

**Partners with built-in support:**
- Shopify
- WooCommerce  
- BigCommerce
- Magento

**Manual setup:**
1. Business Manager → Events Manager
2. Add Events → Web → Conversions API
3. Choose integration method
4. Configure event parameters
5. Include customer data (email, phone, name)
6. Test events

**Use BOTH Pixel + CAPI** for maximum coverage

---

## Key Takeaways

✅ **Match rates:** Facebook typically 10-15% higher than Google  
✅ **Minimum:** 100 users, aim for 10,000+  
✅ **Processing:** 48-72 hours for stable numbers  
✅ **Insights limited:** Use campaigns for detailed data  
✅ **HIPAA:** Facebook NOT compliant - no patient lists  
✅ **Headers:** Use abbreviated (email, phone, fn, ln)  
✅ **Lookalikes:** Powerful expansion from small seed  
✅ **Best approach:** Combine Facebook + Google

---

## Additional Resources

### Official Documentation
- [Meta Business Help - Custom Audiences](https://www.facebook.com/business/help/341425252616329)
- [Customer List Custom Audiences](https://www.facebook.com/business/help/606443329504150)
- [GDPR Compliance for Advertisers](https://www.facebook.com/business/gdpr)

### Tools
- [Facebook Business Manager](https://business.facebook.com)
- [Ads Manager](https://www.facebook.com/adsmanager)
- [Meta Business Suite](https://business.facebook.com/latest/home)

---

**Document Version:** 1.0  
**Last Updated:** October 2024  
**Coverage:** Facebook/Meta 2024 interface and policies
