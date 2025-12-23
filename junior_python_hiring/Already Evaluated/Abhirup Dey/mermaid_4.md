graph TD
    N0_gov[".Gov"]
    N1_ahfs_consumer_medication_information["Ahfs® Consumer Medication Information"]
    N2_american_society_of_health-system_pharmacists["American Society Of Health-System Pharmacists"]
    N3_antibiotics["Antibiotics"]
    N4_antidepressants["Antidepressants"]
    N5_ashp["Ashp"]
    N6_blood_pressure_medicines["Blood Pressure Medicines"]
    N7_blood_thinners["Blood Thinners"]
    N8_cancer_alternative_therapies["Cancer Alternative Therapies"]
    N9_cancer_chemotherapy["Cancer Chemotherapy"]
    N10_cold_and_cough_medicines["Cold And Cough Medicines"]
    N11_complementary_and_alternative_medicine["Complementary And Alternative Medicine"]
    N12_dailymed["Dailymed"]
    N13_diabetes_medicines["Diabetes Medicines"]
    N14_dietary_supplements["Dietary Supplements"]
    N15_drug_safety["Drug Safety"]
    N16_drugs["Drugs"]
    N17_fda["Fda"]
    N18_herbal_medicine["Herbal Medicine"]
    N19_herbs["Herbs"]
    N20_hivaids_medicines["Hiv/Aids Medicines"]
    N21_hormone_replacement_therapy["Hormone Replacement Therapy"]
    N22_https["Https"]
    N23_medicines["Medicines"]
    N24_medlineplus["Medlineplus"]
    N25_over-the-counter_medicines["Over-The-Counter Medicines"]
    N26_pain_relievers["Pain Relievers"]
    N27_prescription_medication["Prescription Medication"]
    N28_statins["Statins"]
    N29_steroids["Steroids"]
    N30_supplements["Supplements"]
    N31_vitamins["Vitamins"]
    N24_medlineplus -- "provides information on" --> N16_drugs
    N24_medlineplus -- "provides information on" --> N19_herbs
    N24_medlineplus -- "provides information on" --> N30_supplements
    N24_medlineplus -- "is hosted on" --> N0_gov
    N0_gov -- "uses" --> N22_https
    N22_https -- "ensures secure connection to" --> N0_gov
    N17_fda -- "approves labels included in" --> N12_dailymed
    N12_dailymed -- "contains labels for" --> N16_drugs
    N16_drugs -- "includes" --> N27_prescription_medication
    N16_drugs -- "includes" --> N25_over-the-counter_medicines
    N16_drugs -- "has side effects" --> N15_drug_safety
    N19_herbs -- "includes" --> N18_herbal_medicine
    N30_supplements -- "includes" --> N14_dietary_supplements
    N30_supplements -- "includes" --> N31_vitamins
    N27_prescription_medication -- "is source from" --> N1_ahfs_consumer_medication_information
    N25_over-the-counter_medicines -- "is source from" --> N1_ahfs_consumer_medication_information
    N1_ahfs_consumer_medication_information -- "is copyrighted by" --> N2_american_society_of_health-system_pharmacists
    N2_american_society_of_health-system_pharmacists -- "is abbreviated as" --> N5_ashp
    N16_drugs -- "includes" --> N20_hivaids_medicines
    N16_drugs -- "includes" --> N3_antibiotics
    N16_drugs -- "includes" --> N4_antidepressants
    N16_drugs -- "includes" --> N6_blood_pressure_medicines
    N16_drugs -- "includes" --> N7_blood_thinners
    N16_drugs -- "includes" --> N9_cancer_chemotherapy
    N16_drugs -- "includes" --> N10_cold_and_cough_medicines
    N16_drugs -- "includes" --> N13_diabetes_medicines
    N16_drugs -- "includes" --> N26_pain_relievers
    N16_drugs -- "includes" --> N28_statins
    N16_drugs -- "includes" --> N29_steroids
    N19_herbs -- "includes" --> N11_complementary_and_alternative_medicine
    N30_supplements -- "includes" --> N11_complementary_and_alternative_medicine
    N16_drugs -- "includes" --> N21_hormone_replacement_therapy