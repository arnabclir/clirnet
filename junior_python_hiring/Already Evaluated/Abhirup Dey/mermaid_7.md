graph TD
    N0_abuse["Abuse"]
    N1_adverse_drug_reactions["Adverse Drug Reactions"]
    N2_adverse_effects["Adverse Effects"]
    N3_adverse_event["Adverse Event"]
    N4_adverse_event_reporting["Adverse Event Reporting"]
    N5_brca1["Brca1"]
    N6_brca2["Brca2"]
    N7_causal_relationship["Causal Relationship"]
    N8_clinical_trial["Clinical Trial"]
    N9_control_group["Control Group"]
    N10_dechallenge["Dechallenge"]
    N11_diabetes["Diabetes"]
    N12_drug_exposure_during_breastfeeding["Drug Exposure During Breastfeeding"]
    N13_drug_exposure_during_pregnancy["Drug Exposure During Pregnancy"]
    N14_drug_safety["Drug Safety"]
    N15_drug_safety_and_pharmacovigilance_audit["Drug Safety And Pharmacovigilance Audit"]
    N16_effectiveness["Effectiveness"]
    N17_efficacy["Efficacy"]
    N18_european_medicines_agency["European Medicines Agency"]
    N19_european_union["European Union"]
    N20_fda["Fda"]
    N21_guideline_on_good_pharmacovigilance_practices["Guideline On Good Pharmacovigilance Practices"]
    N22_harm["Harm"]
    N23_healthcare_provider_reports["Healthcare Provider Reports"]
    N24_high_blood_pressure["High Blood Pressure"]
    N25_implied_causality["Implied Causality"]
    N26_individual_case_safety_report["Individual Case Safety Report"]
    N27_life-threatening["Life-Threatening"]
    N28_medical_literature["Medical Literature"]
    N29_medication_errors["Medication Errors"]
    N30_misuse["Misuse"]
    N31_national_drug_regulatory_authority["National Drug Regulatory Authority"]
    N32_obesity["Obesity"]
    N33_overdose["Overdose"]
    N34_patient_reports["Patient Reports"]
    N35_pharmacovigilance["Pharmacovigilance"]
    N36_phase_i["Phase I"]
    N37_phase_ii["Phase Ii"]
    N38_phase_iii["Phase Iii"]
    N39_phase_iv["Phase Iv"]
    N40_rechallenge["Rechallenge"]
    N41_risk["Risk"]
    N42_risk_factor["Risk Factor"]
    N43_safety_signals["Safety Signals"]
    N44_signal["Signal"]
    N45_social_media["Social Media"]
    N46_temporal_relationship["Temporal Relationship"]
    N47_triage["Triage"]
    N48_us_food_and_drug_administration["U.S. Food And Drug Administration"]
    N49_websites["Websites"]
    N35_pharmacovigilance -- "is also known as" --> N14_drug_safety
    N35_pharmacovigilance -- "addresses" --> N2_adverse_effects
    N35_pharmacovigilance -- "addresses" --> N1_adverse_drug_reactions
    N35_pharmacovigilance -- "addresses" --> N29_medication_errors
    N29_medication_errors -- "include" --> N33_overdose
    N29_medication_errors -- "include" --> N30_misuse
    N29_medication_errors -- "include" --> N0_abuse
    N29_medication_errors -- "include" --> N13_drug_exposure_during_pregnancy
    N29_medication_errors -- "include" --> N12_drug_exposure_during_breastfeeding
    N19_european_union -- "expanded" --> N35_pharmacovigilance
    N48_us_food_and_drug_administration -- "requires inclusion of" --> N29_medication_errors
    N48_us_food_and_drug_administration -- "requires inclusion of" --> N33_overdose
    N48_us_food_and_drug_administration -- "requires inclusion of" --> N30_misuse
    N48_us_food_and_drug_administration -- "requires inclusion of" --> N0_abuse
    N48_us_food_and_drug_administration -- "requires inclusion of" --> N13_drug_exposure_during_pregnancy
    N48_us_food_and_drug_administration -- "requires inclusion of" --> N12_drug_exposure_during_breastfeeding
    N4_adverse_event_reporting -- "involves" --> N47_triage
    N4_adverse_event_reporting -- "involves" --> N26_individual_case_safety_report
    N4_adverse_event_reporting -- "is required by" --> N31_national_drug_regulatory_authority
    N4_adverse_event_reporting -- "is required by" --> N20_fda
    N35_pharmacovigilance -- "aims to identify" --> N43_safety_signals
    N35_pharmacovigilance -- "aims to implement measures to reduce" --> N41_risk
    N15_drug_safety_and_pharmacovigilance_audit -- "assesses compliance with" --> N21_guideline_on_good_pharmacovigilance_practices
    N18_european_medicines_agency -- "defines" --> N3_adverse_event
    N18_european_medicines_agency -- "defines" --> N7_causal_relationship
    N18_european_medicines_agency -- "defines" --> N44_signal
    N7_causal_relationship -- "is established by" --> N10_dechallenge
    N7_causal_relationship -- "is established by" --> N40_rechallenge
    N46_temporal_relationship -- "is necessary for" --> N7_causal_relationship
    N25_implied_causality -- "is presumed positive unless stated other" --> N26_individual_case_safety_report
    N27_life-threatening -- "is a type of" --> N3_adverse_event
    N22_harm -- "is the extent of damage caused by" --> N3_adverse_event
    N41_risk -- "is the probability of" --> N22_harm
    N42_risk_factor -- "may increase" --> N41_risk
    N32_obesity -- "is a" --> N42_risk_factor
    N24_high_blood_pressure -- "is a" --> N42_risk_factor
    N11_diabetes -- "is a" --> N42_risk_factor
    N8_clinical_trial -- "is used to determine" --> N17_efficacy
    N36_phase_i -- "is a phase of" --> N8_clinical_trial
    N37_phase_ii -- "is a phase of" --> N8_clinical_trial
    N38_phase_iii -- "is a phase of" --> N8_clinical_trial
    N39_phase_iv -- "is a phase of" --> N8_clinical_trial
    N9_control_group -- "is used in" --> N8_clinical_trial
    N34_patient_reports -- "are a source of" --> N4_adverse_event_reporting
    N23_healthcare_provider_reports -- "are a source of" --> N4_adverse_event_reporting
    N28_medical_literature -- "is a source of" --> N4_adverse_event_reporting
    N45_social_media -- "is a source of" --> N4_adverse_event_reporting
    N49_websites -- "is a source of" --> N4_adverse_event_reporting