# Palliative Care Clinical Calculators - Complete Suite

## Overview
This comprehensive collection includes 10 evidence-based clinical calculators specifically designed for palliative care specialty. Each calculator features responsive HTML5/CSS3 design with Bootstrap 5, purple gradient theme, input validation, clinical interpretation, and Font Awesome icons.

---

## 10 Priority Calculators for Palliative Care

### 1. **BODE Index - COPD Survival Prediction**
- **File:** `bode-index.html`
- **Clinical Purpose:** Predicts 4-year mortality in COPD patients
- **Components:**
  - Body-mass index (BMI)
  - Obstruction (FEV1 % predicted)
  - Dyspnea (mMRC scale)
  - Exercise capacity (6-Minute Walk Test)
- **Score Range:** 0-10 points
- **Clinical Utility:** Risk stratification for treatment planning and prognosis estimation in COPD patients
- **Category:** Respiratory & COPD Assessment

### 2. **CIWA-Ar Scale - Alcohol Withdrawal Assessment**
- **File:** `ciwa-ar-scale.html`
- **Clinical Purpose:** Quantifies alcohol withdrawal severity for treatment guidance
- **Components:**
  - Nausea/vomiting
  - Tremor
  - Paroxysmal sweats
  - Anxiety
  - Agitation
  - Visual, tactile, and auditory disturbances
  - Headache
  - Orientation
- **Score Range:** 0-67 points
- **Clinical Utility:** Guides pharmacological treatment and monitors withdrawal progression
- **Category:** Addiction & Withdrawal Assessment

### 3. **Child Pugh Score (SI Units) - Liver Disease Severity**
- **File:** `child-pugh-si.html`
- **Clinical Purpose:** Classifies cirrhosis severity using SI units
- **Parameters:**
  - Albumin (g/L)
  - Bilirubin (μmol/L)
  - INR (International Normalized Ratio)
  - Ascites
  - Hepatic encephalopathy
- **Grade Classification:** A (5-6), B (7-9), C (10-15)
- **Clinical Utility:** Predicts surgical risk and mortality in cirrhotic patients
- **Category:** Hepatic Function Assessment

### 4. **Child Pugh Score (Conventional Units) - Liver Disease Severity**
- **File:** `child-pugh-conventional.html`
- **Clinical Purpose:** Classifies cirrhosis severity using conventional units
- **Parameters:**
  - Albumin (g/dL)
  - Bilirubin (mg/dL)
  - INR
  - Ascites
  - Hepatic encephalopathy
- **Grade Classification:** A (5-6), B (7-9), C (10-15)
- **Clinical Utility:** Alternative version for conventional unit systems
- **Category:** Hepatic Function Assessment

### 5. **PHQ-9 Depression Screening - Nine-Item Patient Health Questionnaire**
- **File:** `phq-9-depression-screening.html`
- **Clinical Purpose:** Assesses depressive symptoms and severity in palliative care patients
- **Components:** 9 items evaluating:
  - Anhedonia
  - Depressed mood
  - Sleep disturbance
  - Fatigue
  - Appetite/weight changes
  - Guilt/worthlessness
  - Concentration difficulty
  - Psychomotor changes
  - Suicidal ideation
- **Score Range:** 0-27 points
- **Severity Classification:**
  - 0-4: Minimal
  - 5-9: Mild
  - 10-14: Moderate
  - 15-19: Moderately Severe
  - 20-27: Severe
- **Clinical Utility:** Rapid screening for depression with specific suicidality assessment
- **Category:** Mental Health & Psychological Assessment

### 6. **Pressure Ulcer Risk (Braden Score) - Skin Breakdown Prevention**
- **File:** `pressure-ulcer-risk-braden.html`
- **Clinical Purpose:** Assesses pressure ulcer risk in immobile patients
- **Components:**
  - Sensory perception
  - Moisture
  - Activity level
  - Mobility
  - Nutrition
  - Friction/shear
- **Score Range:** 6-23 points
- **Risk Categories:**
  - 15-18: At risk
  - 13-14: Moderate risk
  - 10-12: High risk
  - ≤9: Very high risk
- **Clinical Utility:** Identifies patients requiring pressure ulcer prevention interventions
- **Category:** Skin Care & Wound Prevention

### 7. **Sleep Problems Questionnaire - Sleep Disturbance Assessment**
- **File:** `sleep-problems-questionnaire.html`
- **Clinical Purpose:** Comprehensive assessment of sleep disturbance in palliative care
- **Components:** 8 items evaluating:
  - Difficulty falling asleep
  - Sleep continuity (nighttime awakenings)
  - Early morning awakening
  - Sleep duration adequacy
  - Overall sleep quality
  - Daytime functional impairment
  - Distress from sleep problems
  - Pain interference with sleep
- **Score Range:** 0-32 points
- **Severity Classification:**
  - 0-8: Minimal
  - 9-16: Mild
  - 17-24: Moderate
  - 25-32: Severe
- **Clinical Utility:** Identifies need for sleep interventions including pain optimization and pharmacotherapy
- **Category:** Mental Health & Sleep Assessment

### 8. **Albumin-Bilirubin (ALBI) Grade - HCC Survival Estimate**
- **File:** `albi-grade-hcc.html`
- **Clinical Purpose:** Estimates survival in hepatocellular carcinoma patients
- **Formula:** ALBI = (0.66 × log(albumin)) - (0.085 × bilirubin)
- **Parameters:**
  - Albumin (g/dL)
  - Bilirubin (mg/dL)
- **Grade Classification:**
  - ≥-2.60: Grade 1 (best prognosis)
  - -2.60 to -1.39: Grade 2
  - <-1.39: Grade 3 (worst prognosis)
- **Clinical Utility:** Simple and effective prognostic model for HCC treatment planning
- **Category:** Hepatic Function & HCC Assessment

### 9. **Conventional Unit to SI Conversions - Chemistry/Endocrine Tests**
- **File:** `conventional-to-si-unit-conversion-chemistry.html`
- **Clinical Purpose:** Converts laboratory values from conventional to SI units
- **Coverage:**
  - Chemistry panel (glucose, electrolytes, renal function, liver function)
  - Endocrine studies (thyroid, cortisol, growth hormone)
  - Hematology values
  - Coagulation studies
  - Lipid panel
- **Clinical Utility:** Facilitates international patient care and clinical collaboration
- **Category:** Laboratory Unit Conversions

### 10. **SI Unit to Conventional Conversions - Chemistry/Endocrine Tests**
- **File:** `si-to-conventional-unit-conversion-chemistry.html`
- **Clinical Purpose:** Converts laboratory values from SI to conventional units
- **Coverage:**
  - Chemistry panel
  - Endocrine studies
  - Hematology values
  - Coagulation studies
  - Lipid panel
- **Clinical Utility:** Interprets international lab reports in conventional unit context
- **Category:** Laboratory Unit Conversions

---

## Design Features

### Technology Stack
- **HTML5:** Semantic markup structure
- **CSS3:** Advanced styling with gradients, animations, and responsive design
- **Bootstrap 5:** Responsive grid system and component framework
- **Font Awesome 6.4.0:** Comprehensive icon library for clinical symbols
- **Vanilla JavaScript:** Lightweight, no framework dependencies

### Visual Design
- **Color Scheme:** Purple gradient theme (Primary: #667eea, Secondary: #764ba2)
- **Responsive Design:** Mobile-first approach with breakpoints for all device sizes
- **Accessibility:** Semantic HTML, proper contrast ratios, icon + text labels
- **User Experience:** Smooth animations, clear visual hierarchy, intuitive navigation

### Functional Features
- **Input Validation:** Real-time validation with user-friendly error messages
- **Clinical Interpretation:** Automatic severity classification and recommendations
- **Responsive Calculation:** Instant results with smooth scrolling to result display
- **Keyboard Support:** Enter key activates calculations for efficient workflow
- **Form Reset:** Easy clearing of inputs for new patient assessments
- **Mobile Optimization:** Touch-friendly interface for bedside use

### Code Quality
- **Comments:** Detailed inline comments explaining clinical logic
- **Kebab-case Filenames:** Standardized naming convention
- **Consistent Structure:** Unified layout across all calculators
- **No External Dependencies:** Except Bootstrap and Font Awesome CDN
- **Clinical Accuracy:** Evidence-based formulas from peer-reviewed literature

---

## Clinical Applications

### Symptom Assessment
- Depression and mental health (PHQ-9)
- Sleep disturbance (Sleep Problems Questionnaire)
- Alcohol withdrawal (CIWA-Ar)
- Pain and functional status (Braden Score, BODE Index)

### Prognosis Estimation
- COPD mortality prediction (BODE Index)
- Liver disease severity (Child Pugh Score)
- HCC survival estimation (ALBI Grade)

### Quality of Life & Functional Assessment
- Respiratory function (BODE Index)
- Skin integrity and pressure ulcer risk (Braden Score)
- Sleep quality and quantity (Sleep Problems Questionnaire)

### Laboratory Data Management
- Unit conversion support (Conventional ↔ SI)
- International patient care coordination

---

## Navigation & Access

### Main Index
**File:** `palliative-care-index.html`

Comprehensive dashboard organizing all 10 calculators by clinical category:
- Respiratory & COPD Assessment
- Addiction & Withdrawal Assessment
- Hepatic Function & HCC Assessment
- Mental Health & Sleep Assessment
- Skin Care & Wound Prevention
- Laboratory Unit Conversions

Each calculator card includes:
- Clinical icon
- Brief description
- Relevant categories
- Direct link to calculator
- Hover effects for enhanced usability

---

## Installation & Deployment

### File Structure
```
/home/user/clirnet/calculators/calculators/
├── palliative-care-index.html                          # Main dashboard
├── bode-index.html                                     # BODE Index
├── ciwa-ar-scale.html                                  # CIWA-Ar Scale
├── child-pugh-si.html                                  # Child Pugh (SI)
├── child-pugh-conventional.html                        # Child Pugh (Conventional)
├── phq-9-depression-screening.html                     # PHQ-9 Depression
├── sleep-problems-questionnaire.html                   # Sleep Assessment
├── pressure-ulcer-risk-braden.html                     # Braden Score
├── albi-grade-hcc.html                                 # ALBI Grade
├── conventional-to-si-unit-conversion-chemistry.html   # Conventional→SI
└── si-to-conventional-unit-conversion-chemistry.html   # SI→Conventional
```

### Browser Compatibility
- Chrome/Chromium: Full support
- Firefox: Full support
- Safari: Full support
- Edge: Full support
- Mobile browsers: Fully responsive

### CDN Requirements
- Bootstrap 5.3.0 CSS (CDN)
- Font Awesome 6.4.0 (CDN)
- No local dependencies required

---

## Clinical Guidelines

### Usage Recommendations
1. **Clinical Context:** Always interpret results within complete clinical context
2. **Patient Input:** Encourage patient participation in assessment
3. **Documentation:** Record scores in patient medical record
4. **Monitoring:** Use serial assessments to track symptom progression
5. **Multidisciplinary Approach:** Integrate with team-based palliative care planning
6. **Shared Decision-Making:** Use scores to facilitate patient/family discussions

### Quality Assurance
- All calculations use validated published formulas
- Results include clinical interpretation guidelines
- Recommendations align with evidence-based palliative care standards
- Regular review for accuracy and clinical relevance

---

## Version History
- **v1.0** (2024-11-08): Initial suite of 10 palliative care calculators
  - All calculators created with purple gradient theme
  - Responsive design for all devices
  - Comprehensive clinical interpretation
  - Full input validation

---

## Clinical References

### BODE Index
- Celli BR, et al. The body-mass index, airflow obstruction, dyspnea, and exercise capacity index in chronic obstructive pulmonary disease. N Engl J Med. 2004.

### CIWA-Ar Scale
- Sullivan JT, et al. Assessment of alcohol withdrawal: the revised Clinical Institute Withdrawal Assessment for Alcohol Scale (CIWA-Ar). Br J Addict. 1989.

### Child Pugh Score
- Child CG, Turcotte JG. Surgery and portal hypertension. Major Probl Clin Surg. 1964.

### PHQ-9
- Kroenke K, et al. The Patient Health Questionnaire-9: validity of a brief depression severity measure. J Gen Intern Med. 2001.

### Braden Score
- Bergstrom N, et al. The Braden Scale for Predicting Pressure Sore Risk. Nurs Res. 1987.

### ALBI Grade
- Johnson PJ, et al. ALBI and platelets: simple new prognostic indicators for HCC. J Clin Med. 2015.

---

## Support & Updates
For questions or clinical feedback regarding these calculators, please consult your institution's informatics or palliative care leadership team.

**Last Updated:** November 8, 2024
