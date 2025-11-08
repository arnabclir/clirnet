# Sports Medicine Unit Conversion Calculators

## Overview
Four comprehensive pure HTML5/CSS3/Bootstrap 5 calculators for Primary Care Sports Medicine practitioners to convert laboratory values between conventional and SI units.

---

## Calculators Built

### 1. Conventional to SI Conversion - Chemistry & Endocrine
**File:** `/home/user/clirnet/calculators/calculators/sports-medicine-conv-to-si-chemistry.html`

**Tests Included:**
- Glucose (mg/dL → mmol/L)
- Urea/BUN (mg/dL → mmol/L)
- Creatinine (mg/dL → μmol/L)
- Sodium (mEq/L → mmol/L)
- Potassium (mEq/L → mmol/L)
- Calcium/Total (mg/dL → mmol/L)

**Features:**
- 6 laboratory test conversions
- Sports medicine-specific clinical interpretations
- Reference tables with normal ranges
- Conversion factors and formulas
- Input validation with error handling
- Real-time conversion display

---

### 2. Conventional to SI Conversion - Immunology
**File:** `/home/user/clirnet/calculators/calculators/sports-medicine-conv-to-si-immunology.html`

**Tests Included:**
- WBC/Leukocyte Count (K/μL → ×10⁹/L)
- Lymphocytes (K/μL → ×10⁹/L)
- Neutrophils (K/μL → ×10⁹/L)
- Monocytes (K/μL → ×10⁹/L)
- Eosinophils (K/μL → ×10⁹/L)
- Immunoglobulin G/IgG (mg/dL → g/L)

**Features:**
- 6 immunology value conversions
- Exercise immunology context
- Immune response monitoring guidance
- Training adaptation assessment tools
- Overtraining syndrome indicators

---

### 3. SI to Conventional Conversion - Chemistry & Endocrine
**File:** `/home/user/clirnet/calculators/calculators/sports-medicine-si-to-conv-chemistry.html`

**Tests Included:**
- Glucose (mmol/L → mg/dL)
- Urea (mmol/L → mg/dL)
- Creatinine (μmol/L → mg/dL)
- Sodium (mmol/L → mEq/L)
- Potassium (mmol/L → mEq/L)
- Calcium (mmol/L → mg/dL)

**Features:**
- Reverse conversion from SI to conventional units
- Same comprehensive interpretations
- Clinical decision support
- International standards compliance

---

### 4. SI to Conventional Conversion - Immunology
**File:** `/home/user/clirnet/calculators/calculators/sports-medicine-si-to-conv-immunology.html`

**Tests Included:**
- WBC Count (×10⁹/L → K/μL)
- Lymphocytes (×10⁹/L → K/μL)
- Neutrophils (×10⁹/L → K/μL)
- Monocytes (×10⁹/L → K/μL)
- Eosinophils (×10⁹/L → K/μL)
- IgG (g/L → mg/dL)

**Features:**
- Bidirectional immunology conversions
- Training load assessment
- Immune function monitoring

---

## Technical Specifications

### Framework & Libraries
- **Bootstrap 5.3.0** - Responsive grid and components
- **Font Awesome 6.4** - 40+ medical/scientific icons
- **Pure HTML5/CSS3** - No external frameworks or dependencies
- **Vanilla JavaScript** - No jQuery or libraries required

### Design Features
- **Color Scheme:** Purple gradient theme (#667eea to #764ba2)
- **Responsive Layout:** Mobile-first design (tested responsive breakpoints)
- **Accessibility:** ARIA labels, semantic HTML, keyboard navigation
- **Performance:** Lightweight (44-45KB per calculator)

### Code Quality
- **Comprehensive Comments:** JSDoc-style function documentation
- **Input Validation:** Error handling for all inputs
- **Error Messages:** User-friendly validation feedback
- **Calculation Accuracy:** 1-2 decimal place precision (clinically appropriate)

### Navigation Features
- **Sticky Navigation Bar:** Always accessible
- **Smooth Scrolling:** Jump to calculator, reference, help sections
- **Mobile Menu:** Collapsible navigation for mobile devices
- **Internal Anchors:** Quick navigation to different sections

---

## Unique Features

### Clinical Interpretation Engine
Each test result includes:
- Automated interpretation based on reference ranges
- Sports medicine-specific clinical context
- Training response indicators
- Overtraining syndrome markers
- Hydration status assessment
- Bone health monitoring

### Reference Materials
- **Conversion Tables:** Complete conversion factors
- **Normal Ranges:** Both conventional and SI units
- **Sports Context:** Athletic performance implications
- **Educational Sections:** How-to guides and medical notes

### User Experience
- **One-Click Conversion:** "Convert All Values" button
- **Reset Form:** Clear all inputs instantly
- **Real-Time Validation:** Immediate error detection
- **Enter Key Support:** Press Enter to convert
- **Result Display:** Side-by-side input/output comparison

---

## File Specifications

| File Name | Size | Lines | Tests |
|-----------|------|-------|-------|
| sports-medicine-conv-to-si-chemistry.html | 45KB | 1130 | 6 Chemistry |
| sports-medicine-conv-to-si-immunology.html | 44KB | 1111 | 6 Immunology |
| sports-medicine-si-to-conv-chemistry.html | 44KB | 1107 | 6 Chemistry |
| sports-medicine-si-to-conv-immunology.html | 44KB | 1107 | 6 Immunology |
| **TOTAL** | **177KB** | **4455** | **24 Tests** |

---

## Key Conversion Factors

### Chemistry & Endocrine (Conversion Formulas)
| Test | Conventional → SI | SI → Conventional |
|------|-------------------|-------------------|
| Glucose | × 0.05551 | ÷ 0.05551 |
| Urea (BUN) | × 0.3567 | ÷ 0.3567 |
| Creatinine | × 88.42 | ÷ 88.42 |
| Sodium | × 1.0 | ÷ 1.0 |
| Potassium | × 1.0 | ÷ 1.0 |
| Calcium | × 0.2495 | ÷ 0.2495 |

### Immunology (Conversion Formulas)
| Test | Conventional → SI | SI → Conventional |
|------|-------------------|-------------------|
| WBC | × 1.0 | ÷ 1.0 |
| Lymphocytes | × 1.0 | ÷ 1.0 |
| Neutrophils | × 1.0 | ÷ 1.0 |
| Monocytes | × 1.0 | ÷ 1.0 |
| Eosinophils | × 1.0 | ÷ 1.0 |
| IgG | × 0.01 | × 100 |

---

## Usage Instructions

### Basic Workflow
1. **Open Calculator:** Select appropriate calculator for your test type and conversion direction
2. **Enter Value:** Input the laboratory result in the source unit
3. **View Results:**
   - Converted value appears in target unit
   - Clinical interpretation displays automatically
   - Reference range comparison provided
4. **Reset:** Click "Reset Form" to clear and start over

### Mobile Usage
- Fully responsive on iOS/Android devices
- Touch-friendly buttons and inputs
- Collapsible navigation menu
- Optimized font sizes for readability

### Keyboard Navigation
- **Tab:** Navigate between inputs
- **Enter:** Trigger conversion (when input focused)
- **Shift+Tab:** Navigate backwards
- **Click or Touch:** All buttons fully functional

---

## Sports Medicine Clinical Context

### Hydration & Performance
- Monitor **sodium** levels during endurance events
- Track **urea/BUN** for dehydration assessment
- Compare **creatinine** baseline for kidney function

### Overtraining Syndrome Detection
- **Elevated urea/creatinine ratio** - Possible overtraining
- **Chronic WBC elevation** - Immune stress
- **Depressed lymphocytes** - Training fatigue

### Bone Health Monitoring
- **Calcium levels** - Important for injury prevention
- **Baseline assessment** - For athletes on restrictive diets
- **Recovery tracking** - Post-injury calcium supplementation

### Immune Function Assessment
- **IgG trends** - Infection risk in endurance athletes
- **Lymphocyte response** - Training adaptation
- **Post-exercise transients** - Normal leukocytosis patterns

---

## Validation & Error Handling

### Input Validation
- Rejects negative numbers
- Detects non-numeric input
- Requires valid numeric values
- Clear error messages with icons

### Display Features
- Appropriate decimal precision (1-2 places)
- Unit labels on all values
- Color-coded interpretation boxes
- Reference range comparisons

### Browser Compatibility
- Chrome/Chromium 90+
- Firefox 88+
- Safari 14+
- Edge 90+
- Mobile browsers (iOS Safari, Chrome Mobile)

---

## Compliance & Disclaimers

All calculators include:
- Educational purpose disclaimer
- Healthcare professional consultation notice
- Clinical reference standards notation
- Date and version information
- No warranty for medical decisions

---

## Future Enhancement Ideas

- Add more laboratory tests (lipid panel, thyroid, etc.)
- Export results to PDF
- Comparison charts for trend analysis
- Integration with EMR systems
- Mobile app versions
- Additional language support
- Dark mode toggle

---

## File Locations

```
/home/user/clirnet/calculators/calculators/
├── sports-medicine-conv-to-si-chemistry.html
├── sports-medicine-conv-to-si-immunology.html
├── sports-medicine-si-to-conv-chemistry.html
├── sports-medicine-si-to-conv-immunology.html
└── SPORTS-MEDICINE-CALCULATORS.md (this file)
```

---

## Version Information

- **Version:** 1.0
- **Release Date:** November 8, 2025
- **Last Updated:** November 8, 2025
- **Status:** Production Ready
- **Maintenance:** As needed for clinical guideline updates

---

**Created for Primary Care Sports Medicine Practitioners**
Pure HTML5/CSS3/Bootstrap 5 Implementation
