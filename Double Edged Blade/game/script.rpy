# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define ray = Character("Raymond", color="#990000")
define als = Character("Miss Alsudo", color="#ff0033")
define elise = Character("Elise", color="#000066")
define saw = Character("Mr Silversaw", color="#005522")
define jodie = Character("Mrs Sketch", color="#ff0066")
define gary = Character("Mr Sketch", color="#993366")
define johanna = Character("Johanna", color="#806dd5")


# The game starts here.

label start:
    scene main_menu_dark with fade
    show ray select at offscreenleft
    show elise select at offscreenright
    with dissolve

    show ray select at left
    show elise select at right
    with ease

    "Choose a character to play as."

    call screen charselect

label raystory:
    scene main_menu_dark
    show ray select confirm at left
    show elise select at right
    scene black with fade
    return

label elisestory:
    scene main_menu_dark
    show ray select at left
    show elise select confirm at right
    scene black with fade
    return