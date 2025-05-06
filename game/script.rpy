# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define narr = Character(" ")
define crown = Character("The Maqdala Crown")
define bust = Character("The Bust of Nefertiti")
define krater = Character("The Euphronios Krater")
define gate = Character("The Ishtar Gate")
define tomb = Character("The Lord of Sipán")
# ETHIOPIA IMAGES

image crownV = "crownV.png"
image CastleView = "CastleView.png"
image MountainExpanse = "MountainExpanse.png"
image MountainView = "MountainView.png"
image MuseumUK = "MuseumUK.png"

image ArtifactLost = "ArtifactLost.png"
image O3E = "Outcome3Egypt.png"
image Miscare  = "MiscareEnding.png"
image AutonomyEnd = "Autonomy.png"
image Germanend = "GermanEnding.png"
image Copat = "EEND5.png"

#ETHIOPIA ENDINGS
image E1V1A = "E1V1A.png"
image E1V1B = "E1V1B.png"
image E1V2 = "E1V2.png"
image E1V3 = "E1V3.png"
image E1V4 = "E1V4.png"
image E2loan = "E2Loan.png"
image E2NoRepat = "E2NoRepat.png"
image E2RepatFull = "E2RepatFull.png"
image NoLoot = "NoLooting.png"


# EGYPT IMAGES
image Bust_NEF = "bustnef.png"
image german_museum = "GerMuseum.png"
image sculptor_head = "Scupltor.png"
image pharoh = "pharoh.png"
image city = "CityEgypt.png"

#PERU IMAGES
image excavate = "ExP.png"
image LordS = "LordS.png"
image SiteP = "SiteP.png"
image museo = "MuseoP.png"
image ruinsPeru = "RuinsP.png"
#PERU ENDINGS
image PV1 = "PV1.png"
image PV2 = "PV2.png"
image PV3 = "PV3.png"


# IRAQ IMAGES
image Gate = "Gate.png"
#IRAQ DEcisions
image I1V1 = "I1V1.png"
image I1V2 = "I1V2.png"
image I1V3 = "I1V3.png"
image I1V4 = "I1V4.png"
image I2V1 = "I2V1.png"
image I2V2 = "I2V2.png"
image I2V3 = "I2V3.png"
image I2V4 = "I2V4.png"
image I2V5 = "I2V5.png"

# GREECE 

image G1 = "37.png"
image G2 = "38.png"
image G3 = "39.png"
image G4 = "40.png"
image G5 = "41.png"
image G6 = "42.png"
image G7 = "43.png"
image G8 = "44.png"

#MISC IMAGES
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
        "The Lord of Sipán":
            jump Peru_Path
    # jump E_V1_Intro

    return
