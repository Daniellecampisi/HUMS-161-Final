label Peru_Path:
    scene black with fade
    narr "You have selected the Lord of Sipán, an elite ruler of the Moche civilization in ancient Peru."
    jump Moche_Period

label Moche_Period:
    scene ruinsPeru with dissolve
    tomb "It is around 250 AD. I, the Lord of Sipán, am buried in Huaca Rajada with great ceremony."
    tomb "Gold, silver, copper, fine ceramics, and sacred animals surround me—guarding my journey to the afterlife."
    tomb "My people mourn. My power lives on in metal and myth."
    tomb "My tomb lies untouched for nearly 1,700 years."
    jump Looting_Era

label Looting_Era:
    scene SiteP with fade
    narr "In 1987 looters discover traces of gold in Huaca Rajada."
    narr "They begin to illegally dig and extract treasures under cover of night."
    menu:
        "Allow looting to continue unchecked.":
            jump BlackMarket_Trafficking
        "Involve local authorities.":
            jump Police_Alerted

label BlackMarket_Trafficking:
    scene excavate with fade
    $chance_looted = random.randint(0, 4)
    if chance_looted > 1:
        narr "Looters smuggle irreplaceable artifacts into the black market."
        narr "Pieces vanish into private hands across Europe and the U.S., unrecorded and unprotected."
        jump CulturalLoss_Ending
    else:
        narr "One looter is caught trying to sell a golden artifact."
        narr "The police raid Huaca Rajada and alert archaeologist Walter Alva."
        jump Scientific_Excavation

label Police_Alerted:
    scene ruinsPeru with dissolve
    narr "Police intercept looters and recover some artifacts."
    narr "They contact Peruvian archaeologist Walter Alva."
    jump Scientific_Excavation

label Scientific_Excavation:
    scene excavate with dissolve
    narr "Walter Alva and his team begin formal excavations in February 1987."
    narr "What they find astounds the world: the intact royal tomb of the Lord of Sipán."
    narr "Over 451 ceremonial objects, including gold necklaces, funerary masks, and intricate earspools are preserved."
    narr "What should be done next?"
    menu:
        "Send key pieces to international museums for protection and exposure.":
            jump Artifact_Export_Debate
        "Create a museum in Peru to honor Moche heritage locally.":
            jump Build_Local_Museum

label Artifact_Export_Debate:
    scene SiteP with dissolve
    narr "Due to infrastructure issues, some artifacts are loaned to international museums."
    narr "They gain global attention—but stir debates at home."
    jump Export_Controversy


label Export_Controversy:
    scene ruinsPeru with dissolve
    narr "Controversy grows over artifacts displayed abroad."
    narr "Should Peru negotiate for permanent repatriation?"
    menu:
        "Negotiate long-term loans and traveling exhibits.":
            jump International_Loan_Ending
        "Push for full repatriation and return of looted pieces.":
            jump Repatriation_Effort

label Repatriation_Effort:
    scene excavate with dissolve
    $chance_looted = random.randint(0, 10)
    if chance_looted > 6:
        narr "Peru succeeds in recovering several artifacts from private collections and museums."
        jump Peru_Cultural_Pride_Ending
    else:
        narr "Many items remain missing or locked in foreign institutions."
        jump CulturalLoss_Ending

label Build_Local_Museum:
    scene museo with fade
    narr "In 2002, the Royal Tombs of Sipán Museum opens in Lambayeque."
    narr "It becomes a source of pride, housing the Lord of Sipán and safeguarding his treasures."
    narr "Thousands visit yearly to learn about the Moche civilization."
    jump Peru_Cultural_Pride_Ending

# ENDINGS
label Peru_Cultural_Pride_Ending:
    scene LordS with fade
    tomb "I am home, where my people honor me with reverence and pride."
    tomb "Their efforts preserve not only my body, but the spirit of the Moche."
    window hide
    show PV1 with fade
    pause
    scene black
    hide PV1 with fade
    window show
    jump start


label CulturalLoss_Ending:
    scene LordS with fade
    tomb "I am scattered, fragmented in forgotten halls and secret vaults."
    tomb "My story is told in whispers, incomplete—my legacy dimmed by greed."
    window hide
    show PV3 with fade
    pause
    scene black
    hide PV3 with fade
    window show
    jump start


label International_Loan_Ending:
    scene LordS with fade
    tomb "Though I travel far, my name carries the glory of Sipán."
    tomb "Perhaps someday I will return—but for now, I teach the world about the greatness of the Moche."
    window hide
    show PV2 with fade
    pause
    scene black
    hide PV2 with fade
    window show
    jump start

