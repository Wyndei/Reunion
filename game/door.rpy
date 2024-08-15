


define ravena = Character("Ravena", image = "ravena")

define aubrey = Character("Aubrey", image = "aubrey_necklace")

define yokari = Character("Yokari", image = "yokari")

define theo = Character("Theo", image = "theo")


image aubrey neutral = "images/Character Sprites/Aubrey/" + "[aubrey_sprite]" + " " + "neutral.png" 
image aubrey happy = "images/Character Sprites/Aubrey/" + "[aubrey_sprite]" + " " + "happy.png" 
image aubrey nervous = "images/Character Sprites/Aubrey/" + "[aubrey_sprite]" + " " + "nervous.png" 
image aubrey sad = "images/Character Sprites/Aubrey/" + "[aubrey_sprite]" + " " + "sad.png" 



label Door_Scene:

    play music ["Reunion Party Theme (Muffled).ogg"] fadeout 0.1 fadein 0.1

    scene door_bg normal




    pov "It's been a long time, maybe years. I wonder if they'll even remember me fully."
    pov "I mean, I haven't changed up my look all that much, and I even have the same phone... "
    pov "Just... take a deep breath, okay? It'll be fine. It's always been fine."


    show yokari neutral at left with dissolve
    show theo phone at center with dissolve
    show aubrey nervous at right with dissolve
    

    pov "That's Yokari on the left, Aubrey on the right, and Theo in the middle." 
    pov "They seem a little somber but I'm sure things'll warm up once we're sitting down."




    if major == "Art History":
        pov "I wonder if the apartment has enough room for all of us? What sort of place has Ravena gotten her hands on?"


    elif major == "Psychology":
        pov "I think Yokari flashed me a grin, but I don't want to be too friendly since it's been so long."
        pov "I'll let him make the first move once we get inside"


    elif major == "Music Theory":
        pov "I can't wait to get inside and chat with Aubrey, but I shouldn't come on too strong." 
        pov " Who knows if they've gotten any more confident since college?"


    elif major == "Computer Science":
        pov "Theo seems the same as ever, just vibing. I'll have to prod him once we're inside."
    


    scene black with fade
    

    play sound "Door Bell Low.mp3"
    
    pause 1.0

    
    scene door_bg normal with fade


    show ravena happy at center
   
    

    ravena "Hey guys, it's great that you could all make it after all this time!"
    ravena "Well, don't wait out here, come on in!"


    menu:
        "Go on in":
            
            jump enter_apartment
        "Slip away":
            jump slip_away





label enter_apartment:
    pov "No time like the present! Let's get this party started!"

    
    jump Room_Scene_Start


label slip_away:

    play music "Reunion Party Theme (Reverse).ogg" fadeout 0.1 fadein 0.1
    scene door_bg bad_end with dissolve

    

    pov "... It's for the best that I don't waste their time"
    pov "I was never really close with these people anyway."
    
    jump bad_ending_slip
