graph TD
    N0_000["000"]
    N1_13_11_26["13 11 26"]
    N2_1300_134_237["1300 134 237"]
    N3_adverse_events["Adverse Events"]
    N4_adverse_medicines_events_line["Adverse Medicines Events Line"]
    N5_adverse_reactions["Adverse Reactions"]
    N6_ame_line["Ame Line"]
    N7_anti-inflammatory_medicines["Anti-Inflammatory Medicines"]
    N8_antibiotics["Antibiotics"]
    N9_approval_and_regulation_processes["Approval And Regulation Processes"]
    N10_australia["Australia"]
    N11_cmi["Cmi"]
    N12_complementary_medicines["Complementary Medicines"]
    N13_consumer_medicine_information["Consumer Medicine Information"]
    N14_daen["Daen"]
    N15_database_of_adverse_event_notifications["Database Of Adverse Event Notifications"]
    N16_doxycycline["Doxycycline"]
    N17_drug_interactions["Drug Interactions"]
    N18_health_professional["Health Professional"]
    N19_herbal_medicines["Herbal Medicines"]
    N20_medicine["Medicine"]
    N21_medicine_management["Medicine Management"]
    N22_medicinewise_app["Medicinewise App"]
    N23_minerals["Minerals"]
    N24_natural_medicines["Natural Medicines"]
    N25_nausea["Nausea"]
    N26_over-the-counter_medicines["Over-The-Counter Medicines"]
    N27_pi["Pi"]
    N28_poisons_information_centre["Poisons Information Centre"]
    N29_prescription_medicines["Prescription Medicines"]
    N30_product_information["Product Information"]
    N31_side_effects["Side Effects"]
    N32_tga["Tga"]
    N33_therapeutic_goods_administration["Therapeutic Goods Administration"]
    N34_vitamins["Vitamins"]
    N31_side_effects -- "are also called" --> N5_adverse_reactions
    N31_side_effects -- "are also called" --> N3_adverse_events
    N20_medicine -- "has" --> N31_side_effects
    N20_medicine -- "has" --> N5_adverse_reactions
    N20_medicine -- "has" --> N3_adverse_events
    N20_medicine -- "can interact with" --> N17_drug_interactions
    N21_medicine_management -- "may reduce" --> N31_side_effects
    N16_doxycycline -- "is an example of" --> N8_antibiotics
    N25_nausea -- "is a side effect of" --> N20_medicine
    N31_side_effects -- "are described in" --> N13_consumer_medicine_information
    N31_side_effects -- "are described in" --> N11_cmi
    N31_side_effects -- "are described in" --> N30_product_information
    N31_side_effects -- "are described in" --> N27_pi
    N13_consumer_medicine_information -- "is required for" --> N29_prescription_medicines
    N11_cmi -- "is required for" --> N29_prescription_medicines
    N11_cmi -- "can be downloaded from" --> N22_medicinewise_app
    N11_cmi -- "can be obtained from" --> N18_health_professional
    N18_health_professional -- "can explain" --> N31_side_effects
    N18_health_professional -- "can report" --> N3_adverse_events
    N18_health_professional -- "can update" --> N21_medicine_management
    N3_adverse_events -- "are reported to" --> N33_therapeutic_goods_administration
    N3_adverse_events -- "are reported to" --> N32_tga
    N31_side_effects -- "can be reported to" --> N4_adverse_medicines_events_line
    N31_side_effects -- "can be reported to" --> N6_ame_line
    N4_adverse_medicines_events_line -- "has phone number" --> N2_1300_134_237
    N6_ame_line -- "has phone number" --> N2_1300_134_237
    N31_side_effects -- "can be reported to" --> N33_therapeutic_goods_administration
    N31_side_effects -- "can be reported to" --> N32_tga
    N32_tga -- "maintains" --> N15_database_of_adverse_event_notifications
    N32_tga -- "maintains" --> N14_daen
    N14_daen -- "includes reports about" --> N29_prescription_medicines
    N14_daen -- "includes reports about" --> N26_over-the-counter_medicines
    N14_daen -- "includes reports about" --> N12_complementary_medicines
    N12_complementary_medicines -- "include" --> N34_vitamins
    N12_complementary_medicines -- "include" --> N23_minerals
    N12_complementary_medicines -- "include" --> N19_herbal_medicines
    N12_complementary_medicines -- "include" --> N24_natural_medicines
    N28_poisons_information_centre -- "can be contacted at" --> N1_13_11_26
    N20_medicine -- "is regulated by" --> N9_approval_and_regulation_processes
    N9_approval_and_regulation_processes -- "apply in" --> N10_australia