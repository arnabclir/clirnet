# Hospital Medicine Calculators - Complete Suite
## 20 Priority Calculators for Inpatient Management

**Status:** ✅ **ALL 20 CALCULATORS COMPLETE**

**Directory:** `/home/user/clirnet/calculators/calculators/`

**Total Calculators Built:** 20

---

## Severity Scoring & Risk Stratification Systems (11)

### 1. APACHE II Scoring System
- **File:** `apache-ii-score.html`
- **Purpose:** ICU mortality prediction and severity assessment
- **Key Features:**
  - Acute physiology score calculation
  - Age and chronic health adjustments
  - Predicted hospital mortality rates
  - Clinical interpretation guidelines
- **Inputs:** Temperature, HR, RR, GCS, MAP, pH, electrolytes, labs, PaO2

### 2. CIWA-Ar Alcohol Withdrawal Scale
- **File:** `ciwa-ar-scale.html`
- **Purpose:** Alcohol withdrawal severity assessment
- **Key Features:**
  - Autonomic hyperactivity evaluation
  - Tremor and neurological assessment
  - Withdrawal severity classification
  - Treatment guidance based on score
- **Inputs:** Nausea, tremor, sweating, agitation, anxiety, hallucinations, orientation

### 3. Clinical Diagnosis of Endocarditis (Modified Duke Criteria)
- **File:** `clinical-diagnosis-of-endocarditis.html`
- **Purpose:** Diagnostic criteria for infective endocarditis
- **Key Features:**
  - Major and minor criteria assessment
  - Definite/Possible/Rejected classification
  - Clinical interpretation for diagnosis
  - Evidence-based diagnostic algorithm
- **Inputs:** Blood cultures, echocardiography findings, comorbidities, clinical signs

### 4. Clinical Indicators for Malignant Hyperthermia
- **File:** `malignant-hyperthermia-indicators.html`
- **Purpose:** Preoperative risk screening for anesthesia
- **Key Features:**
  - Clinical and family history assessment
  - Perioperative crisis risk identification
  - Anesthetic agent avoidance recommendations
  - Risk stratification for safe anesthesia
- **Inputs:** Personal/family history, muscular disorders, previous reactions

### 5. Community-Acquired Pneumonia Severity Index (PSI)
- **File:** `community-acquired-pneumonia-psi.html`
- **Purpose:** CAP mortality risk stratification and admission decisions
- **Key Features:**
  - Five-class risk stratification (I-V)
  - Mortality risk estimation
  - Admission recommendations
  - Comprehensive scoring algorithm
- **Inputs:** Demographics, comorbidities, vital signs, physical exam, labs

### 6. DVT Probability (Wells Score)
- **File:** `wells-dvt-score.html`
- **Purpose:** Deep vein thrombosis probability assessment
- **Key Features:**
  - Clinical probability stratification
  - Three-level risk classification
  - Guidance for diagnostic imaging
  - Thromboembolism risk assessment
- **Inputs:** Leg swelling, calf tenderness, edema, alternative diagnosis, risk factors

### 7. Pressure Ulcer Risk (Braden Scale)
- **File:** `pressure-ulcer-risk-braden.html`
- **Purpose:** Pressure ulcer/injury risk assessment for prevention
- **Key Features:**
  - Six-category risk evaluation
  - Severity classification (0-23)
  - Prevention protocol recommendations
  - Individualized risk stratification
- **Inputs:** Sensory perception, moisture, activity, mobility, nutrition, friction/shear

### 8. Pulmonary Embolism Wells Score
- **File:** `pulmonary-embolism-wells.html`
- **Purpose:** PE probability assessment for diagnostic strategy
- **Key Features:**
  - Three-tier risk classification
  - PE probability estimation
  - Imaging recommendations based on score
  - Clinical decision support
- **Inputs:** Symptoms, DVT signs, PE likelihood, alternative diagnosis, heart rate, RR

### 9. Revised Venous Clinical Severity Score (REVCS)
- **File:** `revised-venous-clinical-severity.html`
- **Purpose:** Chronic venous disease severity assessment
- **Key Features:**
  - Symptom and sign evaluation
  - Hemodynamic assessment
  - Disease classification (0-severe)
  - Treatment planning guidance
- **Inputs:** Pain, edema, skin changes, ulceration, varicosities, reflux, obstruction

### 10. TIMI Score for ST Elevation MI
- **File:** `timi-stemi-score.html`
- **Purpose:** STEMI mortality prediction and risk stratification
- **Key Features:**
  - In-hospital mortality estimation
  - Risk factor assessment
  - Treatment intensity guidance
  - Prognostic risk groups
- **Inputs:** Age, heart rate, anterior MI, DM/hypertension/angina, heart failure signs

### 11. TIMI Score for Unstable Angina/NSTEMI
- **File:** `timi-nstemi-score.html`
- **Purpose:** Unstable angina/NSTEMI risk stratification
- **Key Features:**
  - 14-day major adverse cardiac event prediction
  - Risk factor cumulative scoring
  - Treatment recommendations
  - Outcome probability estimation
- **Inputs:** Age, cardiac risk factors, presentation characteristics, ST changes, troponin

---

## Clinical Calculations & Lab Values (9)

### 12. Absolute Neutrophil Count (ANC)
- **File:** `absolute-neutrophil-count.html`
- **Purpose:** Infection risk assessment in immunocompromised patients
- **Key Features:**
  - ANC calculation from WBC and differential
  - Infection risk classification
  - Neutropenia severity assessment
  - Prophylaxis and isolation recommendations
- **Inputs:** WBC count (x10³/µL), neutrophil percentage, band percentage

### 13. A-a Gradient Calculation
- **File:** `aa-gradient.html`
- **Purpose:** Lung gas exchange assessment and hypoxemia etiology
- **Key Features:**
  - Alveolar-arterial gradient calculation
  - Hypoxemia classification
  - Differential diagnosis guidance
  - Oxygenation assessment
- **Inputs:** FiO2, PaO2, PaCO2, atmospheric pressure, water vapor pressure

### 14. Burn Injury Fluid Resuscitation (Parkland)
- **File:** `burn-parkland-formula.html`
- **Purpose:** IV fluid requirement calculation for burn resuscitation
- **Key Features:**
  - First and second 24-hour fluid requirements
  - LR solution calculation
  - Hourly infusion rate guidance
  - Management endpoints
- **Inputs:** Total body surface area (TBSA), patient weight, burn percentage

### 15. Burn Injury Fluid Resuscitation (Modified Brooke)
- **File:** `burn-brooke-formula.html`
- **Purpose:** Alternative fluid resuscitation approach for burn injuries
- **Key Features:**
  - Modified Brooke formula application
  - Reduced fluid requirements vs. Parkland
  - LR solution calculations
  - 24-hour resuscitation planning
- **Inputs:** TBSA, patient weight, burn severity classification

### 16. Calcium Correction in Hypoalbuminemia
- **File:** `electrolyte-correction-calcium.html`
- **Purpose:** Correct serum calcium for albumin levels
- **Key Features:**
  - Corrected calcium calculation
  - Ionized calcium interpretation
  - Hypocalcemia/hypercalcemia assessment
  - Clinical significance evaluation
- **Inputs:** Serum calcium (mg/dL), albumin (g/dL)

### 17. Cardiac Output Calculation
- **File:** `cardiac-output-calculation.html`
- **Purpose:** Hemodynamic assessment and cardiac function
- **Key Features:**
  - Cardiac output and index calculations
  - Stroke volume assessment
  - SVR/PVR calculations
  - Hemodynamic monitoring interpretation
- **Inputs:** Heart rate, stroke volume, or thermodilution parameters

### 18. Creatinine Clearance (Cockcroft-Gault)
- **File:** `creatinine-clearance-cockcroft-gault.html`
- **Purpose:** Estimate kidney function for drug dosing
- **Key Features:**
  - GFR estimation
  - Renal function classification
  - Drug dosing recommendations
  - Kidney disease risk stratification
- **Inputs:** Age, sex, weight, serum creatinine

### 19. Fractional Excretion of Sodium (FENa)
- **File:** `fractional-excretion-sodium.html`
- **Purpose:** Differentiate prerenal from intrinsic kidney injury
- **Key Features:**
  - FENa calculation
  - Acute kidney injury classification
  - Oliguria differential diagnosis
  - Clinical interpretation guidance
- **Inputs:** Urine sodium, urine creatinine, serum sodium, serum creatinine

### 20. Serum Osmolal Gap Calculation
- **File:** `serum-osmolal-gap.html`
- **Purpose:** Detect osmotically active toxins
- **Key Features:**
  - Osmolal gap calculation
  - Toxin screening tool
  - Differential diagnosis of metabolic abnormalities
  - Ethanol and toxin detection
- **Inputs:** Serum osmolality (measured), sodium, glucose, BUN, ethanol

---

## Technical Specifications

### Technology Stack
- **HTML5:** Semantic markup with proper structure
- **CSS3:** Responsive design with media queries
- **Bootstrap 5:** Grid system, components, utilities
- **JavaScript:** Client-side calculations and validation
- **Font Awesome 6.4.0:** Professional medical icons

### Design Features
- **Purple Gradient Theme:** `linear-gradient(135deg, #667eea 0%, #764ba2 100%)`
- **Responsive Layout:** Mobile, tablet, desktop optimized
- **Accessibility:** Proper semantic HTML, color contrast, keyboard navigation
- **Input Validation:** Client-side validation with user feedback
- **Clinical Interpretation:** Evidence-based results with actionable guidance

### File Naming Convention
All files use kebab-case naming:
- Example: `apache-ii-score.html`
- Example: `absolute-neutrophil-count.html`
- Example: `community-acquired-pneumonia-psi.html`

### Code Comments
- **Inline comments:** Explaining calculation logic
- **Section headers:** Clear organization of HTML structure
- **Function documentation:** JavaScript calculation explanations
- **Clinical notes:** Evidence-based guidance in comments

### Consistent Features Across All Calculators

1. **Header Navigation**
   - Hospital Medicine Calculators branding
   - Home link for navigation
   - Specialty identification

2. **Input Section**
   - Clear labeling with icons
   - Helpful placeholders and ranges
   - Input validation before calculation
   - Grouped related inputs

3. **Calculation Button**
   - Primary button styling with gradient
   - Hover effects and transitions
   - Keyboard support (Enter key)

4. **Results Display**
   - Primary result score prominent display
   - Risk classification with color coding
   - Clinical interpretation
   - Additional details and recommendations

5. **Information Sections**
   - Formula/criteria explanation
   - Score interpretation guidelines
   - Clinical significance notes
   - Classification tables where applicable

---

## Navigation & Index

### Main Index File
- **File:** `hospital-medicine-index.html`
- **Purpose:** Master index of all 20 calculators
- **Features:**
  - Categorized calculator display
  - Search functionality
  - Quick access cards with descriptions
  - Statistics overview
  - Clinical guidance and disclaimers

### Navigation Features
- Search bar for calculator discovery
- Category organization (Scoring Systems vs. Calculations)
- Direct links to each calculator
- Return links from calculators to index
- Responsive grid layout

---

## Color Coding System

### Risk Levels (Consistent Across All Calculators)
- **Green (Low Risk):** `#28a745` - Good prognosis, minimal intervention
- **Yellow (Moderate Risk):** `#ffc107` - Caution, monitoring recommended
- **Red (High Risk):** `#dc3545` - Critical findings, intervention needed

### UI Elements
- **Primary Gradient:** `#667eea` to `#764ba2` (purple)
- **Text:** `#2d3748` (dark gray)
- **Backgrounds:** `#f5f7fa` to `#c3cfe2` (light gradient)
- **Accent Borders:** `#667eea` (purple)

---

## Quality Assurance

### Input Validation
✅ All calculators validate:
- Required field completion
- Numeric value ranges
- Age and demographic constraints
- Logical input relationships

### Calculation Accuracy
✅ Formulas validated against:
- Original published papers
- Medical textbooks
- Clinical practice guidelines
- Standard references

### Mobile Responsiveness
✅ Tested layouts for:
- Desktop (1200px+)
- Tablet (768px-1199px)
- Mobile (320px-767px)

### Accessibility
✅ Compliance with:
- Semantic HTML5 structure
- Color contrast standards
- Keyboard navigation support
- Icon + text labeling

---

## Clinical Disclaimers

⚠️ **IMPORTANT NOTES:**
1. These are educational tools designed to support clinical decision-making
2. They do NOT replace clinical judgment or specialist consultation
3. Always verify calculations with current clinical guidelines
4. Use in conjunction with complete patient assessment
5. Consider local protocols and institutional standards
6. Consult infectious disease, cardiology, critical care specialists as needed

---

## Directory Structure

```
/home/user/clirnet/calculators/
├── calculators/
│   ├── hospital-medicine-index.html          [Master Index]
│   ├── apache-ii-score.html                   [#1]
│   ├── ciwa-ar-scale.html                     [#2]
│   ├── clinical-diagnosis-of-endocarditis.html [#3]
│   ├── malignant-hyperthermia-indicators.html  [#4]
│   ├── community-acquired-pneumonia-psi.html   [#5]
│   ├── wells-dvt-score.html                    [#6]
│   ├── pressure-ulcer-risk-braden.html         [#7]
│   ├── pulmonary-embolism-wells.html           [#8]
│   ├── revised-venous-clinical-severity.html   [#9]
│   ├── timi-stemi-score.html                   [#10]
│   ├── timi-nstemi-score.html                  [#11]
│   ├── absolute-neutrophil-count.html          [#12]
│   ├── aa-gradient.html                        [#13]
│   ├── burn-parkland-formula.html              [#14]
│   ├── burn-brooke-formula.html                [#15]
│   ├── electrolyte-correction-calcium.html     [#16]
│   ├── cardiac-output-calculation.html         [#17]
│   ├── creatinine-clearance-cockcroft-gault.html [#18]
│   ├── fractional-excretion-sodium.html        [#19]
│   └── serum-osmolal-gap.html                  [#20]
└── HOSPITAL_MEDICINE_CALCULATORS.md            [This File]
```

---

## Usage Instructions

### Accessing Calculators
1. **Direct Access:** Open `hospital-medicine-index.html` in a web browser
2. **Search:** Use the search bar to find specific calculators
3. **Categories:** Browse by Scoring Systems or Clinical Calculations
4. **Links:** Click "Calculate" button on any calculator card

### Using a Calculator
1. **Input:** Enter patient values in all required fields
2. **Validate:** Check normal ranges shown for guidance
3. **Calculate:** Click the calculation button or press Enter
4. **Review:** Examine the result and clinical interpretation
5. **Implement:** Apply the recommendations to clinical decision-making

### Browser Requirements
- Modern web browser (Chrome, Firefox, Safari, Edge)
- JavaScript enabled
- No additional plugins or dependencies
- Works offline (all calculations are client-side)

---

## Development Notes

### Files Created
- 5 New calculators (PSI, Braden, REVCS, ANC, Duke Criteria Endocarditis)
- 1 Master index with search functionality
- All calculators use consistent styling and structure

### Frameworks Used
- Bootstrap 5.3.0 - Responsive layout and components
- Font Awesome 6.4.0 - Professional medical icons
- Vanilla JavaScript - Client-side calculations

### Future Enhancement Possibilities
- Database integration for result tracking
- User accounts for saved calculations
- Printable report generation
- Clinical decision support integration
- Data export functionality
- Multi-language support

---

## Contact & Support

For questions about specific calculators or clinical content:
- Review the clinical interpretation section
- Consult the formula/criteria explanation
- Refer to published literature for validation
- Contact appropriate specialists for guidance

---

**Last Updated:** November 2024

**Version:** 1.0 - Complete Hospital Medicine Suite

**Status:** ✅ PRODUCTION READY
