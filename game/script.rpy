# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define narr = Character(" ")
define crown = Character("The Maqdala Crown")
define bust = Character("The Bust of Nefertiti")
define krater = Character("The Euphronios Krater")
define gate = Character("The Ishtar Gate")
image crown = "Crown.jpg"
image kingdom = "kingdom.jpg"
image 1 = "1.jpg"
image 2 = "2.jpg"
image 3 = "3.jpg"
image 4 = "4.jpg"
image 5 = "5.jpg"
image 6 = "6.jpg"
image 7 = "7.jpg"
image aura = "Aura.png"
image start = "Start.png"

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg start
    # show aura
    # show crown
    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.


    # These display lines of dialogue.

    narr "Welcome to the Cultural Trafficking Digital Collection."

    narr "What artifact will you explore?"

    menu:
        "The Bust of Nefertiti":
            jump EgyptV1_Intro
        "The Maqdala Crown.":
            jump E_V1_Intro
        "The Euphronios Krater":
            jump KraterIntro
        "The Ishtar Gate":
            jump Ishtar_Intro

    # jump E_V1_Intro

    return
