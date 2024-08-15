



label Bathroom_Start:
    pass


label Bathroom_Transition:
    scene bathroom_bg normal with fade
    play music ["Reunion Party Theme (Muffled).ogg","Reunion Party Theme.ogg"] fadeout 0.1 fadein 0.1

    pause 0.25
    play sound "door_close_left.ogg"

    jump Bathroom_Scene


label Bathroom_Scene:


    jump bathroom_choice





label bathroom_choice:

    "What should I do?"

    menu:
        
        "Stay in bathroom":
            jump stay_in_bathroom

        "Look around":
            jump Bathroom_Look_Around

        "Return to party":
            jump Room_Transition
        
        
        



label Bathroom_Look_Around:
    call screen Bathroom_Look_Around_Screen




label stay_in_bathroom:

    python:
        bad_points += 1


    if bad_points == 1:
        pov "Maybe I'll stay in here for a bit."
    elif bad_points == 2:
        pov "..."
    elif bad_points == 3:
        pov "coming here was a mistake."
    elif bad_points == 4:
        pov "I'll just stay here until it's dark, they'll forget about me, and I can sneak out."
    elif bad_points >= 5:

        play music "Reunion Party Theme (Reverse).ogg" fadeout 0.1 fadein 0.1

        scene bathroom_bg bad_end with dissolve
        pov "It's so cold. Why is everything in here so dark? Why is it so quiet..."

        

        call screen Bathroom_Bad_End_Look_Around_Screen

    

    jump bathroom_choice




label Bathroom_Continue_Looking:
    "Continue looking?"
    menu:
        "Keep looking":
            call screen Bathroom_Look_Around_Screen
            jump bathroom_choice
        "Stop looking":
            jump bathroom_choice


screen Bathroom_Look_Around_Screen:

    #from left to right

    #toothbrush
    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 0.225
        ypos 0.7

        idle "box ii"
        hover "box ii"

        hovered Jump("toothbrush")
        unhovered Jump("bathroom_reset_bg")


        action Jump("toothbrush_inspect")

    
    #sink_plant
    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 0.15
        ypos 0.8

        idle "box i"
        hover "box i"

        hovered Jump("sink_plant")
        unhovered Jump("bathroom_reset_bg")


        action Jump("sink_plant_inspect")



label toothbrush:
    scene bathroom_focus toothbrush
    call screen Bathroom_Look_Around_Screen
label sink_plant:
    scene bathroom_focus plant
    call screen Bathroom_Look_Around_Screen

label bathroom_reset_bg:
    scene bathroom_bg normal
    pause 0.01
    call screen Bathroom_Look_Around_Screen

label toothbrush_inspect:

    play sound "ting.ogg"

    pov "This is a toothbrush."
    pov "Unlike the plant, this is rather thematic for a bathroom."
    scene bathroom_bg normal
    jump Bathroom_Continue_Looking

label sink_plant_inspect:

    play sound "ting.ogg"

    pov "This is a plant... in the bathroom."
    pov "Why does Ravena have a plant in the bathroom?"
    scene bathroom_bg normal
    jump Bathroom_Continue_Looking




screen Bathroom_Bad_End_Look_Around_Screen:

    #mirror
    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 0.465
        ypos 0.25

        idle "box iv"
        hover "box iv"

        hovered Jump("bad_mirror")
        unhovered Jump("bad_bathroom_reset_bg")


        action Jump("bad_mirror_inspect")



label bad_bathroom_reset_bg:
    scene bathroom_bg bad_end
    pause 0.01
    call screen Bathroom_Bad_End_Look_Around_Screen


label bad_mirror:
    scene bathroom_focus bad_mirror
    call screen Bathroom_Bad_End_Look_Around_Screen

label bad_mirror_inspect:
    scene bathroom_bg bad_end
    jump bathroom_ghost
    




label bathroom_ghost:

    scene bathroom_bg ghost with dissolve

    pov "I know what's wrong. They haven't changed."
    pov "I did."

    
    
    jump bad_ending_bathroom



