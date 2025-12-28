graph TD
    N0_ai["Ai"]
    N1_albert_lasker_award_for_basic_medical_research["Albert Lasker Award For Basic Medical Research"]
    N2_algorithmic_bias["Algorithmic Bias"]
    N3_alphafold["Alphafold"]
    N4_alzheimers_disease["Alzheimer'S Disease"]
    N5_artificial_intelligence["Artificial Intelligence"]
    N6_automation_of_jobs["Automation Of Jobs"]
    N7_breakthrough_prize_in_life_sciences["Breakthrough Prize In Life Sciences"]
    N8_carlos_iii_university["Carlos Iii University"]
    N9_centerstone_research_institute["Centerstone Research Institute"]
    N10_chat-bot_therapy["Chat-Bot Therapy"]
    N11_chatgpt["Chatgpt"]
    N12_concept_processing["Concept Processing"]
    N13_data_privacy["Data Privacy"]
    N14_data_warehouses["Data Warehouses"]
    N15_david_baker["David Baker"]
    N16_ddiextraction_challenge["Ddiextraction Challenge"]
    N17_decision_support_systems["Decision Support Systems"]
    N18_deep_learning["Deep Learning"]
    N19_dementias["Dementias"]
    N20_demis_hassabis["Demis Hassabis"]
    N21_disease_diagnosis["Disease Diagnosis"]
    N22_drug_development["Drug Development"]
    N23_drug_discovery["Drug Discovery"]
    N24_drug-drug_interactions["Drug-Drug Interactions"]
    N25_ehrs["Ehrs"]
    N26_electronic_health_records["Electronic Health Records"]
    N27_emergency_department["Emergency Department"]
    N28_faers["Faers"]
    N29_fda_adverse_event_reporting_system["Fda Adverse Event Reporting System"]
    N30_healthcare["Healthcare"]
    N31_healthcare_data["Healthcare Data"]
    N32_heart_attack["Heart Attack"]
    N33_inference_algorithms["Inference Algorithms"]
    N34_interpretation_of_radiographs["Interpretation Of Radiographs"]
    N35_john_jumper["John Jumper"]
    N36_machine_learning["Machine Learning"]
    N37_medical_data["Medical Data"]
    N38_myocardial_infarction["Myocardial Infarction"]
    N39_natural_language_processing["Natural Language Processing"]
    N40_nlp["Nlp"]
    N41_nobel_prize_in_chemistry["Nobel Prize In Chemistry"]
    N42_patient_care["Patient Care"]
    N43_patient_monitoring["Patient Monitoring"]
    N44_personalized_medicine["Personalized Medicine"]
    N45_protein_structures["Protein Structures"]
    N46_pulse_oximeter["Pulse Oximeter"]
    N47_radiographs["Radiographs"]
    N48_radiology["Radiology"]
    N49_reddits_raskdocs["Reddit'S R/Askdocs"]
    N50_rule-based_system["Rule-Based System"]
    N51_sensors["Sensors"]
    N52_statistical_physics["Statistical Physics"]
    N53_telemedicine["Telemedicine"]
    N54_treatment_protocol_development["Treatment Protocol Development"]
    N55_triage["Triage"]
    N56_university_of_washington["University Of Washington"]
    N57_venki_ramakrishnan["Venki Ramakrishnan"]
    N58_vigibase["Vigibase"]
    N59_wearable_device["Wearable Device"]
    N60_woebot["Woebot"]
    N61_world_health_organization["World Health Organization"]
    N5_artificial_intelligence -- "is used in" --> N30_healthcare
    N5_artificial_intelligence -- "analyzes" --> N37_medical_data
    N5_artificial_intelligence -- "analyzes" --> N31_healthcare_data
    N5_artificial_intelligence -- "provides" --> N21_disease_diagnosis
    N5_artificial_intelligence -- "provides" --> N54_treatment_protocol_development
    N5_artificial_intelligence -- "provides" --> N22_drug_development
    N5_artificial_intelligence -- "provides" --> N44_personalized_medicine
    N5_artificial_intelligence -- "provides" --> N43_patient_monitoring
    N5_artificial_intelligence -- "provides" --> N42_patient_care
    N5_artificial_intelligence -- "assists with" --> N55_triage
    N5_artificial_intelligence -- "assists with" --> N34_interpretation_of_radiographs
    N47_radiographs -- "are" --> N48_radiology
    N5_artificial_intelligence -- "raises" --> N13_data_privacy
    N5_artificial_intelligence -- "raises" --> N6_automation_of_jobs
    N5_artificial_intelligence -- "raises" --> N2_algorithmic_bias
    N0_ai -- "is" --> N5_artificial_intelligence
    N0_ai -- "uses" --> N36_machine_learning
    N36_machine_learning -- "aids" --> N21_disease_diagnosis
    N36_machine_learning -- "analyzes" --> N26_electronic_health_records
    N5_artificial_intelligence -- "predicts" --> N4_alzheimers_disease
    N5_artificial_intelligence -- "predicts" --> N19_dementias
    N5_artificial_intelligence -- "supports" --> N17_decision_support_systems
    N17_decision_support_systems -- "operate in" --> N27_emergency_department
    N11_chatgpt -- "posted on" --> N49_reddits_raskdocs
    N26_electronic_health_records -- "are used in" --> N30_healthcare
    N5_artificial_intelligence -- "interprets" --> N26_electronic_health_records
    N5_artificial_intelligence -- "uses" --> N39_natural_language_processing
    N39_natural_language_processing -- "matches" --> N32_heart_attack
    N39_natural_language_processing -- "matches" --> N38_myocardial_infarction
    N12_concept_processing -- "analyzes" --> N26_electronic_health_records
    N5_artificial_intelligence -- "uses" --> N50_rule-based_system
    N3_alphafold -- "predicts" --> N45_protein_structures
    N3_alphafold -- "accelerates" --> N23_drug_discovery
    N57_venki_ramakrishnan -- "called" --> N3_alphafold
    N20_demis_hassabis -- "won" --> N7_breakthrough_prize_in_life_sciences
    N35_john_jumper -- "won" --> N7_breakthrough_prize_in_life_sciences
    N20_demis_hassabis -- "won" --> N1_albert_lasker_award_for_basic_medical_research
    N35_john_jumper -- "won" --> N1_albert_lasker_award_for_basic_medical_research
    N20_demis_hassabis -- "won" --> N41_nobel_prize_in_chemistry
    N35_john_jumper -- "won" --> N41_nobel_prize_in_chemistry
    N15_david_baker -- "won" --> N41_nobel_prize_in_chemistry
    N15_david_baker -- "affiliated with" --> N56_university_of_washington
    N39_natural_language_processing -- "identifies" --> N24_drug-drug_interactions
    N16_ddiextraction_challenge -- "organized by" --> N8_carlos_iii_university
    N18_deep_learning -- "detects" --> N24_drug-drug_interactions
    N61_world_health_organization -- "manages" --> N58_vigibase
    N5_artificial_intelligence -- "assists in" --> N53_telemedicine
    N5_artificial_intelligence -- "monitors" --> N51_sensors
    N5_artificial_intelligence -- "provides" --> N10_chat-bot_therapy
    N10_chat-bot_therapy -- "includes" --> N60_woebot