# Alternate US-side intro
init python:
    import random

label METV1:
    narr "It is 1972. The Metropolitan Museum of Art is eager to expand its collection of ancient masterpieces."
    narr "A renowned dealer offers the museum an extraordinary Greek vase: the Euphronios Krater, signed by both potter and painter, depicting the death of Sarpedon."
    narr "Should you acquire the object?"
    menu:
        "Proceed with acquisition":
            jump acquired_krater
        "Investigate the object's provenance":
            jump investigate_provenance
    return

label acquired_krater:
    narr "The Board of Trustees debates the risks and rewards. The curator extols the krater's beauty and historical importance, envisioning it as the crown jewel of the Greek galleries."
    narr "The deal is made. The krater is unveiled to great acclaim, drawing crowds and rewriting the narrative of ancient art in America."
    narr "Should the acquisition be publicized to attract media attention?"
    menu:
        "Publicize the acquisition.":
            narr "Articles circulate surrounding the new acquisition: the press praises the museum’s boldness, but not everyone is convinced."
            jump publish
        "Do not publish anything.":
            jump publish

label publish:
    narr "Despite the decision, rumors emerge: the krater may have been looted from an Italian tomb. Journalists and foreign officials demand answers."
    menu:
        "Defend the acquisition and provenance":
            jump defend_provenance
        "Open an internal investigation":
            jump investigate_provenance

label defend_provenance:
    narr "The museum stands by its documentation, citing affidavits and expert opinions."
    $ DP = random.randint(0, 5)
    if DP > 3:
        narr "Yet, the controversy grows, and Italy intensifies its calls for repatriation."
    else:
        narr "The press calms down with the new evidence; however, Italy is still requesting repatriation."
    menu:
        "Negotiate with Italy":
            jump negotiate_return
        "Refuse all demands":
            jump refuse_return

label investigate_provenance:
    narr "An internal review reveals inconsistencies in the krater's paperwork. The museum faces a dilemma: risk scandal or pursue restitution."
    menu:
        "Enter negotiations for return":
            jump negotiate_return
        "Delay and hope the controversy fades":
            $ DP = random.randint(0, 3)
            if DP >= 2:
                jump refuse_return
            else:
                jump public_pressure

label negotiate_return:
    narr "A few options for repatriation come up. Which one should be selected?"
    menu:
        "A co-stewardship model.":
            narr "Italy agrees on a co-stewardship model, allowing the museum to retain the object while still respecting its origin."
            krater "I remain far from my homeland, but still under the influence of my people."

        "Complete return of the object.":
            narr "After lengthy talks, the museum reaches an agreement with Italy. The krater will remain on view for a final exhibition before its return."
            narr "In exchange, Italy promises future loans of other masterpieces. The museum preserves its reputation, but loses a treasure."
            krater "After years abroad, I was finally returned to Italy, welcomed with reverence and sorrow for the journey I endured."
    return

label refuse_return:
    narr "The museum refuses to return the Krater, citing good faith acquisition. Legal and diplomatic pressures mount. The krater becomes a symbol of contested heritage."
    krater "Throughout time, I was kept behind glass, far from the soil where I once belonged."
    return

label public_pressure:
    narr "Media scrutiny and international criticism intensify. The museum's image suffers. Ultimately, negotiations begin, but under less favorable terms."
    narr "After lengthy talks, the museum reaches an agreement with Italy. The krater will remain on view for a final exhibition before its return."
    narr "In exchange, Italy promises future loans of other masterpieces. The museum preserves its reputation, but loses a treasure."
    krater "After years abroad, I was finally returned to Italy, welcomed with reverence and sorrow for the journey I endured."
    return
