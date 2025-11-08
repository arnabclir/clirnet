# Gastroenterology & Hepatology Calculators - Clinical Reference

## 1. Blatchford Score
**File**: `blatchford-score.html`
**Purpose**: Upper GI bleeding severity and risk stratification
**Formula Components**:
- Age ≥60: +1
- Female: +1
- SBP 100-109: +1 | 90-99: +2 | <90: +3
- HR 100-119: +1 | ≥120: +2
- Hb 10-12.9: +1 | <10: +3
- BUN 18.2-22.4: +2 | ≥22.4: +3
- Melena: +1
- Syncope: +2
- Cardiac disease: +2
- Renal disease: +2

**Risk Levels**:
- Score 0: Low risk
- Score 1-2: Low-moderate risk
- Score 3-5: Moderate risk
- Score 6-8: High risk
- Score >8: Very high risk

---

## 2. CLIF-SOFA Score
**File**: `clif-sofa-score.html`
**Purpose**: Acute-on-chronic liver failure prognosis
**Components**:
- Respiratory (PaO2/FiO2 ratio): 0-4 points
- Coagulation (INR): 0-4 points
- Liver function (Bilirubin mg/dL): 0-4 points
- Renal function (Creatinine mg/dL): 0-4 points
- Brain (Encephalopathy grade): 0-4 points
- Circulation (MAP mmHg): 0-3 points

**Total Score**: 0-28 points
- ≤4: No organ failure
- 5-8: Single organ failure
- 9-12: Multiple organ failures
- ≥13: Severe multi-organ failure

---

## 3. Child Pugh Score (SI Units)
**File**: `child-pugh-si.html`
**Parameters** (Each 1-3 points):
- Bilirubin: <34 (1) | 34-51 (2) | >51 (3) μmol/L
- Albumin: >35 (1) | 28-35 (2) | <28 (3) g/L
- INR: <1.3 (1) | 1.3-1.6 (2) | >1.6 (3)
- Ascites: None (1) | Slight (2) | Moderate-Severe (3)
- Encephalopathy: None (1) | I-II (2) | III-IV (3)

**Classification**:
- Class A (5-6): Mild, ~1.5% 1-year mortality
- Class B (7-9): Moderate, ~10% 1-year mortality
- Class C (10-15): Severe, ~45% 1-year mortality

---

## 4. Child Pugh Score (Conventional Units)
**File**: `child-pugh-conventional.html`
**Parameters** (Each 1-3 points):
- Bilirubin: <2 (1) | 2-3 (2) | >3 (3) mg/dL
- Albumin: >3.5 (1) | 2.8-3.5 (2) | <2.8 (3) g/dL
- INR: <1.3 (1) | 1.3-1.6 (2) | >1.6 (3)
- Ascites: None (1) | Slight (2) | Moderate-Severe (3)
- Encephalopathy: None (1) | I-II (2) | III-IV (3)

---

## 5. Crohn Disease Activity Index (CDAI)
**File**: `crohn-disease-activity-index.html`
**Formula** (8-day assessment):
- Liquid/soft stools × 2
- Bloody stools × 5
- Abdominal pain × (severity level) × (days with pain)
- General well-being × 7
- Complications (each 5-20 points)
- Fever: +10
- Abdominal mass: 0-20

**Activity Levels**:
- <150: Clinical remission
- 150-220: Mild-moderate activity
- 220-450: Moderate-severe activity
- >450: Severe activity

---

## 6. Glasgow Alcoholic Hepatitis Score
**File**: `glasgow-alcoholic-hepatitis-score.html`
**Formula**: Prognostic score for severe alcoholic hepatitis
- Age <50: +1
- WBC <15: +1 | ≥15: +2
- Bilirubin <250: +1 | 250-400: +2 | >400: +3
- INR <1.5: +1 | 1.5-1.8: +2 | >1.8: +3

**Prognosis**:
- ≤8: Poor prognosis (≤15% mortality)
- >8: Very poor prognosis (>50% mortality)

---

## 7. Harvey-Bradshaw Index
**File**: `harvey-bradshaw-index.html`
**Components**:
- Abdominal pain: 0-3 points
- Liquid stools per day: 1 point each
- General well-being: 0-3 points
- Abdominal mass: 0-2 points
- Complications: 1 point each

**Activity Levels**:
- ≤4: Clinical remission
- 5-7: Mild disease
- 8-16: Moderate disease
- >16: Severe disease

---

## 8. Hepatitis Discriminant Function
**File**: `hepatitis-discriminant-function.html`
**Formula**: (1.5 × PT prolongation) + (Bilirubin / 2.3)

**Classification**:
- <32: Mild hepatitis
- ≥32: Severe hepatitis (consider corticosteroids)

---

## 9. Mayo Score - Ulcerative Colitis
**File**: `mayo-score-ulcerative-colitis.html`
**Components** (Each 0-3 points):
- Stool frequency
- Rectal bleeding
- Endoscopic findings (mucosal appearance)
- Patient well-being assessment

**Total Score**: 0-12 points
- ≤2: Clinical remission
- 3-5: Mild activity
- 6-10: Moderate-severe activity
- >10: Severe activity

---

## 10. Ranson Criteria - Pancreatitis
**File**: `ranson-criteria-pancreatitis.html`
**At Presentation** (5 criteria):
- Age >55
- Glucose >200 mg/dL
- WBC >16 K/μL
- AST >250 U/L
- LDH >350 U/L

**At 48 Hours** (4 criteria):
- BUN increase >5 mg/dL
- Calcium <8 mg/dL
- PaO2 <60 mmHg
- Fluid sequestration >6 L

**Mortality by Score**:
- 0-2: <1%
- 3-4: 1-3%
- 5-6: 3-15%
- 7-8: 15-50%
- ≥9: >50%

---

## 11. Rockall Score - Upper GI Bleeding
**File**: `rockall-score-gi-bleeding.html`
**Clinical Variables**:
- Age: <60 (0) | 60-79 (1) | >79 (2)
- Shock: No (0) | Tachycardia (1) | Hypotension (2)
- Comorbidity: None (0) | Major (1) | Severe (2)

**Endoscopic Variables**:
- Diagnosis: Mallory-Weiss (0) | Ulcer (1) | Variceal (2)
- Stigmata: None (0) | Major bleeding (2)

**Risk Stratification**:
- ≤2: Low risk
- 3-4: Moderate risk
- ≥5: High risk

---

## 12. APRI Score (SI Units)
**File**: `apri-score-si.html`
**Formula**: (AST/ULN ÷ Platelet count) × 100

Where:
- AST = Aspartate aminotransferase (U/L)
- ULN = Upper limit of normal (typically 40 U/L)
- Platelet count = x10^9/L

**Interpretation**:
- <0.5: No significant fibrosis
- 0.5-1.5: Indeterminate (need further testing)
- >1.5: Probable advanced fibrosis (F3-F4)

---

## 13. APRI Score (Conventional Units)
**File**: `apri-score-conventional.html`
**Formula**: Same as SI version
- AST in U/L
- Platelet count in K/μL

**Interpretation**: Same cutoffs as SI version

---

## 14. MELD/MELDNa Score
**File**: `meld-meldna-score.html`
**MELD Formula**:
MELD = 10 × [0.957 × ln(INR) + 0.378 × ln(Bilirubin) + 1.12 × ln(Creatinine)] + 6.43

**MELDNa Formula**:
MELDNa = MELD + 1.32 × (137 - Na) - (0.033 × MELD × (137 - Na))

**Priority Assessment**:
- ≤10: Low priority
- 11-20: Moderate priority
- 21-30: High priority (8% 3-month mortality)
- >30: Very high priority (>50% 3-month mortality)

---

## 15. FIB-4 Index
**File**: `fib4-index-liver-fibrosis.html`
**Formula**: (Age in years × AST [U/L]) / (Platelet count [x10^9/L] × √ALT [U/L])

**Interpretation**:
- <1.30: Low probability of advanced fibrosis
- 1.30-2.67: Indeterminate (need elastography or biopsy)
- >2.67: High probability of advanced fibrosis (F3-F4)

**Note**: More accurate in HCV, good in HBV, less reliable with normal ALT

---

## Unit Conversion Reference

### Bilirubin
- 1 mg/dL = 17.1 μmol/L

### Albumin
- 1 g/dL = 10 g/L

### Creatinine
- 1 mg/dL = 88.4 μmol/L

### Glucose
- 1 mg/dL = 0.0555 mmol/L

### Hemoglobin
- 1 g/dL = 10 g/L

### BUN/Urea
- 1 mg/dL BUN = 0.357 mmol/L urea

---

## Clinical Notes

1. **Blatchford vs Rockall**: Blatchford more focused on initial risk, Rockall incorporates endoscopy findings
2. **Child Pugh vs MELD**: Child Pugh longer established, MELD better for transplant decisions
3. **CDAI vs Harvey-Bradshaw**: CDAI more comprehensive, HB simpler for clinical practice
4. **APRI vs FIB-4**: Both non-invasive; APRI better at extremes, FIB-4 simpler formula
5. **Mayo Score**: Updated periodically; confirm most recent thresholds with guidelines

---

**Clinical Disclaimer**: These calculators are educational tools. Clinical decisions should be made in conjunction with physician judgment and all available clinical information.

**Last Updated**: November 2024
