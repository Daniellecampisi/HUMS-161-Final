init python:
    import random

#introduction to the scene
label KraterIntro:
    scene krater with fade
    # TODO SHOW KRATER OBJECT
    narr "You have selected the Euphronios Krater as your object. Which side would you like to play as?"
    menu: 
        "Italy":
            jump backgroundKrater
        "The United States":
            jump METV1
        # "England"
    return

label backgroundKrater:
    scene ath1 with fade

        # TODO SHOW ATHENS 1
    krater "I was born in Athens, serving as a centerpiece for cellebrations and gatherings. I was an essential part of my people's social life."
    krater "I had been adorned with illustrations of Sarpedons death. My adornments were meant to inspire discussion of heroism and mortality. I was buried alongside a fellow Etruscan, in a tomb meant to resemble a home to provide comfort beyond death."
    narr "The Euphronios Krater is burried alongside other tombs on private land. Should more protection be added to the necropolis?"
    menu:
        "Add more security to protect the necropolis.":
            narrator "You chose to increase security at the necropolis. Surveillance and site protection deterred illegal excavations."
            jump lootingChance2
        "Leave the necropolis as is.":
            jump lootingChance
    return
label lootingChance2:
    define LC = 0
    $LC = random.randint(1,5)
    if LC > 3:
        narr "The security measures were not sufficient in protecting the necropolis."
        jump looting
    else:
        narr "The security measures were sufficient in protecting the necropolis."
        jump security
    return

label lootingChance:
    define LC = 0
    $LC = random.randint(1,5)
    if LC >= 2:
        narr "The current security measures were not sufficient in protecting the necropolis."
        jump looting
    else:
        narr "The current security measures were sufficient in protecting the necropolis."
        jump security
    return

label looting:
    scene necrop with fade

    krater "In the midst of my rest I was disrupted by looters, who sought to sell me to an antiques dealer."
    krater "They succeeded in finding a buyer and I was soon smuggled to Switzerland. Here efforts were made to restore me" #TODO: add can fail here?
    krater "I was then sold to an American dealer who moved to negotiations with the Metropolitan Museum of Art in New York. The representatives agreed to purchase me and move me into their provenance."
    narr "An article releases regarding the acquisition of the krater. The public are questioning it's acquisition. What should be done?"
    menu:
        "Investigate the aquisition.":
            jump investigateV1
        "Ignore the allegations.":
            jump met
    return

label security:
    scene necrop with fade
    narrator "The Krater remained undisturbed, a hidden treasure of the Etruscan legacy."
    narrator "However, a private collector expresses interest in financing a legal excavation."
    menu:
        "Allow excavation under official supervision":
            jump legalExcavation
        "Deny excavation and preserve the site":
            jump preservedSite
    return
define RC = 0
label met:
    # in met and want to attempt repatriation
    # TODO SHOW MET
    scene met with fade
    krater "I was kept at the Metropolitan Museum of Art, despite the suspicion on my providence."
    narr "What should be done regarding the krater's stewardship?"
    menu:
        "Request repatriation.":
            jump repatChanceKrater
        "Leave the object in the United States.":
            jump repatFailKrater


label investigateV1:
        # TODO SHOW ATHENS 2 
    scene ath2 with fade

    narr "The investigation reveals that the Krater was illegally excavated and exported. What should be done?"
    menu:
        "Negotiate the object's return.":
            $RC  = 1
            jump repatChanceKrater
        "Let the object remain.":
            jump repatFailKrater
    return

label repatChanceKrater:
    
    $RC += random.randint(0, 2)
    if RC >= 2:
        jump repatSuccessKrater
    else:
        narr "Repatriation attempts failed with the representatives from the MET."
        jump repatFailKrater


label repatSuccessKrater:
    # TODO SHOW KRATER
    scene krater with fade
#tested

    #repatriation sucess 
    krater "After years abroad, I was finally returned to Italy, welcomed with reverence and sorrow for the journey I endured."
    narrator "The Krater was placed in the National Etruscan Museum of Villa Giulia, where it now serves as a symbol of cultural restitution."
    
    window hide
    show G1 with fade
    pause
    scene black
    hide G1 with fade
    window show

    jump start
    return

label repatFailKrater:
    scene krater with fade
#tested
    #lost but not forgetton 
    krater "Throughout time, I was kept behind glass, far from the soil where I once belonged."
    krater "Whispers of my stolen past echo through the halls, as I remain a trophy rather than a tribute."
    
    window hide
    show G2 with fade
    pause
    scene black
    hide G2 with fade
    window show

    jump start
    return



label legalExcavation:
    scene krater with fade
    #dignity ending #tested

    krater "This time, my awakening was respectful. Hands trained in care unearthed me, documenting every fragment of my story."
    narrator "The Krater was displayed in a regional Italian museum, with full context of its history and cultural relevance."
    
    window hide
    show G3 with fade
    pause
    scene black
    hide G3 with fade
    window show

    jump start
    return

label preservedSite:
    scene krater with fade
    #untouched silence 
    narrator "The necropolis remained untouched, preserving the mystery and cultural spirit of the site."
    narrator "Generations of scholars debated its potential contents, but the site stood as a symbol of what should remain sacred."
    
    window hide
    show G4 with fade
    pause
    scene black
    hide G4 with fade

    window show
    jump start
    return

