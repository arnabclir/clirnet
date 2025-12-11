graph TD
    N0_2015_paris_agreement["2015 Paris Agreement"]
    N1_agricultural_practices["Agricultural Practices"]
    N2_arctic["Arctic"]
    N3_atlantic_multidecadal_oscillation["Atlantic Multidecadal Oscillation"]
    N4_atmospheric_humidity["Atmospheric Humidity"]
    N5_carbon_dioxide["Carbon Dioxide"]
    N6_carbon_farming["Carbon Farming"]
    N7_carbon_removal["Carbon Removal"]
    N8_climate_change["Climate Change"]
    N9_climate_crisis["Climate Crisis"]
    N10_climate_emergency["Climate Emergency"]
    N11_climate_proxies["Climate Proxies"]
    N12_deforestation["Deforestation"]
    N13_disease["Disease"]
    N14_droughts["Droughts"]
    N15_earth["Earth"]
    N16_economic_loss["Economic Loss"]
    N17_evaporation["Evaporation"]
    N18_flooding["Flooding"]
    N19_food_scarcity["Food Scarcity"]
    N20_forest_cover["Forest Cover"]
    N21_fossil_fuel_burning["Fossil Fuel Burning"]
    N22_glaciers_retreat["Glaciers Retreat"]
    N23_global_dimming["Global Dimming"]
    N24_global_heating["Global Heating"]
    N25_global_surface_temperature["Global Surface Temperature"]
    N26_global_warming["Global Warming"]
    N27_global_warming_hiatus["Global Warming Hiatus"]
    N28_greenhouse_gases["Greenhouse Gases"]
    N29_greenland_ice_sheet["Greenland Ice Sheet"]
    N30_heat_waves["Heat Waves"]
    N31_human_activity["Human Activity"]
    N32_human_migration["Human Migration"]
    N33_hydro_power["Hydro Power"]
    N34_ice_cores["Ice Cores"]
    N35_industrial_practices["Industrial Practices"]
    N36_industrial_revolution["Industrial Revolution"]
    N37_intense_storms["Intense Storms"]
    N38_james_hansen["James Hansen"]
    N39_last_interglacial["Last Interglacial"]
    N40_little_ice_age["Little Ice Age"]
    N41_medieval_warm_period["Medieval Warm Period"]
    N42_nasa["Nasa"]
    N43_nuclear_power["Nuclear Power"]
    N44_ocean_acidification["Ocean Acidification"]
    N45_ocean_heat_content["Ocean Heat Content"]
    N46_ocean_heating["Ocean Heating"]
    N47_pacific_decadal_oscillation["Pacific Decadal Oscillation"]
    N48_paleoclimatology["Paleoclimatology"]
    N49_paris_agreement["Paris Agreement"]
    N50_permafrost_thawing["Permafrost Thawing"]
    N51_precipitation["Precipitation"]
    N52_sea_ice_decline["Sea Ice Decline"]
    N53_sea_level_rise["Sea Level Rise"]
    N54_snow_cover_reduction["Snow Cover Reduction"]
    N55_solar_power["Solar Power"]
    N56_species_extinction["Species Extinction"]
    N57_sulfate_aerosols["Sulfate Aerosols"]
    N58_sulfur_dioxide["Sulfur Dioxide"]
    N59_temperature_record_of_the_last_2000_years["Temperature Record Of The Last 2,000 Years"]
    N60_thermometer_records["Thermometer Records"]
    N61_tree_rings["Tree Rings"]
    N62_upper_atmosphere_cooling["Upper Atmosphere Cooling"]
    N63_water_scarcity["Water Scarcity"]
    N64_weather_extremes["Weather Extremes"]
    N65_wildfires["Wildfires"]
    N66_wind_power["Wind Power"]
    N67_world_health_organization["World Health Organization"]
    N31_human_activity -- "drives" --> N8_climate_change
    N21_fossil_fuel_burning -- "causes" --> N8_climate_change
    N36_industrial_revolution -- "marks beginning of" --> N21_fossil_fuel_burning
    N21_fossil_fuel_burning -- "releases" --> N28_greenhouse_gases
    N12_deforestation -- "releases" --> N28_greenhouse_gases
    N1_agricultural_practices -- "release" --> N28_greenhouse_gases
    N35_industrial_practices -- "release" --> N28_greenhouse_gases
    N28_greenhouse_gases -- "trap heat in" --> N15_earth
    N28_greenhouse_gases -- "cause" --> N26_global_warming
    N5_carbon_dioxide -- "is primary driver of" --> N26_global_warming
    N8_climate_change -- "includes" --> N26_global_warming
    N8_climate_change -- "includes" --> N46_ocean_heating
    N8_climate_change -- "includes" --> N44_ocean_acidification
    N8_climate_change -- "includes" --> N53_sea_level_rise
    N8_climate_change -- "causes" --> N30_heat_waves
    N8_climate_change -- "causes" --> N65_wildfires
    N8_climate_change -- "causes" --> N14_droughts
    N8_climate_change -- "causes" --> N37_intense_storms
    N8_climate_change -- "causes" --> N64_weather_extremes
    N8_climate_change -- "causes" --> N50_permafrost_thawing
    N8_climate_change -- "causes" --> N22_glaciers_retreat
    N8_climate_change -- "causes" --> N52_sea_ice_decline
    N8_climate_change -- "causes" --> N56_species_extinction
    N8_climate_change -- "causes" --> N18_flooding
    N8_climate_change -- "causes" --> N19_food_scarcity
    N8_climate_change -- "causes" --> N63_water_scarcity
    N8_climate_change -- "causes" --> N13_disease
    N8_climate_change -- "causes" --> N16_economic_loss
    N8_climate_change -- "causes" --> N32_human_migration
    N67_world_health_organization -- "calls" --> N8_climate_change
    N0_2015_paris_agreement -- "aims to limit" --> N26_global_warming
    N0_2015_paris_agreement -- "sets target of well under 2 °C" --> N26_global_warming
    N43_nuclear_power -- "replaces" --> N21_fossil_fuel_burning
    N66_wind_power -- "replaces" --> N21_fossil_fuel_burning
    N55_solar_power -- "replaces" --> N21_fossil_fuel_burning
    N33_hydro_power -- "replaces" --> N21_fossil_fuel_burning
    N7_carbon_removal -- "reduces" --> N5_carbon_dioxide
    N20_forest_cover -- "enables" --> N7_carbon_removal
    N6_carbon_farming -- "enables" --> N7_carbon_removal
    N26_global_warming -- "is measured by" --> N25_global_surface_temperature
    N25_global_surface_temperature -- "increased since" --> N36_industrial_revolution
    N25_global_surface_temperature -- "is recorded in" --> N60_thermometer_records
    N25_global_surface_temperature -- "is reconstructed using" --> N11_climate_proxies
    N11_climate_proxies -- "include" --> N34_ice_cores
    N11_climate_proxies -- "include" --> N61_tree_rings
    N45_ocean_heat_content -- "absorbs over 90% of heat from" --> N26_global_warming
    N58_sulfur_dioxide -- "produces" --> N57_sulfate_aerosols
    N57_sulfate_aerosols -- "cause" --> N23_global_dimming
    N23_global_dimming -- "offset" --> N26_global_warming
    N47_pacific_decadal_oscillation -- "caused" --> N27_global_warming_hiatus
    N3_atlantic_multidecadal_oscillation -- "caused" --> N27_global_warming_hiatus
    N27_global_warming_hiatus -- "occurred from 1998 to 2013" --> N25_global_surface_temperature
    N62_upper_atmosphere_cooling -- "is caused by" --> N28_greenhouse_gases
    N28_greenhouse_gases -- "trap heat near" --> N15_earth
    N8_climate_change -- "causes" --> N54_snow_cover_reduction
    N8_climate_change -- "causes" --> N17_evaporation
    N17_evaporation -- "leads to" --> N4_atmospheric_humidity
    N4_atmospheric_humidity -- "leads to" --> N51_precipitation
    N8_climate_change -- "is called" --> N9_climate_crisis
    N8_climate_change -- "is called" --> N10_climate_emergency
    N26_global_warming -- "is sometimes called" --> N24_global_heating
    N38_james_hansen -- "popularized" --> N26_global_warming
    N42_nasa -- "employed" --> N38_james_hansen
    N2_arctic -- "has warmed the most due to" --> N8_climate_change
    N2_arctic -- "experiences" --> N50_permafrost_thawing
    N2_arctic -- "experiences" --> N52_sea_ice_decline
    N29_greenland_ice_sheet -- "can melt due to" --> N8_climate_change
    N41_medieval_warm_period -- "did not occur uniformly across" --> N15_earth
    N40_little_ice_age -- "did not occur uniformly across" --> N15_earth
    N59_temperature_record_of_the_last_2000_years -- "is reconstructed using" --> N48_paleoclimatology