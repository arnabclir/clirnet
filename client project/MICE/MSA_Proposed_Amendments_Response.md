# Proposed Amendments to Master Services Agreement
## CLIRNET Services Private Limited - Response to GSK

**Date:** December 3, 2025
**Re:** Master Services Agreement dated November 27, 2025
**Sections:** Cyber Security Schedule & Artificial Intelligence Schedule

---

Dear Team,

Thank you for sharing the draft Master Services Agreement. We have reviewed the Cyber Security Schedule and Artificial Intelligence sections as requested. Below are our proposed amendments for your consideration before we finalize the agreement for the MiCE pilot.

---

## 1. CYBER SECURITY SCHEDULE

### 1.1 Section 3.1 - Comprehensive Security Program Standards

| Current Language | Area of Concern | Proposed Amendment |
|------------------|-----------------|-------------------|
| "be consistent with generally-accepted industry standards (e.g., ISO 27001, COBIT, NIST 800-53)" | Requires immediate compliance with multiple international standards without allowance for certification timeline | **Proposed Change:** Add language: *"Counterparty shall demonstrate compliance with at least one of the listed standards (ISO 27001, COBIT, or NIST 800-53) or provide a compliance roadmap within 90 days of the SOW Effective Date for any standards not yet achieved."* |

**Rationale:** This allows operational flexibility while maintaining security commitment.

---

### 1.2 Section 7.2 - Patching Timelines

| Current Language | Area of Concern | Proposed Amendment |
|------------------|-----------------|-------------------|
| "critical or high severity vulnerability security patches implemented within 30 days" | 30-day window may be operationally challenging for complex systems requiring testing before deployment | **Proposed Change:** Amend to: *"critical or high severity vulnerability security patches implemented within **45 days**, unless a shorter timeline is mandated by the nature of the vulnerability or regulatory requirement."* |

**Rationale:** Allows adequate time for patch testing in production-equivalent environments to prevent service disruption.

---

### 1.3 Section 8.4 - Cryptography

| Current Language | Area of Concern | Proposed Amendment |
|------------------|-----------------|-------------------|
| "Strong Encryption controls" | Term "Strong Encryption" is undefined, creating ambiguity in compliance assessment | **Proposed Change:** Add definition: *"'Strong Encryption' means encryption using AES-256 or equivalent algorithm for data at rest, and TLS 1.2 or higher for data in transit."* |

**Rationale:** Provides clarity and measurable compliance criteria for both parties.

---

### 1.4 Section 8.6 - Security Breach Notification

| Current Language | Area of Concern | Proposed Amendment |
|------------------|-----------------|-------------------|
| "within 24 hours of Counterparty's verification" | 24-hour window is extremely tight for comprehensive verification and initial assessment | **Proposed Change:** Amend to: *"within **48 hours** of Counterparty's verification of a confirmed Security Breach, with preliminary notification within 24 hours of suspected breach."* |

**Rationale:** Allows for proper verification while maintaining prompt communication through preliminary notification.

---

## 2. ARTIFICIAL INTELLIGENCE SCHEDULE

### 2.1 Section 1.1 - Use of AI Systems Notice

| Current Language | Area of Concern | Proposed Amendment |
|------------------|-----------------|-------------------|
| "Counterparty will not use or include any AI System in the Services and/or Deliverables unless Counterparty has provided notice to GSK and GSK has provided written agreement" | The MiCE platform is AI-assisted; this clause requires explicit pre-approval | **Proposed Change:** Add to the Statement of Work: *"GSK hereby acknowledges and provides written agreement for CLIRNET's use of the MiCE (Moment Marketing Intelligent Content Engine) AI-assisted platform for the Services described herein, subject to the terms of this AI Schedule."* |

**Rationale:** Provides upfront approval for the known AI component of the engagement, avoiding operational delays.

---

### 2.2 Section 1.2 - Modification of AI Systems

| Current Language | Area of Concern | Proposed Amendment |
|------------------|-----------------|-------------------|
| "GSK may, in its sole discretion, instruct Counterparty to stop using the AI System... GSK will have no liability to Counterparty" | Allows unilateral termination of AI usage without notice period or compensation for work in progress | **Proposed Change:** Amend to: *"GSK may, in its sole discretion, instruct Counterparty to stop using the AI System in connection with the Services and/or Deliverables, **provided that GSK shall give Counterparty at least 14 days written notice** (except in cases of Security Breach or regulatory requirement). GSK will have no liability to Counterparty **beyond payment for Services properly rendered prior to such instruction**."* |

**Rationale:** Provides reasonable transition period and protects CLIRNET for work already completed.

---

### 2.3 Section 2.2 - Use of GSK AI Data

| Current Language | Area of Concern | Proposed Amendment |
|------------------|-----------------|-------------------|
| "Counterparty will not use GSK AI Data to train any AI Systems... or to improve the operation of its services or models offered or provided to any entity other than GSK" | Prevents CLIRNET from deriving any generalizable learnings from the engagement | **Proposed Change:** Add clarification: *"Notwithstanding the foregoing, Counterparty may use **anonymized, aggregated insights** derived from the engagement (not including any GSK Confidential Information, GSK Data, or identifiable content) for internal process improvement purposes only, provided such use does not reveal or reconstruct any GSK Data."* |

**Rationale:** Industry-standard allowance for operational learning while protecting GSK's proprietary information.

---

### 2.4 Section 5.5 - AI Incidents Definition & Reporting

| Current Language | Area of Concern | Proposed Amendment |
|------------------|-----------------|-------------------|
| AI Incident includes "inaccuracies in the Deliverables" | Overly broad - could trigger incident reporting for minor content corrections | **Proposed Change:** Amend definition to: *"inaccuracies in the Deliverables **that materially affect the intended use of such Deliverables or result in regulatory non-compliance**"* |

**Rationale:** Introduces materiality threshold appropriate for content generation services where iterative review is expected.

---

### 2.5 Section 3.2 & 3.3 - Training Data Warranties

| Current Language | Area of Concern | Proposed Amendment |
|------------------|-----------------|-------------------|
| Extensive warranties about training data collection methods and quality | Creates significant liability exposure for historical training data | **Proposed Change:** Add qualifier: *"The representations and warranties in Sections 3.2 and 3.3 apply to training data used **after the Effective Date** of this Agreement. For pre-existing AI models, Counterparty represents that it has conducted reasonable due diligence on training data sources and is not aware of any material violations of the stated requirements."* |

**Rationale:** Provides reasonable scope for warranties while acknowledging practical limitations of historical documentation.

---

## 3. ADDITIONAL CLARIFICATIONS REQUESTED

### 3.1 Section 10.2 (Privacy Schedule) - Status of Counterparty

| Current Language | Issue |
|------------------|-------|
| "Counterparty will be considered a [processor, controller, or both]" | Placeholder not filled in |

**Request:** Please confirm CLIRNET's status as **Processor** for this engagement.

---

### 3.2 Subscription Services Definition (Page 19)

| Current Language | Issue |
|------------------|-------|
| "[insert description of Counterparty's technology solution and the problem it solves for customers]" | Placeholder not filled in |

**Proposed Text:** *"'Subscription Services' means the proprietary technology solution of Counterparty that provides an AI-assisted, structured content generation and management platform (MiCE - Moment Marketing Intelligent Content Engine) enabling topic discovery, content creation, compliance validation and approval workflows for medical content needs."*

---

## SUMMARY OF REQUESTED CHANGES

| Section | Nature of Change | Priority |
|---------|------------------|----------|
| Cyber 3.1 | Compliance timeline flexibility | Medium |
| Cyber 7.2 | Extend patching window to 45 days | Medium |
| Cyber 8.4 | Define "Strong Encryption" | Low |
| Cyber 8.6 | Extend breach notification to 48 hours | High |
| AI 1.1 | Pre-approve MiCE platform in SOW | High |
| AI 1.2 | Add 14-day notice period for AI revocation | High |
| AI 2.2 | Allow anonymized learnings | Medium |
| AI 5.5 | Add materiality threshold for incidents | Medium |
| AI 3.2/3.3 | Scope warranties to post-Effective Date | Medium |

---

We believe these amendments balance GSK's legitimate security and compliance requirements with operational practicality for the MiCE pilot. We remain committed to maintaining the highest standards of data protection and AI governance.

Please let us know your availability to discuss these proposed amendments at your earliest convenience.

Best Regards,

**CLIRNET Services Private Limited**

---

*This document is for discussion purposes and does not constitute a binding offer or acceptance.*
