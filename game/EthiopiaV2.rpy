init python:
    import random
label missionaries:
    scene MuseumUK with fade
    narr "It is the height of the British Empire. Across continents, missionaries are dispatched to spread the Christian faith and British influence."
    narr "Now, a group seeks permission to travel to the distant highlands of Ethiopia-a proud, ancient Christian kingdom, yet one that has long resisted foreign intervention."
    narr "Should we allow a missionary group to travel to Ethiopia?"
    menu: 
        "Yes, send a group of missionaries.":
            jump areimprisioned
        "No do not send any missionaries":
            jump imprisionedEurope
    return

label areimprisioned:
    define prisionChance = 0
    $prisionChance = random.randint(1,10)
    if prisionChance >= 3:
        jump imprisioned
    else:
        jump imprisionedEurope
    return

label imprisioned:
    scene MountainView with fade

    narr "The missionaries arrive, hoping to teach and convert, but soon find themselves entangled in local politics."
    narr "Emperor Tewodros II, frustrated by unfulfilled promises from Britain and suspicious of foreign intentions, imprisons the missionaries along with other Europeans."
    narr "News of their capture reaches London, sparking outrage in Parliament and the press. What should be done regarding this?"
    menu:
        "Attempt to resolve tensions.":
            jump diplomacyAttemptedUK
        "Retaliate against the imprisionment.":
            jump militaryExpedition
    return
label imprisionedEurope:
    scene MountainExpanse with fade
    narr "The missionaries are refused approval, though other European powers make expeditions to Ethiopia"
    narr "Emperor Tewodros II, imprisons the other European missionaries and diplomats."
    narr "News of their capture reaches London, sparking outrage in the press. What should be done regarding this?"
    menu:
        "Attempt to resolve tensions.":
            jump diplomacyAttemptedUK
        "Retaliate against the imprisionment.":
            jump militaryExpedition
label diplomacyAttemptedUK:
    define diplomacy = 0
    $prisionChance = random.randint(1,10)
    if prisionChance >= 4:
        jump diplomacySuccess
    else:
        jump diplomacyFail
    return
label diplomacySuccess:
    scene CastleView with fade
    narr "Diplomatic envoys successfully negotiate the release of the captives."
    narr "Though tensions remain, war is averted—for now."
    jump alternateEndings

label diplomacyFail:
    scene CastleView with fade
    narr "Diplomacy fails. The government authorizes a military expedition—not for conquest, but to rescue the hostages and restore British prestige."
    jump militaryExpedition

label militaryExpedition:
    # scene bg march with fade
    narr "A force of British and Indian soldiers is led across hundreds of miles of rugged terrain."
    narr "The expedition is an immense logistical feat—elephants, mules, and thousands of men march toward the mountain fortress of Maqdala, seat of the Emperor himself."
    jump lootingMaqdala

label lootingMaqdala:
    # scene bg looting with fade
    scene MountainExpanse with fade
    narr "Within the fortress, the British discover a trove of treasures: gilded crowns, golden chalices, sacred manuscripts, and priceless relics of Ethiopian heritage."
    narr "Fifteen elephants and nearly two hundred mules are needed to carry away the loot. Some soldiers take items as souvenirs; others become state property."
    jump fateOfCrown

label fateOfCrown:
    # scene bg auction with fade
    narr "Among the spoils is an ornate gold crown, believed to have been commissioned in the 1740s by an Ethiopian ruler."
    narr "An auction is held on the Dalanta Plain. Officers bid for artifacts; the crown is purchased on behalf of the British government and sent to the South Kensington Museum in London."
    jump presentDayDecision


label presentDayDecision:
    scene MuseumUK with fade
    narr "Now the world is reckoning with the legacies of empire. Ethiopia’s calls for restitution grow louder."
    menu:
        "Return the crown permanently.":
            jump repatriationApproved
        "Offer only a long-term loan.":
            jump outcomeLoan
        "Refuse all repatriation efforts.":
            jump outcomeDenied


# ENDINGS
label repatriationApproved:
    # scene bg celebration with fade
    scene crownV with fade
    crown "At long last, I return home. Carried across oceans once more, not as spoils of war—but as a gesture of healing."
    narr "The crown is placed in a restored sanctuary, symbolizing a new era of cooperation."
    window hide
    show E2RepatFull with fade
    pause
    scene black
    hide E2RepatFull with fade
    window show
    jump start

label outcomeLoan:
    # scene bg shared with fade
    scene crownV with fade
    crown "I remain far from home, yet Ethiopian scholars now walk these halls, sharing stewardship of my legacy."
    narr "Though imperfect, the loan symbolizes a step toward dialogue and shared guardianship."
    window hide
    show E2loan with fade
    pause
    scene black
    hide E2loan with fade
    window show
    jump start
label outcomeLoan2:
    # scene bg shared with fade
    scene crownV with fade
    crown "I remain far from home, yet Ethiopian scholars now walk these halls, sharing stewardship of my legacy."
    narr "Though imperfect, the loan symbolizes a step toward dialogue and shared guardianship."
    window hide
    show E2Loan2 with fade
    pause
    scene black
    hide E2Loan2 with fade
    window show
    jump start
label outcomeDenied:
    # scene bg museum with fade
    scene crownV with fade
    crown "Here I remain, a silent witness to the passing of years."
    crown "I hear the footsteps of strangers and the murmur of distant lands. But my heart remembers the songs of my homeland."
    narr "The crown remains a glittering prize of empire—its future uncertain, its legacy contested."
    window hide
    show E2NoRepat with fade
    pause
    scene black
    hide E2NoRepat with fade
    window show
    jump start

label alternateEndings:
    scene MountainExpanse with fade
    define ethiopiaCare = 0
    $ethiopiaCare = random.randint(0,5)
    if ethiopiaCare > 3:
        scene crownV with fade
        narr "Ethiopia is able to keep the Maqdala Crown in its stewardship. "
        crown "I remain in my homeland, with my people. They expanded conservation efforts to protect me, as I bask in our country's greatness."
        window hide
        show NoLoot with fade
        pause
        scene black
        hide NoLoot with fade
        window show
        jump start
    else:
        narr "Ethiopia is unable to keep the crown and other artifacts in quality conditions. What should be done?"
        menu:
            "Offer a long-term loan.":
                jump outcomeLoan  
            "Arrange a co-stewardship program.":
                jump outcomeLoan2
        jump start