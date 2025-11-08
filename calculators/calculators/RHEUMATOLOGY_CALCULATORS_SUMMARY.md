# Rheumatology Calculators - Summary

## Project Overview

This collection contains **6 comprehensive rheumatology calculators** for disease activity assessment in inflammatory arthritis and gout. All calculators are built with pure HTML5/CSS3/Bootstrap 5 with responsive design, clinical interpretation, and professional styling.

---

## Calculators Created

### 1. BASDAI Calculator
- **File**: `basdai-calculator.html`
- **Full Name**: Bath Ankylosing Spondylitis Disease Activity Index
- **Purpose**: Assess disease activity in ankylosing spondylitis patients
- **Variables**: 6 VAS scales (fatigue, spinal pain, peripheral joints, morning stiffness severity, morning stiffness duration, swelling)
- **Score Range**: 0-10
- **Interpretation Levels**:
  - 0-2.9: Remission/Low Activity
  - 3-5.9: Moderate Activity
  - 6-10: High Activity

**Features**:
- Visual VAS sliders with real-time value display
- Automatic score calculation
- Clinical interpretation with color-coded results
- Reference interpretation table
- Responsive design

---

### 2. Gout Flare Calculator
- **File**: `gout-flare-calculator.html`
- **Full Name**: Clinical Diagnostic Rule for Initial Gout Flare
- **Purpose**: Assess likelihood of gout flare diagnosis based on clinical criteria
- **Variables**: 8 clinical criteria + optional serum urate
- **Scoring System**: Criteria-based (0-8 points, plus 1 for elevated urate)
- **Interpretation Levels**:
  - ≥6 criteria: Gout diagnosis VERY LIKELY
  - 4-5 criteria: Gout diagnosis LIKELY
  - ≤3 criteria: Gout diagnosis LESS LIKELY

**Features**:
- Checkbox-based clinical criteria assessment
- Real-time criteria counting
- Serum urate level integration
- Detailed diagnostic interpretation
- ACR gout diagnostic rule reference

---

### 3. CDAI Calculator
- **File**: `cdai-calculator.html`
- **Full Name**: Clinical Disease Activity Index (Rheumatoid Arthritis)
- **Purpose**: Assess rheumatoid arthritis disease activity without lab tests
- **Variables**:
  - Swollen Joint Count (SJC, 0-28)
  - Tender Joint Count (TJC, 0-28)
  - Patient Global Assessment (PGA, 0-10 VAS)
  - Evaluator Global Assessment (EGA, 0-10 VAS)
- **Score Range**: 0-76
- **Interpretation Levels**:
  - ≤2.8: Remission
  - 2.9-10: Low Disease Activity
  - 10.1-22: Moderate Disease Activity
  - >22: High Disease Activity

**Features**:
- Component-wise score breakdown
- Input validation (0-28 for joint counts, 0-10 for VAS)
- ACR/EULAR remission criterion alignment
- Clinical management recommendations
- Score component visualization

---

### 4. DAS28-CRP Calculator
- **File**: `das28-crp-calculator.html`
- **Full Name**: Disease Activity Score 28 with C-Reactive Protein
- **Purpose**: Comprehensive RA disease activity assessment with CRP
- **Variables**:
  - Swollen Joint Count (0-28)
  - Tender Joint Count (0-28)
  - Patient Global Assessment (0-100 VAS)
  - Evaluator Global Assessment (0-100 VAS)
  - C-Reactive Protein (CRP) level
- **Score Range**: 0-10
- **Formula**: 0.56×√(TJC) + 0.28×√(SJC) + 0.36×ln(CRP+1) + 0.014×PG + 0.96
- **Interpretation Levels**:
  - ≤2.6: Remission
  - 2.7-3.2: Low Disease Activity
  - 3.3-5.1: Moderate Disease Activity
  - >5.1: High Disease Activity

**Features**:
- Logarithmic mathematical transformations
- CRP unit conversion (mg/dL ↔ mg/L)
- Detailed component breakdown with mathematical calculations
- ESR vs CRP comparison
- Professional scoring guide

---

### 5. DAS28-ESR Calculator
- **File**: `das28-esr-calculator.html`
- **Full Name**: Disease Activity Score 28 with Erythrocyte Sedimentation Rate
- **Purpose**: Comprehensive RA disease activity assessment with ESR
- **Variables**:
  - Swollen Joint Count (0-28)
  - Tender Joint Count (0-28)
  - Patient Global Assessment (0-100 VAS)
  - Evaluator Global Assessment (0-100 VAS)
  - Erythrocyte Sedimentation Rate (ESR in mm/hr)
- **Score Range**: 0-10
- **Formula**: 0.56×√(TJC) + 0.28×√(SJC) + 0.70×ln(ESR) + 0.014×PG + 0.08
- **Interpretation Levels**:
  - ≤2.6: Remission
  - 2.7-3.2: Low Disease Activity
  - 3.3-5.1: Moderate Disease Activity
  - >5.1: High Disease Activity

**Features**:
- ESR-based calculation (traditional method)
- Higher ESR weighting (0.70) vs CRP weighting
- Component-wise mathematical breakdown
- CRP-ESR concordance considerations
- Clinical remission target emphasis

---

### 6. SDAI Calculator
- **File**: `sdai-calculator.html`
- **Full Name**: Simplified Disease Activity Index (Rheumatoid Arthritis)
- **Purpose**: Simple RA disease activity assessment with equal weighting
- **Variables**:
  - Swollen Joint Count (0-28)
  - Tender Joint Count (0-28)
  - Patient Global Assessment (0-10)
  - Evaluator Global Assessment (0-10)
  - C-Reactive Protein (CRP in mg/L)
- **Score Range**: 0-~86
- **Formula**: SJC + TJC + PG + EG + CRP (all components equal weighting)
- **Interpretation Levels**:
  - ≤3.3: Remission
  - 3.4-11: Low Disease Activity
  - 11.1-26: Moderate Disease Activity
  - >26: High Disease Activity

**Features**:
- Simple linear addition (no logarithmic transformation)
- Equal component weighting
- Most stringent remission criterion (≤3.3)
- Excellent ACR/EULAR agreement
- Mental math calculation capability
- Advantages section highlighting simplicity

---

## Technical Specifications

### Framework & Libraries
- **Bootstrap 5.3.0**: Responsive grid system and components
- **Font Awesome 6.4.0**: Clinical and UI icons
- **Pure HTML5/CSS3**: No external dependencies for core functionality
- **Vanilla JavaScript**: All calculations client-side (no server required)

### Design Features

#### Purple Gradient Theme
```css
--purple-gradient-start: #667eea;
--purple-gradient-end: #764ba2;
--purple-light: #f3e9ff;
--purple-dark: #4a235a;
```

#### Responsive Design
- Mobile-first approach
- Tablet and desktop optimizations
- Touch-friendly input fields
- Adaptive navigation menu with hamburger toggle

#### User Interface Elements
- **Navigation Bar**: Sticky header with links to all 6 calculators
- **Header Section**: Gradient background with calculator title and description
- **Form Section**: Clearly organized input groups with helpful text
- **Results Section**: Color-coded interpretation with icons and detailed analysis
- **Reference Tables**: Disease activity interpretation guides
- **Footer**: Medical disclaimer and calculation formula

### Validation & Error Handling
- Input range validation for all numeric fields
- Alert messages for invalid inputs
- Joint count constraints (0-28)
- VAS scale constraints (0-10 or 0-100 as appropriate)
- Negative value prevention
- User-friendly error messages

### Clinical Features
- **ACR/EULAR Remission Criteria**: Alignment with treatment targets
- **Color-Coded Results**:
  - Green (Remission): #d4edda
  - Blue (Low Activity): #cfe2ff
  - Yellow (Moderate Activity): #fff3cd
  - Red (High Activity): #f8d7da
- **Clinical Interpretation**: Context-specific recommendations
- **Reference Data**: Standard cutoff values and disease activity classifications
- **Component Breakdown**: Transparent calculation showing all variables

### Code Quality
- **Comments**: Clear inline comments explaining functionality
- **Structured HTML**: Semantic HTML5 elements
- **DRY CSS**: Variables and mixins for consistent styling
- **JavaScript Functions**: Modular, reusable functions
  - `validateInputs()`: Input validation
  - `calculateXXX()`: Calculator-specific logic
  - `displayResults()`: Result presentation
  - `resetForm()`: Form reset functionality

### Accessibility
- Semantic HTML labels linked to form inputs
- Clear visual hierarchy
- High contrast color scheme
- Keyboard navigable
- Mobile-friendly touch targets
- Help text for all input fields

---

## File Structure

```
/home/user/clirnet/calculators/calculators/
├── basdai-calculator.html              (24 KB)
├── cdai-calculator.html                (24 KB)
├── das28-crp-calculator.html           (25 KB)
├── das28-esr-calculator.html           (25 KB)
├── gout-flare-calculator.html          (25 KB)
├── sdai-calculator.html                (26 KB)
└── RHEUMATOLOGY_CALCULATORS_SUMMARY.md (this file)
```

---

## Usage Instructions

### Basic Use
1. Open any calculator HTML file in a web browser
2. Fill in the clinical assessment data
3. Click "Calculate" button
4. View results with clinical interpretation
5. Use "Reset" button to clear form for new patient

### Navigation
- Use the sticky navigation bar to switch between calculators
- Icons help identify each calculator type
- Mobile menu available on small screens

### Interpreting Results
- **Score Range**: Upper scale shows possible score range
- **Activity Level**: Color-coded classification
- **Clinical Recommendation**: Suggested management approach
- **Reference Table**: Full interpretation guide
- **Component Breakdown**: Shows calculation details

---

## Clinical Applications

### BASDAI
- Serial monitoring of ankylosing spondylitis
- Treatment response assessment
- Research studies in spondylitis

### Gout Flare Rule
- Rapid bedside diagnosis of acute arthritis
- Differentiation from other causes of acute monoarticular arthritis
- Research and clinical validation

### CDAI
- Rheumatoid arthritis disease monitoring
- Does not require lab tests (practical advantage)
- Clinical practice and research

### DAS28-CRP & DAS28-ESR
- Comprehensive RA disease activity assessment
- Treatment response evaluation
- Comparison between CRP and ESR approaches
- International standard for RA assessment

### SDAI
- Simplified RA assessment
- Remission achievement evaluation
- Practical clinical use (can calculate mentally)
- ACR/EULAR remission target definition

---

## Browser Compatibility

- Chrome/Edge 90+
- Firefox 88+
- Safari 14+
- Mobile browsers (iOS Safari, Chrome Mobile)

No external APIs or server calls required - fully functional offline.

---

## Disclaimer

These calculators are provided for educational purposes only. They should not replace professional medical judgment. Always consult with a qualified rheumatologist for clinical decision-making, treatment planning, and patient management.

---

## References

**BASDAI**: Garrett S, et al. Ann Rheum Dis. 1994;53(6):365-368.

**Gout Diagnostic Rule**: Janssens HJ, et al. Arthritis Rheum. 2010;62(10):3050-3059.

**CDAI**: Aletaha D, et al. Arthritis Rheum. 2005;52(9):2873-2876.

**DAS28**: Prevoo ML, et al. Br J Rheumatol. 1995;34(12):1174-1177.

**SDAI**: Smolen JS, et al. Arthritis Rheum. 2003;48(3):723-735.

---

## Created

November 8, 2025 - Rheumatology Calculator Suite
