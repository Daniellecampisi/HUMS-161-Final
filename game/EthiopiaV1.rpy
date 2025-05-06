init python:
    import random
define europeanAffection = 0
define diplomacyAttempted = False
define britishDiplomacy = 0
define repatriationSuccess = False

#introduction to the scene
label E_V1_Intro:
    scene black with fade
    narr "You have selected the Maqdala Crown as your object. Which side would you like to play as?"
    menu: 
        "Ethiopia":
            jump consoldationV1
        "England":
            jump missionaries
        # "England"
    return

#Consolidate?
label consoldationV1:
    # CASTLE
    scene CastleView with fade
    crown "I was born in 1740, commissioned by King Iyyasu II—golden, radiant, and adorned with the sacred images of the Apostles and Evangelists."
    crown "Bestowed as an imperial gift, I was meant to secure eternal prayers for the emperor's soul."
    scene MountainExpanse with fade
    crown "My early years were peaceful, resting in the sanctuary of the Church of Our Lady of Qwesqwam."
    
    narr "As you hold control of Ethiopia's power, you must make all executive decisions for the nation."
    narr "The kingdom's power and wealth is spread across its land. Should a consoldated treasury be constructed in the fortress of Maqdala?"
    menu:
        "Consolodate the kingdom's power.":
            jump diplomacyV1
        "Keep the kingdom's riches dispersed.":
            crown "As time passed I was able to survive lootings and warfare. "
            jump goodDiplomacyV1
    return

#try to be civil?
label diplomacyV1:
    #MOUNTAIN
    scene MountainView with fade
    crown "When Emperor Tewodros II sought to unite and strengthen the empire, I was carried to the mountain fortress of Maqdala, joining a treasury of Ethiopia's most cherished relics."
    crown "But my sanctuary became a battleground."
    narr "Tensions are rising with the arrival of European armies. What should be done?"
    menu:
        "Attempt to reconcile tensions.":
            $ diplomacyAttempted = True
            jump tensionsV1
        "Withdrawl diplomatic efforts.":
            $ diplomacyAttempted = False
            jump tensionsV1
    return

#randomize negotiation efforts
label tensionsV1:
    if(diplomacyAttempted == True):
        $britishDiplomacy = random.randint(2,5)

    else:
        $britishDiplomacy  = random.randint(0,5)
    python:
        print("Diplomacy = ",britishDiplomacy)
    if(britishDiplomacy >= 3):
        jump goodDiplomacyV1
    else:
        jump badDiplomacyV1
    return

#negottation efforts fail, crown captured
label badDiplomacyV1:
    scene CastleView with fade
    crown "As tensions escalated with the arrival of European armies, Maqdala fell."

    crown "I was seized alongside my companions, auctioned off as spoils to foreign hands."
    scene MuseumUK with fade
    crown "Shipped across continents, I found myself confined within the then South Kensington Museum, with the approval of the British Treasury."
    narr "The crown is now outside of Ethiopian control. Should repatriation efforts be made?"
    menu:
        "Take efforts to negociate repatriation.":
            jump repatriationTry 
        "Leave the crown in the England's stewardship.":
            jump outcome4V1
    return
label repatriationTry:
    define repatChance = 0
    $repatChance = random.randint(0, 5)
    if(repatChance > 2):
        narr "Negotiation with the English has failed."
        jump outcome4V1
    else:
        narr "The British agreed to return the crown and other artifacts!"
        jump goodDiplomacyV1
    return

label goodDiplomacyV1:
    # narr "The British work diplomatically with Ethiopia."
    scene CastleView with fade
    crown "I survived the tense arrival of the Europeans, remaining in my homeland."
    narr "Preservation efforts have been made, however the crown and other artifacts are kept in poor conditions."
    narr "What should be done?"
    menu:
        "Keep the artifacts in Ethiopia.":
            jump outcome1V1
        "Move the artifact elsewhere.":
            narr "How should the crown's stwardship be structured?"
            menu:
                "A long-term loan of the crown to another musuem.":
                    jump outcome2V1
                "A co-stewardship model with Ethiopian representatives and another museum.":
                    jump outcome3V1 

    return

        


label outcome1V1:
    scene crownV with fade
    define qualityRandomizer = 0
    $qualityRandomizer = random.randint(0,1)
    if(qualityRandomizer == 1):
        crown "I remain in my homeland, with my people. Despite our closeness my time is fading as I slowly decay from inadequate care."
        show E1V1A
        pause
        hide E1V1A
        jump start
    else:
        crown "I remain in my homeland, with my people. They expanded conservation efforts to protect me, as I bask in our country's greatness."
        show E1V1B
        pause
        hide E1V1B
        jump start
    return
label outcome2V1:
    scene crownV with fade
    crown "I remain in the hands of outsiders, protected from poor conditions, but still far from my home."
    show E1V2
    pause
    hide E1V2
    jump start
    return
label outcome3V1:
    scene crownV with fade
    crown "I was transfered to a museum in England, watching my people negociate my stewardship and protect my longjevity."
    crown "Although I am far from my homeland, some of my people come to England to guide my conservation and presentation to the public."
    show E1V3
    pause
    hide E1V3
    jump start
    return
label outcome4V1:
    scene crownV with fade
    crown "Here I remain, a silent witness to the passing of years, watching as my people's voices rise in hope and sorrow—calling for my return, while those who hold me show little urgency to let me go."
    show E1V4
    pause
    hide E1V4
    jump start
    return