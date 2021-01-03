screen tourCourtyard():   
    imagemap:
        ground "images/courtyard1.png"
        hotspot(180, 305, 790, 680) action Jump('tourDt')
        hotspot(805, 305, 1400, 680) action Jump("tourArt")

screen tourCourtyard2():   
    imagemap:
        ground "images/courtyard2.png"
        hotspot(496, 326, 1111, 231) action Jump('tourPond')
        hotspot(1,340,475,870) action Jump("tourTheatre")