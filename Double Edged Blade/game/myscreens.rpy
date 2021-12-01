screen tourCourtyardR():
    imagemap:
        ground "images/courtyard1.png"
        hotspot(1200, 430, 1530, 760) action Jump('tourArtR')
        hotspot(300, 430, 540, 700) action Jump("tourDtR")
    text "Control:"  size 50 color "#dae2f1" at controltitle
    text "[mp.control]"  size 100 color "#dae2f1" at controlnumber

screen tourCourtyard2R():
    imagemap:
        ground "images/courtyard2.png"
        hotspot(1400, 290, 1580, 620) action Jump('tourLibraryR')
        hotspot(60, 415, 235, 670) action Jump("tourTheatreR")
    text "Control:"  size 50 color "#dae2f1" at controltitle
    text "[mp.control]"  size 100 color "#dae2f1" at controlnumber

screen tourCourtyardE():
    imagemap:
        ground "images/courtyard1.png"
        hotspot(1200, 430, 1530, 760) action Jump('tourArtE')
        hotspot(300, 430, 540, 700) action Jump("tourDtE")
    text "Control:"  size 50 color "#dae2f1" at controltitle
    text "[mp.control]"  size 100 color "#dae2f1" at controlnumber

screen tourCourtyard2E():
    imagemap:
        ground "images/courtyard2.png"
        hotspot(1400, 290, 1580, 620) action Jump('tourLibraryE')
        hotspot(60, 415, 235, 670) action Jump("tourTheatreE")
    text "Control:"  size 50 color "#dae2f1" at controltitle
    text "[mp.control]"  size 100 color "#dae2f1" at controlnumber


screen cupboardR():
    imagemap:
        ground "images/cupboard.png"
        hotspot(1210, 640, 1640, 835) action Jump('screwdriverR')
        #hotspot(250, 280, 400, 540) action Jump('lightswitchR')
        hotspot(895, 95, 1235, 345) action Jump('escapecupboardR')
    text "Control:"  size 50 color "#dae2f1" at controltitle
    text "[mp.control]"  size 100 color "#dae2f1" at controlnumber

screen cupboardE():
    imagemap:
        ground "images/cupboard.png"
        hotspot(1210, 640, 1640, 835) action Jump('screwdriverE')
        #hotspot(250, 280, 400, 540) action Jump('lightswitchE')
        hotspot(895, 95, 1235, 345) action Jump('escapecupboardE')
    text "Control:"  size 50 color "#dae2f1" at controltitle
    text "[mp.control]"  size 100 color "#dae2f1" at controlnumber

screen museumR():
    imagemap:
        ground "images/museum.png"
        hotspot(80, 500, 555, 700) action Jump('royalportraitsR')
        hotspot(570, 160, 930, 500) action Jump('mapofscholiteR')
        hotspot(1250, 165, 1630, 630) action Jump('sworddisplayR')
    text "Control:"  size 50 color "#dae2f1" at controltitle
    text "[mp.control]"  size 100 color "#dae2f1" at controlnumber

screen museumE():
    imagemap:
        ground "images/museum.png"
        hotspot(80, 500, 555, 700) action Jump('royalportraitsE')
        hotspot(570, 160, 930, 500) action Jump('mapofscholiteE')
        hotspot(1250, 165, 1630, 630) action Jump('sworddisplayE')
    text "Control:"  size 50 color "#dae2f1" at controltitle
    text "[mp.control]"  size 100 color "#dae2f1" at controlnumber

screen charselect():
    imagemap:
        ground "images/main_menu_dark.png"
        imagebutton:
            idle "images/ray select.png"
            hover "images/ray select hover.png"
            hovered ShowTransient("raydesc") unhovered Hide("raydesc")
            action Jump("raystory")
        imagebutton:
            idle "images/elise select.png"
            hover "images/elise select hover.png"
            xpos 1030
            hovered ShowTransient("elisedesc") unhovered Hide("elisedesc")
            action Jump("elisestory")

screen raydesc():
    add "gui/overlay/char_description.png" at rayselectbackground
    text "Prince Raymond Pseudeland:\nHeir of the Pseudeland Region.\n\nHe's just trying his best. He's quite shy,\nand a sweetheart who's in desperate need\nof a hug, but has a sensible and calm\nmind...\n\n...most of the time." size 40 color "#dae2f1" at rayselecttext

screen elisedesc():
    add "gui/overlay/char_description.png" at eliseselectbackground
    text "Princess Elise Realis:\nHeir of the Realis Region.\n\nShe wants to be confident and a\ngood friend. She likes to build things,\nand sometimes they work. She's\na little scatterbrained...\n\n...or maybe 'a little' is an understatement." size 40 color "#dae2f1" at eliseselecttext