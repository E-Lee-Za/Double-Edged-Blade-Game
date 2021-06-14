transform titlecharacters:
        ypos 1080 xpos 950
        easein 0.5 ypos -10
        easein 0.5 ypos 0

transform titlelogo:
        xpos 1920 ypos 700
        pause 1
        easein 0.75 xpos 1000

transform rayselectbackground:
        on show:
                ypos 1080 xpos 1030
                easein 0.25 ypos 0
        on hide:
                ypos 0 xpos 1030
                easein 0.15 ypos 1080

transform eliseselectbackground:
        on show:
                ypos 1080 xpos 0
                easein 0.25 ypos 0
        on hide:
                ypos 0 xpos 0
                easein 0.15 ypos 1080

transform rayselecttext:
        on show:
                xpos 1130 ypos 400 alpha 0
                easein 0.3 ypos 350 alpha 1
        on hide:
                xpos 1130 ypos 350 alpha 1
                easein 0.2 ypos 500 alpha 0

transform eliseselecttext:
        on show:
                xpos 100 ypos 400 alpha 0
                easein 0.3 ypos 350 alpha 1
        on hide:
                xpos 100 ypos 350 alpha 1
                easein 0.2 ypos 500 alpha 0