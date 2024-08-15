



label cake_ending:


    show ravena happy at center with dissolve

    ravena "Alright everyone, there's one last thing to take care of tonight."

    hide ravena with dissolve

    pov "they're gathering in the kitchen. I should probably follow."


    stop music fadeout 1.0

    scene black with dissolve


    ravena "It's time"
    "..."


    scene cake_bg lit with dissolve

    
    ravena "Happy birthday, [pov]! It's been five years since you left us."
    yokari "You're gone."
    aubrey "But you aren't really gone."
    theo "You're still with us."
    ravena "In our minds..."
    yokari "In our hearts..."
    aubrey "In all the little things that you left behind..."
    theo "And in today."
    ravena "You were patient and kind. You taught me to stand up for myself."
    yokari "You were chill. You taught me to slow down and enjoy life."
    aubrey "You were confident. You taught me to be brave and put myself out there."
    theo "You were modest. You taught me how to show others grace."

    if major == "Art History":
        ravena "So, for all the gifts that you've given us, here's one more..."

    elif major == "Psychology":
        yokari "So, for all the gifts that you've given us, here's one more..."

    elif major == "Music Theory":
        aubrey "So, for all the gifts that you've given us, here's one more..." 
        
    elif major == "Computer Science":
        theo "So, for all the gifts that you've given us, here's one more..."


    define all_characters = Character("All")

    all_characters "Happy Birthday!"


    pov "thats right...."
    pov "I died... but even still..."
    pov "I am remembered"


    scene cake_bg blown with dissolve



    play music "Reunion Credits Theme.ogg" noloop




    python:
        ending_text = "Ending 4/4 - Stayed"

    pause 3.0


    show screen end_screen_timer("cake_ending_display")


    centered "[ending_text]"

    jump cake_ending_display
    
    

screen end_screen_timer(jumpto):
    timer 62.0 action Jump(jumpto)


label cake_ending_display:
    scene black with dissolve


    stop music fadeout 3.0
    pause 3.0

    return
