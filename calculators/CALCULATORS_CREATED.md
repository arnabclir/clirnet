# Medical Calculators - Anesthesiology & Emergency Medicine

## Summary
Successfully created **21 clinical calculators** for Anesthesiology (14) and Emergency Medicine (7) specialties.

All calculators feature:
- Pure HTML5/CSS3/Bootstrap 5 responsive design
- Purple gradient theme (#667eea to #764ba2)
- Font Awesome icons (v6.4.0)
- Input validation and error handling
- Clinical interpretation of results
- Display of calculation formulas
- Mobile-friendly responsive layout
- Navigation back to dashboard
- Kebab-case file naming

---

## ANESTHESIOLOGY CALCULATORS (14)

### 1. **apache-ii-score.html**
   - APACHE II Scoring System
   - Acute Physiology and Chronic Health Evaluation II
   - ICU mortality prediction
   - Calculates severity of acute illness with physiological parameters
   - Output: Score 0-71 with mortality risk percentage

### 2. **ariscat-score.html**
   - ARISCAT Preoperative Pulmonary Risk Index
   - Assess Respiratory Risk In Surgical Patients In Catalonia
   - Predicts postoperative pulmonary complications
   - Includes age, SpO2, infection history, anemia, surgery type, duration
   - Output: Risk categories (Low, Intermediate, High)

### 3. **ciwa-ar-scale.html**
   - CIWA-Ar Clinical Institute Withdrawal Assessment for Alcohol
   - Assesses severity of alcohol withdrawal syndrome
   - 10-point assessment with sliders for symptom scoring
   - Output: Severity categories with treatment recommendations

### 4. **child-pugh-score-si.html**
   - Child-Pugh Score (SI Units)
   - Evaluates liver disease severity
   - Bilirubin (μmol/L), Albumin (g/L), INR, Encephalopathy, Ascites
   - Output: Class A/B/C with survival rates

### 5. **child-pugh-score-conventional.html**
   - Child-Pugh Score (Conventional Units)
   - Same assessment using conventional units
   - Bilirubin (mg/dL), Albumin (g/dL)
   - Output: Class A/B/C with prognosis

### 6. **enhanced-stop-bang-osa.html**
   - Enhanced STOP-Bang Screening Questionnaire
   - Sleep Apnea screening for surgical patients
   - 8-point assessment (Snore, Tired, Observed, Pressure, BMI, Age, Neck, Gender)
   - Output: Risk categories with recommendations

### 7. **bmi-calculator.html**
   - Body Mass Index (Quetelet's Index)
   - Metric (kg, cm) and Imperial (lb, in) support
   - Dual unit toggle
   - Output: BMI value with weight classification

### 8. **bsa-mosteller.html**
   - Body Surface Area (Mosteller Method)
   - Formula: √[Height(cm) × Weight(kg) / 3600]
   - Most commonly used BSA calculation
   - Output: BSA in m² with interpretation

### 9. **bsa-du-bois.html**
   - Body Surface Area (Du Bois Method)
   - Historical formula: 0.007184 × Height^0.725 × Weight^0.425
   - Alternative for extremes of body composition
   - Output: BSA in m² with comparison

### 10. **fat-free-mass-female.html**
    - Fat-Free Mass (LBW) for Adult Females
    - Hume formula for females
    - Used for drug dosing and anesthetic calculations
    - Output: FFM in kg with body fat percentage

### 11. **fat-free-mass-male.html**
    - Fat-Free Mass (LBW) for Adult Males
    - Hume formula for males
    - Adjusted formula for male body composition
    - Output: FFM in kg with body fat percentage

### 12. **ideal-body-weight.html**
    - Ideal Body Weight and Adjusted Body Weight
    - Devine formula for IBW
    - Adjusted weight for obese patients: AdjBW = IBW + 0.4(ActualW - IBW)
    - Output: IBW, AdjBW, BMI, dosing recommendations

### 13. **endotracheal-tube-size.html**
    - Endotracheal Tube Size for Children (1-8 years)
    - Cole formula: ETT size = (Age/4) + 4
    - Insertion depth: (Age/2) + 12
    - Output: Recommended ETT size, depth, backup tube sizes with reference table

### 14. **malignant-hyperthermia-indicators.html**
    - Clinical Indicators for Malignant Hyperthermia
    - Screening questionnaire for MH susceptibility
    - 6-point risk assessment
    - Output: Risk level with drug contraindications and safe alternatives

---

## EMERGENCY MEDICINE CALCULATORS (7)

### 1. **cows-withdrawal-scale.html**
   - Clinical Opioid Withdrawal Scale
   - Assesses opioid withdrawal severity in emergency patients
   - 10-item assessment (pulse, sweating, nausea, tremor, ptosis, ache, goose flesh, nose itch, GI, tremor)
   - Output: Score with severity categories and treatment guidance

### 2. **perc-rule.html**
   - Pulmonary Embolism Rule-Out Criteria
   - 8-point safety criteria for PE exclusion
   - All criteria must be met (Age <50, HR <100, SpO2 ≥95%, RR <30, SBP ≥100, Normal mental status, No DVT, No O2 required)
   - Output: PERC Negative (low risk) or PERC Positive (need imaging)

### 3. **qsofa-score.html**
   - Sequential Organ Failure Assessment (qSOFA)
   - Quick sepsis risk assessment
   - 3-point scale (Altered mental status, RR ≥22, SBP ≤100)
   - Output: Score with sepsis risk classification

### 4. **blood-ethanol-concentration.html**
   - Blood Ethanol Concentration Estimator
   - Widmark formula: BAC = (Drinks × 5.14 / (Weight × r)) - (0.015 × Hours)
   - Accounts for gender, weight, drinks consumed, time elapsed
   - Output: BAC in mg/dL with impairment level

### 5. **burn-parkland-formula.html**
   - Burn Injury Fluid Resuscitation (Parkland Formula)
   - Total 24h = 4 mL × TBSA (%) × Weight (kg)
   - Ringer's Lactate, 50% first 8 hours, 50% next 16 hours
   - Output: Total fluid, 8-hour, 16-hour volumes, hourly infusion rate

### 6. **burn-brooke-formula.html**
   - Burn Injury Fluid Resuscitation (Modified Brooke Formula)
   - Total 24h = 2 mL × TBSA (%) × Weight (kg)
   - Reduces fluid overload compared to Parkland
   - Output: Total fluid, 8-hour, 16-hour volumes, hourly infusion rate

### 7. **endotracheal-tube-size.html** (same as Anesthesia #13)
   - Endotracheal Tube Size for Children (1-8 years)
   - Applicable to both anesthesia and emergency medicine

---

## Technical Features

### All Calculators Include:
- **Responsive Design**: Mobile, tablet, and desktop compatible
- **Bootstrap 5.3.0**: Modern CSS framework
- **Font Awesome 6.4.0**: Professional medical icons
- **Purple Gradient Theme**: #667eea to #764ba2
- **Input Validation**: Ensures proper data entry
- **Error Handling**: User-friendly error messages
- **Clinical Context**: Formula explanations and clinical interpretation
- **Navigation**: Back button to dashboard
- **Pure HTML/CSS/JavaScript**: No external dependencies (CDN-based)

### File Naming Convention:
All files use kebab-case (lowercase with hyphens):
- `apache-ii-score.html`
- `enhanced-stop-bang-osa.html`
- `blood-ethanol-concentration.html`
- etc.

### Directory Structure:
```
/home/user/clirnet/calculators/calculators/
├── apache-ii-score.html
├── ariscat-score.html
├── bmi-calculator.html
├── blood-ethanol-concentration.html
├── bsa-du-bois.html
├── bsa-mosteller.html
├── burn-brooke-formula.html
├── burn-parkland-formula.html
├── child-pugh-score-conventional.html
├── child-pugh-score-si.html
├── ciwa-ar-scale.html
├── cows-withdrawal-scale.html
├── endotracheal-tube-size.html
├── enhanced-stop-bang-osa.html
├── fat-free-mass-female.html
├── fat-free-mass-male.html
├── ideal-body-weight.html
├── malignant-hyperthermia-indicators.html
├── perc-rule.html
└── qsofa-score.html
```

---

## Calculation Examples

### APACHE II Score
- Input: 12 physiological parameters (temperature, HR, RR, GCS, pH, sodium, potassium, creatinine, WBC, hematocrit, glucose, PaO2)
- Formula: Acute Physiology Score (0-60) + Age Points + Chronic Health Points
- Output: Total score 0-71 with mortality risk percentage

### Parkland Formula
- Input: Weight (kg), TBSA (%)
- Formula: 4 mL × TBSA × Weight
- Output: Total fluid volume, distribution over 24 hours

### CIWA-Ar Scale
- Input: 10 symptom assessments
- Formula: Sum of all component scores
- Output: Total score 0-67 with withdrawal severity

### BSA (Mosteller)
- Input: Height (cm), Weight (kg)
- Formula: √[(Height × Weight) / 3600]
- Output: BSA in m²

---

## Clinical Notes

1. **APACHE II**: Used for ICU mortality prediction; scores increase exponentially with mortality risk
2. **ARISCAT**: Identifies patients at risk for postoperative pulmonary complications; helps guide preoperative optimization
3. **CIWA-Ar**: Scores >15 indicate need for pharmacological intervention
4. **PERC Rule**: All 8 criteria must be met to safely exclude PE; use with clinical judgment
5. **qSOFA**: Score ≥2 suggests sepsis; highly specific but less sensitive than full SOFA
6. **Parkland Formula**: Provides starting point; adjust based on urine output (target 0.5 mL/kg/h)
7. **Modified Brooke**: Reduces fluid overload compared to Parkland; becoming preferred formula
8. **Malignant Hyperthermia**: Positive screening requires avoiding volatile anesthetics and succinylcholine

---

## Status: COMPLETE
All 21 calculators have been successfully created and deployed.
Created: November 8, 2025
