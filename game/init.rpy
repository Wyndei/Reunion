




define aubrey_sprite = "aubrey"




label init_scene:

    
    stop music


    python:
        name = renpy.input("What is my name?", length = 32) 
        name = name.strip()

        if not name:
            name = "Jon"



    pov "College was such a wild time."
    pov "So much to do every day, early mornings, late nights…friends." 
    pov "It was all worth it, of course. I was always destined to get into…"

    menu:
        "Art History":
            jump Art_History
                
        "Psychology":
            jump Psychology
                
        "Music Theory":
            jump Music_Theory
                
        "Computer Science":
            jump Computer_Science
                






label Art_History:
    python:
        major = "Art History"

    pov "Art History"

    pov "During college, I became friends with Ravena." 
    pov "We both studied under the same major and were paired up for an assignment. "
    pov "She was quiet at first, and even wanted to do the entire project herself!" 
    pov "In the end, I somehow managed to convince her to let me help."

    jump init_final


label Psychology:
    python:
        major = "Psychology"

    pov "Psychology"

    pov "I wouldn't have gotten through junior year if it wasn't for Yokari!"
    pov "He's just the sort of person that can't stand to see someone else struggle, and boy was I struggling." 
    pov "It was just lecture notes at first, then conversation in the hall, and suddenly we were hanging out all the time."
    pov "I can't wait to see him at the party today!"

    jump init_final


label Music_Theory:
    python:
        major = "Music Theory"
    
        aubrey_sprite = "aubrey_necklace" 
    

    pov "Music Theory"

    pov "I'm glad I never threw out old song books, otherwise I wouldn't have gotten to meet Aubrey."
    pov "They could play just as well as the rest of the band, but no amount of skill could make up for missing sheet music."
    pov "If I didn't know better, I'd say they were forgetting on purpose."
    pov ".. Hopefully they remembered the party was today."

    jump init_final
    

label Computer_Science:
    python:
        major = "Computer Science"

    pov "Computer Science"

    pov "Comp sci wouldn't have been the same without Theo." 
    pov "Great at arguing, but then again, how else would I have learned to just look things up when I didn't know the answer?"
    pov "I wonder if he's still as argumentative, or if he's mellowed out some..."
    pov "Guess I'll find out soon."

    jump init_final




label init_final:




    jump Door_Scene





