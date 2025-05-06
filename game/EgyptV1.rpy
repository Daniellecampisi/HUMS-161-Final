init python:
    import random

define chance_moved = 0

label EgyptV1_Intro:
    scene Bust_NEF with fade
    narr "You have selected the Bust of Nefertiti as your object. Which side would you like to play as?"
    menu: 
        "Egypt":
            jump Creation_of_Bust
        "Germany":
            jump German_Culture_Bust
        # "England"
    return

label Creation_of_Bust:
    # ART TODO city of Akhetaten
    scene city with fade
    bust "I was born in 1340 B.C crafted by the royal court sculptor Thutmose in the ancient Egyptian city of Akhetaten."
    bust "Made from limestone covered with stucco and painted in vibrant colors, my muse is Queen Nefertiti, the Great Royal Wife of Akhenaten."
    bust "I adorn her distinctive blue crown and intrictae neck piece. I was used as a sculptor’s model and a reference for other portraits of the queen."
    bust "Near the time of my making, Pharaoh Akhenaten introduced the monotheistic worship of the sun disc Aten to the city of Akhetaten."
   
    #tutmose image TODO ART
    scene sculptor_head with fade

    bust "I was held for many years in Thutmose’s workshop in Amarna, along with other models and unfinished sculptures of the royal family."
    narr "The city is a vibrant yet contested place. What should be done?"
    menu:
        "Move the bust to alternate storage.":
            jump Attempt2moveBust
        "Leave the bust in the city.":
            jump Abandonment_Akhetaten

label Attempt2moveBust:
    $chance_moved = random.randint(0,5)
    if(chance_moved == 1):
        scene city with fade
        narr "The Bust was succesfully moved to another part of the city."
        narr "Due to its relocation, the Bust survived many centuries more burried under ancient sand."
        jump Egypt_Autonomy_Ending
    else:
        narr "Thutmose had no incentive to move the bust and continued to use it for his works."
        narr "The Bust was unsuccessfully moved to another part of the city and remained in Thutmose’s workshop in Amarna"
        jump Abandonment_Akhetaten




label Abandonment_Akhetaten:
    scene city with fade
    narr "Pharaoh Akhenaten has passed away."
    narr "There is a rise of support for polytheistic religion and his successors hope to restore the historic beliefs of Egypt."
    narr "The city of Akhenaten may fall as a result."
    narr "What should be done?"

    menu:
        "Restore polytheistic religion in the empire.":
            jump ANTIQUTIE_LAW
        "Maintain the monotheism established under Pharaoh Akhenaten.":
            jump Attempt_to_Save_Akhetaten


label Attempt_to_Save_Akhetaten:
    $chance_moved = random.randint(0,5)
    if(chance_moved > 2): 
        scene pharoh with fade
        narr "His successors have quickly restored the old polytheistic religion centered on Amun and moved the capital back to Thebes."
        narr "The worship of Aten was abandoned, and Akhetaten lost its religious and political significance"
        narr "Following the decline of Akhenaten’s reign and the abandonment of Amarna, the bust remained buried and forgotten in the ruins of Thutmose’s workshop for over 3,200 years."
        jump ANTIQUTIE_LAW
    else:
        scene pharoh with fade
        narr "The attempt to save Akhenaten succeeded!"
        narr "The empire maintains the religion from under Akhenaten's rule and the city of Akhenaten remains strong."
        jump Egypt_Autonomy_Ending

label ANTIQUTIE_LAW:
    scene city with fade
    narr "It is now the advent of the 20th century. The bust has stayed burried for many centuries."
    narr "Egypt is in contention over a new law to be passed."
    narr "The Antiquities Law of 1912 plans to permit foreign missions to conduct scientific excavations in exchange for a system called \"partage.\""
    narr "Partrage would let all artifacts of cultural significance to stay in Egypt while allowing Europeans to excavate and explore Egypt's archient ruins."
    narr "What should be done?"

    menu: 
        "Pass the Antiquities Law of 1912.":
            jump Discoved_Bust_German
        "Reject the Antiquities Law of 1912.":
            $chance_moved = random.randint(0,10)
            if(chance_moved < 4):
                narr "The rejection of the law succeeds!"
                jump Egypt_Autonomy_Ending
            elif (chance_moved < 7):
                narr "The rejection of the law succeeds!"
                jump ArtifactLostBust
            else:
                narr "The rejection of the law fails due to British influence in the Egyptian governent."
                narr "Europeans begin to excavate Egypt's ruins."
                jump Discoved_Bust_German




label Discoved_Bust_German:
    scene city with fade
    bust "I was discovered by a German archaeological team led during an excavation at Tell el-Amarna, funded by the German Oriental Society."
    bust "I was found in Thutmose’s workshop, alongside other royal sculptures."
    narr "In the division of finds (partage) between Egypt and Germany, the bust was allocated to the German share."
    narr "What should Egyptian officials do in this situation?"

    menu:
        "Investigate the artifact.":
            $chance_moved = random.randint(0,10)
            if(chance_moved > 6):
                narr "The investigation of the artifact suceeds and Egypt keeps the bust!"

                jump Egypt_Autonomy_Ending
            else: 
                narr "The investigation of the artifact suceeds and Egypt keeps the bust!"
                narr "Preservation efforts have been attempted but are not sucessful."
                jump Egypt_Miscare_Ending
        "Allow German Aquisition":
            jump InGermayBust


label InGermayBust:
    scene german_museum with fade

    bust "I was first publicly displayed in Berlin in 1924 and has since become one of the most iconic artifacts of ancient Egypt."
    bust "It am currently housed in the Neues Museum, Berlin, and remain at the center of a longstanding dispute between Egypt and Germany over where my home should be."
    $chance_moved = random.randint(0,5)
    narr "Should Egypt attemt to negotiate with Germany?"
    menu:
        "Negotiate":
            if(chance_moved > 3):
                jump conservation_not_sucess_bust
            else:
                bust "Here I remain, a silent witness to the passing of years, watching as my people's voices rise in hope and sorrow—calling for my return, while those who hold me show little urgency to let me go."
        "Leave the bust in Germany":
                bust "Here I remain, a silent witness to the passing of years, watching as my people's voices rise in hope and sorrow—calling for my return, while those who hold me show little urgency to let me go."

label conservation_not_sucess_bust:
    narr "How should Egypt attempt to regain ownership of the bust?"
    menu:
        "A long-term loan of the crown to another musuem.":
            jump outcome2V1EGYPT
        "A co-stewardship model with Egyptian representatives and another museum.":
            jump outcome3BUST 


# ENDING ONE 
label ArtifactLostBust:
    scene Bust_NEF with fade
    
    bust "Here I lay, burried under the sands of my people. My people are left unware of my presence and my history."
    bust "As I lie here for centuries to come, I can only hope that one day I will be discovered."

    window hide
    show ArtifactLost with fade
    pause
    scene black
    hide ArtifactLost with fade
    window show

    jump start
    return

#ENDING TWO 
label Egypt_Autonomy_Ending:
    scene Bust_NEF with fade
    # change the background TODO to object 
    bust "I remain in my homeland, with my people. They expanded conservation efforts to protect me, as I bask in our country's greatness."
   
    window hide
    show AutonomyEnd with fade
    pause
    scene black
    hide AutonomyEnd with fade
    window show

    jump start
    return

#ENDING THREE
label Egypt_Miscare_Ending:
    scene Bust_NEF with fade
    # change the background TODO to object 

    bust "I remain in my homeland, with my people. Despite our closeness my time is fading as I slowly decay from inadequate care."
    window hide
    show Miscare with fade
    pause
    scene black
    hide Miscare with fade
    window show
    jump start
    return
# ENDING FOUR
label outcome3BUST:
    scene Bust_NEF with fade    
    # change the background TODO to object 

    bust "I was transfered to a museum in Germany, watching my people negociate my stewardship and protect my longjevity."
    bust "Although I am far from my homeland, some of my people come to Germany to guide my conservation and presentation to the public."
   
    window hide
    show O3E with fade
    pause
    scene black
    hide O3E with fade
    window show
    jump start
    return
