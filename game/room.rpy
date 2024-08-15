




define ListenedToRavenaYokari = False
define ListenedToAubreyTheo = False
define assignments_inspected = False
define picture_inspected = False


label Room_Scene_Start:
    
    
    

   


    #show screen Room_Look_Around_Screen

    play music ["Reunion Party Theme.ogg"] fadeout 0.1 fadein 0.1

    scene apartment normal with fade


    play sound "door_close.ogg"
    



    pov "(Wow, this is cozy!)"
    pov "(Not a lot of party decorations though…what sort of decorations would even be appropriate?)"

    pov "Well, we're here. Ravena seems to have a few more tattoos than I remember.."
    pov "Yokari started wearing button ups -"
    pov "Aubrey's sweater seems comfy."
    pov "... and Theo has the same old hoodie on... At least some things say the same."



    if major == "Art History":
        pov "On top of all that, Ravena seems an awful lot more confident."
        pov "Doubt that I'll have to walk on eggshells around her any more... not that I ever minded, of course!"


    elif major == "Psychology":
        pov "Besides all that, Yokari seems to have really taken a load off."
        pov "I don't think I've ever seen him without bags under his eyes before now!"


    elif major == "Music Theory":
        pov "Aubrey's somehow even more closed off than I recalled."
        pov "I hope the others give them enough space during the party."


    elif major == "Computer Science":
        pov "Theo especially seems to have perked up. I wonder where that confidence came from?"
    


    jump Room_Scene_Roam




label Room_Transition:
    scene apartment normal with fade
    play music ["Reunion Party Theme.ogg"] fadeout 0.1 fadein 0.1

    pause 0.25
    play sound "door_close_right.ogg"


    jump Room_Scene_Roam



label Room_Scene_Roam:
    
    if good_points >= 5:
        jump good_ending


    if bad_points >= 5:
        jump bad_ending_apartment

    
    if ListenedToRavenaYokari and ListenedToAubreyTheo and ListenedToAubreyTheo and picture_inspected and not good_point >= 5:
        jump bad_ending_apartment



    "What should I do?"

    menu:
        "Listen in on conversations" if not ListenedToRavenaYokari or not ListenedToAubreyTheo:
            jump Listen_In

        "Look around":
            jump Room_Look_Around
        
        "Go to the bathroom":
            jump Bathroom_Transition




label Room_Look_Around:
    call screen Room_Look_Around_Screen
    
    

label continue_looking:
    "Continue looking?"
    menu:
        "Keep looking":
            call screen Room_Look_Around_Screen
            jump Room_Scene_Roam
        "Stop looking":
            jump Room_Scene_Roam




screen Room_Look_Around_Screen:

    #from left to right

    #frames
    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 0.075
        ypos 0.325

        idle "box ii"
        hover "box ii"

        hovered Jump("picture_frames")
        unhovered Jump("reset_bg")


        action Jump("frame_inspect")


    #plants_bot
    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 0.235
        ypos 0.75

        idle "box i"
        hover "box i"

        hovered Jump("plants_bot")
        unhovered Jump("reset_bg")


        action Jump("plants_bot_inspect")
    

    #picture
    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 0.25
        ypos 0.55

        idle "box i"
        hover "box i"

        hovered Jump("picture")
        unhovered Jump("reset_bg")


        action Jump("picture_inspect")
    

    #assignments
    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 0.225
        ypos 0.25

        idle "box ii"
        hover "box ii"

        hovered Jump("assignments")
        unhovered Jump("reset_bg")


        action Jump("assignments_inspect")


    #matcha
    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 0.325
        ypos 0.25

        idle "box i"
        hover "box i"

        hovered Jump("matcha")
        unhovered Jump("reset_bg")


        action Jump("matcha_inspect")

    #plants_top
    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 0.25
        ypos 0.05

        idle "box iii"
        hover "box iii"

        hovered Jump("plants_top")
        unhovered Jump("reset_bg")


        action Jump("plants_top_inspect")



label picture_frames:
    scene room_focus frames
    call screen Room_Look_Around_Screen

label plants_bot:
    scene room_focus plants_lower
    call screen Room_Look_Around_Screen

label picture:
    scene room_focus picture
    call screen Room_Look_Around_Screen

label assignments:
    scene room_focus assignments
    call screen Room_Look_Around_Screen

label matcha:
    scene room_focus matcha
    call screen Room_Look_Around_Screen

label plants_top:
    scene room_focus plants_higher
    call screen Room_Look_Around_Screen

label reset_bg:
    scene apartment normal
    pause 0.01
    call screen Room_Look_Around_Screen





label frame_inspect:

    play sound "ting.ogg"

    pov "Some of Ravena's old oil paintings from college.  She always preferred watercolors though..."

    scene apartment normal
    jump continue_looking


label plants_bot_inspect:

    play sound "ting.ogg"

    pov "Ravena always had a green thumb."
    scene apartment normal
    jump continue_looking

label matcha_inspect:

    play sound "ting.ogg"

    pov "This is a cute cat plushie! She looks like she could run a cafe."
    scene apartment normal
    jump continue_looking


label plants_top_inspect:

    play sound "ting.ogg"

    pov "Ravena always had a green thumb."
    scene apartment normal
    jump continue_looking





label picture_inspect:
    
    play sound "ting.ogg"

    if not picture_inspected:
        pov "Hey, that's a picture of us! We'd just graduated, I remember how exciting it was."
        
        menu:
            "Why am I not in it?":
                python:
                    bad_points += 1
                
                "Were we really even friends? Was I really even there?"

            "I was always quite handy with a camera":
                python:
                    good_points += 1

                pov "Shame we couldn't get another one with me in it. Still, it's a beautiful memory."
    else:
        pov "That's a picture of us when we'd just graduated."


    python:
        picture_inspected = True
    scene apartment normal
    jump continue_looking



label assignments_inspect:
    
    play sound "ting.ogg"
    
    if major == "Art History":
        if not assignments_inspected:

            pov "This is an old art history assignment! I can't believe Ravena held onto it for so long."
        
            menu:
                "That's actually kind of sweet":
                    python:
                        good_points +=1

                    pov "I mean, we did it together. She was struggling with the research half."
                    pov "I couldn't spell check properly, but we managed it together."

                "That doesn't make sense":
                    python:
                        bad_points +=1

                    pov "Why would someone hold onto that sort of thing? It's just paper and ink. What a waste of space."
        
        else:
            "This is an old art history assignment! I can't believe Ravena held onto it for so long."

    elif major == "Psychology":
        if not assignments_inspected:

            pov "This is a psych paper Yokari and I worked on together. I wonder how it ended up here?"

            menu:
                "He probably studied with Ravena":
                    python:
                        bad_points +=1
                    pov "She was just as hard a worker as he was."
                    pov "It could have gotten mixed in with her stuff at any point."

                "This can't be right":
                    python:
                        good_points +=1
                    pov "Yokari would never have misplaced something like this."
                    pov "There must be something wrong here."

        else:
            pov "This is a psych paper Yokari and I worked on together. I wonder how it ended up here?"
            
    elif major == "Music Theory":
        if not assignments_inspected:

            pov "Aubrey's end-of-term speech? Did Ravena really like it that much?"

            menu:
                "It really was inspiring":
                    python:
                        good_points +=1
                    pov "They spent the whole week bouncing ideas off of me. I hardly needed to give them feedback, either."
                    pov "It was the most confident they'd ever been."


                "It was embarrassing":
                    python:
                        bad_points +=1
                    pov "I barely even remember what was in it. Probably just a bunch of niceties, kid stuff."
        else:
            "Aubrey's end-of-term speech. I guess Ravena really liked it."

    elif major == "Computer Science":
        if not assignments_inspected:

            pov "Ew, handwritten code. Theo must have accidentally left it with Ravena's stuff a while back."

            menu:
                "Oh well":
                    python:
                        bad_points +=1

                    pov "What does it matter? We had tons of homework, this isn't special."
                

                "Hey I remember this!":
                    python:
                        good_points +=1

                    pov "The power was out in our dorm and we still had to get our homework done!"
                    pov "It was so bizarre, flipping through a textbook and drawing things out manually."
                    pov "He really worked hard that night."
        
        else:
            pov "handwritten code. Theo must have accidentally left it with Ravena's stuff a while back"


    python:
        assignments_inspected = True
    scene apartment normal
    jump continue_looking






label Listen_In:
    
    if bad_points >= 5:
        jump Room_Scene_Roam


    if ListenedToRavenaYokari and ListenedToAubreyTheo:
        jump Room_Scene_Roam


    "Who should I listen to?"

    menu:
        "Listen to Ravena and Yokari" if not ListenedToRavenaYokari:
            python:
                ListenedToRavenaYokari = True
            jump Ravena_Yokari

        "Listen to Aubrey and Theo" if not ListenedToAubreyTheo:
            python:
                ListenedToAubreyTheo = True
            jump Aubrey_Theo
        
        "Go back":
            jump Room_Scene_Roam





label Ravena_Yokari:


    "Ravena and Yokari are standing by the window, listening to the rain."


    show ravena tired at left with dissolve
    "Ravena has a half sleeve of flower tattoos, she's dyed her hair, and has a few more piercings. That's new."
    show yokari neutral at right with dissolve
    "Yokari seems more comfortable than I remember. I wonder what happened to mister argumentative?"

    
    ravena neutral "So... how's it been? Are you comfy?"

    

    yokari happy "Same as always, except for all the ways it isn't. I like the fairy lights. Your decorations are... uh... sparse"
    
    show yokari neutral
    ravena happy "What can I say? I've been less worried about keeping up appearances"
    

    show ravena neutral
    yokari happy "Rightly so. You do a good job on your own"

    show yokari neutral
    ravena happy "Yeah. It's nice to have people over anyway"

    pov "(Is it nice? Why hasn't she had more people over? Wasn't she shy?)"


    menu:
        "She's been missing us":
            python:
                good_points +=1
            pov "It's been a long time, it's been too long. Grad studies, apartment ownership."
            pov "who knows what else? She's been going through that without company or help."

        "She has better things to do":
            python:
                bad_points += 1
            pov "She always kept to herself, this party is just a time killer. We'll hang out for however long, then get back to our lives."


    show ravena neutral
    yokari happy "Have you been keeping busy?"
    show yokari neutral
    ravena tired "Grad studies never end, and I've had a little extra time to do watercolors. I can't complain. What about you?"

    show ravena neutral
    yokari happy "I've been drowning in work at the florist. Just trying to keep busy since..."
  
    yokari sad "hmm."

    show yokari happy
    ravena tired "It's fine. We're all thinking about it"
  
    yokari "..."


    pov "What are they worrying about? Is there some secret I'm being left out of?"

    menu:
        "There's a good explanation, I'm sure of it.":
            pov "Whatever seems to be the problem, they just need time. I'm sure they'll explain things as soon as they feel ready to"
            python:
                good_points +=1
            
        "This doesn't make sense. They're hiding something":
            python:
                bad_points +=1
            pov "I don't know what changed, but I don't think we're really friends anymore. Maybe I'm not wanted here."


        "Ravena is loyal. That won't have changed." if major == "Art History":
            python:
                good_points +=1
            pov "Whatever seems to be the problem, they just need time. I'm sure they'll explain things as soon as they feel ready to"
            
        

        "Yokari is stubborn, but he's kind. There's a reason for this." if major == "Psychology":
            python:
                good_points +=1
            pov "Whatever seems to be the problem, they just need time. I'm sure they'll explain things as soon as they feel ready to"
                            


    
    hide ravena with dissolve
    hide yokari with dissolve
    


    jump Listen_In

            


label Aubrey_Theo:

    show aubrey nervous at left with dissolve
    

    "Aubrey and Theo are hovering by the bookshelf, speaking quietly to one another."
    

    pov "Aubrey seems a little withdrawn. I thought their confidence had been growing by graduation, I wonder what changed?"
    
    show theo phone at right with dissolve
    pov "Theo isn't quite as laid back either. I hope he hasn't started taking things too seriously." 


    aubrey neutral "I've kept playing gigs, but it's hard to relax at all between that and work."

    show aubrey neutral
    theo happy "Yeah, work.. my favorite"

    show theo neutral
    aubrey happy "Oh yeah how did your internship go?"

    show aubrey neutral
    theo phone "What, the one at the medical-tech place? Terribly."
    theo "They took me on full time, but I was on starting pay for three years."
    theo neutral "I quit."

    menu:
        "Of course it's been that long":
            python:
                good_points += 1
            pov "Why would Theo make that up? It's easy enough to lose track of time after college. There's so much to do."

        "That isn't possible":
            python:
                bad_points += 1
            pov "That's wrong. It was a little while, but not three years. Theo's memory must be off, or he must be hiding something."


    show theo phone
    aubrey nervous "...wow"

    show aubrey nervous
    theo happy "Oh, sorry, I shouldn't be talking about that sort of thing at a party! How was your latest show?"
   
    show theo neutral
    aubrey happy "Just fine! It was kind of a throwback, actually."
    aubrey "We played a bunch of the classics at this place downtown."

    show aubrey neutral
    theo happy "Did you do that one you'd always blast on road trips?"
    
    show theo neutral
    aubrey happy "Which one? you mean..."

    show theo neutral
    aubrey nervous "oh. No, I haven't played that since..."
    
    show aubrey sad
    theo neutral "You don't have to say. I forgot that was their favorite, not yours."

    pov "Whose favorite? What song? Why are they getting so cagey all of a sudden?"    

    menu:

        "It's just a song. I need to relax.":
            python:
                good_points +=1
            pov "We're at a party. Breath and let the tension roll over yourself. If there's a problem, my friends will tell me."


        "There must be someone else they'd rather have here.":
            python:
                bad_points +=1
            pov "They've changed too much since we last met. I can't believe that they'd leave me out like this."


        "Aubrey wouldn't keep something from me unless it was important. It's fine." if major == "Music Theory":
            python:
                good_points +=1
            pov "We're at a party. Breath and let the tension roll over yourself. If there's a problem, my friends will tell me."


        "Theo knows how to set boundaries, and this is one. I need to respect that." if major == "Computer Science":
            python:
                good_points +=1
            pov "We're at a party. Breath and let the tension roll over yourself. If there's a problem, my friends will tell me."

                



    hide aubrey with dissolve
    hide theo with dissolve


    jump Listen_In





