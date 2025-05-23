init python:
    import random
define germanPosition = 0
define diplomacyAttempted = False
define iraqEffort = 0
define repatriationSuccess = False

label Ishtar_Intro:
    scene black with fade
    narr "You have selected the Ishtar Gate of Babylon. Which side would you like to play as?"
    menu:
        "Iraq":
            jump iraq_intro
        "Germany":
            jump ISHTARV1
    return

label iraq_intro:
    scene babylon with fade
    gate "I was built in the time of Nebuchadnezzar II, a symbol of Babylon's glory and devotion to the goddess Ishtar."
    gate "Centuries buried me in silence—until foreign hands unearthed me in the 20th century."
    narr "German archeologists excavated fragments of the gate and shipped them out of Iraq."
    narr "From there gate was reconstructed in the Pergamon Museum in Germany."
    narr "What should be done regarding the gate's stewardship?"
    menu:
        "Launch diplomatic campaign to reclaim the gate.":
            $ diplomacyAttempted = True
            jump iraq_diplomacy
        "Focus on preserving what remains in Iraq.":
            jump iraq_preservation
    return

label iraq_diplomacy:
    scene Gmny with fade
    gate "Delegations are sent, letters written. Iraq's call grows louder: Return the gate."
    $iraqEffort = random.randint(0, 5)
    if iraqEffort >= 3:
        jump repatriation_success
    else:
        jump repatriation_fail
    return


label repatriation_success:
    scene babylon with fade
    gate "Against all odds, Germany agrees to return key fragments and collaborates with Iraq on a future reconstruction."
    narr "What should be done?"
    menu:
        "Keep the artifacts in Iraq.":
            jump iraq_outcome_repatriated
        "Move the artifact elsewhere.":
            narr "How should the crown's stwardship be structured?"
            menu:
                "A long-term loan of the crown to another musuem.":
                    jump iraq_outcome_repatriated2
                "A co-stewardship model with Ethiopian representatives and another museum.":
                    jump iraq_outcome_repatriated2 
    return

label repatriation_fail:
    scene iraq with fade
    gate "The Pergamon Museum offers no formal response. The gate remains a centerpiece in Berlin."
    jump iraq_outcome_failed
    return



label iraq_preservation:
    scene iraq with fade
    gate "Teams of archaeologists and conservationists begin to care for what fragments remain in Babylon."
    narr "Though the full gate remains in Berlin, the Iraqi government invests in making Babylon a UNESCO heritage site."
    jump iraq_outcome_preservation
    return

label iraq_outcome_repatriated:
    scene Gate with fade
    gate "The parts of me which we're taken are returned home. Though I am not whole, I am among my people once more."
    window hide
    show I1V1 with fade
    pause
    scene black
    hide I1V1 with fade
    window show
    jump start
label iraq_outcome_repatriated2:
    scene Gate with fade
    gate "Although I am far from my homeland,  my people come to Germany to guide my conservation and presentation to the public."
    window hide
    show I1V2 with fade
    pause
    scene black
    hide I1V2 with fade
    window show
    jump start

label iraq_outcome_failed:
    scene Gate with fade
    gate "Still far from home, I wait. But the voices calling for my return grow stronger every year."
    window hide
    show I1V3 with fade
    pause
    scene black
    hide I1V3 with fade
    window show
    jump start

label iraq_outcome_preservation:
    scene Gate with fade
    gate "Though I remain distant, Iraq has rekindled Babylon's legacy through careful restoration of what remains."

    window hide
    show I1V4 with fade
    pause
    scene black
    hide I1V4 with fade
    window show
    jump start
