# Additional Strategic Considerations for GSK MSA
## Beyond Cyber Security & AI Sections

**Document:** Master Services Agreement - GSK & CLIRNET
**Prepared for:** Internal Review Before Finalization
**Date:** December 3, 2025

---

## EXECUTIVE SUMMARY

While the Cyber Security Schedule and AI sections contain critical compliance requirements, several other aspects of this MSA warrant careful consideration before signing. This document identifies additional risk areas, strategic concerns, and operational implications that could significantly impact CLIRNET's position in this engagement and future business.

---

## 1. LIABILITY AND INDEMNIFICATION CONCERNS

### 1.1 Liability Cap Analysis
**FLAG: CRITICAL - REVIEW ACTUAL NUMBERS**

| Consideration | Risk Assessment |
|---------------|-----------------|
| What is the liability cap relative to contract value? | Pilot value is INR 6,52,500 (~$7,800 USD). Is liability capped at contract value or a multiple? |
| Are there carve-outs from the liability cap? | Security breaches, IP infringement, and data protection violations typically have UNLIMITED liability |
| Does indemnification fall within or outside the cap? | Indemnification obligations often bypass liability caps entirely |

**Recommendation:** Ensure liability cap is reasonable (typically 1-2x annual contract value) and understand all carve-outs explicitly.

### 1.2 Indemnification Scope
**FLAG: HIGH RISK**

Standard pharma MSAs require vendors to indemnify against:
- Third-party IP claims
- Data breaches
- Regulatory violations
- Personal injury claims
- Violation of laws

**Key Questions:**
1. Is indemnification mutual or one-sided?
2. Does GSK control the defense of claims?
3. What are the notice and cooperation requirements?
4. Are there monetary thresholds before indemnification kicks in?

**Recommendation:** Push for mutual indemnification and ensure CLIRNET has the right to participate in defense of claims.

---

## 2. INTELLECTUAL PROPERTY BEYOND AI

### 2.1 Pre-Existing IP Protection
**FLAG: CRITICAL FOR MiCE PLATFORM**

| Issue | Concern |
|-------|---------|
| Background IP Definition | Is MiCE platform architecture, algorithms, and codebase clearly defined as CLIRNET's pre-existing IP? |
| License Grant Scope | What license is CLIRNET granting to GSK for using MiCE? Is it limited to the pilot? |
| Derivative Works | If MiCE is enhanced during this engagement, who owns those enhancements? |

**Recommendation:** Add explicit clause: *"All intellectual property in the MiCE platform, including its architecture, algorithms, user interface designs, and underlying codebase, constitutes Counterparty's Background IP and remains the sole property of Counterparty."*

### 2.2 Work Product vs. Platform
**FLAG: IMPORTANT DISTINCTION**

- **Content generated** (the 20 deliverables) → GSK owns this (acceptable)
- **Platform improvements** → Should remain CLIRNET's property
- **Workflows/templates created** → Clarify ownership

**Risk:** Broad "work product" language could inadvertently transfer MiCE improvements to GSK.

---

## 3. COMMERCIAL AND FINANCIAL TERMS

### 3.1 Payment Terms
**FLAG: CASH FLOW IMPACT**

| Standard Issue | Question |
|----------------|----------|
| Payment timeline | Net 30? Net 60? Net 90? Pharma companies often have 60-90 day payment terms |
| Milestone vs. time-based | Is payment tied to deliverable acceptance or calendar milestones? |
| Acceptance criteria | What constitutes "acceptance" of deliverables? Who decides? |
| Right to reject | Can GSK reject deliverables indefinitely, delaying payment? |

**Recommendation:** Ensure clear acceptance criteria with defined review period (e.g., 10 business days) and deemed acceptance if no response.

### 3.2 Pilot to Production Economics
**FLAG: STRATEGIC**

| Consideration | Why It Matters |
|---------------|----------------|
| Pricing lock for production phase | Is the pilot pricing indicative of production pricing, or can it be renegotiated? |
| Volume commitments | Any minimum commitments if pilot succeeds? |
| Exclusivity | Is CLIRNET prohibited from offering MiCE to GSK competitors during/after pilot? |
| Right of first refusal | Does GSK have ROFR for future content needs? |

**Recommendation:** If not addressed, add language: *"Pricing for any production phase following successful pilot completion shall be negotiated in good faith based on scope and volume requirements."*

### 3.3 Scope Creep Protection
**FLAG: OPERATIONAL**

- Is there a formal change order process?
- What happens if GSK requests additional deliverables beyond the 20 specified?
- Who bears cost of revisions beyond a reasonable number?

**Recommendation:** Define revision limits (e.g., "up to 2 rounds of revisions per deliverable included; additional revisions at [rate]")

---

## 4. TERM, TERMINATION, AND EXIT

### 4.1 Termination Rights Asymmetry
**FLAG: HIGH RISK**

| Party | Likely Rights |
|-------|---------------|
| GSK | Terminate for convenience with 30 days notice |
| CLIRNET | Terminate only for GSK material breach with cure period |

**Key Concerns:**
1. Can GSK terminate mid-pilot without paying for work in progress?
2. What notice period does CLIRNET get?
3. Does termination trigger immediate data return/deletion obligations?

**Recommendation:** Ensure: *"Upon termination for convenience by GSK, CLIRNET shall be entitled to payment for (a) all Services properly performed through the termination date, and (b) reasonable wind-down costs incurred."*

### 4.2 Transition Assistance
**FLAG: RESOURCE COMMITMENT**

Standard MSAs require vendor to provide transition assistance for 90-180 days post-termination. This can be:
- At additional cost or included
- Mandatory or optional
- With knowledge transfer requirements

**Risk:** Extended transition obligations can tie up CLIRNET resources without compensation.

### 4.3 Data Return and Deletion
**FLAG: COMPLIANCE BURDEN**

- Timeline for returning/deleting GSK data post-termination
- Certification requirements
- Exception for legally required retention
- Backup and archive deletion (often overlooked)

---

## 5. SERVICE LEVELS AND PERFORMANCE

### 5.1 SLA Definitions
**FLAG: PILOT CONTEXT**

| Question | Implication |
|----------|-------------|
| Are there defined SLAs for the pilot? | Content turnaround time, revision response time, etc. |
| What are the penalties for SLA breaches? | Service credits? Termination rights? |
| How are SLAs measured? | Who tracks and reports? |

**Recommendation for Pilot:** Suggest: *"Given the pilot nature of this engagement, SLAs shall be monitored and reported but service credits shall not apply during the pilot period. Parties will use pilot performance data to establish production SLAs."*

### 5.2 Deliverable Acceptance Process
**FLAG: OPERATIONAL CLARITY**

- Who at GSK approves deliverables?
- What is the approval timeline?
- Escalation path for disputes?
- Impact of GSK delays on overall timeline?

---

## 6. DATA PROTECTION AND PRIVACY

### 6.1 Processor Status Confirmation
**FLAG: ALREADY IDENTIFIED**

The document contains placeholder: *"Counterparty will be considered a [processor, controller, or both]"*

**Recommendation:** Confirm CLIRNET as **Processor only** - this limits liability exposure.

### 6.2 Cross-Border Data Transfer
**FLAG: OPERATIONAL**

| Consideration | Question |
|---------------|----------|
| Data location | Where can GSK data be processed? India only? |
| SCCs requirement | Are Standard Contractual Clauses required for any data leaving the EEA? |
| Subprocessor location | Can CLIRNET use cloud services in other jurisdictions? |

**Risk:** Overly restrictive data localization could increase infrastructure costs.

### 6.3 Data Retention Limits
**FLAG: COMPLIANCE**

- How long can CLIRNET retain GSK data?
- Is there a defined retention schedule?
- What about aggregated/anonymized data?

---

## 7. PHARMA INDUSTRY-SPECIFIC CONSIDERATIONS

### 7.1 Regulatory Compliance Obligations
**FLAG: INDUSTRY CONTEXT**

GSK operates in a heavily regulated environment. The MSA likely includes:
- FDA/EMA compliance for promotional materials
- Adverse event reporting obligations
- Product complaint handling
- GxP (Good Practice) requirements

**Question:** Does CLIRNET have any obligation to report adverse events or product complaints encountered in content?

**Recommendation:** Add clarity: *"Counterparty's obligations are limited to content creation services. Counterparty has no obligation to monitor for or report adverse events, though Counterparty will promptly notify GSK if such information is inadvertently received during content review."*

### 7.2 Anti-Bribery and Corruption
**FLAG: STANDARD BUT IMPORTANT**

- FCPA (US) and UK Bribery Act compliance
- Prohibition on facilitation payments
- Healthcare provider interaction restrictions
- Third-party due diligence requirements

**Risk:** Violations can result in termination and potential legal exposure for CLIRNET.

### 7.3 Transparency and Sunshine Act
**FLAG: POTENTIAL APPLICABILITY**

If any payments flow to healthcare professionals through this engagement:
- Disclosure and reporting requirements
- Transfer of value tracking
- Aggregate spend reporting

**Clarification Needed:** Confirm no HCP payments are in scope for MiCE pilot.

---

## 8. INSURANCE REQUIREMENTS

### 8.1 Coverage Mandates
**FLAG: COST IMPLICATION**

Standard pharma MSAs require:

| Insurance Type | Typical Minimum |
|----------------|-----------------|
| Commercial General Liability | $1-5 million |
| Professional Liability/E&O | $1-5 million |
| Cyber Liability | $1-5 million |
| Workers' Compensation | Statutory |

**Action Required:** Verify CLIRNET's current coverage meets MSA requirements. If additional coverage is needed, factor cost into engagement economics.

### 8.2 Additional Insured Status
**FLAG: STANDARD REQUEST**

GSK will likely require:
- Named as additional insured
- Certificate of insurance provided
- Notice of policy cancellation

---

## 9. CONFIDENTIALITY CONSIDERATIONS

### 9.1 Survival Period
**FLAG: LONG-TERM OBLIGATION**

- How long do confidentiality obligations survive?
- 3 years? 5 years? Indefinite for trade secrets?
- Does this align with CLIRNET's data retention practices?

### 9.2 Residuals Clause
**FLAG: PRACTICAL PROTECTION**

**Recommendation:** Seek inclusion of residuals clause: *"Nothing in this Agreement shall restrict either party's use of general knowledge, skills, and experience, including ideas, concepts, know-how, or techniques that are retained in the unaided memories of personnel who have had access to the other party's Confidential Information."*

This protects CLIRNET employees from being "contaminated" by exposure to GSK information.

### 9.3 Publicity and References
**FLAG: MARKETING VALUE**

- Can CLIRNET mention GSK as a client?
- Can CLIRNET publish case studies?
- Can GSK be used as a reference?

**Recommendation:** Negotiate: *"Counterparty may identify GSK as a client in general marketing materials, provided no Confidential Information is disclosed."*

---

## 10. FORCE MAJEURE AND BUSINESS CONTINUITY

### 10.1 Force Majeure Scope
**FLAG: POST-PANDEMIC RELEVANCE**

- Is pandemic explicitly included or excluded?
- What are notification requirements?
- At what point does extended force majeure trigger termination rights?

### 10.2 Business Continuity Requirements
**FLAG: OPERATIONAL**

- Is CLIRNET required to maintain a BCP?
- Recovery time objectives (RTO)?
- Backup and redundancy requirements?

---

## 11. DISPUTE RESOLUTION

### 11.1 Governing Law and Jurisdiction
**FLAG: STRATEGIC**

| Option | Implication for CLIRNET |
|--------|-------------------------|
| India law, India courts | Most favorable - home jurisdiction |
| UK/US law | GSK's preferred jurisdiction - higher litigation costs |
| Singapore/Hong Kong | Common neutral choice for APAC contracts |

**Recommendation:** Push for Indian law and Mumbai/Delhi jurisdiction, or at minimum, neutral venue arbitration.

### 11.2 Arbitration vs. Litigation
**FLAG: COST-BENEFIT**

- Arbitration typically faster but expensive upfront
- Consider: ICC, SIAC, or Indian arbitration bodies
- Ensure expedited procedure available for urgent matters

### 11.3 Escalation Before Legal Action
**FLAG: PRACTICAL**

Ensure tiered dispute resolution:
1. Project manager discussion (5 business days)
2. Senior executive escalation (10 business days)
3. Mediation (optional)
4. Arbitration/litigation

---

## 12. PILOT-SPECIFIC STRATEGIC CONSIDERATIONS

### 12.1 Success Criteria Definition
**FLAG: CRITICAL FOR FUTURE BUSINESS**

| Question | Why It Matters |
|----------|----------------|
| How is pilot "success" defined? | Determines likelihood of production phase |
| Who evaluates success? | Subjective vs. objective criteria |
| What metrics will be tracked? | Content quality? Turnaround time? Cost per asset? |

**Recommendation:** Propose mutual success criteria: *"The pilot shall be deemed successful if: (a) at least [X] of 20 deliverables are approved by GSK without substantive revision, (b) average delivery time meets agreed timeline, and (c) no material security or AI incidents occur."*

### 12.2 Competitive Intelligence Protection
**FLAG: STRATEGIC**

- GSK will learn CLIRNET's AI capabilities, pricing, and processes
- This information could be shared with competitors or used to develop in-house capability
- Consider whether any reverse confidentiality protections are needed

### 12.3 Pilot Extension or Early Termination
**FLAG: FLEXIBILITY**

- What happens if pilot needs more time?
- Can it be extended? On what terms?
- What if GSK wants to accelerate to production?

### 12.4 Reference Rights and Case Study
**FLAG: MARKETING VALUE**

A successful GSK pilot is significant for CLIRNET's market positioning. Ensure:
- Right to use GSK logo with permission
- Ability to describe the engagement in general terms
- Potential for joint case study or press release

---

## 13. SUBCONTRACTOR AND PERSONNEL

### 13.1 Key Personnel Clauses
**FLAG: OPERATIONAL CONSTRAINT**

- Are specific individuals required to be assigned?
- What notice/approval is needed to change personnel?
- Does this constrain CLIRNET's operational flexibility?

### 13.2 Subcontractor Approval
**FLAG: ALREADY IDENTIFIED IN CYBER SECTION**

Remember: CLIRNET is fully liable for all subcontractors, including cloud providers.

**Action:** Ensure all cloud/SaaS providers used by MiCE are pre-approved or fall within acceptable categories.

### 13.3 Non-Solicitation
**FLAG: TALENT PROTECTION**

- Does the MSA prevent GSK from hiring CLIRNET employees?
- Is this mutual?
- Duration and scope?

---

## 14. AUDIT AND COMPLIANCE VERIFICATION

### 14.1 Audit Frequency and Scope
**FLAG: OPERATIONAL BURDEN**

Beyond security audits (already covered), consider:
- Financial audits (especially for T&M billing)
- Process audits
- Quality audits
- Frequency limitations

**Recommendation:** Limit to once per year (except for cause) with reasonable notice.

### 14.2 Audit Cost Allocation
**FLAG: FINANCIAL**

- Who bears the cost of audits?
- CLIRNET cooperation costs vs. actual audit costs
- What if audit finds issues?

---

## 15. REPRESENTATIONS AND WARRANTIES

### 15.1 Authority and Capacity
**FLAG: STANDARD**

Verify CLIRNET can make all required representations about:
- Corporate authority to enter agreement
- No conflicting obligations
- Compliance with laws
- Ownership of necessary rights

### 15.2 Warranty of Services
**FLAG: QUALITY STANDARD**

- "Professional and workmanlike manner" is typical
- Ensure warranty doesn't guarantee specific outcomes
- Define remedy for breach (re-performance, not unlimited liability)

---

## SUMMARY: PRIORITY ACTION ITEMS

### Before Signing

| Priority | Item | Section |
|----------|------|---------|
| CRITICAL | Verify liability cap and carve-outs | 1.1, 1.2 |
| CRITICAL | Confirm MiCE Background IP protection | 2.1 |
| CRITICAL | Understand termination payment obligations | 4.1 |
| HIGH | Review insurance requirements against current coverage | 8.1 |
| HIGH | Confirm payment terms and acceptance process | 3.1 |
| HIGH | Verify governing law and dispute resolution | 11.1, 11.2 |
| MEDIUM | Define pilot success criteria | 12.1 |
| MEDIUM | Negotiate reference and publicity rights | 9.3 |
| MEDIUM | Review subcontractor approval process | 13.2 |
| LOW | Add residuals clause | 9.2 |

### Questions to Ask GSK

1. What is the liability cap and what are the carve-outs?
2. Can we add explicit Background IP protection for MiCE platform?
3. What are the payment terms (Net 30/60/90)?
4. What insurance certificates do you need and by when?
5. Can we discuss reference/case study rights for a successful pilot?
6. What is the formal change order process for scope additions?
7. Is there flexibility on governing law (Indian law) or dispute resolution (arbitration in Singapore)?

---

## APPENDIX: CHECKLIST FOR INTERNAL READINESS

Before committing to the MSA, CLIRNET should verify:

| Area | Ready? | Notes |
|------|--------|-------|
| ISO 27001 or equivalent certification | ☐ | Or 90-day roadmap |
| Cyber insurance at required levels | ☐ | |
| Professional liability insurance | ☐ | |
| 24/7 incident response capability | ☐ | For 24-hour breach notification |
| AI training data documentation | ☐ | For Section 3.2/3.3 warranties |
| Bias testing procedures documented | ☐ | For Section 5.4 compliance |
| 30-day (or negotiated 45-day) patching capability | ☐ | |
| Subcontractor security agreements | ☐ | Cloud providers, etc. |
| Data classification and handling procedures | ☐ | |
| Written approval from GSK for MiCE AI usage | ☐ | Critical before pilot starts |

---

*This document is for internal strategic review. Consult legal counsel before finalizing MSA negotiations.*
