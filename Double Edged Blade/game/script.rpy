# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define ray = Character("Raymond", color="#990000")
define als = Character("Ms Alsudo", color="#2c222e")
define elise = Character("Elise", color="#000066")
define silversaw = Character("Mr Silversaw", color="#005522")
define jodie = Character("Mrs Sketch", color="#2c222e")
define gary = Character("Mr Sketch", color="#2c222e")
define rosanna = Character("Queen Rosanna", color="#990000")
define johanna = Character("Johanna", color="#2c222e")
define catherine = Character("Catherine", color="#2c222e")
define catia = Character("Catia", color="#2c222e")
define antoine = Character("Antoine", color="#2c222e")
define fritz = Character("Fritz", color="#2c222e")
define maribel = Character("Maribel", color="#2c222e")
define sara = Character("Queen Sara", color="#000066")

# The game starts here.

label start:

    init python:
        mp = MultiPersistent("allundercontrol")
        mp.save_on_quit = True
        mp.maxyear = 1 #how many years have been released so far

    if mp.nextyear and (mp.currentyear < mp.maxyear): #Tells the game to switch to the next year
        scene main_menu_dark with fade
        "Continuing from the previous Year..."
        scene black with fade
        $ mp.currentyear += 0.5
        $ mp.nextyear = False
        jump yearswitch

    if mp.nextyear and (mp.currentyear > mp.maxyear):
        scene main_menu_dark with fade
        "Looks like the next Year hasn't been released yet. Be sure to download the update from e-lee-za.itch.io when it comes."
        
        menu:
            "Restart From First Year":
                $ mp.control = 50
                $ mp.risky = 0
                $ mp.safer = 0
                $ mp.currentyear = 0
                $ mp.nextyear = False
                $ mp.character = ""

                scene main_menu_dark with fade
                show ray select at offscreenleft
                show elise select at offscreenright
                with dissolve

                show ray select at left
                show elise select at right
                with ease

                "Choose a character to play as."

                call screen charselect
            "Exit":
                return
    
    if not mp.nextyear: #character select, this should only happen on First Year
        $ mp.control = 50
        $ mp.risky = 0
        $ mp.safer = 0
        $ mp.currentyear = 0
        $ mp.nextyear = False
        $ mp.character = ""

        scene main_menu_dark with fade
        show ray select at offscreenleft
        show elise select at offscreenright
        with dissolve

        show ray select at left
        show elise select at right
        with ease

        "Choose a character to play as."

        call screen charselect

label raystory: #this begins Ray's first year
    scene main_menu_dark
    show ray select confirm at left
    show elise select at right
    scene black with fade
    jump rayfirst

label elisestory: #this begins Elise's first year
    scene main_menu_dark
    show ray select at left
    show elise select confirm at right
    scene black with fade
    jump elisefirst

label yearswitch: #This is used to start different Years
    if mp.currentyear == 2:
        if mp.character == "Ray":
            jump raysecond
        if mp.character == "Elise":
            jump raysecond
    if mp.currentyear == 3:
        "Third Year hasn't been released yet."
        return
    if mp.currentyear == 4:
        "Fourth Year hasn't been released yet."
        return
    if mp.currentyear == 5:
        "Fifth Year hasn't been released yet."
        return
    if mp.currentyear == 6:
        "Sixth Year hasn't been released yet."
        return
    if mp.currentyear == 7:
        "Seventh Year hasn't been released yet."
        return
    

label devmessage:

    $ mp.save()

    if mp.nextyear and (mp.currentyear < mp.maxyear): #Tells the game to switch to the next year
        scene main_menu_dark with fade
        "Continuing from the previous Year..."
        scene black with fade
        $ mp.currentyear += 0.5
        $ mp.nextyear = False
        jump yearswitch

    else:
        scene main_menu_dark
        show eleeza 1 with easeinleft
        "Hello! I'm Eleeza, the creator of this game."
        "Thank you very much for playing First Year!"
        show eleeza 2
        "You can think of this Year as a sort of taster for the rest of the game - a demo, an introduction to the world."
        "First 'Year' is actually a misnomer...it should really be 'First...like two weeks I guess.' Ray just joined the school really late in the year."
        show eleeza 3
        "Well, I hope you enjoyed this first part of the story, because there's much, much more to come!"
        "In the next few Years, Ray and Elise's stories are going to diverge a bit, and things are going to get pretty interesting..."
        show eleeza 2
        "There's still six Years of this game left for me to release, and even more of the story beyond what All Under Control can tell...even beyond Raymond and Elise's stories."
        "So stay tuned for updates! I'll be updating and polishing this game often, and I'm open to suggestions for improvements."
        show eleeza 3
        "Anyways, that's all from me for now- see you around!"
        hide eleeza with easeoutright
    
    return

