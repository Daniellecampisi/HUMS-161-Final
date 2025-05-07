label German_Culture_Bust:
    scene Bust_NEF with fade    
    narr "You have selected to play as Germany during the early 20th century."
    narr "In 1912, a German archaeological team begins excavations at Tell el-Amarna, funded by the German Oriental Company."
    narr "On December 6, 1912, the team, led by Ludwig Borchardt, makes a remarkable discovery..."
    bust "I was unearthed in Thutmose’s workshop, still bearing the vibrant colors of ancient Egypt."
    bust "My discovery was seen as an artistic marvel, and Borchardt knew the value I held."
    narr "The archaeological team wants to keep the bust in their archives. What should be done?"
    menu:
        "Accurately report the bust’s significance to the Egyptian Antiquities Authority.":
            jump Honest_Declaration
        "Downplay the bust’s importance to secure it for Germany.":
            jump Deceptive_Declaration

label Honest_Declaration:
    scene city with fade
    narr "Borchardt presents the bust truthfully, identifying it as a limestone portrait of Queen Nefertiti."
    $chance_moved = random.randint(0,5)
    if chance_moved > 2:
        narr "The Egyptian Antiquities Authority, recognizing its significance, retains the bust for Egypt."
        jump Egypt_Autonomy_Ending
    else:
        narr "Due to bureaucratic oversight and undervaluation, the Egyptian Antiquities Authority still allows the bust to be included in Germany’s share."
        jump Bust_Sent_to_Germany

label Deceptive_Declaration:
    scene city with fade
    narr "Borchardt describes the bust as a 'painted plaster bust of a princess.'"
    narr "He shows an unflattering photo and leaves it concealed in a dimly lit room during the inspection."
    
    menu:
        "Proceed with the misleading presentation.":
            jump Misrepresentation_Succeeds
        "Reconsider and offer a partial truth about the bust’s value.":
            jump Honest_Declaration

label Misrepresentation_Succeeds:
    $chance_moved = random.randint(0,10)
    if chance_moved > 3:
        narr "The deception is successful. Egyptian officials do not recognize the bust’s true worth."
        jump Bust_Sent_to_Germany
    else:
        narr "The Egyptian Antiquities Authority grows suspicious and investigates further."
        narr "He realizes the bust's importance and claims it for Egypt."
        jump Egypt_Autonomy_Ending

label Bust_Sent_to_Germany:
    scene german_museum with fade
    bust "I was quietly shipped to Germany in 1913, my value unnoticed by the Egyptian officials."
    narr "Years later, in 1924, I was displayed in Berlin to public acclaim."
    narr "Egypt, realizing the mistake, began a campaign for my return."
    
    menu:
        "Cooperate with Egyptian diplomatic efforts for return.":
            jump German_Concedes
        "Refuse all claims and assert German ownership.":
            jump Germany_Refuses_Return

label German_Concedes:
    $chance_moved = random.randint(0,5)
    if chance_moved < 3:
        narr "Germany agrees to a cultural cooperation agreement and returns the bust."
        jump Egypt_Autonomy_Ending
    else:
        narr "Negotiations break down due to political tensions and the bust remains in Germany."
        jump Germany_Refuses_Return

label Germany_Refuses_Return:
    #show bust 
    scene german_museum with fade    
    bust "I remain in the Neues Museum, a centerpiece of Berlin’s collection, but also a symbol of colonial extraction."
    narr "The debate over my rightful home continues in courts and public forums."
    
    menu:
        "Offer a rotating loan agreement to Egypt.":
            jump outcome2V1EGYPT
        "Maintain exclusive ownership.":
            jump Germany_Final_Ownership

label Germany_Final_Ownership:
    scene Bust_NEF with fade    
    bust "Germany continues to deny repatriation claims. Despite international pressure, I remain here."
    bust "Yet I hear my people’s voices echo through halls far from their homeland."

        
    window hide
    show Germanend with fade
    pause
    scene black
    hide Germanend with fade
    window show
    jump start
    return


label outcome2V1EGYPT:
    scene Bust_NEF with fade    
    bust "I remain in the hands of outsiders, protected from poor conditions, but still far from my home."
    bust "My people help guide my conservation and presentation to the public in my new home."

    window hide
    show Copat with fade
    pause
    scene black
    hide Copat with fade
    window show

    jump start
    return