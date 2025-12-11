graph TD
    N0_2002_food_crisis_in_southern_africa["2002 Food Crisis In Southern Africa"]
    N1_active_and_healthy_life["Active And Healthy Life"]
    N2_amartya_sen["Amartya Sen"]
    N3_basic_foodstuffs["Basic Foodstuffs"]
    N4_cereals["Cereals"]
    N5_chronic_food_insecurity["Chronic Food Insecurity"]
    N6_consumer_expenditure_data["Consumer Expenditure Data"]
    N7_consumer_expenditure_surveys["Consumer Expenditure Surveys"]
    N8_cross-sectional_comparisons["Cross-Sectional Comparisons"]
    N9_dietary_energy_requirements["Dietary Energy Requirements"]
    N10_dietary_needs["Dietary Needs"]
    N11_economic_access["Economic Access"]
    N12_entitlements["Entitlements"]
    N13_famine["Famine"]
    N14_fao["Fao"]
    N15_food_balance_sheets["Food Balance Sheets"]
    N16_food_crisis["Food Crisis"]
    N17_food_preferences["Food Preferences"]
    N18_food_safety["Food Safety"]
    N19_food_security["Food Security"]
    N20_green_revolution["Green Revolution"]
    N21_household_food_security["Household Food Security"]
    N22_human_rights["Human Rights"]
    N23_human_security["Human Security"]
    N24_hunger["Hunger"]
    N25_income_distribution["Income Distribution"]
    N26_malnutrition["Malnutrition"]
    N27_nutritional_balance["Nutritional Balance"]
    N28_nutritional_status["Nutritional Status"]
    N29_physical_access["Physical Access"]
    N30_poverty["Poverty"]
    N31_poverty_lines["Poverty Lines"]
    N32_protein-energy_malnutrition["Protein-Energy Malnutrition"]
    N33_social_access["Social Access"]
    N34_social_security["Social Security"]
    N35_sofi_2001["Sofi 2001"]
    N36_sub-nutrition["Sub-Nutrition"]
    N37_time_series_comparisons["Time Series Comparisons"]
    N38_trade_liberalization["Trade Liberalization"]
    N39_transitory_food_insecurity["Transitory Food Insecurity"]
    N40_undp["Undp"]
    N41_vulnerability["Vulnerability"]
    N42_wider["Wider"]
    N43_world_bank["World Bank"]
    N44_world_food_conference_of_1974["World Food Conference Of 1974"]
    N45_world_food_summit_wfs["World Food Summit (Wfs)"]
    N5_chronic_food_insecurity -- "is associated with" --> N30_poverty
    N43_world_bank -- "introduced distinction between" --> N5_chronic_food_insecurity
    N43_world_bank -- "introduced distinction between" --> N39_transitory_food_insecurity
    N19_food_security -- "in 1996 definition includes" --> N18_food_safety
    N19_food_security -- "in 1996 definition includes" --> N27_nutritional_balance
    N19_food_security -- "in 1996 definition includes" --> N17_food_preferences
    N19_food_security -- "in 1996 definition includes" --> N10_dietary_needs
    N35_sofi_2001 -- "refined food security to include" --> N33_social_access
    N19_food_security -- "in SOFI 2001 includes" --> N33_social_access
    N2_amartya_sen -- "focused on" --> N12_entitlements
    N12_entitlements -- "are related to" --> N19_food_security
    N19_food_security -- "is influenced by" --> N22_human_rights
    N40_undp -- "promoted" --> N23_human_security
    N23_human_security -- "includes" --> N19_food_security
    N42_wider -- "focused on" --> N34_social_security
    N19_food_security -- "relates to" --> N28_nutritional_status
    N28_nutritional_status -- "is the focus of" --> N21_household_food_security
    N21_household_food_security -- "is the application of" --> N19_food_security
    N36_sub-nutrition -- "results from insufficient" --> N9_dietary_energy_requirements
    N36_sub-nutrition -- "is measured using" --> N15_food_balance_sheets
    N36_sub-nutrition -- "is measured using" --> N6_consumer_expenditure_data
    N5_chronic_food_insecurity -- "is measured using" --> N7_consumer_expenditure_surveys
    N43_world_bank -- "calculates" --> N31_poverty_lines
    N3_basic_foodstuffs -- "include" --> N4_cereals
    N8_cross-sectional_comparisons -- "are used in" --> N35_sofi_2001
    N37_time_series_comparisons -- "are used in" --> N35_sofi_2001
    N20_green_revolution -- "did not automatically reduce" --> N30_poverty
    N20_green_revolution -- "did not automatically reduce" --> N26_malnutrition
    N41_vulnerability -- "describes risk to" --> N28_nutritional_status
    N41_vulnerability -- "occurs as" --> N5_chronic_food_insecurity
    N41_vulnerability -- "occurs as" --> N39_transitory_food_insecurity
    N0_2002_food_crisis_in_southern_africa -- "highlights issues in" --> N19_food_security
    N38_trade_liberalization -- "has implications for" --> N39_transitory_food_insecurity