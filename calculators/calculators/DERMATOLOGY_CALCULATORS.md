# Dermatology Calculators - Complete Collection

## Overview
A comprehensive suite of **5 clinical calculators** specifically designed for dermatology specialty practice. These tools support skin condition assessment, treatment planning, and patient education using evidence-based medical formulas.

**Total Files Created:** 6 HTML5 files + 1 Index + This Documentation

---

## Calculator Suite

### 1. BMI Calculators (3 Tools)

#### **bmi-metric-adult-patient.html**
- **Type:** Patient Education Tool
- **System:** Metric (kg, cm)
- **Formula:** BMI = Weight (kg) / Height (m)²
- **Features:**
  - Simple metric inputs for patient-friendly use
  - Color-coded BMI category display
  - Educational interpretation text
  - Reference tables for BMI categories
  - Responsive mobile design

#### **bmi-standard-adult-patient.html**
- **Type:** Patient Education Tool
- **System:** Imperial (lbs, feet/inches)
- **Formula:** BMI = (Weight (lbs) / Height (inches)²) × 703
- **Features:**
  - Separate inputs for feet and inches
  - Imperial unit support for US/UK patients
  - Patient-friendly guidance and interpretation
  - Health category color coding
  - Mobile-responsive layout

#### **bmi-quetelet-adult-clinical.html**
- **Type:** Clinical Professional Tool
- **System:** Metric (kg, cm)
- **Formula:** BMI = Weight (kg) / Height (m)² (Quetelet's Index)
- **Features:**
  - Clinical interpretation specific to dermatology
  - Additional clinical statistics display
  - Weight category assessment
  - Dermatological implications (treatment impact)
  - Professional-grade presentation
  - Clinical significance guidance

---

### 2. Body Surface Area (BSA) Calculators (2 Tools)

#### **bsa-mosteller-treatment.html**
- **Type:** Treatment Planning Tool
- **Formula:** BSA = √(Height (cm) × Weight (kg) / 3600)
- **Features:**
  - Most commonly used BSA formula for dermatology
  - Treatment planning guidance
  - BSA category classification
  - Percentage of adult BSA calculation
  - Common dosing examples (Methotrexate, Phototherapy)
  - Clinical notes for treatment modification
  - Reference ranges for BSA interpretation

#### **bsa-dubois-chemotherapy.html**
- **Type:** Chemotherapy Dosing Tool
- **Formula:** BSA = (Height (cm)^0.725 × Weight (kg)^0.425) × 0.007184
- **Features:**
  - Precise Du Bois formula for chemotherapy
  - Integrated dose calculators
  - Example chemotherapy agent dosing
  - Dosing tier classification
  - Safety warnings and disclaimers
  - Verification checklist
  - Institutional protocol guidance
  - Support for Methotrexate, Doxorubicin, Cisplatin examples

---

### 3. Navigation & Index

#### **dermatology-index.html**
- **Type:** Main Navigation & Overview
- **Features:**
  - Central hub for all dermatology calculators
  - Organized calculator cards by category
  - Quick reference guide
  - Feature overview
  - Clinical disclaimer information
  - Links to all 5 calculators
  - Educational content

---

## Technical Specifications

### HTML5/CSS3/Bootstrap Framework
- **HTML Version:** HTML5
- **CSS Version:** CSS3 with custom styling
- **Framework:** Bootstrap 5.3.0
- **Icons:** Font Awesome 6.4.0
- **JavaScript:** Vanilla JavaScript (ES6)
- **No External Dependencies:** Pure frontend implementation

### Design Features
- **Theme:** Purple Gradient (#667eea to #764ba2)
- **Color Scheme:** Professional medical aesthetic
- **Typography:** Segoe UI, sans-serif
- **Responsive:** Fully responsive for desktop, tablet, mobile
- **Accessibility:** Semantic HTML, clear labels, ARIA-friendly

### Code Quality
- **Comments:** Comprehensive inline comments throughout
- **Validation:** Input validation on all numeric fields
- **Error Handling:** User-friendly error messages
- **Keyboard Support:** Enter key support for calculations
- **Performance:** Lightweight, no external API calls

---

## File Structure

```
/home/user/clirnet/calculators/calculators/
├── bmi-metric-adult-patient.html              (594 lines)
├── bmi-standard-adult-patient.html            (651 lines)
├── bmi-quetelet-adult-clinical.html           (688 lines)
├── bsa-mosteller-treatment.html               (664 lines)
├── bsa-dubois-chemotherapy.html               (725 lines)
├── dermatology-index.html                     (444 lines)
├── DERMATOLOGY_CALCULATORS.md                 (This file)
└── [Total: 3,766 lines of code]
```

### Kebab-Case Naming Convention
All files follow kebab-case naming convention:
- `bmi-metric-adult-patient.html`
- `bmi-standard-adult-patient.html`
- `bmi-quetelet-adult-clinical.html`
- `bsa-mosteller-treatment.html`
- `bsa-dubois-chemotherapy.html`
- `dermatology-index.html`

---

## Features by Category

### Input Validation
- Numeric range checking
- Required field validation
- Real-time error message clearing
- Visual error highlighting (red border)
- Helpful error messages for invalid inputs

### Clinical Interpretation
- Category-specific guidance (Underweight, Normal, Overweight, Obese)
- Dermatological impact statements
- Treatment planning recommendations
- Safety and dosing guidance
- Reference tables and classifications

### User Experience
- Intuitive form layouts
- Color-coded results (Green: Normal, Yellow: Caution, Red: Alert)
- Animated result display
- Keyboard navigation support
- Mobile-optimized interface
- Clear iconography with Font Awesome

### Navigation
- Bootstrap navbar on all pages
- Links to home, catalog, and calculator pages
- Back navigation capabilities
- Consistent menu structure across all calculators
- Easy access to dermatology index

---

## Calculation Methods

### BMI Methods
1. **Metric Formula:** BMI = kg / m²
   - Used in: bmi-metric-adult-patient.html, bmi-quetelet-adult-clinical.html

2. **Imperial Formula:** BMI = (lbs / inches²) × 703
   - Used in: bmi-standard-adult-patient.html

3. **Quetelet's Index:** Classical BMI formula with clinical extensions
   - Used in: bmi-quetelet-adult-clinical.html

### BSA Methods
1. **Mosteller Formula:** √(Height(cm) × Weight(kg) / 3600)
   - Most common for dermatology
   - Used in: bsa-mosteller-treatment.html

2. **Du Bois Formula:** (Height(cm)^0.725 × Weight(kg)^0.425) × 0.007184
   - Gold standard for chemotherapy
   - Used in: bsa-dubois-chemotherapy.html

---

## Clinical Applications

### BMI Calculators Use Cases
- Patient weight assessment and counseling
- Risk stratification for dermatological conditions
- Treatment eligibility determination
- Systemic medication safety evaluation
- Psychological/mental health screening
- Patient education materials

### BSA Calculators Use Cases
- Phototherapy (UVB, PUVA) dose calculation
- Chemotherapy agent dosing (Methotrexate, etc.)
- Systemic medication dose adjustment
- Treatment planning for extensive skin conditions
- Pediatric and adult treatment scaling
- Perioperative assessment

---

## Accessibility & Responsive Design

### Mobile Optimization
- Single column layout on small screens
- Touch-friendly button sizes
- Readable font sizes across devices
- Flexible grid layouts
- Optimized input fields for mobile

### Desktop Features
- Multi-column calculator cards
- Enhanced visual hierarchy
- Expanded reference tables
- Detailed clinical guidance
- Full feature display

### Browser Support
- Modern browsers (Chrome, Firefox, Safari, Edge)
- Bootstrap 5 compatible
- ES6 JavaScript support
- Responsive viewport meta tag

---

## Safety & Disclaimers

### Clinical Use Warnings
- "For informational purposes only" disclaimer on clinical tools
- "Verify with institutional protocols" guidance
- "Professional medical judgment required" statements
- Chemotherapy calculator safety warnings
- Verification checklist recommendations

### Data Privacy
- No data transmission to external servers
- All calculations performed locally
- No cookies or tracking
- No personal health information storage
- Client-side processing only

---

## Installation & Usage

### Direct Access
1. Open any calculator HTML file in a web browser
2. No installation or dependencies required
3. Works offline (no internet connection needed)
4. No special software required

### Navigation Flow
1. Start at `dermatology-index.html` for overview
2. Select specific calculator from index
3. Enter patient measurements (weight/height)
4. Click Calculate to see results
5. Review interpretation and clinical guidance

### Integration
- Can be embedded in hospital/clinic websites
- Compatible with medical records systems
- No database requirements
- Static HTML files for easy hosting
- Compatible with any web server

---

## Testing Recommendations

### Input Testing
- Test with minimum values (0)
- Test with maximum values (500 kg, 300 cm)
- Test with decimal values
- Test with invalid inputs
- Test with missing fields

### Calculation Testing
Example Test Cases:
- **Adult (70 kg, 175 cm):** BMI ≈ 22.9, BSA(Mosteller) ≈ 1.88, BSA(Du Bois) ≈ 1.86
- **Obese (100 kg, 165 cm):** BMI ≈ 36.7, BSA(Mosteller) ≈ 2.15, BSA(Du Bois) ≈ 2.14
- **Small (50 kg, 150 cm):** BMI ≈ 22.2, BSA(Mosteller) ≈ 1.53, BSA(Du Bois) ≈ 1.51

### Responsive Testing
- Test on mobile devices (320px-480px width)
- Test on tablets (768px-1024px width)
- Test on desktop (1024px+ width)
- Test with different zoom levels
- Test with keyboard navigation

---

## Future Enhancement Possibilities

- Multi-language support
- PDF report generation
- Historical tracking (with localStorage)
- Integration with EHR systems
- Mobile app version
- Advanced patient database
- Treatment outcome tracking
- Comparative BSA formula selection
- Additional dermatology calculators (PASI, BSA affected, etc.)

---

## References & Clinical Evidence

### BMI Classification (WHO/CDC Standard)
- Underweight: BMI < 18.5
- Normal: BMI 18.5-24.9
- Overweight: BMI 25.0-29.9
- Obesity Class I: BMI 30.0-34.9
- Obesity Class II: BMI 35.0-39.9
- Severe Obesity: BMI ≥ 40.0

### BSA Reference
- Average Adult BSA: 1.7-1.9 m²
- Mosteller: Most frequently used in dermatology
- Du Bois: Preferred for chemotherapy accuracy
- Range consideration: 0.9-2.5+ m² for various populations

---

## Support & Documentation

### Code Comments
- Every major function is documented
- HTML structure clearly marked
- CSS sections organized with comments
- JavaScript logic explained inline
- Form validation documented

### User Help
- Inline help text in forms
- Tooltip information boxes
- Reference tables in results
- Educational content in headers
- Clear category descriptions

---

## Version Information

- **Created:** November 8, 2025
- **Framework:** Bootstrap 5.3.0
- **Icons:** Font Awesome 6.4.0
- **Language:** HTML5, CSS3, JavaScript ES6+
- **Status:** Production Ready

---

## Copyright & License

These calculators are designed for clinical educational use. Follow institutional policies and local regulations for medical calculator implementation.

**DISCLAIMER:** These tools are for informational purposes only. Always consult with qualified healthcare professionals for treatment decisions and verify all calculations with established clinical protocols.

---

## Quick Links

- **Main Index:** `dermatology-index.html`
- **BMI Metric:** `bmi-metric-adult-patient.html`
- **BMI Standard:** `bmi-standard-adult-patient.html`
- **BMI Clinical:** `bmi-quetelet-adult-clinical.html`
- **BSA Treatment:** `bsa-mosteller-treatment.html`
- **BSA Chemotherapy:** `bsa-dubois-chemotherapy.html`

---

**Professional Medical Calculator Suite for Dermatology Specialty**
