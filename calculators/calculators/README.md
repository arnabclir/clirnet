# Gastroenterology & Hepatology Clinical Calculators

A comprehensive suite of 15 responsive, interactive clinical calculators for gastroenterology and hepatology professionals. Built with pure HTML5, CSS3, and Bootstrap 5.

## Features

- **Pure HTML5/CSS3/Bootstrap 5** - No dependencies beyond CDN links
- **Responsive Design** - Works seamlessly on desktop, tablet, and mobile devices
- **Purple Gradient Theme** - Modern, professional appearance with consistent branding
- **Font Awesome Icons** - Intuitive visual indicators and navigation icons
- **Input Validation** - Prevents calculation errors with required field checks
- **Clinical Interpretation** - Automatic risk stratification and clinical recommendations
- **Unit Conversion** - Support for both SI and conventional units where applicable
- **Code Comments** - Well-documented JavaScript for maintainability
- **Navigation Menu** - Easy access to home, calculator list, and current calculator

## Available Calculators

### 1. **Blatchford Score** (`blatchford-score.html`)
- **Purpose**: GI bleeding severity risk stratification
- **Units**: Conventional and SI units supported
- **Inputs**: Age, sex, vital signs, hemoglobin, BUN, clinical symptoms, comorbidities
- **Output**: Risk stratification (low to very high risk)

### 2. **CLIF-SOFA Score** (`clif-sofa-score.html`)
- **Purpose**: Acute-on-chronic liver failure prognosis
- **Inputs**: PaO2/FiO2, INR, bilirubin, creatinine, encephalopathy grade, MAP
- **Output**: Organ failure assessment, 3-month mortality prediction
- **Units**: Supports both SI and conventional units

### 3. **Child Pugh Score (SI Units)** (`child-pugh-si.html`)
- **Purpose**: Liver disease severity classification
- **Inputs**: Bilirubin (μmol/L), albumin (g/L), INR, ascites, encephalopathy
- **Output**: Child Pugh Class (A, B, C) with mortality estimates

### 4. **Child Pugh Score (Conventional Units)** (`child-pugh-conventional.html`)
- **Purpose**: Liver disease severity classification
- **Inputs**: Bilirubin (mg/dL), albumin (g/dL), INR, ascites, encephalopathy
- **Output**: Child Pugh Class (A, B, C) with mortality estimates

### 5. **Crohn Disease Activity Index (CDAI)** (`crohn-disease-activity-index.html`)
- **Purpose**: Crohn's disease activity assessment (8-day period)
- **Inputs**: Liquid stools, bloody stools, abdominal pain, well-being, complications, fever, abdominal mass
- **Output**: Activity classification (remission, mild-moderate, moderate-severe, severe)

### 6. **Glasgow Alcoholic Hepatitis Score** (`glasgow-alcoholic-hepatitis-score.html`)
- **Purpose**: Prognosis prediction in severe alcoholic hepatitis
- **Inputs**: Age, WBC, bilirubin, INR or PT
- **Output**: 28-day mortality prediction
- **Units**: Supports both SI and conventional units

### 7. **Harvey-Bradshaw Index** (`harvey-bradshaw-index.html`)
- **Purpose**: Simplified Crohn's disease activity assessment
- **Inputs**: Abdominal pain, liquid stools, general well-being, abdominal mass, complications
- **Output**: Activity classification (remission, mild, moderate, severe)

### 8. **Hepatitis Discriminant Function** (`hepatitis-discriminant-function.html`)
- **Purpose**: Distinguishes severe from mild hepatitis
- **Inputs**: PT prolongation, total bilirubin
- **Output**: Severe vs mild hepatitis classification

### 9. **Mayo Score** (`mayo-score-ulcerative-colitis.html`)
- **Purpose**: Ulcerative colitis disease activity assessment
- **Inputs**: Stool frequency, rectal bleeding, mucosal appearance, patient well-being
- **Output**: Activity classification (remission, mild-moderate, moderate-severe, severe)

### 10. **Ranson Criteria** (`ranson-criteria-pancreatitis.html`)
- **Purpose**: Acute pancreatitis prognosis and mortality prediction
- **Inputs**: Age, glucose, WBC, AST, LDH (at presentation); BUN, calcium, PaO2, fluid sequestration (at 48 hours)
- **Output**: Risk stratification with mortality estimates

### 11. **Rockall Score** (`rockall-score-gi-bleeding.html`)
- **Purpose**: Upper GI bleeding risk stratification
- **Inputs**: Age, shock status, comorbidities, endoscopic diagnosis, stigmata of recent hemorrhage
- **Output**: Risk stratification (low, moderate, high risk)

### 12. **APRI Score (SI Units)** (`apri-score-si.html`)
- **Purpose**: Liver fibrosis assessment using AST-to-Platelet Ratio
- **Inputs**: AST (U/L), platelet count (x10^9/L), AST upper limit of normal
- **Output**: Fibrosis probability (no significant, indeterminate, advanced)

### 13. **APRI Score (Conventional Units)** (`apri-score-conventional.html`)
- **Purpose**: Liver fibrosis assessment using AST-to-Platelet Ratio
- **Inputs**: AST (U/L), platelet count (K/μL), AST upper limit of normal
- **Output**: Fibrosis probability (no significant, indeterminate, advanced)

### 14. **MELD/MELDNa Score** (`meld-meldna-score.html`)
- **Purpose**: Liver transplant priority and mortality prediction
- **Inputs**: INR, total bilirubin, creatinine, sodium (optional), dialysis history
- **Output**: MELD and MELDNa scores with transplant priority assessment

### 15. **FIB-4 Index** (`fib4-index-liver-fibrosis.html`)
- **Purpose**: Non-invasive liver fibrosis marker
- **Formula**: (Age × AST) / (Platelet count × sqrt(ALT))
- **Inputs**: Age, AST, ALT, platelet count
- **Output**: Fibrosis probability (low, indeterminate, high risk)

## File Naming Convention

All files use kebab-case naming:
- `blatchford-score.html`
- `clif-sofa-score.html`
- `child-pugh-si.html`
- `child-pugh-conventional.html`
- etc.

## Technical Details

### HTML5 Structure
- Semantic HTML5 elements
- Proper meta tags for character encoding and viewport
- Valid DOCTYPE declaration

### CSS3/Bootstrap 5
- Bootstrap 5.3.0 via CDN
- Custom CSS variables for purple gradient theme
- Responsive grid system
- Custom styling for calculator-specific elements

### Font Awesome Icons
- Font Awesome 6.4.0 via CDN
- Descriptive medical/health icons throughout
- Consistent icon usage across all calculators

### JavaScript Functionality
- Pure vanilla JavaScript (no jQuery required)
- Input validation and error handling
- Dynamic result display with clinical interpretation
- Reset functionality for all form fields
- Conversion between unit systems where applicable

### Purple Gradient Theme
```css
Primary: linear-gradient(135deg, #667eea 0%, #764ba2 100%)
Secondary: linear-gradient(135deg, #764ba2 0%, #f093fb 100%)
```

## Clinical Accuracy

All calculators implement clinically validated formulas and interpretation guidelines:

1. **Blatchford Score**: Risk stratification for upper GI bleeding
2. **CLIF-SOFA**: Acute-on-chronic liver failure assessment
3. **Child Pugh**: Validated since 1973 for cirrhosis severity
4. **CDAI**: Original 8-day disease activity index for Crohn's
5. **Glasgow Score**: Prognostic marker in alcoholic hepatitis
6. **Harvey-Bradshaw**: Simplified version of CDAI
7. **Hepatitis DF**: Discriminates severe hepatitis
8. **Mayo Score**: Standard UC disease activity assessment
9. **Ranson Criteria**: Pancreatitis mortality prediction (1974-present)
10. **Rockall Score**: Upper GI bleeding prognosis
11. **APRI**: Validated non-invasive fibrosis marker
12. **MELD/MELDNa**: Standard for liver transplant allocation
13. **FIB-4**: Simple non-invasive fibrosis assessment

## Usage

1. Open any calculator HTML file in a web browser
2. Fill in required clinical parameters
3. Click "Calculate" button
4. View results with clinical interpretation
5. Use "Reset" button to clear and start over
6. Navigate between calculators using the navbar

## Browser Compatibility

- Chrome/Chromium (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)
- Mobile browsers (iOS Safari, Chrome Mobile)

## Dependencies

All dependencies are loaded via CDN:
- Bootstrap 5.3.0
- Font Awesome 6.4.0
- No local dependencies required

## Integration Notes

- Calculators can be integrated into existing medical applications
- Each calculator is self-contained (single HTML file)
- No server-side processing required
- Can be embedded in iframes or used as standalone pages
- Navigation links point to index.html, catalog.html (modify as needed)

## Future Enhancements

- Print functionality for reports
- PDF export of results
- Data storage/history tracking
- Unit conversion presets
- Multi-language support
- Integration with EHR systems
- Mobile app versions

---

**Last Updated**: November 2024
**Version**: 1.0
**Clinical Review Status**: Ready for clinical use
