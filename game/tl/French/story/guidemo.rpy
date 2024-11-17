label guidemo:
    
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    
    $ devnumba1 = False
    
    stop music fadeout 1.0
    
    pause 0.5

    play music chill fadein 1.0
    pause 2.5

    scene college_entrance_day_summer

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.

    show dev neutral at moveinright(0.2) with eidissolve_nd
    
    "Ive been at this college for all of 2 minutes yet I am still a soy incel beta cuck."
    
    D "Oh woe is me, when will I get a sexy wiafu so I can not be pathetic anymore."
    
    show dev:
        setx(0.2)
        movex(0.15)
    show emihead neutral left at moveinleft(0.5) with eidissolve_nd
    show rebecca neutral left at moveinleft(0.6) with eidissolve_nd
    show emily neutral left at moveinleft(0.85) with eidissolve_nd
    show dev surprised with eidissolve_nd
    
    "Suddenly two people approach you."
    
    "One is a midget with clear daddy issues and the other is a man with pretty nice breasts."
    
    show rebecca skeptical left with eidissolve_nd

    R "Look Emily, that is the skinnie. He must be the protaganist of the story."
    
    "The large chested man takes out some sort of tablet and begins writing."
    
    show dev annoyed with eidissolve_nd
    show rebecca surprised with eidissolve_nd
    show emihead surprised with eidissolve_nd
    
    D "Bitch are you ignoring me?"
    
    Em "... "
    
    show emihead sad with eidissolve_nd
    
    "She turns the tablet towards you."
    
    Et "He looks cute."

    show rebecca annoyed with eidissolve_nd
    show dev sad with eidissolve_nd
    
    D "Oh..."
    
    D "Uh... thanks."
    
    show rebecca neutral with eidissolve_nd
    show dev neutral with eidissolve_nd
    show emihead neutral with eidissolve_nd
    
    R "Right."
    
    R "So who's back are you going to blow out."
    
    menu:
        "Goth mommy.":
            pause 0.5
            jump rebecca_simp

        "Big lady.":
            pause 0.5
            jump emily_simp
        "I demand both of your asses!":
            pause 0.5
            jump both_simp
        "Neither, the only simping I do is for Raptor Jesus.":
            pause 0.5
            jump good_boy

label rebecca_simp:

    show rebecca cheerful with eidissolve_nd
    show rebecca blush with eidissolve_nd
    show emihead sad with eidissolve_nd
    
    R "Good choice."
    
    jump demo_cont
    
label emily_simp:

    show emihead cheerful with eidissolve_nd
    show emihead blush with eidissolve_nd
    show rebecca sad with eidissolve_nd
    
    Et "Good choice."
    
    jump demo_cont

label both_simp:

    show emihead cheerful with eidissolve_nd
    show emihead blush with eidissolve_nd
    show rebecca cheerful with eidissolve_nd
    show rebecca blush with eidissolve_nd
    
    R "Good choice."
    
    jump demo_cont

label good_boy:

    show emihead cheerful with eidissolve_nd
    show rebecca cheerful with eidissolve_nd
    
    R "Good choice, you beat your base desired and chose the light."
    
    jump demo_cont

label demo_cont:
    # This ends the game.

    return