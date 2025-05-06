label ISHTARV1:
    scene babylon with fade
    narr "It is 1902. German archeologists, have begun excavating the ancient city of Babylon in Ottoman Iraq."
    narr "Soon, an extraordinary discovery emerges: fragments of a monumental gateway adorned with dragons and lions—the Ishtar Gate."
    narr "Koldewey proposes the gate be shipped to Berlin for reconstruction. Should the museum support the proposal?"
    menu:
        "Approve relocation to Berlin":
            jump approve_gate_transfer
        "Leave the gate.":
            jump leave_in_situ
    return

label approve_gate_transfer:
    scene Gmny with fade
    narr "With permission from Ottoman authorities and German funding, hundreds of crates begin their journey to Berlin."
    narr "The Pergamon Museum's team reconstructs the gate from the fragments—carefully, meticulously."
    narr "The result is a masterpiece of archaeological display. Crowds flock to see it. Berlin becomes a center of Near Eastern heritage."
    menu:
        "Publicize the reconstruction widely":
            jump public_acclaim
        "Keep a lower profile for now":
            jump quiet_acclaim

label public_acclaim:
    narr "The museum releases photos and articles; international journals laud the achievement. But whispers begin about imperial extraction."
    jump scrutiny_begins

label quiet_acclaim:
    narr "The museum limits publicity, but word of the gate still spreads. Scholars visit. Iraqis begin asking questions."
    jump scrutiny_begins

label scrutiny_begins:
    scene iraq with fade
    narr "In the 21st century, Iraq formally requests the return of the Ishtar Gate. The call is amplified by scholars and cultural officials."
    menu:
        "Defend the legality and preservation value of the acquisition":
            jump defend_berlin
        "Open dialogue with Iraq for co-stewardship or restitution":
            jump open_dialogue

label leave_in_situ:
    scene Gate with fade
    narr "The team documents the gate in detail, but does not remove it. Fragments remain in Babylon, exposed to time and conflict."
    narr "In the decades that follow, political turmoil hampers preservation. Yet Iraqis retain ownership of their cultural past."
    gate "Though battered, I stayed in my birthplace. My scars are real—but so is my story."
    window hide
    show I2V5 with fade
    pause
    scene black
    hide I2V5 with fade
    window show
    jump start

label defend_berlin:
    scene Gmny with fade
    narr "The Pergamon Museum cites the original permits from the Ottoman Empire, the careful reconstruction, and decades of preservation."
    $ germanPosition = random.randint(0, 5)
    if germanPosition >= 3:
        narr "Public opinion is divided. Some call for return, others praise the museum's stewardship."
        jump continue_debate
    else:
        narr "The museum's response is criticized as dismissive. Iraq renews its call for repatriation."
        jump increasing_pressure

label open_dialogue:
    scene babylon with fade
    narr "German officials meet with Iraqi cultural leaders. Multiple proposals are discussed—none simple, all politically sensitive."
    menu:

        "Propose a long-term loan of select fragments":
            jump loan_fragments
        "Return the gate in stages":
            jump partial_return


label loan_fragments:
    scene Gate with fade
    narr "Germany agrees to loan decorative elements to Iraq for long-term display and rotating exhibitions."
    gate "A compromise—but one that restores connection and story to my birthplace."
    
    window hide
    show I2V1 with fade
    pause
    scene black
    hide I2V1 with fade
    window show
    jump start


label partial_return:
    scene Gate with fade
    narr "In a historic agreement, Germany returns key fragments and begins training Iraqi conservators."
    gate "Piece by piece, I return to the cradle of my creation—carried not by conquest, but collaboration."
    window hide
    show I2V2 with fade
    pause
    scene black
    hide I2V2 with fade
    window show
    jump start

label continue_debate:
    scene Gate with fade
    narr "The museum maintains possession, citing its responsibility to global audiences and the fragility of the structure."
    gate "Behind glass, I speak to millions—but not in the language of my land."
    window hide
    show I2V3 with fade
    pause
    scene black
    hide I2V3 with fade
    window show
    jump start

label increasing_pressure:
    narr "Iraqi officials bring the issue to UNESCO. Protests and op-eds raise the stakes. Germany must decide again."
    menu:
        "Reopen negotiations":
            jump open_dialogue
        "Double down on defense":
            scene Gate with fade
            narr "Germany reasserts its claims. The gate remains, but criticism grows. The story is far from over."
            gate "Once again, my fate lies not in stone—but in memory and debate."
            window hide
            show I2V4 with fade
            pause
            scene black
            hide I2V4 with fade
            window show
            jump start
    return

# label germany_intro:
#     gate "In 1902, I was exhumed from the earth by Koldewey’s expedition—fragment by fragment, packed and shipped far from my cradle."
#     gate "In Berlin, I was reborn, assembled into a monument of archaeological triumph."
#     menu:
#         "Defend the gate’s preservation in Berlin.":
#             jump germany_defend
#         "Explore cooperative stewardship with Iraq.":
#             jump germany_co_steward
#     return

# label germany_defend:
#     scene bg pergamon with fade
#     gate "Germany asserts that I was rescued from oblivion, reconstructed with care, and protected in a world-class museum."
#     jump germany_outcome_defend
#     return

# label germany_co_steward:
#     scene bg berlin_meeting with fade
#     gate "German officials propose a partnership: co-curation, loans, or virtual repatriation."
#     jump germany_outcome_shared
#     return

# label germany_outcome_defend:
#     gate "I remain in Berlin—safe, restored, admired—but shadowed by calls of injustice from afar."
#     jump start

# label germany_outcome_shared:
#     gate "Though I have not left Berlin, my story now includes Iraq’s voice, and my guardianship is shared."
#     jump start
