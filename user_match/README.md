# Customer Match Toolkit for Doctor Demographics

**Complete solution for enriching doctor demographics using Google Customer Match and Facebook Custom Audiences**

---

## 📌 Overview

This toolkit provides everything you need to upload customer data to Google Ads and Facebook, then access aggregated behavioral insights about your doctor audience. Get demographics, interests, search patterns, and social behaviors without accessing individual-level data—fully HIPAA/GDPR compliant.

### What's Included

✅ **4 comprehensive documentation guides** (70KB+)  
✅ **3 production-ready Python conversion scripts**  
✅ **Sample data and outputs** for testing  
✅ **Platform comparison tables**  
✅ **Troubleshooting guides**  

---

## 📁 Project Structure

```
user_match/
├── README.md                 ← You are here
│
├── docs/                     ← Comprehensive guides
│   ├── google_insights_available.md           (38KB)
│   ├── google_step_by_step_guide.md           (6.8KB)
│   └── facebook_upload_and_insights_guide.md  (15KB)
│
├── scripts/                  ← Conversion tools
│   ├── convert_to_google_customer_match_simple.py    (No dependencies)
│   ├── convert_to_google_customer_match.py           (Uses pandas)
│   └── convert_to_facebook_custom_audience.py        (Facebook format)
│
├── sample_data/              ← Test files
│   ├── sample_doctor_data.csv           (30 Indian doctors)
│   ├── hashed_doctor_data.csv           (Google format output)
│   └── facebook_audience_output.csv     (Facebook format output)
│
└── reference/                ← Additional info
    └── grok_conversation_how_to_prepare_csv.txt
```

---

## 🚀 Quick Start

### For Google Customer Match

```bash
cd D:\writing\clirnet\user_match
uv run scripts/convert_to_google_customer_match_simple.py your_data.csv google_output.csv
```

**Then upload to:** Google Ads → Tools → Audience Manager → Create Customer List

### For Facebook Custom Audiences

```bash
cd D:\writing\clirnet\user_match
uv run scripts/convert_to_facebook_custom_audience.py your_data.csv facebook_output.csv
```

**Then upload to:** Facebook Business Manager → Audiences → Create Custom Audience

---

## 📚 Documentation Guides

### 1. **Google Insights Available** (`docs/google_insights_available.md`)
**38KB comprehensive guide covering:**
- What insights Google provides after matching
- Demographics, interests, search behaviors, YouTube habits
- Professional audience insights (healthcare-specific)
- In-market segments and life events
- Accessing data via Audience Manager, GA4, BigQuery
- Limitations and privacy protections
- Use cases: personalization, segmentation, lookalikes, churn prediction

**Key Topics:**
- Affinity segments (~150 categories)
- Search intent analysis
- Device and cross-device tracking
- Professional development patterns for doctors
- CME/CPD content consumption
- Medical specialty insights

### 2. **Google Step-by-Step Guide** (`docs/google_step_by_step_guide.md`)
**6.8KB actionable tutorial with:**
- Prerequisites and account setup
- CSV format requirements
- Upload process with detailed steps
- Monitoring match rates (40-60% typical)
- Accessing insights through multiple methods
- Troubleshooting common issues
- Advanced features: Lookalikes, Enhanced Conversions

**Perfect for:** First-time uploads and team training

### 3. **Facebook Upload & Insights Guide** (`docs/facebook_upload_and_insights_guide.md`)
**15KB complete Facebook guide including:**
- Data format requirements (Facebook's unique headers)
- Upload process through Business Manager
- Current insights available (post-2021 Audience Insights deprecation)
- Facebook vs Google comparison tables
- Healthcare compliance warnings (HIPAA)
- Lookalike audience creation
- Facebook Conversions API overview

**Key Differences from Google:**
- Higher match rates (60-70% vs 40-60%)
- Different column headers (email, phone, fn, ln)
- 10,000 max records per upload
- Country always required

---

## 🐍 Conversion Scripts

### 1. **Google Simple Converter** (Recommended)
**File:** `scripts/convert_to_google_customer_match_simple.py`

**Features:**
- ✅ No external dependencies (Python standard library only)
- ✅ Converts to Google format
- ✅ SHA-256 hashing
- ✅ Email/phone validation
- ✅ Country code standardization
- ✅ Detailed conversion reports

**Usage:**
```bash
uv run scripts/convert_to_google_customer_match_simple.py input.csv output.csv
```

**Input format:**
```csv
Email,Phone,First Name,Last Name,Country,Zip
doctor@hospital.in,+91-9876543210,Dr. Rajesh,Kumar,India,560001
```

**Output:** Google-ready CSV with SHA-256 hashed PII

### 2. **Facebook Converter** (NEW!)
**File:** `scripts/convert_to_facebook_custom_audience.py`

**Features:**
- ✅ Converts to Facebook format (email, phone, fn, ln, ct, st, zip, country, gen)
- ✅ Optional pre-hashing with `--hash` flag
- ✅ Removes Gmail dots, cleans names
- ✅ E.164 phone formatting
- ✅ Facebook-specific validations

**Usage:**
```bash
# Without hashing (recommended - Facebook will auto-hash)
uv run scripts/convert_to_facebook_custom_audience.py input.csv output.csv

# With pre-hashing
uv run scripts/convert_to_facebook_custom_audience.py input.csv output.csv --hash
```

**Output:** Facebook-ready CSV with abbreviated headers

### 3. **Google Pandas Converter** (Alternative)
**File:** `scripts/convert_to_google_customer_match.py`

**Requires:** `pip install pandas`
**Best for:** Users already using pandas in their workflow

---

## 📊 Platform Comparison

### Data Format Differences

| Aspect | Google | Facebook |
|--------|--------|----------|
| **Column Headers** | Email, Phone, First Name, Last Name | email, phone, fn, ln |
| **File Formats** | CSV only | CSV, TXT, XLSX, MailChimp |
| **Records/Upload** | No limit | 10,000 max |
| **Min Size** | 100 users | 100 users |
| **Country** | Required for phone | Always required |
| **Phone Format** | E.164 | E.164 with + |
| **Hashing** | Optional (auto-hash) | Optional (auto-hash) |

### Match Rates

| Data Quality | Google | Facebook | Winner |
|--------------|--------|----------|--------|
| Personal email only | 30-40% | 40-50% | Facebook ✅ |
| Email + Phone | 50-60% | 60-70% | Facebook ✅ |
| Complete data | 60-70% | 70-80% | Facebook ✅ |
| Business emails (B2B) | 15-25% | 10-15% | Google ✅ |

**Key Insight:** Facebook typically has 10-15% higher match rates for consumer/personal data

### Insights Comparison

| Insight Type | Google | Facebook | Best For |
|--------------|--------|----------|----------|
| **Demographics** | ⚠️ Limited | ✅ Better | Facebook |
| **Search Behavior** | ✅ Excellent | ❌ None | Google |
| **Social Interests** | ❌ None | ⚠️ Limited | Facebook |
| **Video Viewing** | ✅ YouTube | ✅ Facebook/IG | Both |
| **Device Usage** | ✅ Campaign data | ✅ Campaign data | Both |
| **Lookalike Quality** | ✅ Good | ✅ Excellent | Facebook |
| **Professional Data** | ⚠️ Minimal | ⚠️ Minimal | Both limited |

### When to Use Each Platform

**Use Google for:**
- ✅ High-intent search targeting
- ✅ B2B with work emails
- ✅ Considered purchases (research phase)
- ✅ YouTube video marketing
- ✅ Gmail direct marketing
- ✅ Capturing active searchers

**Use Facebook for:**
- ✅ B2C visual products
- ✅ Brand awareness and social proof
- ✅ Instagram/mobile-first targeting
- ✅ Impulse purchases
- ✅ Higher match rates needed
- ✅ Lookalike audience expansion

**Best Strategy:** Use **BOTH** platforms for maximum demographic insights and reach

---

## 💡 Common Workflows

### Workflow 1: Initial Setup (First Time)

```bash
# 1. Organize your data
# Export from your CRM with: email, phone, first_name, last_name, country, zip

# 2. Convert for Google
uv run scripts/convert_to_google_customer_match_simple.py doctors.csv google_output.csv

# 3. Convert for Facebook
uv run scripts/convert_to_facebook_custom_audience.py doctors.csv facebook_output.csv

# 4. Upload both
# - Google Ads > Audience Manager > Upload google_output.csv
# - Facebook Business Manager > Audiences > Upload facebook_output.csv

# 5. Wait 72 hours for stable numbers

# 6. Access insights
# - Google: Tools > Audience Insights
# - Facebook: Meta Business Suite > Insights
```

### Workflow 2: Segmentation by Specialty

```bash
# Export by specialty
# cardiologists.csv, gps.csv, surgeons.csv, etc.

# Convert each segment
uv run scripts/convert_to_google_customer_match_simple.py cardiologists.csv cardio_google.csv
uv run scripts/convert_to_facebook_custom_audience.py cardiologists.csv cardio_facebook.csv

# Upload as separate audiences
# Compare insights between specialties
# Create specialty-specific campaigns
```

### Workflow 3: Regular Updates (Monthly)

```bash
# 1. Export updated customer list
# 2. Convert with same scripts
# 3. In Google/Facebook: Edit existing audience → Add members
# 4. Or create new dated audience: "Doctors_Nov_2024"
```

---

## 🔐 Privacy & Compliance

### HIPAA Compliance (Healthcare)

⚠️ **CRITICAL:** Neither Google nor Facebook signs Business Associate Agreements (BAAs)

**CANNOT Upload:**
- ❌ Patient lists without explicit authorization
- ❌ Protected Health Information (PHI)
- ❌ Medical record numbers
- ❌ Health conditions or diagnoses

**CAN Upload:**
- ✅ Marketing lists (with consent)
- ✅ Newsletter subscribers (opt-in)
- ✅ Event registrants (consent obtained)
- ✅ Doctor/HCP lists for professional targeting (B2B)

### GDPR Compliance (EU/EEA/UK)

**Requirements:**
- ✅ Explicit consent for ad_user_data and ad_personalization
- ✅ Privacy policy mentions data sharing with Google/Facebook
- ✅ "Do Not Sell" link (CCPA - California)
- ✅ Consent Management Platform (CMP) implemented
- ✅ Data Processing Agreement with platforms

### Required Consent Language

**Example for doctors:**
> "I authorize [Your Organization] to use my contact information, including email address and phone number, for marketing purposes, which may include advertising on platforms such as Google Ads, YouTube, Facebook, and Instagram. I understand that my information will be shared with these platforms in hashed form for advertising purposes."

---

## 📈 Expected Results

### Match Rates by Data Quality

| Data Provided | Google Match Rate | Facebook Match Rate |
|---------------|-------------------|---------------------|
| Email only (personal) | 30-40% | 40-50% |
| Email + Phone | 50-60% | 60-70% |
| Email + Phone + Name | 55-65% | 65-75% |
| Complete data (all fields) | 60-70% | 70-80% |
| Business emails only (B2B) | 15-25% | 10-15% |

### Minimum Viable Audiences

| Platform | Minimum Upload | Minimum Matches | Recommended |
|----------|----------------|-----------------|-------------|
| **Google** | 100 records | 100 matches | 1,000+ |
| **Facebook** | 100 records | 100 matches | 10,000+ |

**For Insights:** Need 1,000+ matched users on Google for detailed insights

### Processing Time

| Stage | Duration |
|-------|----------|
| Upload | 1-5 minutes |
| Initial processing | 15-60 minutes |
| Matching | 1-24 hours |
| Stable numbers | 48-72 hours |

⏰ **Best practice:** Wait 72 hours before evaluating match rates

---

## 🐛 Troubleshooting

### Common Upload Errors

**"Invalid column headers"**
- **Google:** Use `Email`, `Phone`, `First Name`, `Last Name`, `Country`, `Zip`
- **Facebook:** Use `email`, `phone`, `fn`, `ln`, `country`, `zip`
- Case-sensitive!

**"Minimum 100 records required"**
- Add more customer data
- Combine multiple small lists

**"Cannot read file"**
- Save as CSV UTF-8 encoding
- Remove special characters
- Use standard line breaks

### Low Match Rates (<30%)

**Common causes:**
1. **Business emails** → Add personal emails
2. **Missing country codes** → Format phones as +[country][number]
3. **Old/invalid data** → Validate and clean emails
4. **Single identifier** → Add phone + name + location

**Solutions:**
```bash
# Before upload: validate emails
# Add phone numbers → +10-15% match rate
# Include first + last names → +5-10% match rate
# Add city, state, zip → +3-5% match rate
```

### Account Restrictions

**Google: "Account not eligible"**
- Need 90 days history + $50k lifetime spend for full access
- Basic access: observation mode only
- Wait or use Facebook instead

**Facebook: Error #2654 "Several weeks required"**
- New account restriction
- Wait 2-4 weeks with compliant activity
- Run standard campaigns in the meantime

---

## 🎯 Use Cases & Examples

### 1. **Specialty-Based Content Personalization**

```
Upload Segment: Cardiologists (3,000 records, 60% match = 1,800)

Google Insights Show:
- 65% age 35-54
- 80% mobile usage
- High interest in "Medical Research" affinity category
- Search for "cardiology guidelines" and "heart failure treatment"

Action: Create mobile-first content on latest cardiology guidelines
```

### 2. **Geographic Expansion Planning**

```
Upload: All doctors in India (50,000 records, 65% match = 32,500)

Facebook Insights Show:
- Mumbai: 22%
- Delhi: 18%
- Bangalore: 15%

Google Insights Show:
- High searches for "CME credits online" in tier-2 cities

Action: Expand CME platform to tier-2 cities with high search volume
```

### 3. **Lookalike Audience for Acquisition**

```
Seed: High-engagement doctors (500 top users)
Facebook Lookalike (2% similarity): Finds 10,000 similar doctors
Google Lookalike (Demand Gen): Finds 8,000 similar professionals

Combined Campaign: 18,000 net new prospects with similar characteristics
```

### 4. **Churn Prediction & Re-engagement**

```
Upload Segment: Lapsed doctors (no login 180+ days) - 2,000 records

Campaign:
- Google Search: Target when searching for alternatives
- Facebook: Video testimonials, success stories
- Special offer: Free CME credits

Result: 35% reactivation rate, $450 avg CLV increase
```

---

## 📚 Additional Resources

### Official Documentation
- [Google Customer Match Help](https://support.google.com/google-ads/answer/6379332)
- [Facebook Custom Audiences Help](https://www.facebook.com/business/help/606443329504150)
- [GDPR Compliance for Google](https://support.google.com/google-ads/answer/9028179)
- [GDPR Compliance for Facebook](https://www.facebook.com/business/gdpr)

### Your Documentation
- `docs/google_insights_available.md` - Comprehensive insights guide
- `docs/google_step_by_step_guide.md` - Upload tutorial
- `docs/facebook_upload_and_insights_guide.md` - Complete Facebook guide
- `reference/grok_conversation_how_to_prepare_csv.txt` - Extended reference

---

## ✅ Pre-Upload Checklist

Before uploading to either platform:

**Data Quality:**
- [ ] Emails validated (90%+ deliverable)
- [ ] Phones in E.164 format with country codes
- [ ] Names separated (first and last in different columns)
- [ ] All data normalized (lowercase, trimmed)
- [ ] Country included for all records
- [ ] Duplicates removed
- [ ] Minimum 100 records (1,000+ recommended)

**Compliance:**
- [ ] Explicit consent obtained from users
- [ ] Privacy policy updated to mention Google/Facebook
- [ ] No PHI or patient data included
- [ ] GDPR/CCPA requirements met
- [ ] Opt-out mechanism in place

**Technical:**
- [ ] CSV UTF-8 encoding
- [ ] Correct headers for platform (see comparison table)
- [ ] File tested with sample data first
- [ ] Backup of original data stored securely

---

## 🔄 Update Schedule

**Recommended frequency:**

| Business Type | Update Frequency |
|---------------|------------------|
| High-volume e-commerce | Weekly |
| SaaS/Subscription (doctors) | Monthly |
| B2B services | Quarterly |
| Seasonal business | Before each season |

**Why update regularly:**
- Google lists expire after 540 days (effective April 2025)
- Facebook audiences stay fresh
- Capture new customers
- Remove churned users
- Improve match rates with updated data

---

## 🎓 Learning Path

**Beginner (Week 1):**
1. Read `docs/google_step_by_step_guide.md`
2. Convert sample data with scripts
3. Upload to Google Ads
4. Wait 72 hours, view basic insights

**Intermediate (Week 2-3):**
1. Read `docs/facebook_upload_and_insights_guide.md`
2. Upload same data to Facebook
3. Compare match rates and insights
4. Create first lookalike audience

**Advanced (Month 2+):**
1. Read `docs/google_insights_available.md` (full depth)
2. Set up GA4 integration
3. Export to BigQuery
4. Build segmentation strategy
5. Automate uploads via API

---

## 🚀 Next Steps

1. **Start with sample data:** Test both converters with `sample_data/sample_doctor_data.csv`
2. **Read the guides:** Pick Google or Facebook first, follow step-by-step guide
3. **Export your data:** Get 1,000+ doctor records from your CRM
4. **Convert and upload:** Use scripts, upload to both platforms
5. **Wait and analyze:** 72 hours for stable numbers, then explore insights
6. **Create campaigns:** Use insights to target, create lookalikes, personalize
7. **Iterate:** Update monthly, refine segments, expand reach

---

## 📞 Support

**For script issues:**
- Check the troubleshooting section above
- Review script comments (detailed inline documentation)
- Scripts are Python 3.7+ compatible, zero/minimal dependencies

**For platform-specific issues:**
- Google: [Google Ads Support](https://support.google.com/google-ads)
- Facebook: [Facebook Business Help](https://www.facebook.com/business/help)

**For compliance questions:**
- Consult with your legal/compliance team
- Review HIPAA, GDPR, CCPA requirements for your jurisdiction
- Neither platform is HIPAA-compliant for PHI

---

## 🎯 Key Takeaways

| Aspect | Details |
|--------|---------|
| **Purpose** | Enrich doctor demographics using first-party data |
| **Platforms** | Google Ads Customer Match + Facebook Custom Audiences |
| **Match Rates** | Google: 40-60%, Facebook: 60-70% (personal emails) |
| **Minimum Size** | 100 upload, 1,000+ for insights |
| **Processing Time** | 48-72 hours for stable numbers |
| **Insights** | Demographics, interests, behaviors (aggregated only) |
| **Compliance** | GDPR/CCPA ready, NOT HIPAA-compliant |
| **Best Practice** | Use BOTH platforms for maximum insights |
| **Cost** | Free (uploads and basic insights) |
| **Privacy** | All data hashed, aggregated, anonymized |

---

**Ready to unlock powerful audience insights?** Start with the sample data, pick a platform, and make your first upload today! 🎉

---

**Version:** 2.0  
**Last Updated:** October 28, 2024  
**Toolkit Includes:** 4 guides (60KB+), 3 scripts, sample data, complete workflows
