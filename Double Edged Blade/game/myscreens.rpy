#screen tourCourtyard():   
#    imagemap:
#        ground "images/courtyard1.png"
#        hotspot(180, 305, 790, 680) action Jump('tourDt')
#        hotspot(805, 305, 1400, 680) action Jump("tourArt")

#screen tourCourtyard2():   
#    imagemap:
#        ground "images/courtyard2.png"
#        hotspot(496, 326, 1111, 231) action Jump('tourPond')
#        hotspot(1,340,475,870) action Jump("tourTheatre")

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
    text "Princess Elise Realis:\nHeir of the Realis Region.\n\nShe wants to be confident and a\ngood friend.She likes to build things,\nand sometimes they work. She's\na little scatterbrained...\n\n...or maybe 'a little' is an understatement." size 40 color "#dae2f1" at eliseselecttext