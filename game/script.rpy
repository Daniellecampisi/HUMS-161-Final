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
image iraq = "Iraq.png"
image Gmny = "german.png"
image babylon = "Babylon.png"
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


image ath1 = "Ath1.png"
image ath2 = "Ath2.png"
image met = "met.png"
image necrop = "Necrop.png"
image krater = "krater.png"
# The game starts here.
define started = 0
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
    if started == 0:
        play music "music/finalmusic.mp3" fadein 1.0
        narr "Welcome to the Cultural Trafficking Digital Collection."
    
    $started = 1
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
label credits:
    scene black
    with fade

    show text """
    Works Cited
    Ahmed, Fatema. “England's Other Crown.” The Dial, 2 Aug. 2024, www.thedial.world/articles/news/issue-3/ethiopia-emperor-tewodros-crown-victoria-albert-museum-london.\n
    “The Flavian Trilogy and More.” This Was Rome, www.thiswasrome.com/post/euphronios_krater. Accessed 7 May 2025.\n
    “An Audience with Nefertiti.” Google Arts & Culture, artsandculture.google.com/story/an-audience-with-nefertiti-neues-museum-staatliche-museen-zu-berlin/_AWhSnxV4cRAIw. Accessed 7 May 2025.\n
    Butters, Luis Jaime Castillo, and Karla Paola Patroni Castillo. “The Moche.” Oxford Research Encyclopedia of Latin American History, 30 Apr. 2020, oxfordre.com/...e-755.\n
    Desplat, Juliette. “The Nefertiti Affair.” The National Archives Blog, 16 Sept. 2016, blog.nationalarchives.gov.uk/nefertiti-affair-history-repatriation-debate/.\n
    “Euphronios (Sarpedon) Krater.” Trafficking Culture, traffickingculture.org/...krater/. Accessed 7 May 2025.\n
    British Museum. “From Chavin to the Inca.” www.britishmuseum.org/...timeline-central-andes-south-america. Accessed 7 May 2025.\n
    """ at truecenter
    pause
    show text """
    Smarthistory. “From Tomb to Museum: The Story of the Sarpedon Krater.” smarthistory.org/euphronios-krater-2/. Accessed 7 May 2025.\n
    “Ishtar Gate.” Cultural Repatriation, repatriation-his111.weebly.com/ishtar-gate.html. Accessed 7 May 2025.\n
    “Loot from Maqdala.” Together We Learn, twlethiopia.org/article/maqdala-and-its-loot-a-brief-history/. Accessed 7 May 2025.\n
    “The Loot Museum.” thelootmuseum.com/maqdala-gold-crown/. Accessed 7 May 2025.\n
    DOJ. “Peruvian Artifact Repatriated.” justice.gov/archives/opa/pr/peruvian-artifact-repatriated. 5 Feb. 2025.\n
    Radley, Dario. “Construction Timeline of Babylon's Ishtar Gate.” Archaeology News Online Magazine, 16 Apr. 2024, archaeologymag.com/...ishtar-gate/.\n
    Staatliche Museen zu Berlin. “Discovery and Partage.” www.smb.museum/...bust-of-nefertiti/discovery-and-partage/. Accessed 7 May 2025.\n
    GatherTales. “The Moche Lords of Sipán.” www.gathertales.com/.../sid-302. Accessed 7 May 2025.\n
    Madain Project. “Timeline of the Ishtar Gate.” madainproject.com/...ishtar_gate#google_vignette. Accessed 7 May 2025.\n
    Wizevich, Eli. “The Bust of Nefertiti.” Smithsonian Magazine, 6 Dec. 2024, www.smithsonianmag.com/...nefertiti-180985565/.
    """ at truecenter

    with dissolve

    pause 

    # Returns to main menu