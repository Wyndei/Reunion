


label bad_ending_slip:

    scene black
    
    "And with that, you fade away from the lives of these people you once called friends. Maybe they'll miss you. Maybe they already do."

    python:
        ending_text = "Ending 1/4 - Fled"
    jump ending_display



label bad_ending_bathroom:
    scene black

    python:
        ending_text = "Ending 2/4 - Changed"
    jump ending_display
   




label bad_ending_apartment:
    
    play music "Reunion Party Theme (Reverse).ogg" fadeout 0.1 fadein 0.1
    scene apartment bad_end with dissolve


    pov "They aren't listening to me, they're whispering about me, they don't want me here. I shouldn't have come."
    pov "Am I even real?"
    pov "Am I even here?"
    pov "Is any of this real?"

    pov "I'll check my phone, that will prove I'm real."

    menu:
        "Check Your Phone":
            jump check_phone




label check_phone:
    

    scene apartment bad_blurred with dissolve
    show phone broken with moveinbottom

    pause 1.0

    "Are you okay?"
    pov "This is from Ravena. What is she talking about? I'm right here!"

    "Why haven't you picked up?"
    pov "I'm right…I…these aren't from today."
    pov "These aren't about the party. They're from five years ago."
    pov "I'm not real."
    pov "..."
    pov "I'm gone."



    python:
        ending_text = "Ending 3/4 - Gone"
    jump ending_display







label good_ending:
    


    jump cake_ending




label ending_display:
    scene black with dissolve

    

    centered "[ending_text]"


    return


