graph TD
    N0_astro-tourism["Astro-Tourism"]
    N1_astronomy_ambassadors["Astronomy Ambassadors"]
    N2_astrophotography["Astrophotography"]
    N3_bengaluru["Bengaluru"]
    N4_bortle_1["Bortle 1"]
    N5_buddhist_monastery["Buddhist Monastery"]
    N6_chennai["Chennai"]
    N7_china["China"]
    N8_dark_sky_reserve["Dark Sky Reserve"]
    N9_digpa-ratsa_ri["Digpa-Ratsa Ri"]
    N10_energy-systems_engineer["Energy-Systems Engineer"]
    N11_global_development["Global Development"]
    N12_hanle["Hanle"]
    N13_hashika_raj["Hashika Raj"]
    N14_himalayan_chandra_telescope["Himalayan Chandra Telescope"]
    N15_himalayas["Himalayas"]
    N16_homestay["Homestay"]
    N17_indian_astronomical_observatory["Indian Astronomical Observatory"]
    N18_indian_institute_of_astrophysics["Indian Institute Of Astrophysics"]
    N19_kesang_dorjey["Kesang Dorjey"]
    N20_ladakh["Ladakh"]
    N21_light_pollution["Light Pollution"]
    N22_military_camp["Military Camp"]
    N23_milky_way["Milky Way"]
    N24_nawang_tsoundu["Nawang Tsoundu"]
    N25_niruj_mohan_ramanujam["Niruj Mohan Ramanujam"]
    N26_padma_chamchot["Padma Chamchot"]
    N27_star_party["Star Party"]
    N28_summer_triangle["Summer Triangle"]
    N29_the_guardian["The Guardian"]
    N30_tsering_dolkar["Tsering Dolkar"]
    N31_venus["Venus"]
    N12_hanle -- "is located in" --> N20_ladakh
    N12_hanle -- "is located in" --> N15_himalayas
    N12_hanle -- "hosts" --> N17_indian_astronomical_observatory
    N17_indian_astronomical_observatory -- "is located on" --> N9_digpa-ratsa_ri
    N12_hanle -- "became" --> N8_dark_sky_reserve
    N30_tsering_dolkar -- "is" --> N1_astronomy_ambassadors
    N26_padma_chamchot -- "is" --> N1_astronomy_ambassadors
    N19_kesang_dorjey -- "is" --> N1_astronomy_ambassadors
    N24_nawang_tsoundu -- "is" --> N1_astronomy_ambassadors
    N1_astronomy_ambassadors -- "work in" --> N12_hanle
    N1_astronomy_ambassadors -- "guide" --> N0_astro-tourism
    N0_astro-tourism -- "draws visitors to" --> N12_hanle
    N0_astro-tourism -- "supports" --> N16_homestay
    N30_tsering_dolkar -- "runs" --> N16_homestay
    N16_homestay -- "is located in" --> N12_hanle
    N14_himalayan_chandra_telescope -- "was installed in" --> N17_indian_astronomical_observatory
    N17_indian_astronomical_observatory -- "attracts" --> N0_astro-tourism
    N12_hanle -- "has" --> N4_bortle_1
    N4_bortle_1 -- "describes" --> N8_dark_sky_reserve
    N21_light_pollution -- "threatens" --> N8_dark_sky_reserve
    N21_light_pollution -- "is caused by" --> N22_military_camp
    N22_military_camp -- "is located near" --> N12_hanle
    N1_astronomy_ambassadors -- "revive knowledge of" --> N28_summer_triangle
    N28_summer_triangle -- "is constellation pattern observed in" --> N23_milky_way
    N30_tsering_dolkar -- "observes" --> N31_venus
    N1_astronomy_ambassadors -- "organize" --> N27_star_party
    N27_star_party -- "is hosted in" --> N12_hanle
    N27_star_party -- "is organized by" --> N17_indian_astronomical_observatory
    N27_star_party -- "includes" --> N2_astrophotography
    N13_hashika_raj -- "attended" --> N27_star_party
    N13_hashika_raj -- "is" --> N10_energy-systems_engineer
    N13_hashika_raj -- "is from" --> N6_chennai
    N24_nawang_tsoundu -- "is acting head monk at" --> N5_buddhist_monastery
    N5_buddhist_monastery -- "is located in" --> N12_hanle
    N29_the_guardian -- "reports on" --> N11_global_development
    N11_global_development -- "includes" --> N0_astro-tourism
    N1_astronomy_ambassadors -- "educate on" --> N21_light_pollution