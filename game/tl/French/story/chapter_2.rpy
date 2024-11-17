label chapter_2:

####PART 1####

    stop music
    
    play music dreamy_nights fadein 3
    
    pause 0.5
    
    scene black

    "{cps=6}{bt=5}{i}YAWN{/i}{/bt}{/cps}"
    
    pause 2.0
    
    "Wow,{w=0.3} these dorm room beds are actually surprisingly nice."
    
    "I figured that the dorms here would be as simple and functional as possible, but this is probably better than my own room back home."
    
    "The walls are perhaps a bit plain,{w=0.3} but I never found a band I liked enough to get their posters, and even action figures or cars were more my dad's thing."
    
    "Still,{w=0.3} I appreciate the sturdy carpentry that has gone into making these beds solid.{w=0.1} I try to shake myself awake and find that the mattress doesn't shift at all{w=0.2}, no matter how much I thrash around."
    
    "Makes sense,{w=0.3} considering the very different bodies and species that are supposed to fit in these."
    
    "Man,{w=0.3} they must've spent half their budget on these beds.{w=0.1} It's like lying on a cloud that's made out of{cps=5}...{/cps} softer clouds."
    
    "I could get used to this,{w=0.2} seriously. No wonder dinosaurs almost went extinct{w=0.3}—they probably spent all day lounging around,{w=0.1} too comfy to notice the meteor."
    
    "You can just sink into the mattress and just{cps=5}...{/cps} Let go-"
    
    "{cps=6}{bt=10}{i}Snore{/i}{/bt}{/cps}"
    
    pause 2
    
    "Wait{cps=5}...{/cps}"
    
    "Something is wrong."
    
    "I'm comfortable."
    
    "TOO comfortable."
    
    play sound alarm fadein 3 loop
    
    "Alarm bells are triggered in my brain.{w=0.1} Holdovers from one too many \"talks\" my boss gave me back when I had a summer job.{w=0.2} The type that came with a deep frown and a stern warning about coming in late because{cps=5}...{/cps}"
    
    
    
    show dormroom_dev_empty_day with eDissolve(3)
    
    
    pause 2
    stop sound fadeout 2
    play music no_rest_in_ccc fadein 0.5
    
    show dev yiik at moveinup(x=0.5, y=0.0, m=1.2, t=0.75)
    with eidissolve_nd
    
    
    
    play music no_rest_in_ccc fadein 0.5
    
    D "{sc}OH CRAP! I SLEPT IN!{/sc}"
    
    show dev sad:
        easein_cubic 0.5 xpos 0.7
    
    
    "I grab my phone from the nightstand, and looking at the time is like being punched in the gut:{w=0.3} It's 9:48 AM."
    
    show dev:
        xpos 0.7
        ypos 0.0
    
    "{cps=5}...{/cps}"
    
    show dev terrified
    with eidissolve_nd
    
    "My first class starts at 10:00!"
    
    show dev skeptical
    with eidissolve_nd
    
    "How did this happen?{w=0.3} I know I set my alarm for 8:30–"
    
    show dev neutral
    with eidissolve_nd
    
    "{cps=5}...{/cps}"
    
    show dev ashamed
    with eidissolve_nd
    
    "{cps=5}...{/cps} 8:30 {cps=5}{i}PM{/i}...{/cps}"
    
    show dev annoyed left
    with eidissolve_nd
    
    "Whatever,{w=0.3} I {i}literally{/i} have no time to dwell on it."
    
    
    show dev neutral:
        transform_anchor True
        subpixel True
        yoffset 0.5 * 1500
        yanchor 0.5
        
        parallel:
            xpos 0.7 
            bop_in_time_warp 0.01 xpos 0.7 
            ease_cubic 0.99 xpos 0.3 
        parallel:
            ypos 0.0 rotate 0.0 
            easein_cubic 0.47 ypos 0.0 rotate 0.0 
            easein_cubic 0.53 ypos 0.2 rotate -10.0 
    with Pause(1.35)
    show dev:
        transform_anchor True
        subpixel True
        yoffset 0.5 * 1500
        yanchor 0.5
        
        parallel:
            pos (0.3, 0.2) rotate -10.0
        parallel:
            easein_cubic 1 ypos 0.2
            easein_cubic 1 ypos 0.23
            easein_cubic 1 ypos 0.21
            repeat
    
    
    
    "I sprint across the room,{w=0.3} clothes flying in every direction as I search for everything I'll need for the day."
    
    "The day that also happens to be my official first day as a Cretaceous College of Computing student. No pressure."

    "Usually, I wouldn't care much about this, but my phone displays a text received just a few minutes ago from Theo."
    
    $ theo_chat.transient = False

    phone register "theo_chat":
        time hour 6 minute 23
        "T" "HEY!!"
        "T" "You awake?"
        "T" "??"
        "T" "probably not." 
        "T" "well when you come back to the land of the living, I want you to know morning classes freakin BLLLOOOWWWW!"
        time hour 8 minute 32
        "T" "if you are awake yet i'm gonna be in the cafeteria at 9"
        time hour 9 minute 16
        "T" "i miss you T_T"
        time hour 9 minute 28
        "T" "dude!" 
        "T" "almost forgot, we got a first day tradition."
        "T" "you should write ‘#1' on your forehead. all the freshmen are doing it"
    phone discussion "theo_chat":
        pause
        
    phone end discussion
    
    show dev sad:
        parallel:
            easein_cubic 1 rotate 0.0 
        parallel:
            easein_cubic 1 ypos 0.0
        
    
    "My sleep-deprived brain needs an extra few moments to process the text."
    
    show dev:
        rotate 0.0
        xpos 0.3
        ypos 0.0
    
    show dev thinking t_skeptical
    with eidissolve_nd

    "First day tradition?{w=0.3} How come I haven't heard about it before?"
    
    show dev annoyed
    with eidissolve_nd
    
    "It's ridiculous.{w=0.3} I'm{cps=5}...{/cps}"
    
    show dev neutral
    with eidissolve_nd
    
    menu:
        "Gonna go with it anyway.":
            
            show dev right:
                easein_cubic 2.5 xpos 0.7
            "In the midst of my search for clothes in respectable condition, I quickly scrawl Theo's suggestion  on my smooth forehead."
            "Well,{w=0.3} it's not so smooth this morning. My hairline is starting to grow in again;{w=0.1} looks like I'll have to shave soon before it gets too long."
            show dev_marker1 with dissolve
            "And looking closer, I'm finding it increasingly hard to tell what the scribbled symbol on my forehead is supposed to be."
            "Ugh,{w=0.3} why did I do this?"
            show dev_marker2 with dissolve
            hide dev_marker1 with dissolve
            $ devnumba1 = True
            "I idly glance at the marker as I go to set it down on my desk."
            "Wait{cps=5}...{/cps}"
            hide dev_marker2 with dissolve
            show dev yiik with eidissolve_nd
            extend " {sc}{cps=5}PERMANENT{/cps} MARKER?!{/sc}"
            show dev:
                parallel:
                    easein_cubic 0.2 ypos 0.05
                    easein_cubic 0.2 ypos 0.0
                    repeat
                parallel:
                    xzoom 1
                    pause 1
                    xzoom -1
                    pause 1
                    repeat
                    
            "Oh no{cps=5}...{/cps}"
            show dev annoyed:
                xzoom -1.0
                ypos 0.0
            with eidissolve_nd
            "No time to fix it!{w=0.1} Just gotta hope I can find some way to get rid of it later."
        "Super duper not gonna go with it. AT ALL.":
            #have him move around the room as if looking for stuff, maybe trip and fall on his back
            show dev:
                transform_anchor True
                subpixel True
                yoffset 0.5 * 1500
                yanchor 0.5
                
                easein_cubic 1 ypos 0.2 rotate -10.0 
                parallel:
                    easein_cubic 1 ypos 0.2
                    easein_cubic 1 ypos 0.23
                    easein_cubic 1 ypos 0.21
                    repeat
            "A pair of jeans from my duffle{w=0.3}—check. Shirt{cps=5}...{/cps} shirt{cps=5}...{/cps} there!{w=0.1} It's crumpled but it'll have to do.{w=0.1} Comfortable shoes for all the running between classes, and a pair of mismatched socks to tie it all together."
            "No one's gonna see them under my jeans, anyway."
            show dev right:
                transform_anchor True
                subpixel True
                yoffset 0.5 * 1500
                yanchor 0.5
            
                parallel:
                    easein_cubic 1 ypos 0.0 rotate 0.0 
                parallel:
                    easein_cubic 2.5 xpos 0.7
            "In record time, I'm dressed and fumbling to tie my shoes with hands shaking from adrenaline."
    
    show dev thinking:
        xzoom -1.0
    with eidissolve_nd
    
    "Teeth{w=0.3}—no time to brush 'em.{w=0.1} I grab a stick of gum instead and chew it until my jaw starts screaming for mercy."
    
    show dev neutral
    with eidissolve_nd        
    
    "Phone,{w=0.1} wallet,{w=0.1} keys{w=0.1}—shove them into my pockets as I rush out the door. The hallway is empty; everyone else is already where they need to be."

    
    show dev left at moveoutleft(x=1.2)
    hide dev
    
    scene black with eDissolve(2)
    pause 2
    
    "I run down the stairs and out of the building,{w=0.2} only to find the colorful campus outside is already buzzing with activity;{w=0.3} I dodge a couple of triceratops playing frisbee and nearly trip over a velociraptor on a bike."
    
    scene quad_1 with eDissolve(2)
    pause 1
    
    
    
    show dev left:
        transform_anchor True
        subpixel True
        yoffset 0.5 * 1500
        yanchor 0.5
        
        subpixel True 
        parallel:
            xpos 1.2 
            easein_expo 0.99 xpos 0.5 
        parallel:
            ypos 0.0 
            easein_cubic 0.31 ypos 0.0 
            easein_cubic 0.23 ypos -0.12 
            easein_cubic 0.25 ypos 0.55 
        parallel:
            rotate 0.0 
            easein_cubic 0.31 rotate 0.0 
            easein_cubic 0.20 rotate 81.0 
    with Pause(1.09)
    show dev left:
        pos (0.5, 0.55) rotate 81.0 
    
    pause 1
    
    show dev annoyed:
        parallel:
            easein_cubic 1 rotate 0.0 
        parallel:
            easein_cubic 1 ypos 0.0
            
    pause 1
    
    show dev at moveoutleft
    hide dev
    
    "My lungs burn as I push through the quad,{w=0.2} sidestepping students and jumping over benches like some kind of parkour athlete. Or at least,{w=0.3} that's how it feels."
    
    scene black with eDissolve(2)
    
    "The MathematiS building looms ahead, and I glance at my phone again{w=0.3}—9:57 AM."
    "Almost there{cps=5}...{/cps}"
    "I'm inside the building,{w=0.2} but now I've gotta find the right classroom."
    "I'm so close to the finish line,{w=0.3} so close{cps=5}...{/cps}"
    show mathclass_day_summer behind black
    show dev:
        xpos 1.2
    show c_standing1 left behind dev:
        matrixcolor ColorizeMatrix("#7e3e9b", "#ffffff")
        block:
            xpos 0.94
        block:
            pause 1
            easein_cubic 0.2 ypos -0.02
            pause 0.01
            easein_cubic 0.2 ypos 0.00
            pause 4
            easein_cubic 0.2 ypos -0.01
            pause 0.01
            easein_cubic 0.2 ypos 0.0
            pause 0.01
            easein_cubic 0.2 ypos -0.01
            pause 0.01
            easein_cubic 0.2 ypos 0.0
            pause 3
            repeat
    show c_standing3 behind dev:
        matrixcolor ColorizeMatrix("#9b3e4c", "#ffffff")
        block:
            xpos 0.79
        block:
            pause 0.3
            easein_cubic 0.2 ypos -0.01
            pause 0.01
            easein_cubic 0.2 ypos 0.0
            pause 0.01
            easein_cubic 0.2 ypos -0.01
            pause 0.01
            easein_cubic 0.2 ypos 0.0
            pause 3
            easein_cubic 0.2 ypos -0.02
            pause 0.01
            easein_cubic 0.2 ypos 0.00
            pause 4
            repeat
    show c_walking2 behind dev:
        matrixcolor ColorizeMatrix("#989b3e", "#ffffff")
        xpos 0.65
    
    hide black with dissolve
    
    pause 1
    
    show dev happy left:
        easein_cubic 1 xpos 0.5
    
    show c_walking2:
        pause 0.5
        xzoom -1.0
        pause 1
        xzoom 1.0
        pause 1
        block:
            easein_cubic 0.2 ypos -0.01
            pause 0.01
            easein_cubic 0.2 ypos 0.0
            pause 0.01
            easein_cubic 0.2 ypos -0.01
            pause 0.01
            easein_cubic 0.2 ypos 0.0
            pause 4
            easein_cubic 0.2 ypos -0.02
            pause 0.01
            easein_cubic 0.2 ypos 0.00
            pause 5
            repeat
    with eidissolve_nd
    "I made it!"
    
    stop music fadeout 10
    
    show dev smug with eidissolve_nd
    "With two entire minutes to spare, at that."
    show dev sad with eidissolve_nd
    "Now if only I could stop the fiery pain in my lungs and legs."

####PART 2####
    
    show dev neutral
    with eidissolve_nd
    
    play music half_past_math fadein 10
    
    "Stepping into the first class of my college life, it's{cps=5}...{/cps}"
    
    show dev thinking
    with eidissolve_nd
    
    "{cps=5}...{/cps}"
    
    show dev sad
    with eidissolve_nd
    
    "Not exactly what I was expecting."
    "I assumed all the classes would be in large auditorium style rooms,{w=0.1} a gigantic whiteboard dominating the whole back wall,{w=0.1} semi-comfy seats. But this?"
    
    show dev skeptical
    with eidissolve_nd
    
    "It's a simple room,{w=0.3} with wooden desks and chairs, complete with metal legs that you just know aren't properly balanced. The desks even have a cubby hole beneath them to hold books and whatever else you can fit."    
    "At the very front, there's the teacher's desk, and a blackboard."
    
    show dev surprised
    with eidissolve_nd
    
    "A blackboard."
    
    show dev unimpressed
    with eidissolve_nd
    
    "Not a white one for markers. A black one with tiny pieces of chalk under it."
    "{cps=5}...{/cps}"
    
    show dev sad
    with eidissolve_nd
    
    "This just looks like high school."
    "I cringe at the thought of all the chalk-scraping hell to come,{w=0.1} as if math couldn't be bad enough on its own."
    
    show dev thinking
    with eidissolve_nd
    
    "Hmmm{cps=5}...{/cps}"
    
    show dev thinking t_skeptical
    with eidissolve_nd
    
    "Do I just sit anywhere, or is this {i}actually{/i} like high school and we have assigned seats?"
    
    show dev thinking
    with eidissolve_nd
    
    "Beyond that, I need to consider that some students have wings and actual horns.{w=0.3} Should I sit at the front to make sure I can see at all, or hide behind them to avoid standing out so much?"
    
    show hawthorn left at moveinleft(x=0.75)
        
    MrHu "You must be the human I-."
    show dev terrified right:
        easein_cubic 0.5 xpos 0.4
    show hawthorn surprised:
        easein_cubic 0.5 xpos 0.76
    with eidissolve_nd
    D "{sc}Ah!{/sc}"
    
    show hawthorn skeptical
    show dev sad
    with eidissolve_nd
    
    "I jump at a voice right behind me, feeling my heart skip one too many beats.{w=0.3} Turning to its source, I find a short, heavyset pachysaurus,{w=0.1} looking at me with a stern but tired expression."
    
    show dev neutral
    with eidissolve_nd
    
    "Based on the way he is dressed{w=0.2} - dress pants, a tie and a well ironed shirt{w=0.3} - I am guessing he's our professor?"
    
    show dev thinking
    show hawthorn unimpressed
    with eidissolve_nd
    
    "Either that, or a really old student."
    
    show dev thinking t_skeptical
    with eidissolve_nd
    
    "Which is not an entirely unreasonable assumption.{w=0.3} This is a college, I remind myself, not a high school, no matter how much it looks like one."
    
    show hawthorn unimpressedconsidering
    show dev thinking t_surprised
    with eidissolve_nd
    
    "And even if it was a high school, it would be okay for anyone of any age to get their education done.{w=0.3} Commendable, even."
    
    show hawthorn skeptical
    with eidissolve_nd
    
    MrHu "Kid,{w=0.2} are you listening?"
    
    show dev sad
    with eidissolve_nd
    
    "Crap,{w=0.2} I spaced out, didn't I?"
    D "Uh, yeah{cps=5}...{/cps} I mean no.{w=0.3} Sorry. What did you ask me?"
    MrHu "Your name.{w=0.3} You're the only human kid around this year."
    
    show dev surprised
    show hawthorn neutral
    with eidissolve_nd
    
    D "Yes, I'm Dev Loper."
    
    show dev neutral
    show hawthorn grin
    with eidissolve_nd
    
    MrH "Julian Hawthorn."
    "Mr. Hawthorn speaks in a surprisingly deep,{w=0.1} gravelly rumble."
    
    if devnumba1:
        show dev sad
        show hawthorn annoyed
        with eidissolve_nd
        "His eyes suddenly narrow,{w=0.1} honing in on the marker on my forehead."
        show hawthorn skeptical
        with eidissolve_nd
        MrH "Already enjoying college life, are we, Mister Loper?"
        MrH "I hope you'll take your academics seriously.{w=0.3} College is more than a place for partying and marking each other up when you pass out."
        show dev ashamed
        with eidissolve_nd
        D "No, I{cps=5}...{/cps} a friend told me it was a freshman tradition{cps=5}...{/cps}"
        show dev sad
        show hawthorn neutralconsidering
        with eidissolve_nd
        "Mr. Hawthorn looks around, prompting me to do the same."
        "Not a single other student has \"#1\" on their head."
        show hawthorn skeptical
        with eidissolve_nd
        MrH "If you insist{cps=5}...{/cps}"
        show dev neutral
        show hawthorn neutral
        with eidissolve_nd
        MrH "But as for academics, I'll be your professor for this class. Just pay attention, and you'll do fine, I'm sure."
    
    
    else:
        show dev neutral
        show hawthorn grin
        with eidissolve_nd
        MrH "I'll be your professor for this class. Just pay attention, and you'll do fine, I'm sure."
    
    show dev skeptical
    show hawthorn neutral
    with eidissolve_nd
    
    D "You mentioned \"only human kid this year\"? Have there been other humans before then?"
    
    show dev neutral
    show hawthorn neutralconsidering
    with eidissolve_nd
    
    MrH "No,{w=0.3} but we're hoping to have a more varied student body in the coming semesters."
    
    "This is good. It feels like I'm making a good impression.{w=0.3} I think."
    
    show dev thinking
    show hawthorn grin
    with eidissolve_nd
    
    "But{w=0.2} now that I'm talking to him, I am still wondering about the seating, so{cps=5}...{/cps}"
    
    show dev somber
    show hawthorn neutral
    with eidissolve_nd
    
    D "Thanks. I'm new to this whole \"college\" thing, do we have assigned seats or{cps=5}...{/cps}?"
    
    show dev neutral
    show hawthorn grin:
        chuckle
    with eidissolve_nd
    
    "He chuckles at the question. My ears grow warm out of a slight feeling of embarrassment"
    MrH "No, kiddo. You're all adults,{w=0.2} sit where you like. I must warn you though, it's \"first come first serve\", so if you want the good seats you'll want to get here early."
    D "Thanks, Mr. Hawthorn."
    
    show dev happy:
        easein_cubic 0.5 xpos 0.5
        pause 0.1
        nudgeup
        easein_cubic 0.5 xpos 0.45
    show hawthorn happy:
        easein_cubic 0.5 xpos 0.7
        pause 0.1
        nudgeup
        easein_cubic 0.5 xpos 0.75
    with eidissolve_nd
    
    "Out of courtesy - and to get on his good side - I offer a handshake, which he accepts with a smile."
    
    show dev sad
    show hawthorn neutral:
        0.25
        easein_cubic 10 xpos -0.5
    with eidissolve_nd
    
    show dev neutral
    with eidissolve_nd
    
    "This is an adjustment.{w=0.3} With how similarly this place looks to high school, I was expecting more of the same. But{w=0.1} he's right.{w=0.3} I {i}am{/i} an adult now."
        
    show c_walking2:
        easein_cubic 0.2 ypos -0.02
        pause 0.01
        easein_cubic 0.2 ypos 0.0
        pause 0.01
        xzoom -1
        easein_quad 3 xpos -0.5
    
    "That'll be an adjustment to wrap my head around now too."
    
    show c_chilling1 right behind c_standing1:
        xpos 1.2
    show c_texting1 right behind c_standing1:
        xpos 1.2
        
    show c_chilling1 left:
        matrixcolor ColorizeMatrix("#559b3e", "#ffffff")
        easein_quad 6 xpos -0.5
    show c_texting1 left:
        matrixcolor ColorizeMatrix("#9b5c3e", "#ffffff")
        pause 0.4
        easein_quad 7 xpos -0.5
    
    "I hear the clamor of voices approaching the already half-filled room. How does this work?{w=0.3} Is this like the \"guy code\"? Where you don't - and I emphasize - you {i}don't{/i} choose the seat next to one already in use? Or will people even care at all?"
    
    show c_standing3 left:
        ypos 0.0
        pause 0.2
        parallel:
            easein_cubic 1 xpos 0.5
        parallel:
            pause 0.55
            easein_cubic 1 ypos 0.1
    show c_standing1 left:
        ypos 0.0
        parallel:
            easein_cubic 1 xpos 0.8
        parallel:
            pause 0.3
            easein_cubic 1 ypos 0.1
    
    hide c_walking2
    hide c_chilling1
    hide c_texting1
    
    "Hmmm."
    
    show hawthorn right:
        easein_cubic 4 xpos 0.15
    
    show dev:
        parallel:
            easein_cubic 1 xpos 0.65
        parallel:
            pause 0.3
            xzoom -1
            easein_cubic 1 ypos 0.1
    
    "I just take a random spot in the middle.{w=0.2} Ideal.{w=0.3} Won't make me look too eager, but I also won't have to squint to see anything important."
    
    show hawthorn:
        xpos 0.15
        nudgeup
    
    "I hear the professor clear his throat.{w=0.3} Silence sets in."
    
    show hawthorn grin
    with eidissolve_nd
    
    MrH "As some of you who have had me in other classes might know,{w=0.2} my name is Professor Hawthorn."
    
    show hawthorn neutralconsidering
    with eidissolve_nd
    
    MrH "For the sake of those that have mistakenly walked into the wrong class,{w=0.2} which happens far more often than I would hope: this is College Algebra,{w=0.3} an introductory course to advanced algebra."
    
    show hawthorn unimpressed
    with eidissolve_nd
    
    show dev:
        pause 0.5
        xzoom 1
        pause 2.5
        xzoom -1
    
    show c_standing3:
        pause 0.2
        parallel:
            pause 0.55
            xzoom -1
            easeout_cubic 2 xpos 1.5
        parallel:
            easein_cubic 1 ypos 0.0
    show c_standing1:
        parallel:
            pause 0.3
            xzoom -1
            easeout_cubic 2 xpos 1.5
        parallel:           
            easein_cubic 1 ypos 0.0
    
    "A few students sheepishly stand up and walk out, to which Mr. Hawthorn just rubs his temples in frustration."
    "I double check my schedule, just to be sure.{w=0.3} Yep, my adrenaline spiked brain didn't fail me - this is the right class."
    
    hide c_standing1
    hide c_standing3
    show hawthorn neutral
    with eidissolve_nd
    
    MrH "Anyway,{w=0.3} for this first week we will just be doing a refresher on what you {b}should{/b} have been taught in your senior year of high school."
    
    show hawthorn grin
    with eidissolve_nd
    
    MrH "After that we will be jumping into the more fun stuff."
    
    show hawthorn happy
    with eidissolve_nd
    
    "Mr. Hawthorn gives an awkward toothy smile.{w=0.3} Despite his forced attempt at enthusiasm, no one in class can be bothered to offer so much as an uninterested grunt."
    
    show hawthorn unimpressed
    with eidissolve_nd
    
    MrH "Right{cps=5}...{/cps}"
    
    show hawthorn left neutral:
        block:
            linear 0.05      ypos 0.015
            easein_cubic 0.2 ypos 0.01
            linear 0.05      ypos 0.015
            easein_cubic 0.2 ypos 0.01
            pause 0.5
            linear 0.05      ypos 0.015
            easein_cubic 0.2 ypos 0.01
            pause 0.25
            linear 0.05      ypos 0.015
            easein_cubic 0.2 ypos 0.01
            pause 1.0
            linear 0.05      ypos 0.015
            easein_cubic 0.2 ypos 0.01
            linear 0.05      ypos 0.015
            easein_cubic 0.2 ypos 0.01
            linear 0.05      ypos 0.015
            easein_cubic 0.2 ypos 0.01
            pause 0.5
            repeat

    with eidissolve_nd
    
    "The rest of the class is exactly as he said.{w=0.1} Just a bunch of stuff I only half remember from high school.{w=0.3} I have a feeling YouSnoot and other people's notes are gonna be a necessary resource this year."
    "Maybe from Theo, and if that fails, then Rebecca or Elliot. Not sure if they like me enough to help me, but worth a try I guess."
    
    show dev sad
    
    
    "It's difficult to stay focused in the class, all things considered.{w=0.3} My mind begins to quickly drift,{w=0.2} and the fact that Mr. Hawthorn talks in such a monotone voice doesn't help.{w=0.3} It actually becomes impossible to stay focused."
    
    
    show dev thinking
    show black behind dev:
        alpha 0.5
    with eidissolve_nd
    pause 0.3
    
    camera:
        subpixel True 
        pos (0, 0) zoom 1.0 
        easein_cubic 5 pos (-921, -20) zoom 1.52
    

    
    "It does give me time to think, though.{w=0.3} About what Theo said last night. About making a game."
    "It's a neat idea."
    
    show dev neutral
    with eidissolve_nd
    
    "I've been trying to figure out what I want to do with my future anyway, so{w=0.3} maybe game design is it?"
    
    if VTSD:
        "I've made mods for games before, but an actual game?"
    else:
        "I haven't tried doing anything like it before."

    "What would it even be about?{w=0.3} What kind of game would it be?"
    
    show dev surprised
    
    show fighting:
        xpos 0.32
        zoom 0.68
    with eidissolve_nd
    
    "I like fighting games,{w=0.2} and they're not as frustrating as an open world adventure game filled with busywork.{w=0.3} I have a love-hate relationship with those."
    
    show dev skeptical
    show openworld:
        xpos 0.32
        zoom 0.68
    hide fighting
    with eidissolve_nd
    
    "Open world types usually have either great stories, or the most slapped-on, cardboard-tasting excuse for a plot{w=0.3} and the fetch quests end up being more entertaining."
    "And almost no one likes fetch quests.{w=0.2} I'm not sure if I want to meet anyone who does."
    
    show dev annoyed
    show visualnovel:
        xpos 0.32
        zoom 0.68
    hide openworld
    with eidissolve_nd
    
    "Visual novels are out of the question.{w=0.1} I mean, reading?{w=0.3} In my videogame?"
    
    show dev thinking t_surprised
    show shooter:
        xpos 0.32
        zoom 0.68
    hide visualnovel
    with eidissolve_nd
    
    "And then there are shooters.{w=0.3} It could be a BOOM clone,{w=0.2} a linear and narrative focused one{cps=5}...{/cps} or a competitive shooter, ultra replayable, not that many assets required. "
    
    show dev thinking t_skeptical
    with eidissolve_nd
    
    "What I fear the most about those is the balancing part.{w=0.3} We'd have to make sure that every character offers a fair chance for anyone to win."
    
    hide shooter with eidissolve_nd
    
    "But also make them feel different because the first-person POV doesn't help much at making them stand out at first glance."
    "And there's the matter of objectives and gameplay{w=0.3} - we can't just have a deathmatch mode and call it a day."
    "I hum to myself,{w=0.1} thinking that if I have this many thoughts about shooters,{w=0.2} maybe they're the idea I like the most."
    
    camera:
        subpixel True 
        pos (-921, -20) zoom 1.52 
        easein_cubic 5 pos (0, 0) zoom 1.0
    hide black with eidissolve_1s_nd 
    
    "I write all of this down in the empty spaces of the margins of my notes.{w=0.3} Regardless of my feelings on it for now, I'll have to discuss this with Theo later."
    "I can't deny that I'm excited about having an actual friend in college, and having something fun to talk about with them. Something that-" #Loud door creek noise here 
    
    window auto hide
    stop music fadeout 10
    pause .5

    scene black with dissolve
    pause .5
    show screen cutscene("emilyintro_skip")
    window auto hide
    pause .5
    
    play sound emilyintro_audio
    show anim_emilyintro behind black
    # Loading a video takes a second, so this is here so the fadein isn't choppyRR
    pause 0.2
    hide black with Dissolve(1) 
    pause 16
    label emilyintro_skip hide:
    hide screen cutscene
    scene mathclass_day_summer with dissolve
    
    #        #Under Construction: TODO add sounds
    
    stop sound
    play music half_past_math fadein 2 if_changed
    
    show hawthorn surprised right:
        xpos 0.15
        ypos 0.0
        alpha 0
    show dev left surprised:
        xpos 0.6
        ypos 0.1
        alpha 0
        
    show hawthorn surprised right:
        ease_cubic 1 alpha 1
    show dev left surprised:
        ease_cubic 1 alpha 1
    
    pause 1
    
    show emily left behind dev at moveinleft(x=0.99)
    show emihead sad left behind dev at moveinleft(0.8)
    
    pause 0.7
    show dev right surprised
    with eidissolve_nd
    
    "My thoughts are interrupted by what could best be described as an \"absolute unit of an individual\" trying their best to enter the classroom as quietly as possible."
    
    show hawthorn surprised right:
        alpha 1
    show dev left surprised:
        alpha 1
    
    show hawthorn unimpressedconsidering
    with eidissolve_nd
    
    "Unfortunately for them, however, it seems the world wishes to play the cruelest prank on them by making the door as ear-gratingly squeaky as possible.{w=0.3} It even eclipses Mr. Hawthorn's chalk sounds."
    
    "It creaks loud,{w=0.1} long{w=0.1} and clear, making everyone's head turn in their direction."
    
    show dev neutral
    show hawthorn unimpressed
    with eidissolve_nd
    
    "Hard not to be distracted by some guy with shoulders that reach 6 feet on their own,{w=0.3} and a neck that is easily twice as long, if not more."
    
    show hawthorn annoyed
    with eidissolve_nd
    
    "The professor looks at the late arrival with quite a bit of annoyance."
    
    show emihead:
        easein_cubic 0.5 ypos 0.05
    show emily sad with eidissolve_nd
    

    MrH "Ms. Bennett,{w=0.3} so glad for you to finally decide to join us today."
    
    show dev shocked
    with eidissolve_nd

    "That behemoth is a girl!?{w=0.3} I feel the need to slap my own face for my stupid assumption."
    
    show dev skeptical
    with eidissolve_nd
    
    "I'm also getting the feeling that these two know each other."

    
    show emihead:
        subpixel True 
        parallel:
            pos (0.8, 0.05) 
            easein_cubic 2.00 pos (0.76, 0.1) 
        parallel:
            rotate 0.0 
            easein_cubic 0.01 rotate 0.0 
            easein_cubic 0.97 rotate -5.0 
    
    "The large girl looks around the room as all eyes are on her, and her face turns beet red at the attention."
    
    show dev neutral
    show hawthorn unimpressedconsidering
    show emily neutral
    with eidissolve_nd
    
    "I see her mouth something to Mr. Hawthorn but don't hear anything at all.{w=0.1} He just rolls his eyes and gestures for her to take a seat."
    
    show emily:
        parallel:
            easein_cubic 1 xpos 0.9
        parallel:
            pause 0.3
            easein_cubic 1 ypos 0.1
    show emihead:
        parallel:
            easein_cubic 1 pos (0.5, 0.0)
        parallel:
            pause 0.3
            easein_cubic 1 rotate 0
    
    "I guess he wasn't joking about the seats, the only one left is the one right next to me."
    "{cps=5}...{/cps}"
    
    show dev sad
    with eidissolve_nd
    
    "Does it say something about me that the only seat left is beside me?"
    "It's not a bad seat,{w=0.3} and there's someone on my other side. But{w=0.2} now that I take a look, they've scooted closer to the seat to their left, conspicuously a few extra inches farther from me."
    
    show emily:
        transform_anchor True
        subpixel True
        yoffset 1.0 * 2250
        yanchor 1.0
        
        easein_cubic 0.50 rotate 2.0 
        easein_cubic 1 rotate -2.0
        easein_cubic 1 rotate 0.0
    
    "The chair creaks too as the brontosaur girl tries to adjust to the desk beside me, all while failing to make herself seem smaller."
    "Her long neck bends down at a painful angle and rests on the floor, not wanting to obscure the person behind her's view of the board."
    
    show emily:
        transform_anchor True
        subpixel True
        yoffset 0.0 * 2250
        yanchor 0.0

    show hawthorn left neutral:
        block:
            linear 0.05      ypos 0.015
            easein_cubic 0.2 ypos 0.01
            linear 0.05      ypos 0.015
            easein_cubic 0.2 ypos 0.01
            pause 0.5
            linear 0.05      ypos 0.015
            easein_cubic 0.2 ypos 0.01
            pause 0.25
            linear 0.05      ypos 0.015
            easein_cubic 0.2 ypos 0.01
            pause 1.0
            linear 0.05      ypos 0.015
            easein_cubic 0.2 ypos 0.01
            linear 0.05      ypos 0.015
            easein_cubic 0.2 ypos 0.01
            linear 0.05      ypos 0.015
            easein_cubic 0.2 ypos 0.01
            pause 0.5
            repeat

    with eidissolve_nd
    
    "Once she's done accommodating her head, the professor gets back to his lecture."
    
    
    show emily:
        easein_cubic 5 xpos 1.5
    show emihead:
        easein_cubic 5 ypos -0.5
    
    show dev thinking left
    show black behind dev:
        alpha 0.5
    with eidissolve_nd
    pause 0.3
    
    camera:
        subpixel True 
        pos (0, 0) zoom 1.0 
        easein_cubic 5 pos (-921, -20) zoom 1.52
    
    "I, too, get back to my battle against passing out from boredom.{w=0.3} I decide to write down any game-related idea I have,{w=0.2} or draw an asterisk on every topic that I can't remember anything about."
    "Math isn't my forte, never was,{w=0.2} but I do remember most of the topics Mr. Hawthorn lists on the black board. I wasn't half bad at them in high school, so I don't feel like paying that much attention anyway."
    "Back to thinking about other things."
    "Maybe we could just start simple.{w=0.3} Like a basic platformer? A point and click game?"
    
    show hawthorn grin right:
        ypos 0.0
    
    show emily:
        easein_cubic 0.5 xpos 0.95
    show emihead surprised:
        easein_cubic 0.5 ypos -0.1
    
    show dev shocked
    camera:
        subpixel True 
        pos (-921, -20) zoom 1.52 
        easein_cubic 0.5 pos (0, 0) zoom 1.0
    hide black
    with eidissolve_nd
    
    "Mr. Hawthorn claps once and I jump in my seat at the harsh sound."
    
    show dev neutral
    show emihead neutral
    with eidissolve_nd
    
    MrH "And that will be all for today.{w=0.3} For the rest of class, just study the material and be sure to copy all the notes on the board."
    
    show dev sad
    with eidissolve_nd
    
    MrH "All the information about upcoming tests will be posted at the end of the week, and all of the topics too."
    
    show emihead left neutral:
        subpixel True
        pos (0.5, -0.1) xrotate 0.0 rotate 0.0
        easein_cubic 2.00 pos (0.76, 0.04) xrotate 0.0 rotate -16.0

    show emily draw:
        pause 1
        block:
            linear 0.05      xpos 0.952
            easein_cubic 0.2 xpos 0.95
            linear 0.05      xpos 0.952
            easein_cubic 0.2 xpos 0.95
            pause 0.5
            linear 0.05      xpos 0.952
            easein_cubic 0.2 xpos 0.95
            pause 0.25
            linear 0.05      xpos 0.952
            easein_cubic 0.2 xpos 0.95
            pause 1.0
            linear 0.05      xpos 0.952
            easein_cubic 0.2 xpos 0.95
            linear 0.05      xpos 0.952
            easein_cubic 0.2 xpos 0.95
            linear 0.05      xpos 0.952
            easein_cubic 0.2 xpos 0.95
            pause 0.5
            repeat
    
    MrH "A list of references and suggested bibliography can be requested at the library,{w=0.2} just mention my name and the name of the course, and the librarian will give it to you."
    
    show hawthorn neutral:
        pause 0.3
        xzoom -1
        easein_quad 6 xpos -0.5
    
    show dev surprised
    with eidissolve_nd
    
    "Oh, shit{cps=5}...{/cps}"
    
    show dev yiik
    with eidissolve_nd
    
    "I realize that I haven't listened to a single thing he said,{w=0.2} besides some random tidbits that don't really connect to one another."
            
    show dev surprised
    with eidissolve_nd
    
    "The value of x will forever remain lost to me if things stay this way."
    
    show dev neutral
    with eidissolve_nd
    
    "I quickly copy everything on the board."
    
    show dev somber
    with eidissolve_nd
    
    "It's only the first day, I'll{cps=5}...{/cps} figure it out{cps=5}...{/cps} or something."
    
    show dev thinking right:
        parallel:
            xzoom 1
        parallel:
            easein_cubic 2 xpos 0.35
    
    show emily:
        easein_cubic 2 xpos 0.85
        pause 0.5
        block:
            linear 0.05      xpos 0.852
            easein_cubic 0.2 xpos 0.85
            linear 0.05      xpos 0.852
            easein_cubic 0.2 xpos 0.85
            pause 0.5
            linear 0.05      xpos 0.852
            easein_cubic 0.2 xpos 0.85
            pause 0.25
            linear 0.05      xpos 0.852
            easein_cubic 0.2 xpos 0.85
            pause 1.0
            linear 0.05      xpos 0.852
            easein_cubic 0.2 xpos 0.85
            linear 0.05      xpos 0.852
            easein_cubic 0.2 xpos 0.85
            linear 0.05      xpos 0.852
            easein_cubic 0.2 xpos 0.85
            pause 0.5
            repeat
    show emihead:
        easein_cubic 2 xpos 0.66
        
    with eidissolve_nd
    
    "Hmm."
    "The brontosaurus girl next to me seems to be writing quite a bit down. Bennett, was it?{w=0.3} But that's her surname, surely."
    "I wish Mr. Hawthorn had called her by her first name earlier. It would sound weird if I tried to get her attention with a \"Bennett!\" or a \"hey, girl!\""
    "Maybe a quick peek at her notes,{w=0.2} then I don't need to bother her."
    
    show emily_math_sketches1 with eidissolve_nd
    
    "I glance closer and see{cps=5}...{/cps}"
    "{cps=5}...{/cps}"
    "She wrote nothing down."
    "Even though she came in late, she hasn't even written down the notes from the board.{w=0.3} Her notebook is covered in detailed doodles that extend from one page to another."
    "Huh."
    "They're actually pretty good.{w=0.3} Like, jaw-droppingly good."
    "The one in the middle especially, it looks like some demon. The shading is uncannily realistic despite only being done in pencil."
    "Although looking at it more closely{cps=5}...{/cps} is that{cps=5}...{/cps}"
    "It's Mr. Hawthorn, but as some weird Japanese demon thing,{w=0.1} a big club on his back and an expression of anger like those on old Japanese samurai ink drawings."
    
    hide emily_math_sketches1
    show emihead sad
    show dev sad
    with eidissolve_nd
    
    "Guess she didn't take the dressing down he gave her well.{w=0.3} Can't blame her for that.{w=0.3} Had it been me in her place, well I don't quite know what I would do."
    
    show dev annoyed
    with eidissolve_nd
    
    "Probably drop dead from shame, to be honest."
    
    show dev neutral
    with eidissolve_nd
    
    "The drawing looks pretty cool though!"
    "Glancing up at the bronto to make sure she hasn't noticed me staring, I notice she looks{cps=5}...{/cps} sad?"
    
    show dev skeptical
    with eidissolve_nd
    
    "Does she not like her own drawing?{w=0.3} But it looks so good!"
    
    show dev somber
    with eidissolve_nd
    
    "Maybe I should compliment it?"
    
    show dev sad
    with eidissolve_nd
    
    "But,{w=0.3} would that come off as creepy?{w=0.3} Like I'm spying on her?"
    
    show dev thinking
    with eidissolve_nd
    
    "I guess I could ask her if she's doing alright,{w=0.2} then it's more like I'm only concerned about her."
    
    show dev thinking t_skeptical
    with eidissolve_nd
    
    "But I {i}am{/i} also just some random stranger,{w=0.2} so would I be overstepping?"
    
    menu:
        "Stop overthinking it and compliment her drawing!":
            jump ask_art
            #+1 Emily (She doesn't want to think about how she is a fuck-up, and complimenting her art is an ego boost)
        "Oh yeah, nothing is more creepy than someone showing some kindness! Ask her if she is alright.":
            jump ask_alright
        "As if I have the balls to just talk to some random girl. Keep quiet like the coward I am.":
            jump ignore

label ask_art:
    
    show dev happy:
        ease_cubic 1 xpos 0.37
    
    show emily:
        shudder(x=0.85)
        pause 0.1
        xpos 0.85
    
    show emihead surprised:
        shudder(0.66)
    with eidissolve_nd
    
    D "Hey, that's a cool drawing."
    
    show dev sad
    
    show emihead shocked:
        subpixel True
        ypos 0.04 rotate -16.0 
        easein_cubic 3.00 ypos -0.02 rotate 0.0 
    
    with eidissolve_nd
    
    "She freezes like a deer caught in headlights.{w=0.1} Slowly,{w=0.2} she lifts her head,{w=0.3} but her eyes remain hidden behind a curtain of messy hair."
    
    show dev skeptical
    with eidissolve_nd
    
    "I push on,{w=0.2} hoping to break the ice."
    
    show dev happy
    with eidissolve_nd
    
    D "Seriously,{w=0.1} it's amazing.{w=0.3} Did you draw that just now?"
    
    show emihead sad:
        subpixel True 
        rotate 0.0
        parallel:
            ease_cubic 0.5 rotate -2.0
        parallel:
            pause 0.49
            ease_cubic 0.5 rotate 0.0
        parallel:
            pause 0.98
            ease_cubic 0.5 rotate -2.0
        parallel:
            pause 1.47
            ease_cubic 0.5 rotate 0.0

    
    "Her face flushes red. She nods slightly but still doesn't meet my gaze."
    "Okay, so far so good?"
    
    show emihead neutral:
        rotate 0.0
        
    show dev somber
    with eidissolve_nd
    
    D "I couldn't help but notice it{cps=5}...{/cps} I-I wasn't spying on you or anything{cps=5}...{/cps}"
    
    show dev neutral
    with eidissolve_nd
    
    "She's just staring back at me{cps=5}...{/cps}"
    
    show dev somber
    with eidissolve_nd
    
    D "It's{cps=5}...{/cps} really detailed and uh{cps=5}...{/cps} neat{cps=5}...{/cps}"
    "She is giving me nothing to work with here,{w=0.3} her face is completely obscured by her hair and she hasn't said a word since she sat down."
    D "It's, uh{cps=5}...{/cps} Mr. Hawthorn as a demon or something, right?"
    
    show dev neutral
    with eidissolve_nd
    
    show emihead sad:
        subpixel True 
        rotate 0.0
        parallel:
            ease_cubic 0.5 rotate -2.0
        parallel:
            pause 0.49
            ease_cubic 0.5 rotate 0.0
        parallel:
            pause 0.98
            ease_cubic 0.5 rotate -2.0
        parallel:
            pause 1.47
            ease_cubic 0.5 rotate 0.0
    
    "She gives me a slight nod."
    "A reaction.{w=0.3} Progress!"
    
    show dev happy
    with eidissolve_nd
    if CIDA:
        D "I draw a little bit myself but you are way {b}way{/b} better than me."
    else:
        D "I mean, I'm not great at drawing or anything, but I can tell you've got talent."
    
    show emihead neutral
    show dev neutral
    with eidissolve_nd
    
    "Her shoulders relax a bit. She tilts her head slightly as if considering my words."
    
    show dev happy
    with eidissolve_nd
    
    D "I'd love to see more of your drawings if you don't mind."
    
    show emily_math_sketches2 with eidissolve_nd
    
    "Her head darts to the side before she slowly turns the page in her sketchbook. There are more drawings{w=0.1} - landscapes,{w=0.1} creatures,{w=0.1} abstract shapes - all meticulously detailed."
    D "Wow, these are awesome."
    "She glances at me again and this time there's the tiniest hint of a smile on her lips."
    "I point to one of the drawings that looks like some sort of futuristic cityscape."
    D "This one is incredible.{w=0.3} The details are insane. I can't even imagine how long it took you."
    
    
    show emihead happy
    show emily showdrawing1
    with eidissolve_nd
    hide emily_math_sketches2
    
    "Her face lights up with a shy smile and she gestures towards another drawing as if to say \"look at this one too\"."
    
    show dev neutral:
        ease_cubic 1 xpos 0.4
    show emily showdrawing2
    
    "I lean in closer and notice the intricate lines and shading in each piece. It's clear she puts a lot of thought and effort into her work."
    D "Do you do this often?"
    
    show emihead neutral:
        subpixel True 
        rotate 0.0
        parallel:
            ease_cubic 0.5 rotate -1.0
        parallel:
            pause 0.49
            ease_cubic 0.5 rotate 0.0
        parallel:
            pause 0.98
            ease_cubic 0.5 rotate -1.0
        parallel:
            pause 1.47
            ease_cubic 0.5 rotate 0.0
    show emily:
        pause 0.1
        ease_cubic 0.5 ypos 0.07
        ease_cubic 0.5 ypos 0.1
    
    "She shrugs, nodding lightly."
    D "Well,{w=0.3} if you ever want to share more of your work, I'd love to see it."
    
    jump talk_emily
    
label ask_alright:
    
    show dev happy:
        ease_cubic 1 xpos 0.37
    
    show emily:
        shudder(x=0.85)
        pause 0.1
        xpos 0.85
        
    with eidissolve_nd
    
    show emihead surprised:
        shudder(0.66)
    with eidissolve_nd
    
    D "Hey,{w=0.3} you okay?"
    
    show dev sad
    
    show emihead shocked:
        subpixel True
        ypos 0.04 rotate -16.0 
        easein_cubic 3.00 ypos -0.02 rotate 0.0 
    
    with eidissolve_nd
    
    "She turns her head towards me, but with her face nearly completely covered in hair,{w=0.3} it's hard to get a read on her."
    
    show dev somber
    with eidissolve
    
    D "Uh,{w=0.3} I saw what happened earlier.{w=0.1} That was kinda rough."
    
    show emihead neutral
    with eidissolve
    
    "No response.{w=0.1} Not even a nod or a shake of her head. Just more silence and awkwardness."
    
    show dev neutral
    with eidissolve
    
    "{cps=5}...{/cps}"
    "She's giving me nothing to work with.{w=0.3} I try to focus on her expression under all the hair, but all I can see is the very tip of her nose and her mouth."
    D "You were looking down and{cps=5}...{/cps} uh{cps=5}...{/cps} I figured I'd make sure you were ok{cps=5}...{/cps}"
    
    show emihead:
        parallel:
            choice:
                "emihead left annoyed" with eidissolve
            choice:
                "emihead left shocked" with eidissolve
            choice:
                "emihead left surprised" with eidissolve
            choice:
                "emihead left sad" with eidissolve
            choice:
                "emihead left neutral" with eidissolve
            pause 0.65
            repeat
        parallel:
            movex(0.6775)
            movex(0.6675)
            repeat
    
    "Her lips go through a whole series of different emotions in rapid sequence before settling on a weak smile."
    
    show emihead happy:
        ease_cubic 1 xpos 0.66
    
    show dev skeptical
    with eidissolve
    
    "Maybe she's just really shy? I can sympathize with that."
    
    show dev neutral
    with eidissolve
    
    Emu "...{w=0.3} ..."
    
    show dev skeptical
    with eidissolve
    
    "I see her mouth move, but I don't hear anything."
    
    show dev somber
    with eidissolve
    
    D "I'm sorry, I couldn't hear you."
    
    show emihead neutral
    show dev neutral
    with eidissolve
    
    Emu "...{w=0.3} ..."
    "Again,{w=0.3} her mouth moves, but nothing comes out of it."
    "I had guessed earlier that I couldn't hear her response to Mr. Hawthorn because of the distance between us,{w=0.3} but now I'm not so sure."
    
    show dev skeptical
    with eidissolve
    
    "I think I can hear a faint whisper, but even with how quiet it is in the class now that most of the students have stormed out, it's impossible to be sure."
    "Maybe she's just {i}insanely{/i} shy?"
    
    show emihead annoyed
    show dev somber
    with eidissolve
    
    D "I'm really sorry, I can't hear you.{w=0.1} Could you speak a little louder?"
    
    show emihead sad:
        ease_cubic 1 ypos 0.05
    show dev sad
    with eidissolve
    
    "Her mouth and neck drop at my comment. She buries herself deeper into her hoodie, quickly closing her notebook."
    "Did I say something wrong?{w=0.3} I feel bad about my insistent tone, I shouldn't have done that."
    "I've made her uncomfortable and now I'm feeling just as uncomfortable and terrible too."
    
    show dev:
        ease_cubic 1 xpos 0.43
    
    show emihead left:
        subpixel True
        pos (0.66, 0.05) rotate 0.0
        easein_cubic 2.00 pos (0.66, 0.04) xrotate 0.0 rotate -16.0
    show emily:
        pause 1
        block:
            linear 0.05      xpos 0.855
            easein_cubic 0.2 xpos 0.85
            linear 0.05      xpos 0.855
            easein_cubic 0.2 xpos 0.85
            pause 0.5
            linear 0.05      xpos 0.855
            easein_cubic 0.2 xpos 0.85
            pause 0.25
            linear 0.05      xpos 0.855
            easein_cubic 0.2 xpos 0.85
            pause 1.0
            linear 0.05      xpos 0.855
            easein_cubic 0.2 xpos 0.85
            linear 0.05      xpos 0.855
            easein_cubic 0.2 xpos 0.85
            linear 0.05      xpos 0.855
            easein_cubic 0.2 xpos 0.85
            pause 0.5
            repeat
    
    "I'm about to apologize, but she turns away from me."
    
    "Great."
    
    show dev ashamed left
    with eidissolve_nd
    
    "Perfect job, Dev."
    
    show dev sad
    with eidissolve_nd
    
    "You barely said anything to her, and she already hates you.{w=0.3} I {i}knew{/i} I should have just kept my big mouth shut. I scratch my bald head harshly, my fingernails surely leaving red marks along my scalp."
    
    show emihead neutral:
        subpixel True 
        ypos 0.04 rotate -16.0 
        easein_cubic 3.00 ypos -0.02 rotate 0.0 
    show emily:
        xpos 0.84
    
    with eidissolve_nd
    
    "I give a brief consideration to the time, but I still have a two hours hour before my next class{cps=5}...{/cps}"
    
    show emihead neutral
    show emily:
        pause 0.1
        easein_quad 2 xpos 0.65
        pause 0.2
        ease_cubic 1 xpos 0.7
    with eidissolve_nd    
    
    "Just as I'm about to think myself into a self-deprecating spiral though, I feel a finger poke my shoulder."
    
    show emihead happy
    show emily:
        easein_quad 2 xpos 0.85
    
    show dev surprised right:
        ease_cubic 1 xpos 0.4
    with eidissolve_nd 
    
    "It's the bronto girl again."
    
    show dev skeptical
    show emily showdrawing2
    with eidissolve_nd
    
    "She's sliding a piece of paper over to me."
    "It's a picture of her,{w=0.3} her long neck now comically longer and twisting around so it spells out \"Thank You\" in cursive. At the end is her head, her eyes looking in different directions, with her tongue sticking out and tied into a knot."
    
    show dev somber
    show emily neutral
    with eidissolve_nd
    
    "Heh."
    
    jump talk_emily

label ignore:

    show dev neutral
    with eidissolve_nd
    
    "She's imposing,{w=0.1} silent,{w=0.1} and talented, and her sheer artistic prowess intimidates me almost as much as her size and whole weird vibe."
    
    show dev thinking
    with eidissolve_nd
    
    "I'll admit,{w=0.3} she doesn't look like she has it all together. I get why Mr. Hawthorn was upset with her{w=0.1} - she came in late and caused a bit of a ruckus, disrupting the class."
    
    stop music fadeout 40
    
    show emily:
        easein_cubic 5 xpos 1.5
    show emihead:
        easein_cubic 5 ypos -0.5
    
    show dev thinking t_skeptical left
    show black behind dev:
        alpha 0.25
    with eidissolve_nd
    pause 0.3
    
    camera:
        subpixel True 
        pos (0, 0) zoom 1.0 
        easein_cubic 5 pos (-100, -200) zoom 1.52                
    
    "She didn't even apologize before sitting down, though I can't really tell if that was due to arrogance or just shyness."
    
    show dev sad
    with eidissolve_nd
    
    "Despite that,{w=0.3} I'd rather not add to her embarrassment. Not only on our first day, but right after Mr. Hawthorn ridiculed her in front of the entire class."
    
    show dev annoyed
    with eidissolve_nd
    
    "That wasn't cool."
    
    show dev skeptical right
    with eidissolve_nd
    
    "Mr. Hawthorn made a good impression on me, but{w=0.2} considering how he welcomed this Bennett girl, maybe he's got a harsher personality than I expected."
    
    play ambience anxiety_ambient fadein 10 volume 4 loop
    
    show black behind dev:
        ease_cubic 5 alpha 0.50
    with eidissolve_nd
    
    "Point is, the guy's mean, the girl's odd, and I'm a chicken."
    
    show dev skeptical
    with eidissolve_nd
    
    "Okay, maybe if I were a chicken, things would be easier for me because birds are related to dinosaurs. Aren't they?"
    
    show dev sad
    with eidissolve_nd
    
    "More than humans like me are."
    
    show dev ashamed left
    with eidissolve_nd
    
    "Come to think of it,{w=0.3} what if she's uncomfortable because I'm a human? We still aren't that common in some towns, and for all I know, I could be the first one she's ever been this close to."
    
    show black behind dev:
        ease_cubic 5 alpha 0.75
    with eidissolve_nd
    
    "Maybe my mere presence is creeping her out."
    
    show dev sad
    with eidissolve_nd
    
    "{cps=5}...{/cps}"
    "I knew this might happen when I decided to go here, but the idle thought still stings.{w=0.3} What if this happens again during my next class? And the one after that?"
    
    show dev ashamed
    with eidissolve_nd
    
    "Is this what the next handful of years here are going to be like?{w=0.3} Judgment because of what I am?"
    "Maybe I made a mistake coming here after all{cps=5}...{/cps}"
    
    stop ambience
    
    show dev surprised
    with eidissolve_nd
    
    "A note falls softly in front of me. It's a piece of torn paper, the remnants of doodles seen on its edges.{w=0.3} In the middle, it says something:"
    
    show dev skeptical
    with eidissolve_nd
    
    "{font=BrownBagLunch.ttf}{size=+40}Are you okay?{/size}{/font}"
    "The world pauses for a moment as I force my breathing to return to a normal rhythm."
    
    play music half_past_math fadein 10
    
    show emily neutral:
        easein_cubic 0.5 xpos 0.85
    show emihead sad:
        xzoom 1
        rotate 0.0
        easein_cubic 0.5 xpos 0.66 ypos -0.02
    
    show dev sad right:
        ease_cubic 0.7 xpos 0.4
    camera:
        subpixel True 
        pos (-100, -200) zoom 1.52 
        easein_cubic 0.5 pos (0, 0) zoom 1.0
    hide black
    with eidissolve_nd
    
    "The note snaps me out of my cascading thoughts, and my jaw slackens as I struggle to formulate an answer."
    "Her head turns to me, bushy brown hair covering what looks like a worried expression,{w=0.2} judging by her pursed lips and hunched shoulders."
    
    show emihead neutral
    show dev somber
    with eidissolve_nd
    
    D "Uh, I'm f'okay- Fine!{w=0.3} Okay. Yes.{w=0.2} I'm good."
    
    show dev:
        chuckle(y=0.1)
    with eidissolve_nd
    
    "I chuckle nervously, trying to recover from the faux-pas."
    
    show dev skeptical
    with eidissolve_nd
    
    D "I guess I was just{cps=5}...{/cps} getting a little {i}too{/i} into my own head there for a second."
    
    show emihead happy
    with eidissolve_nd
    
    "She gives an understanding smile back, nodding at the sentiment.{w=0.3} Despite catching me off-guard, the gesture does wonders to calm my nerves and I find myself following up with more explanation."
    
    show dev somber
    with eidissolve_nd
    
    D "And uh,{w=0.1} th-thanks for asking,{w=0.3} first day jitters I guess. Never really been this far from home, you know?"
    
    show dev skeptical
    show emihead:
        subpixel True 
        rotate 0.0
        parallel:
            ease_cubic 0.5 rotate -1.0
        parallel:
            pause 0.49
            ease_cubic 0.5 rotate 0.0
        parallel:
            pause 0.98
            ease_cubic 0.5 rotate -1.0
        parallel:
            pause 1.47
            ease_cubic 0.5 rotate 0.0
    with eidissolve_nd
    
    "She nods before patting her chest twice."
    
    show emihead annoyed
    show dev sad
    with eidissolve_nd
    
    D "Uh{cps=5}...{/cps} I{w=0.1}-I'm not completely sure what you mean by that. S-{w=0.1}sorry{cps=5}...{/cps}"    
    "She turns and grabs her note book, writing something down before handing it off to me."
    
    show emihead happy
    show dev somber
    with eidissolve_nd
    
    Emu "Me too."
    "She gives me a sheepish grin."
    
    show dev ashamed
    with eidissolve_nd
    
    "Of course, why didn't I guess that? Real smooth, Dev. I've practically forgotten how to converse like a normal person recently."
    
    show dev thinking
    with eidissolve_nd
    
    "Weird though she may be, there's something undeniably easy about talking to her."
    
    show dev thinking t_skeptical
    with eidissolve_nd
    
    "Or at her.{w=0.3} Is that mean to say?"
    
    show emily_math_sketches2 with eidissolve_nd
    
    "Either way,{w=0.2} I find myself mirroring her smile as she angles her notebook towards me again. I see the drawing she was working on before, but then she turns the page,{w=0.2} revealing yet more drawings."
    
    show dev happy
    hide emily_math_sketches2
    with eidissolve_nd
    
    "Only art:{w=0.3} not a number or note in sight."
    "I let out a snicker."
    
    show dev somber
    with eidissolve_nd
    
    D "Guess we're both lost causes."
    
    show emihead sad
    show dev sad
    with eidissolve_nd
    
    "A flash of hurt crosses her face, and for a moment I feel like I've blown it."
    
    show emihead happy
    show dev somber
    with eidissolve_nd
    
    "Thankfully,{w=0.3} it gives way to a little shrug from her, and her expression widens back into a smile."
    
    show dev surprised
    with eidissolve_nd
    
    "Just as I'm about to leave to preserve this blooming friendship from my own dumb mouth,{w=0.3} I realize I haven't even gotten her name yet."

    jump talk_emily

label talk_emily:

    show emihead neutral
    show dev neutral
    with eidissolve_nd
    
    D "I'm Dev, by the way."
    
    show emihead:
        subpixel True 
        rotate 0.0
        parallel:
            ease_cubic 0.5 rotate -1.0
        parallel:
            pause 0.49
            ease_cubic 0.5 rotate 0.0
        parallel:
            pause 0.98
            ease_cubic 0.5 rotate -1.0
        parallel:
            pause 1.47
            ease_cubic 0.5 rotate 0.0
    
    "She nods and closes her note book and pushes it towards me. On the top is the name \" {font=BrownBagLunch.ttf}{size=+25}Emily{/size}{/font} \"."
    
    show dev happy
    with eidissolve_nd
    
    D "Nice to meet you, Emily."
    
    show emihead happy:
        subpixel True 
        rotate 0.0
        parallel:
            ease_cubic 0.5 rotate -1.0
        parallel:
            pause 0.49
            ease_cubic 0.5 rotate 0.0
        parallel:
            pause 0.98
            ease_cubic 0.5 rotate -1.0
        parallel:
            pause 1.47
            ease_cubic 0.5 rotate 0.0
    with eidissolve_nd
    
    "She gives a small smile and nods again."
    
    if devnumba1:
        "Suddenly,{w=0.3} I'm acutely aware of her gaze as it drifts up to my forehead."
        
        show emihead neutral
        show dev sad
        with eidissolve_nd
        
        "So this is gonna plague me all day, huh?"
        
        show dev annoyed
        with eidissolve_nd
        
        "Freaking Theo{cps=5}...{/cps}"
        "She writes in the margins of her notebook."
        
        show dev skeptical
        with eidissolve_nd
        
        Et "Why is there a #1 on your forehead?"
        
        show dev somber
        with eidissolve_nd
        
        D "It's{cps=5}...{/cps} it's a freshman thing."
        
        show emihead annoyed
        with eidissolve_nd
        
        Et "No{cps=5}...{/cps} it isn't."
        
        show dev annoyed
        with eidissolve_nd
        
        "I facepalm to hide my growing shame before the sound of wispy chortles draws my attention back to Emily."
        
        show emihead happy
        show dev sad
        with eidissolve_nd
        
        Et "It's okay. It doesn't look too weird."
        D "Somehow I doubt that,{w=0.3} but thanks."
    
    show emihead neutral
    show dev neutral
    with eidissolve_nd
    
    "Now that we're actually on a first name basis, I realize I could still use any help I can get.{w=0.3} I take a deep breath in preparation, maybe she took {i}some{/i} notes? Better than the nothing I currently have."
    
    show dev skeptical
    with eidissolve_nd
    
    D "Hey,{w=0.1} I know it's a long shot since you came in late, but{w=0.3} you wouldn't happen to take notes on what the professor went over would you?"
    
    show emihead happy
    show dev somber
    with eidissolve_nd
    
    D "I{cps=5}...{/cps} kind of zoned out for some of the class.{w=0.3} Most of it, honestly."
    
    show emihead:
        chuckle(y=-0.02)
    show emily:
        chuckle(y=0.1)
    with eidissolve_nd
    
    "She mutely snickers at that before digging through her bookbag. After a moment,{w=0.2} she pulls out a weathered notebook and flips deftly through it to reveal the very notes I need."
    "Huh, I guess she did take notes after all."
    
    show dev sad
    with eidissolve_nd
    
    "Great job Dev,{w=0.1} even the girl that came in late is more prepared and focused than you."
    
    show dev neutral
    with eidissolve_nd
    
    "I take out my phone and just snap a photo of the notes. Work smarter, not harder and all that."
    
    show dev happy
    with eidissolve_nd
    
    D "Thanks,{w=0.1} I appreciate it."
    "I still have quite a while until my next class. Might as well use the time."
    
    show emihead neutral
    show dev neutral
    with eidissolve_nd
    
    D "So{cps=5}...{/cps} you majoring in art?"
    "She tilts her head."
    
    show dev thinking
    with eidissolve_nd
    
    D "I was just assuming based on all those drawings and doodles.{w=0.3} They're really good."
    
    show emihead sad
    show dev skeptical
    with eidissolve_nd
    
    "She looks down at her notebook again. Her face briefly shows a bit of sadness before she turns back to me and shakes her head."
    
    show emihead neutral
    show dev neutral
    with eidissolve_nd
    
    "Yet again she digs around in her bag and pulls out a sheet I recognize as a college schedule. She points to several entries."
    "Animal Science,{w=0.1} agriculture business,{w=0.1} horticulture."
    
    show dev surprised
    with eidissolve_nd
    
    D "You're a farmer?"
    
    show emihead cheerful:
        subpixel True 
        rotate 0.0 
        easein_quad 0.2 rotate -2.0 
        easeout_quad 0.2 rotate 0.0 
        easein_quad 0.2 rotate -2.0 
        easeout_quad 0.2 rotate 0.0
        easein_quad 0.2 rotate -2.0 
        easeout_quad 0.2 rotate 0.0 
    show dev neutral
    with eidissolve_nd
    
    "She nods her head enthusiastically."
    
    show emihead happy
    show dev happy
    with eidissolve_nd
    
    D "That's cool! I've worked on a farm before too, you know. Nothing all that fancy, just a summer job."
    
    show dev skeptical
    with eidissolve_nd
    
    D "Was hoping I would get to drive one of those big tractors but all I ended up doing was cleaning up messes and getting half my pant leg eaten by a pig."
    
    show emihead:
        chuckle(y=-0.02)
    show emily:
        pause 0.05
        chuckle(y=0.1)
    show dev unimpressed
    with eidissolve_nd
    
    "She lets out a mousy laugh, and I frown in mock annoyance."
    
    show dev somber
    with eidissolve_nd
    
    D "H{w=0.1}-hey, those things are terrifying!"
    
    show dev skeptical
    with eidissolve_nd
    
    "I can't help but notice something off about her laugh. It sounded odd, more like she was choking than chuckling."
    
    show dev sad
    with eidissolve_nd
    
    "Yeesh{cps=5}...{/cps}"
    "She must have a cold or something."
    "Well,{w=0.3} at least that would explain her lack of speech."
    
    show emihead surprised
    show dev surprised:
        hitx(0.4, i=1.2, s=1.5)
    with eidissolve_nd
    
    "My stomach growls loudly, pulling me out of my train of thought. I cringe at the inopportune noise."
    
    show emihead cheerful
    with eidissolve_nd
    
    "Emily glances at me, her lips twitching in what I can swear is amusement."
    
    show dev somber
    with eidissolve_nd
    
    D "Uh,{w=0.1} sorry about that.{w=0.3} I kinda skipped breakfast this morning.{w=0.3} Probably should go grab something to eat before my next class."
    
    show emihead happy:
        ease_cubic 1 ypos -0.13
    show emily:
        ease_cubic 1 ypos 0.0
    show dev neutral:
        ease_cubic 1 ypos 0.0
    with eidissolve_nd
    
    "I stand up and start grabbing my things, and a moment later Emily does the same."
    
    show dev left
    pause 1
    show dev right
    with eidissolve_nd
    
    "It's only now that I notice that we're the only ones left in the room other than the professor."
    
    #there seems to be a error when choicing option 3
    show emihead right:
        parallel:
            pause 0.01
            ease_quad 3 xpos 0.8
        parallel:
            pause 3.3
            "emihead left shocked" with eidissolve
    
    show emily right:
        parallel:
            pause 0.01
            ease_quad 3 xpos 0.95
        parallel:
            pause 3.3
            "emily left" with eidissolve
    
    show dev neutral right:
        parallel:
            ease_quad 3 xpos 0.6
        parallel:
            pause 3
            choice:
                "dev surprised" with eidissolve
                xzoom(-1.0)
    show hawthorn annoyed left:
        ease_quad 3 xpos 0.1
    with eidissolve_nd
    
    "Just as we're both about to leave, Mr. Hawthorn's voice calls out."
    
    show emihead sad left:
        xpos 0.8
    show emily left:
        xpos 0.95
    show dev skeptical
    with eidissolve_nd
    
    MrH "Miss Bennettt,{w=0.1} could you stay behind for a moment? I'd like to discuss something with you."
    
    show dev sad left
    with eidissolve_nd
    
    "Emily freezes,{w=0.1} her shoulders sagging slightly. She looks over at me, and I can see the embarrassment in the set of her mouth. I give her a sympathetic smile."
    
    show dev somber
    with eidissolve_nd
    
    D "Well, uh,{w=0.3} see you around?"
    
    show emihead:
        subpixel True 
        rotate 0.0
        parallel:
            ease_cubic 0.5 rotate -2.0
        parallel:
            pause 0.49
            ease_cubic 0.5 rotate 0.0

    show dev:
        pause 2
        easein_quad 6 xpos 1.5
    with eidissolve_nd
    
    "She nods again, her head bobbing up and down slowly. I hesitate for a moment before turning on my heel and heading towards the door."

    window auto hide
    
    stop music fadeout 5
    
    pause 0.25

    scene black with eDissolve(2)

    pause 2
    
    hide emily
    hide emihead
    hide dev
    hide hawthorn

####PART 3####

    play music daydreaming fadein 3.0
    play ambience school_cafeteria_ambience volume 2 fadein 3.0 loop
    
    show cafeteria_summer behind black
    hide black with Dissolve(1)
    window auto show

    pause .5
    
    show dev at moveinright(0.15, m=0.5)
    with eidissolve_nd

    "Lunch is another part of college I hadn't accounted for."
    
    show dev thinking:
        ease_cubic 5 xpos 0.175
    with eidissolve_nd
    
    "Back in high school, we followed a strict schedule.{w=0.3} I could always rely on being able to eat at the same time every day."
    
    show dev sad:
        ease_cubic 5 xpos 0.2
    with eidissolve_nd
    
    "Now, though?{w=0.3} My jumbled schedule is set in such a way that I have to find time whenever I can to eat.{w=0.3} This place certainly isn't holding my hand when it comes to fending for myself outside of class."
    
    show dev neutral left
    with eidissolve_nd
    
    "The wide dining hall with all of its stations and cooking staff is open during regular class hours only.{w=0.3} I guess the college must see dinner as a business left to students to solve either with the vending machines or the local dining establishments."
    
    show dev skeptical right:
        ease_cubic 5 xpos 0.25
    with eidissolve_nd
    
    "Some nearby restaurants offer students like me discounts on some of their menu items, but I'm as new to the college as I am to the area."
    "I'll have to ask around for opinions on whose pizza lasts the longest in the fridge or which place's tacos won't make me sick."
    
    show dev happy
    with eidissolve_nd
    
    "Better for me to focus on the long-term issues, right?"

    ## Dev pulls out Phone and gets into a line of people
    
    show dev neutral:
        ease_cubic 2 xpos 0.4
    show c_standing1 at moveinleft(0.6):
        matrixcolor ColorizeMatrix("#559b3e", "#ffffff")
    show c_standing2 at moveinleft(0.75):
        matrixcolor ColorizeMatrix("#9b3e4c", "#ffffff")
    show c_standing3 at moveinleft(0.95):
        matrixcolor ColorizeMatrix("#7e3e9b", "#ffffff")
    with eidissolve_nd

    "I pull out my phone as I get in the lunch line."
    "Of course, a college of computing has an app to track classes, grades, important notifications coming directly from the administration and some forums for official clubs and events."
    "It's also a great place to set a calendar with test dates, but I figure that those change so much that they won't bother to update it. Too bad,{w=0.3} I bet a lot of students would find that helpful, myself included."
    
    show rebecca at moveinright(x=0.03, y=0.1):
        matrixcolor BrightnessMatrix(-1.0)
        alpha 0
        ease_cubic 5 alpha 0.3
        
    
    show dev skeptical:
        ease_quad 0.9 xpos 0.55
    show c_standing1:
        ease_quad 0.9 xpos 0.75
    show c_standing2:
        ease_quad 0.9 xpos 0.95
    show c_standing3:
        ease_quad 0.9 xpos 1.5

    "Huh,{w=0.3} it looks like I have a request from the counselor to have a meeting today.{w=0.1} I can probably just make it before my next class."
    
    show dev sad
    show rebecca:
        alpha 0.3
        ease_cubic 5 alpha 0.5
    
    show c_texting2 behind dev at moveinright(0.35):
        matrixcolor ColorizeMatrix("#989b3e", "#ffffff")
    
    with eidissolve_nd

    "I hope it isn't anything serious. It brings to mind how Elliot said something about the entire general studies course being my doing."
    
    show dev happy
    with eidissolve_nd
    
    "Then,{w=0.2} a quick browse through my college account tells me that the funds made it to my virtual wallet sooner than expected."
    "Which means that I{nw}"

    hide c_standing3
    
    show rebecca:
        ease_quad 0.9 xpos 0.2
        alpha 0.5
        ease_cubic 3 alpha 1
    show c_texting2:
        ease_quad 0.9 xpos 0.55    
    show dev:
        ease_quad 0.9 xpos 0.75
    show c_standing1:
        ease_quad 0.9 xpos 0.95
    show c_standing2:
        ease_quad 0.9 xpos 1.5
    show dev thinking

    if LUNCH:
        extend" am able to buy a warm meal without relying on handouts anymore."
    else:        
        extend" won't have to satisfy my hunger with mystery-flavored food bars of suspicious origin."

    hide c_standing2
    
    show c_texting2:
        ease_quad 0.9 xpos 0.75    
    show dev neutral:
        ease_quad 0.9 xpos 0.95
        pause 1.5
        choice:
            "dev left sad"
    show c_standing1:
        ease_quad 0.9 xpos 1.5
    show rebecca neutraldown:
        alpha 1
        ease_cubic 1 matrixcolor BrightnessMatrix(0.0)
        typing
        
    with eidissolve_nd

    "I'm second in line to fill my tray with the day's special.{w=0.3} Scanning the packed cafeteria when I notice Rebecca sitting alone, again. She's the only familiar face in this sea of dinosaurs."
    
    hide c_standing1
    
    show rebecca neutraldown with eidissolve_nd:
        matrixcolor BrightnessMatrix(0.0)
        typing

    show dev right neutral:
        pause 0.5
        hop(h=0.02)
        pause 0.5
        choice:
            "dev left"
        ease_quad 2 xpos 0.75
    show c_texting2:
        pause 1.4
        ease_quad 0.9 xpos 0.95
    with eidissolve_nd
        

    "Once I've paid for my food, my feet start moving towards her."
    
    show dev sad left
    with eidissolve_nd
    
    "Wait,{w=0.3} do I really want to do this?{w=0.3} She wasn't exactly{cps=5}...{/cps} friendly yesterday."

    show dev:
        parallel:
            ease_quad 2 xpos 0.80
        parallel:
            pause 1.8
            choice:
                "dev terrified"
            easein_bounce 0.2 xpos 0.77
    show c_texting2:
        pause 2.1
        choice:
            "c_texting2 left"
        
    
    "I take a step back, nearly bumping into someone behind me."
    
    show dev right ashamed
    show c_texting2 left:
        pause 1
        choice:
            "c_texting2 right"

    D "Sorry."

    show dev left neutral
    show c_texting2 right:
        ease_quad 0.9 xpos 1.5

    "Rebecca hasn't noticed me yet. She's hunched over, typing furiously on her laptop."
    
    hide c_texting2

    "At the same time, she's idly sipping soda through a straw and eating strips of bacon with{cps=5}...{/cps} chopsticks?"
    
    show dev skeptical
    with eidissolve_nd
    
    "Interesting choice."
    
    show dev sad
    with eidissolve_nd
    
    "Alright. Do I want to try to sit with the girl who only wanted me to get lost yesterday?"
    
    show dev thinking
    with eidissolve_nd
    
    "Maybe I should just eat outside?{w=0.3} It's a sunny day, and the trees have benches under them. The surrounding foliage gives the whole scenery a zen feel."
    
    show dev sad
    with eidissolve_nd
    
    "But the exit takes me right past her table anyways{cps=5}...{/cps}"
    
    show dev sad
    with eidissolve_nd
    
    "{i}Come on, Dev,{w=0.2} it's just lunch.{w=0.3} Not like she's going to bite your head off.{/i}"

    show dev skeptical
    with eidissolve_nd
    
    "But then again, she's a raptor. {w=0.3}{i}Do{/i} raptors bite heads off?"
    
    show dev sad
    with eidissolve_nd
    
    "Is even thinking that racist?{w=0.3} Note to self: Gruugle that later."

    show dev neutral:
        ease_quad 1.2 xpos 0.75
    show rebecca:
        ease_quad 1.2 xpos 0.25
        pause 0.2
        typing
        
        
    "I take a deep breath and start walking towards her table. Either way, I need to make a decision quickly."

    menu:
        "Sit with her":
            show dev sad:
                ease_quad 0.9 xpos 0.7

            "I take a deep breath and approach Rebecca's table. My palms are sweating profusely and my heart's trying to escape my chest.{w=0.3} Here goes nothing."

            show dev somber:
                parallel:
                    ease_quad 1.2 xpos 0.6
                parallel:
                    pause 0.3
                    ease_cubic 1 ypos 0.1
            show rebecca surprised:
                ypos 0.1
            with eidissolve_nd

            "I plop down across from her without a word and offer her a smile. Smooth AF."
            
            show rebecca annoyed:
                ypos 0.1
            with eidissolve_nd
            
            "Rebecca's head snaps up, her eyes narrowing."
            
            show dev sad
            show rebecca angry
            with eidissolve_nd

            R "Excuse me?"
            
            show dev somber
            with eidissolve_nd

            D "H-{w=0.1}hey."

            show rebecca:
                setx(0.25)
                backmovey(0.1)
                block:
                    linear 0.05      ypos 0.105
                    easein_cubic 0.2 ypos 0.1
                    linear 0.05      ypos 0.105
                    easein_cubic 0.2 ypos 0.1
                    pause 0.5
                    linear 0.05      ypos 0.105
                    easein_cubic 0.2 ypos 0.1
                    pause 0.25
                    linear 0.05      ypos 0.105
                    easein_cubic 0.2 ypos 0.1
                    pause 1.0
                    linear 0.05      ypos 0.105
                    easein_cubic 0.2 ypos 0.1
                    linear 0.05      ypos 0.105
                    easein_cubic 0.2 ypos 0.1
                    linear 0.05      ypos 0.105
                    easein_cubic 0.2 ypos 0.1
                    pause 0.5
                    repeat
            with eidissolve_nd

            "She glares at me,{w=0.3} her claws still tapping away on her laptop."

            R "Is it a normal skinnie custom to just sit at someone's table without asking?"
            
            show dev skeptical
            with eidissolve_nd

            "\"Skinnie\"?"
            
            show rebecca skeptical
            show dev happy
            with eidissolve_nd

            D "No, I just{cps=5}...{/cps} thought{cps=5}...{/cps}"
            
            show dev somber
            with eidissolve_nd

            "My brain's desperately searching for words, but it's coming up empty."
            
            show dev sad:
                ease_quad 0.3 ypos 0.0
            
            "I feel my face burning. This was a mistake. A huge, embarrassing mistake. I stand up so fast I nearly spill my entire tray."
            
            show rebecca surprised
            show dev sad
            with eidissolve_nd
            
            D "I'm sorry, I'll just{cps=5}...{/cps} go. Sorry for bothering you."

            show dev right:                
                ease_quad 1.2 xpos 0.65
            show rebecca annoyedconsidering:
                backmovey(0.1)
            with eidissolve_nd

            "As I turn to leave, Rebecca sighs loudly."
            
            show rebecca angry
            show dev neutral left
            with eidissolve_nd

            R "Oh, for fuck's sake.{w=0.2} Sit down."

            show dev surprised
            with eidissolve_nd

            "I freeze, caught between fleeing and staying."
            
            show dev skeptical
            with eidissolve_nd
            
            D "{w=0.3}What?"
            
            show rebecca point
            with eidissolve_nd
            
            R "Sit.{w=0.1} Down."

            "I still don't move."
            
            show rebecca grumpy
            with eidissolve_nd

            R "Great, now you're making me look like an asshole. Just sit already."
            
            show rebecca annoyed
            show dev neutral:
                parallel:
                    ease_quad 1.2 xpos 0.6
                parallel:
                    pause 0.3
                    ease_cubic 1 ypos 0.1

            "I slowly lower myself back into the chair, feeling like I'm navigating a minefield."
            
            show rebecca ugh
            show dev somber
            with eidissolve_nd

            D "I{cps=5}...{/cps} uh{cps=5}...{/cps} thanks?"
            
            show rebecca angry
            show dev ashamed
            with eidissolve_nd

            R "D{w=0.1}-don't thank me!"
            
            show rebecca annoyedconsidering
            show dev sad
            with eidissolve_nd

            R "God{cps=5}...{/cps} just,{w=0.3} stop making this so damn awkward{cps=5}...{/cps}"
            
            show dev skeptical
            with eidissolve_nd

            "{i}She's{/i} the one making such a big deal about this!"

            show rebecca neutraldown:
                setx(0.25)
                backmovey(0.1)
                block:
                    linear 0.05      ypos 0.105
                    easein_cubic 0.2 ypos 0.1
                    linear 0.05      ypos 0.105
                    easein_cubic 0.2 ypos 0.1
                    pause 0.5
                    linear 0.05      ypos 0.105
                    easein_cubic 0.2 ypos 0.1
                    pause 0.25
                    linear 0.05      ypos 0.105
                    easein_cubic 0.2 ypos 0.1
                    pause 1.0
                    linear 0.05      ypos 0.105
                    easein_cubic 0.2 ypos 0.1
                    linear 0.05      ypos 0.105
                    easein_cubic 0.2 ypos 0.1
                    linear 0.05      ypos 0.105
                    easein_cubic 0.2 ypos 0.1
                    pause 0.5
                    repeat
            show dev somber
            with eidissolve_nd

            "I simply nod, staring back down at my food. Another social situation effortlessly navigated, Dev{cps=5}...{/cps}"

        "Sit outside":
            show dev neutral:
                ease_quad 1.5 xpos 0.6

            "I take a deep breath and start walking towards Rebecca's table, trying to look casual.{w=0.3} Maybe if I just act natural, she won't even notice me."
            show dev somber
            with eidissolve_nd
            "I'm just another student heading outside,{w=0.3} nothing to see here."
            "My heart's pounding as I get closer.{w=0.1} Just a few more steps and I'll be past her.{w=0.2} Home free."
            
            show dev shocked
            show rebecca skeptical:
                backmovey(0.1)
            with eidissolve_nd

            "But because the universe hates me, she looks up from her laptop at that exact moment. Our eyes lock."
            
            show dev sad
            with eidissolve_nd
            
            "Crap."
            "I freeze mid-step, my tray wobbling dangerously in my hands. My brain's screaming at me to keep walking, but my feet aren't getting the message.{w=0.3} I'm just standing there like an idiot, staring at her."
            
            show rebecca skeptical
            with eidissolve_nd

            "She raises an eyebrow, looking annoyed and confused."

            R "Uh,{w=0.3} did you want something?"
            
            show dev ashamed
            with eidissolve_nd

            D "I,{w=0.2} uh{cps=5}...{/cps}"
            
            show dev sad
            with eidissolve_nd
            
            "Great job, Dev. King of casual you are not."
            "She sighs, closing her laptop."
            
            show rebecca neutral
            show dev surprised
            with eidissolve_nd

            R "Look skinnie, if you want to sit here, just sit.{w=0.3} I'm not going to bite your head off or whatever."

            show dev skeptical
            with eidissolve_nd

            "\"Skinnie\"?"
            
            show dev sad
            with eidissolve_nd
            
            "Well,{w=0.2} now I'm stuck. If I say I wasn't planning to sit with her, I'll look like a total ass. But if I sit down{cps=5}...{/cps}"
            
            show rebecca skeptical
            with eidissolve_nd
            
            "My mouth opens and closes a few times, no words coming out.{w=0.2} I probably look like a fish out of water.{w=0.3} A very confused, very awkward fish."
            "Rebecca's staring at me like I've grown a second head."

            show rebecca annoyed

            R "Seriously,{w=0.1} are you going to sit or not?"
            
            show dev neutral
            with eidissolve_nd
            
            "I clear my throat."
            
            show dev somber
            with eidissolve_nd

            D "Yeah, um, thanks.{w=0.3} I'll{cps=5}...{/cps} I'll sit."
            
            show dev neutral:
                ease_quad 1.5 ypos 0.1

            "Slowly,{w=0.1} I lower myself into the chair across from her,{w=0.1} my tray clattering loudly on the table. Rebecca winces at the noise."
            
            show dev somber
            with eidissolve_nd
            
            D "Sorry."

            show rebecca neutraldown with eidissolve_nd:
                    setx(0.25)
                    backmovey(0.1)
                    typing
            show dev neutral
            with eidissolve_nd

            "She shrugs, reopens her laptop, and continues typing,{w=0.3} leaving me to poke at my food in silence."

    if devnumba1:
        show rebecca skeptical

        R "So uh,{w=0.3} what's with that stuff on your forehead?"

        "I gesture to the rough \"#1\" I scribbled on this morning."

        D "Your brother's idea.{w=0.3} He texted me that I should do this and I{cps=5}...{/cps} well{cps=5}...{/cps}"
        
        show dev skeptical
        with eidissolve_nd

        D "I just did it,{w=0.1} I guess."

        show rebecca annoyed
        show dev sad
        with eidissolve_nd

        "Rebecca's eyes become thin lines of curiosity and doubt. Her squinting makes it difficult to read what she must be thinking."
        "Surely,{w=0.2} she sees me as the fool I am."
        "I stare down at my food.{w=0.3} Maybe I can bury my face in this plate and hide from the whole world."

        show rebecca neutral
        show dev skeptical
        with eidissolve_nd

        R "You really are gullible, huh."
        
        show rebecca devious
        show dev surprised
        with eidissolve_nd

        R "If all your friends jumped off-"
        
        show dev annoyed
        with eidissolve_nd

        D "I know what you are going to say, and no, I would not."

        show rebecca grin
        with eidissolve_nd

        "Rebecca gives me a toothy grin. A {i}sharp{/i},{w=0.2} toothy grin."

        R "You would jump off that bridge so hard.{w=0.2} Probably do a backflip too."
        
        show dev unimpressed
        with eidissolve_nd

        D "First of all, nope! Second, if I {i}did{/i}, it would be the sickest backflip."
        
        show rebecca happy
        show dev smug
        with eidissolve_nd

        R "Pfft."
        
        show rebecca devious
        show dev happy
        with eidissolve_nd

        R "Dream on, dude."

    show rebecca neutraldown
    show dev neutral
    with eidissolve_nd

    "With a roll of her eyes, she continues picking away at her bacon with the grace and speed of someone accustomed to handling chopsticks.{w=0.3} It's a curious sight."
    
    show rebecca neutral
    show dev skeptical
    with eidissolve_nd
    
    D "So{cps=5}...{/cps} uh,{w=0.2} why are you{cps=5}...{/cps} eating like that?"

    show rebecca skeptical
    show dev neutral
    with eidissolve_nd
    
    "She raises one eyebrow at me."

    D "You know{cps=5}...{/cps} with the chopsticks?"

    show rebecca neutral:
        backmovey(0.1)
    with eidissolve_nd

    R "It keeps my hands clean.{w=0.2} Can't risk getting grease on my laptop."

    D "Oh, right.{w=0.3} That makes sense, I guess."
    
    show dev skeptical
    with eidissolve_nd
    
    D "But why not use a fork?"
    
    show dev neutral
    show rebecca neutraldown
    with eidissolve_nd
    
    "She looks at the chopsticks in her hand for a moment and shrugs."
    
    show rebecca neutral
    with eidissolve_nd
    
    R "I just like them."
    
    show rebecca neutraldown
    show dev neutral
    with eidissolve_nd
    
    "{cps=5}...{/cps}"
    "We continue to eat our food in awkward quiet.{w=0.4} The silence is killing me, so I try another approach."
    
    show dev happy
    with eidissolve_nd
    
    D "Uh,{w=0.1} that laptop looks pretty sturdy.{w=0.3} Was it expensive?"
    
    show rebecca surprised
    show dev skeptical
    with eidissolve_nd

    "Rebecca's eyes light up.{w=0.1} Clearly this is a topic she's interested in."
    
    show dev neutral
    show rebecca angry
    with eidissolve_nd
    
    R "Expensive?"
    
    show rebecca devious
    with eidissolve_nd

    R "This isn't just any laptop. It's a top-of-the-line gaming rig.{w=0.3} It's a freaking monster more than anything!"
    
    show dev happy
    show rebecca skeptical
    with eidissolve_nd
    
    D "Cool."
    
    show dev skeptical
    show rebecca point po_devious
    with eidissolve_nd

    R "This baby can run any game at max settings.{w=0.3} It's got a 7090 Ti,{w=0.1} 64 gigs of RAM,{w=0.1} and a 4K OLED display."
    
    show dev neutral
    show rebecca delighted d_gleeup
    with eidissolve_nd

    R "It's well beyond cool.{w=0.3} Cost me a fortune."
    
    show dev somber
    with eidissolve_nd

    "I nod,{w=0.3} pretending I understand half of what she's saying."
    
    show rebecca skeptical
    show dev skeptical
    with eidissolve_nd

    D "That's{cps=5}...{/cps} impressive?"

    show rebecca ugh
    show dev neutral
    with eidissolve_nd

    "Rebecca scoffs."
    
    show dev skeptical
    with eidissolve_nd

    R "Of course it is. I thought you played games too?"

    show rebecca skeptical
    with eidissolve_nd

    D "Console games,{w=0.2} and even then, only ones I could find used at Gameplace."

    show dev sad
    with eidissolve_nd

    D "My family never really had the cash for anything too fancy."

    show rebecca worried
    with eidissolve_nd

    R "O{w=0.1}-oh{cps=5}...{/cps} uh{cps=5}...{/cps} that sucks{cps=5}...{/cps}"
    
    show rebecca neutraldown
    with eidissolve_nd

    "Bravo, Dev. Way to throw such a downer into the conversation."
    
    show dev neutral
    with eidissolve_nd
    
    "I shrug in an effort to ease the tension."
    
    show dev happy
    show rebecca neutral
    with eidissolve_nd

    D "It is what it is."
    
    show dev neutral
    show rebecca neutraldown:
        setx(0.25)
        backmovey(0.1)
        typing
    with eidissolve_nd

    "We lapse into another awkward silence. I take a bite of my food, desperately thinking of something to say."
    "She goes back to typing. Her fingers fly across the keyboard, piquing my interest."
    
    show dev skeptical
    with eidissolve_nd
    
    "You know what?{w=0.3} Today, I'm letting my curiosity win twice in a row."
    
    if SUI:
        show dev happy
        with eidissolve_nd
        D "So,{w=0.1} uh,{w=0.1} what are you writing there?"
        
        show dev neutral
        show rebecca annoyed:
            backmovey(0.1)
        with eidissolve_nd

        "Rebecca's fingers freeze over her keyboard.{w=0.2} She looks up at me, her eyes narrowing again."

        R "Why do you care?"
        
        show dev neutral
        with eidissolve_nd

        "I shrug, pushing my food around on my plate."
        if beccainvade:
            show rebecca skeptical
            with eidissolve_nd
            D "Just curious.{w=0.3} I write sometimes too, you know."
            show rebecca neutraldown
            with eidissolve_nd
            R "Oh yeah,{w=0.3} I think you mentioned that yesterday{cps=5}...{/cps}"
            show rebecca neutral
            with eidissolve_nd
            R "What {i}do{/i} you write?"
        
        else:
            show rebecca surprised
            with eidissolve_nd
            R "Wait,{w=0.3} {b}you{/b} write?"
            show dev skeptical
            with eidissolve_nd
            D "Yeah?"
            show dev neutral
            show rebecca skeptical
            with eidissolve_nd
            R "Hmm, well, what exactly?"

        show dev sad

        D "Promise not to laugh?{w=0.3} Mostly stories about{cps=5}...{/cps} uh{cps=5}...{/cps} other stories. Nothing serious though,{w=0.2} just for fun."

        show rebecca surprised
        show dev skeptical
        with eidissolve_nd
        
        "Rebecca's eyes widen slightly."
        
        show rebecca love:
            ease_quad 3 xpos 0.3
        show dev shocked
        with eidissolve_nd

        R "You write fanfiction too!"

        show rebecca pissed p_shocked:
            ease_quad 0.5 xpos 0.25
        show dev skeptical
        with eidissolve_nd
        

        R "Uh{cps=5}...{/cps} {i}cough{/i} I mean{cps=5}...{/cps} R{w=0.1}-really? I write{cps=5}...{/cps} stuff{cps=5}...{/cps} like that too."

        show dev neutral
        show rebecca surprised
        with eidissolve_nd

        D "No kidding?{w=0.3} What fandoms?"

        show rebecca worried
        with eidissolve_nd

        "She hesitates,{w=0.1} her claws tapping nervously on her laptop."
        
        show rebecca neutraldown
        with eidissolve_nd

        R "I{cps=5}...{/cps} I'd rather not say."

        "I nod in understanding, silently glad for the excuse to avoid answering the question myself."
        "This is the unspoken, fanfiction writer's code.{w=0.3} The world can never know{cps=5}...{/cps}"
        
        show rebecca neutral
        show dev happy
        with eidissolve_nd
        
        D "That's fair.{w=0.3} I guess I'm pretty private with my writing, too."
        
        show rebecca neutraldown
        with eidissolve_nd

        "Rebecca looks down at her screen, then back at me with an inquisitive expression."
        
        show rebecca worried
        with eidissolve_nd

        R "Have you ever{cps=5}...{/cps} shared your writing with anyone though? Like, posted it online or something?"
        
        show dev skeptical
        show rebecca disappointed
        with eidissolve_nd

        D "Yeah, it never really got any attention or anything, but I figure{w=0.1} - what's the point of writing a story if you're not going to share it with {i}someone{/i}, right?"
        
        show rebecca disappointeddown
        show dev neutral
        with eidissolve_nd

        R "I guess{cps=5}...{/cps}"

        "There's a pause, and I notice her fidgeting uncomfortably, deep in thought."
        
        show dev somber
        with eidissolve_nd

        D "Um, would you be willing to show some of it to me?{w=0.3} W{w=0.1}-what you're writing, I mean.{w=0.1} I could give feedback, if you'd like."
        
        show rebecca neutraldown
        with eidissolve_nd

        R "Feedback{cps=5}...{/cps} yeah{cps=5}...{/cps}"
        
        show rebecca neutral
        with eidissolve_nd

        R "I{cps=5}...{/cps} I guess I could show you what I'm working on{cps=5}...{/cps}"
        
        show rebecca worried
        with eidissolve_nd

        D "Are you sure? I completely get it if you're not comfortable.{w=0.3} I'd be hesitant, myself."
        
        show dev happy
        with eidissolve_nd
        
        "Rebecca nods slowly."

        show rebecca neutral

        R "Yeah, I think so. Just{cps=5}...{/cps} don't laugh, okay?"

        show dev:
            chuckle(0.1)
        with eidissolve_nd

        "I chuckle,{w=0.1} trying to lighten the mood."
        
        show rebecca grin
        with eidissolve_nd
        
        D "I wouldn't dream of it."

    else:
        show dev happy
        with eidissolve_nd
        D "So,{w=0.1} uh,{w=0.1} what are you writing there?"
        
        show dev sad
        show rebecca annoyed:
            backmovey(0.1)
        with eidissolve_nd

        "Rebecca's fingers freeze over her keyboard.{w=0.2} She looks up at me, her eyes narrowing again."
        
        show dev skeptical
        with eidissolve_nd
        
        R "Why do you care?"
        
        show rebecca skeptical
        with eidissolve_nd

        "I shrug, pushing my food around on my plate."
        
        show dev thinking
        with eidissolve_nd

        D "Just curious,{w=0.1} I guess?"
        
        show dev sad
        show rebecca grumpy
        with eidissolve_nd

        R "Then prepare to stay curious. It's nothing important."
        
        show dev happy
        with eidissolve_nd

        D "Come on,{w=0.1} it must be something cool.{w=0.1} Both times I've seen you here, you were pretty focused on it."
        
        show rebecca disappointeddown
        with eidissolve_nd
        
        "She shifts uncomfortably in her seat."

        show rebecca angry
        show dev skeptical
        with eidissolve_nd

        R "It's just{cps=5}...{/cps} stuff.{w=0.3} Stupid stuff."
        
        show dev neutral
        with eidissolve_nd

        D "Hey, if it matters to you,{w=0.1} it's not stupid."
        
        show rebecca annoyedconsidering
        with eidissolve_nd

        "Rebecca scoffs."
        
        show rebecca annoyed
        with eidissolve_nd

        R "You don't even know what it is."
        
        show rebecca surprised
        show dev happy
        with eidissolve_nd

        D "True,{w=0.3} but I know it matters to you. That's enough, isn't it?"

        show rebecca neutral
        with eidissolve_nd

        "She stares at me for a moment, then shakes her head."
        
        show rebecca neutraldown
        show dev neutral
        with eidissolve_nd

        R "It's just{cps=5}...{/cps} writing.{w=0.2} Stories and stuff.{w=0.3} Like I said nothing special."
        
        show rebecca neutral
        with eidissolve_nd

        D "That sounds pretty neat to me, what kind of stories?"
        
        show rebecca neutraldown
        with eidissolve_nd

        "Rebecca looks away, her claws tapping nervously on the table."
        
        show rebecca worried
        with eidissolve_nd

        R "Just{cps=5}...{/cps} fanfiction, mostly."

        "She shakes her head."
        
        show rebecca upset
        with eidissolve_nd

        R "Nevermind I told you,{w=0.3} it was stupid."
        
        show rebecca surprised
        show dev happy
        with eidissolve_nd

        D "No way, that's awesome! I wish I could write stuff like that.{w=0.3} Never had much talent for it, though."

        "She looks back at me, surprised."
        R "R-really?"

        show rebecca annoyed
        show dev skeptical
        with eidissolve_nd

        R "{cps=5}...{/cps} Are you screwing with me?"

        "I shake my head, brushing aside a twinge of envy."

        D "Not at all! I mean,{w=0.1} you have something you're passionate about.{w=0.3} That's more than I can claim{cps=5}...{/cps} that's really cool. Honest."

        show rebecca annoyed
        show dev sad
        with eidissolve_nd

        "Rebecca tilts her head, studying me with an inscrutable gaze."
        
        show rebecca skeptical
        with eidissolve_nd

        R "You don't have {i}anything{/i} you're passionate about?"
        
        show rebecca neutraldown
        with eidissolve_nd

        R "I've got a hard time believing that. Everyone's interested in {i}something{/i}."
        
        show dev ashamed
        with eidissolve_nd

        "I shrug, suddenly feeling exposed."
        
        show dev sad
        show rebecca neutral
        with eidissolve_nd

        D "Not really.{w=0.3} I've tried a bunch of different things but never found anything that actually {i}clicked{/i}, you know?"

        show rebecca neutraldown
        with eidissolve_nd

        "She nods slowly, her expression softening a bit."

        R "Yeah,{w=0.3} I guess{cps=5}...{/cps}"
        
        show rebecca neutral
        show dev somber
        with eidissolve_nd

        D "So,{w=0.1} would you be willing to show it to me? Your writing, I mean.{w=0.3} Who knows, maybe seeing your work might spark a deep passion for writing in me."
        
        show rebecca worried
        with eidissolve_nd

        R "{cps=5}...{/cps}"
        
        show rebecca ugh
        with eidissolve_nd

        R "Ugh, fine. If you {i}really{/i} want to read it{cps=5}...{/cps} I guess I could show you."
        
        show rebecca neutral
        show dev happy
        with eidissolve_nd

        D "Really?{w=0.3} That's awesome!"
        
        show rebecca sass s_grinconsidering
        with eidissolve_nd

        "She rolls her eyes, but I catch a hint of a smile."
        
        show rebecca sass s_grin
        with eidissolve_nd

        R "Don't get too excited. You'll probably think it's terrible."
        
        show dev smug
        with eidissolve_nd

        D "I doubt that, but even if it is, who cares? You're doing something you love. That's what matters, right?"
        
        show rebecca grin
        with eidissolve_nd
        
        R "Yeah{cps=5}...{/cps} I guess you're right."
    
    show rebecca neutral
    show dev neutral
    with eidissolve_nd
    
    R "Look, consider this a vote of confidence, okay?{w=0.1} Close your eyes."

    show dev skeptical
    with eidissolve_nd
    
    D "Wh{w=0.1}-what?"
    
    show rebecca angry
    show dev surprised
    with eidissolve_nd

    R "Just do it, Dev."
    
    show black with dissolve_nd
    show becca_storytime1 behind black:
        subpixel True ypos 0.0
    show becca_storytime2 behind becca_storytime1:
        subpixel True ypos 0.0
    stop music fadeout 3
    stop ambience fadeout 3
    "I do."
    pause 1
    play music dragons_of_faira fadein 5.0
    
    "I hear her take a deep breath before she begins to speak, her words rolling out like the opening lines of a long-forgotten epic."
    
    hide black with dissolve_nd
    pause 1
    show becca_storytime1:
        subpixel True
        parallel:
            ease_cubic 7 ypos -0.78
        parallel:
            ease_cubic 7 alpha 0
    show becca_storytime2:
        subpixel True
        ease_cubic 7 ypos -0.78

    R "The great hall of Castle Elfinheil stretches out before you.{w=0.1} A long red carpet runs the length of the room, its plush fibers thick and warm beneath your feet.{w=0.1} A massive, open balcony spans the back of the hall, casting golden sunlight over everything."
    
    hide becca_storytime1 with dissolve_nd
    show becca_storytime3 behind becca_storytime2

    "I picture it immediately. The red carpet feels rich and inviting. The warmth surrounds me as I stand there, taking it all in."
    
    show becca_storytime2:
        ypos -0.78
    pause 1
    show becca_storytime2:
        ease_cubic 7 alpha 0

    R "Silk curtains flow from the high ceilings, billowing softly as if stirred by an unseen breeze.{w=0.1} They shimmer with every flicker of light. Around you gather beings of all shapes and sizes—some tall and regal,{w=0.2} others small and nimble."
    
    hide becca_storytime2
    show becca_storytime3:
        subpixel True 
        parallel:
            ease_cubic 5 ypos 1.29
        parallel:
            ease_cubic 5 zoom 2.25
        parallel:
            ease_cubic 5 xpos 1.12 
        ease_quart 8 xpos -0.12
    show becca_storytime4 behind becca_storytime3
    
    "My eyes dart around this imagined space filled with countless races, each one unique. I feel as though I've entered the presence of something grand and profound."
    
    show becca_storytime4:
        ypos 1.29
        zoom 2.25
        xpos -0.12
    show becca_storytime3:
        ypos 1.29
        zoom 2.25
        xpos -0.12
    show becca_storytime3:
        subpixel True 
        parallel:
            ease_cubic 3 ypos 1.0
        parallel:
            ease_cubic 3 zoom 1.0
        parallel:
            ease_cubic 3 xpos 0.5
        parallel:
            pause 1
            ease_cubic 3 alpha 0
    show becca_storytime4:
        subpixel True 
        parallel:
            ease_cubic 3 ypos 1.0
        parallel:
            ease_cubic 3 zoom 1.0
        parallel:
            ease_cubic 3 xpos 0.5
    

    R "At the far end of the hall stands a massive throne occupied by an enormous red dragon,{w=0.1} scales glistening like jewels under the golden light.{w=0.1} Much of its body is cast in shadow from the bright light at its back, only its piercing eyes visible."
    
    hide becca_storytime3
    show becca_storytime4:
        ease_cubic 7 ypos 1.67

    "A chill runs down my spine at her description. Confronting such a beast almost defies imagination, but with Rebecca's words: it's as if I'm standing there, at its mercy."
    
    show becca_storytime4:
        ypos 1.67
        parallel:
            ease_cubic 7 ypos 1.0
        parallel:
            pause 3
            ease_cubic 5 zoom 1.2
    
    pause 7
    
    show becca_storytime5:
        default
        subpixel True 
        parallel:
            xpos 981 zoom 1.2 
            easein_cubic 3 xpos 960 zoom 1.2 
        parallel:
            ypos 1449 
            easein_cubic 3 ypos 1080 



    R "A smaller dragon walks forward on shaky legs.{w=0.1} It bows low before the towering figure."
    
    show becca_storytime4:
        zoom 1.2
        ypos 1.0
        
    show becca_storytime5:
        ypos 1080
        xpos 960
        zoom 1.2

    R "The air is thick with anticipation and silence blankets the room.{w=0.1} The subservient drake speaks in a shaky voice while lowering its head even further."
    
    show becca_storytime6 behind becca_storytime4
    
    "Her words draw me in deeper."
    
    show becca_storytime6:
        ypos 1.0
        zoom 1.2
    show becca_storytime4:
        ease_cubic 7 alpha 0
    show becca_storytime5:
        ease_cubic 7 alpha 0
    
    R "As it speaks, a deep rumble resonates in response from the massive beast on its throne{w=0.1}—a sound that shakes the very bones of every being present."
    
    hide becca_storytime4
    hide becca_storytime5
    
    "I can almost feel that rumble vibrating through my chest."
    
    show becca_storytime6:
        subpixel True 
        ypos 1.0 
        easein_cubic 7 ypos 1.9 

    R "The smaller dragon lifts its head slowly, daring to meet those fierce eyes filled with wisdom and power."
    
    show becca_storytime6:
        subpixel True 
        ypos 1.9 zoom 1.2 
        easein_cubic 7 ypos 2.4 zoom 1.60 
    
    "Rebecca's tone captures me completely; I'm hanging on every word."

    R "And for a moment,{w=0.3} time seems to stop."
    
    show champy behind dev:
        xpos 0.8
        ypos 0.0
    show dev terrified right:
        xpos 0.45
    show rebecca shocked
    
    Cu "Miss Chase?{w=0.3} I am here to talk to you about some matters brought to my attention."    
        
    stop music
    play ambience school_cafeteria_ambience volume 2 loop
    show champy sass s_annoyed left
    hide becca_storytime6 with dissolve
    
    D "Huh?"
    
    play music daydreaming fadein 3.0
    
    show dev sad
    show rebecca skeptical
    with eidissolve_nd
    
    "Suddenly the magic is gone, and I'm yanked back to the CCC cafeteria.{w=0.3} A large Saurian stands in front of us, hands on her hips and foot tapping in consternation."
    
    show champy sass s_unimpressed
    with eidissolve_nd
    
    Cu "I said,{w=0.2} I need to talk with Miss Chase about some things."
    
    show dev neutral
    show rebecca neutral
    with eidissolve_nd
    
    R "Oh,{w=0.1} uh,{w=0.1} hey.{w=0.2} Aren't you in the same-"
    
    show champy annoyed
    with eidissolve_nd
    
    Cu "My name is Sandra Champy, assistant to the student union head, and I am here to inform you of several complaints made against you."
    
    show dev skeptical left
    show rebecca skeptical
    with eidissolve_nd
    
    R "{cps=5}...{/cps}"
    
    show champy unimpressed
    show dev skeptical right
    with eidissolve_nd
    
    D "{cps=5}...{/cps}"
    
    show rebecca grin
    with eidissolve_nd

    R "What{cps=5}...{/cps}?"
    
    show champy sass s_annoyed
    show rebecca neutral
    with eidissolve_nd

    C "{i}Sigh{/i}{cps=5}...{/cps} You were disrupting most of Mrs. Harper's class. Not only did you play music through your speakers-"
    
    show dev neutral right
    show rebecca sass s_skeptical
    with eidissolve_nd

    R "I had it at a low volume."
    
    show champy angry
    show dev neutral left
    show rebecca sass s_annoyed
    with eidissolve_nd

    C "{cps=5}...{/cps} {i}Not only did you play music through your speakers{/i}, but several other students claimed you used some{cps=5}...{/cps} choice words during a disagreement with them."
    
    show champy surprised
    show dev shocked:
        easein_bounce 0.5 xpos 0.48
    show rebecca grin
    with eidissolve_nd
    
    R "You mean the two meteor dodgers I called \"cunts\"?{w=0.3} Kind of deserved it, since they were acting like,{w=0.2} well,{w=0.1} cunts."
    
    show dev sad
    show rebecca devious
    with eidissolve_nd

    "A sneer crawls across the larger girl's face."
    
    show champy angry
    show dev ashamed right
    show rebecca neutral
    with eidissolve_nd

    C "Right{cps=5}...{/cps} Well,{w=0.3} I'm fine with keeping this out of the ear of the counselor - or worse{w=0.1} - the head of the student union, so long as you apologize to those students and at least use earpods."
    
    show champy unimpressed
    show rebecca annoyed
    with eidissolve_nd

    C "And since the student union head has the ear of the Dean, I assume we can both agree that it would be best if he didn't hear about this."
    
    show champy surprised:
        easein_bounce 0.5 xpos 0.83
    show dev surprised:
        pause 0.5
        choice:
            "dev terrified"
        easein_cubic 0.7 xpos 0.3 ypos 0.0
        choice:
            "dev surprised"
    show rebecca point:
        parallel:
            pause 0.3
            easein_cubic 1 xpos 0.54
        parallel:
            ease_cubic 0.5 ypos 0
    with eidissolve_nd
    
    R "Are you threatening me?!"
    
    show champy annoyed
    show rebecca point po_devious:
        easein_cubic 0.5 xpos 0.57
    with eidissolve_nd

    R "Well, go right ahead bitch,{w=0.1} tell him! The guy is like{cps=5}...{/cps} best friends with my brother. And as if I would care what some \"college counselor\" has to say."
    
    show champy angry
    show dev shocked
    show rebecca pissed p_gritting:
        hop
    with eidissolve_nd
    
    R "I am {i}not{/i} apologizing to those {sc}{b}cunts{/b}{/sc}!"
    
    show champy disgust
    show dev sad
    with eidissolve_nd
    
    C "{cps=5}...{/cps}"
    show champy sass s_disgust right
    show rebecca grumpy
    with eidissolve_nd

    C "{i}Hmph{/i}."
    
    show champy at moveoutright(x=0.83)
    hide champy

    "The large girl walks away with a huff."
    
    show rebecca annoyed left
    with eidissolve_nd

    D "Wasn't that a bit{cps=5}...{/cps} much?"
    
    show dev neutral:
        parallel:
            pause 0.4
            "dev left" with eidissolve
        parallel:
            easein_cubic 1.5 xpos 0.6      
        parallel:
            pause 0.5
            ease_cubic 1 ypos 0.1
    show rebecca annoyedconsidering:
        parallel:
            easein_cubic 1.5 xpos 0.3
            "rebecca right annoyed" with eidissolve
        parallel:
            pause 0.5
            ease_cubic 1 ypos 0.1

    R "Pfft, I know her type. A goody two-shoes that thinks they can make everything perfect by getting on people's cases."
    
    show dev sad left
    show rebecca skeptical right
    with eidissolve_nd

    D "Right{cps=5}...{/cps} and the two girls? The ones you called{cps=5}...{/cps} um{cps=5}...{/cps}"
    
    show dev annoyed
    show rebecca devious
    with eidissolve_nd
    
    R "Cunts?{w=0.1} Meteor dodgers?"
    
    show dev neutral
    with eidissolve_nd
    
    D "Yeah, them,{w=0.1} what did they do?"
    
    show dev skeptical
    show rebecca ugh
    with eidissolve_nd

    R "They wouldn't.{w=0.1} Shut.{w=0.1} Up.{w=0.1} All class they just talked, and talked, and talked. Part of the reason I turned my music on.{w=0.3} If I couldn't concentrate, then neither would they."
    
    show rebecca sass s_skeptical
    with eidissolve_nd
    
    D "And neither would the rest of the class{cps=5}...{/cps}"
    
    show dev surprised
    show rebecca point
    with eidissolve_nd

    R "Look skinnie, don't think just because we shared one \"moment\" that gives you the right to lecture me."
    
    show dev skeptical
    show rebecca angry
    with eidissolve_nd

    "I don't know why she keeps calling me that or what it means, but I find myself getting annoyed with how much she's pushing back on this."
    
    show dev sad
    show rebecca annoyed
    with eidissolve_nd

    D "I'm not trying to lecture you, it just seems like a bad idea to lash out because two other girls were being rude."
    
    show rebecca angry
    with eidissolve_nd

    "Her jaw tightens as she shifts in her seat."
    
    show rebecca point po_gritting
    with eidissolve_nd

    R "I don't \"lash out\"{cps=5}...{/cps}"
    
    show dev annoyed
    show rebecca grumpy
    with eidissolve_nd

    D "I mean, I've been trying to be nice, but you keep snapping at me too.{w=0.3} Insulting me."
    
    show rebecca:
        block:
            choice:
                "rebecca sass s_annoyed" with eidissolve
            choice:
                "rebecca sass s_angry" with eidissolve
            choice:
                "rebecca sass s_angrydown" with eidissolve
            choice:
                "rebecca sass s_gritting" with eidissolve
            choice:
                "rebecca sass s_worried" with eidissolve
            choice:
                "rebecca sass s_sad" with eidissolve
            pause 0.65
            repeat

    "Rebecca's expression quickly shifts between a myriad of emotions,{w=0.1} annoyance,{w=0.1} frustration,{w=0.1} sadness?"
    
    show rebecca sad:
        "rebecca annoyedconsidering" with eidissolve

    R "I didn't mean anything by it!{w=0.3} I was just{cps=5}...{/cps} joking around!"
    
    show dev skeptical
    show rebecca annoyeddown
    with eidissolve_nd

    D "Joking or not, it feels like you're just waiting for an excuse to insult me."
    
    show dev neutral
    show rebecca neutraldown
    with eidissolve_nd

    "She looks down at her bacon bites, sharply jabbing at them as if they've personally offended her as well."
    
    show dev skeptical
    show rebecca neutral
    with eidissolve_nd
    
    R "Look,{w=0.2} it's not personal.{w=0.3} I joke with everyone."
    
    show dev unimpressed
    show rebecca annoyed
    with eidissolve_nd

    D "Well it doesn't feel like a joke to me."
    
    show rebecca annoyeddown
    with eidissolve_nd

    "Rebecca huffs and glances back at her screen,{w=0.1} avoiding eye contact."
    
    show rebecca disappointeddown
    with eidissolve_nd 

    R "You're way too sensitive then."

    "I feel my irritation bubbling up. It's hard enough trying to fit in without being treated like some punchline."

    D "I'm just trying to get along here.{w=0.3} You don't have to make it harder."
    
    show rebecca worried
    with eidissolve_nd

    "She opens her mouth like she wants to respond but then just shuts it again."
    
    show dev annoyed
    show rebecca sad
    with eidissolve_nd

    D "Whatever.{w=0.3} I guess I'll just leave you alone then."
    
    show dev sad
    show rebecca sadforward
    with eidissolve_nd

    D "I really did like your story by the way,{w=0.3} I wish I could have heard more."
    
    show dev annoyed:
        ease_cubic 1 ypos 0.0
    show rebecca upset
    with eidissolve_nd
    
    "I push back my chair and stand up, tray in hand. Her silence hangs heavy between us as I turn away."
    
    show dev:
        ease_cubic 1 xpos 0.15
    show rebecca:
        parallel:
            ease_cubic 1 xpos 0.6
        parallel:
            pause 0.5
            "rebecca upset left" with eidissolve
    
    "As I walk toward the exit, I hear her voice behind me."
    
    show rebecca worried left
    with eidissolve_nd
    
    R "Dev{cps=5}...{/cps}"

    "But I don't turn around. The cafeteria buzzes with life around me while I leave Rebecca there in silence."
    
    show dev at moveoutleft(x=0.15)
    hide dev
    
    pause 2
    scene black with dissolve
    stop music fadeout 10
    stop ambience fadeout 10
    
    "For a moment,{w=0.3} I feel bad for leaving things this way."
    "But{cps=5}...{/cps} I just don't feel like dealing with her right now."
    
    window auto hide
    
    pause 1
####PART 4####

    play music moonlit_reverie fadein 3.0
    
    show quad_2 behind black
    show quad_2:
        zoom 1.2
    hide black with Dissolve(1)
    window auto show

    pause .5
    
    show dev sad at moveinright(0.15, m=0.3)
    
    "In the middle of my walk to the counselor's office, I realize that I never bothered to ask anyone for directions."
    
    show dev ashamed
    with eidissolve_nd
    
    "I should have asked Rebecca, but going back after the way I left,{w=0.3} I can't imagine that would work out very well."
    
    show dev neutral
    with eidissolve_nd
    
    "Plus,{w=0.3} I have another class in less than half an hour, so I can't backtrack now."
    
    show dev sad
    with eidissolve_nd
    
    "Ugh.{w=0.3} It looks like I'm going to have to ask a random student for directions. The thought alone makes me want to retch."
    
    
    show quad_2:
        subpixel True ypos 1.0 
        xpos 0.5 
        ease_cubic 1.0 xpos 0.4 

    show dev:
        ease_cubic 1 xpos 0.35
    
    pause 0.1
    show c_selfie1 left at moveinleft(0.65, m=0.3):
        matrixcolor ColorizeMatrix("#989b3e", "#ffffff")
    
    with eidissolve_nd
    
    "I eventually stop a psittacosaurus walking towards me, scrolling through their phone. I blurt out my question as fast as I can and they can give me a weird look for bothering them out of nowhere."
    
    show dev somber
    with eidissolve_nd
    
    D "H{w=0.1}-Hi! Uh, do you know where the counselor's office is?"
    
    show dev ashamed
    with eidissolve_nd
    
    "The weird look doesn't disappear from their face, causing me to squirm."
    
    show dev sad
    with eidissolve_nd
    
    "After an awkward stare, they eventually give me directions.{w=0.3} It turns out that I'm closer than I thought I was, and I also get a snarky comment on the fact that the school app has a detailed map."
    "I open it to double check and yep, it's there.{w=0.3} Feeling horrible, I apologize for wasting their time."
    
    show dev somber
    with eidissolve_nd
    
    unknown "No problem, dude."
    
    show quad_2:
        subpixel True ypos 1.0 
        xpos 0.4 
        ease_cubic 1.0 xpos 0.5
    
    show dev neutral with eidissolve_nd:
        ease_cubic 1.5 xpos 0.65
        pause 0.4
        "dev left" with eidissolve
    
    show c_selfie1:
        ease_cubic 1 xpos 0.15
        pause 0.2
        "c_selfie1 right" with eidissolve
        pause 0.01
        hop
    
    "They start walking away before throwing one more weird look at me over their shoulder."
    
    show dev surprised left
    with eidissolve_nd
    
    unknown "Uh,{w=0.1} by the way,{w=0.1} you should chill out, man.{w=0.3} It's just college."
    
    show dev ashamed
    with eidissolve_nd
    
    show c_selfie1 left at moveoutleft(x=0.15)
    hide c_selfie1
    
    "Leaving me with that odd nugget of wisdom, they turn and briskly walk in the other direction."
    
    show dev skeptical
    with eidissolve_nd
    
    "Right.{w=0.3} {i}Just{/i} college.{w=0.3} Somehow I doubt that will radically change my approach going forward."
    
    show dev surprised
    with eidissolve_nd
    
    "Before I am able to put too much thought into that little bit of wisdom I hear the familiar ping of my phone."
    
    show dev skeptical
    with eidissolve_nd
    
    "Huh,{w=0.3} I don’t recognize this number."
    
    $ unknownr_chat.transient = False

    phone register "unknownr_chat":
        time hour 15 minute 3
        image "Ur" "goombecca"
        "Ur" "Sup skinnie"
    phone discussion "unknownr_chat":
        pause
        "D" "Um, who is this?"
        "Ur" "Rebecca"
        "Ur" "Theo gave me your number"
        "D" "Okay"
        "D" "And the picture you sent?"
        "Ur" "Just a little goof my roommate made me"
        "Ur" "I've been sending these to like everyone"
    
    "I just{cps=5}...{/cps} I don't get her.{w=0.1} At{w=0.1} All."
    "First she acts like she hates me,{w=0.1} then she is nice to me."
    "Then she hates me again, now she is being nice again?"
    "Everytime I interact with her I feel like I understand her less."
    
    show dev neutral
    with eidissolve_nd
    
    "Unless{cps=5}...{/cps}"
    
    show dev sad
    with eidissolve_nd
    
    "Did I fuck up?"
    
    show dev thinking
    with eidissolve_nd
    
    "Thinking back,{w=0.3} I did kinda lecture her, even if I didn't intend to{cps=5}...{/cps} hmmm{cps=5}...{/cps}"
    
    phone discussion "unknownr_chat":
        "D" "{emoji=thumbsup}"
    
    phone discussion "unknownr_chat":
        pause
        
    phone end discussion
    
    show dev happy
    with eidissolve_nd
    
    "There, that will show I liked her image.{w=0.3} Maybe now things will go more smoothly."
    
    show dev neutral right with eidissolve_nd
    pause 0.2
    show dev at moveoutright(x=0.65)
    hide dev
    
    pause 1
    scene black with dissolve    
    window auto hide
    
    pause 1    
    
    "I continue until I reach the counselor's office. I raise my hand to knock, before noticing a sign that says \"Come in!\" with a little smiley face. I push the door open and slide inside."    
    
    show sam_office_day_summer behind black
    
    show sam neutralclosed left:
        matrixcolor BrightnessMatrix(-1.0)
        
        transform_anchor True
        subpixel True
        yoffset 0.5 * 1500
        yanchor 0.5
        
        xpos 0.75
        ypos 0.1
        rotate 10
    
    hide black with Dissolve(1)
    window auto show

    pause .5
    
    show dev at moveinright(0.15, m=0.3)            
    
    "The counselor's office is a cozy room. Comfy cushions, motivational posters and stacks of papers decorate what would otherwise be a rather cramped space."
    
    show sam neutralclosed left:
        ease_cubic 1.5 matrixcolor BrightnessMatrix(0.0)
    
    "However,{w=0.1} the homely vibe ends at the liopleurodon leaning back in her chair behind the desk, eyes tightly shut in an expression of frustration and a can of soda held to her temple."
    "Without even opening her eyes, she gestures to the pair of chairs on the other side of the desk."
    
    show dev neutral:
        parallel:
            ease_quad 1.2 xpos 0.35
        parallel:
            pause 0.3
            ease_cubic 1 ypos 0.1
    
    Su "You Dev?"
    
    show dev happy
    with eidissolve_nd
    
    D "Oh!{w=0.3} You know my name.{w=0.3} Hi."
    
    show sam:
        transform_anchor True
        subpixel True
        yoffset 0.5 * 1500
        yanchor 0.5
        
        ease_cubic 1.2 rotate 0.0
        pause 0.2
        "sam left neutral"
    
    "She sits forward, her messy hair bouncing around her face as we both get a good look at each other."
    
    show sam neutral left
    show dev sad
    with eidissolve_nd
    
    "To say she doesn't look like the college counselor type would be an understatement."
    "Her rather casual, messy clothes, stern intimidating look on her face, and most conspicuously, the numerous scars patchworking her scales tell a different story altogether."
    "Then there's the eyepatch covering her left eye."
    
    show dev annoyed
    with eidissolve_nd
    
    "Not to mention that as I move closer, I can't help but notice a smell that sadly reminds me of a part of home I wish to forget. A frown reflexively appears on my face as she shuffles around the papers on her desk."
    
    show sam skeptical
    show dev skeptical
    with eidissolve_nd
    
    Su "You {i}are{/i} the only human around this semester, I wouldn't be doing my job if I didn't know who you were."
    
    show sam neutral
    show dev sad
    with eidissolve_nd
    
    "My ears start burning at the familiar answer. I wish it wasn't that simple, but{w=0.3} it is. Until the novelty wears off, I'm going to stick out like a sore thumb among my peers."
    
    show dev surprised
    with eidissolve_nd
    
    Su "Mind if I smoke?"
    
    show dev skeptical
    with eidissolve_nd
    
    D "Huh? Uh, no?{w=0.3} It's{cps=5}...{/cps} your office."
    
    show dev annoyed
    with eidissolve_nd
    
    "I cringe. Along with the motivational posters, there's a \"no smoking\" sign literally right behind her."
    "The irony seems lost on the counselor, who fishes around in her desk before withdrawing a large cigar."
    
    show sam cigar
    with eidissolve_nd
    
    "The woman lights her it and blows a perfect circle of smoke towards the roof where I notice a clearly disassembled fire alarm{cps=5}...{/cps}"
    "She follows my gaze and gives me a toothy grin."
    
    show dev terrified
    with eidissolve_nd
    
    Su "Don't worry about it too much.{w=0.3} Most of the campus is new, but this building's got so much asbestos in the walls you couldn't burn it down if you soaked it in gasoline first."
    "Seeing my worried gaze flick to the walls, she coughs, bringing my attention back to the conversation."
    
    show dev sad
    with eidissolve_nd
    
    Su "My name's Samantha Parker, but you can call me Sam since we're all adults here."
    if devnumba1:
        "Counselor Sam seems to notice the glaring numeral on my face as she reaches for one of her cabinets."
        show sam skeptical
        with eidissolve_nd
        "Intrigue plays across her face before deciding on ignorance for the sake of keeping the conversation going."
    
    show sam grin
    show dev neutral
    with eidissolve_nd
    
    S "It's nice to meet you.{w=0.3} Would you like some tea?"    
    D "Uh, no,{w=0.1} thanks.{w=0.3} Not much of a tea fan."
    "I also don't see a kettle of any kind."
    
    show dev skeptical
    with eidissolve_nd
    
    S "Good, me neither. I think I've got some soda cans in a drawer somewhere.{w=0.3} Here, have one."
    
    show sam neutral
    show dev neutral
    with eidissolve_nd
    
    "She rummages around and pushes a room temperature can of soda into my hands with much more force than I expected.{w=0.3} Thrown for a loop, I can't do anything more than give her a blank stare."
    S "Sorry, used the cold ones to take care of my hangover this morning. That's why I didn't message you sooner."
    "I crack open the soda can. The fizz hisses and fills the silence."
    
    show sam neutralclosed:
        transform_anchor True
        subpixel True
        yoffset 0.5 * 1500
        yanchor 0.5
        
        ease_cubic 1.2 rotate 10
    show dev sad
    with eidissolve_nd
    
    "Sam sits across from me, taking slow drags from her cigar, smoke curling toward the ceiling. The air feels thick with it, and I glance around, unsure of what to do with my hands."
    
    show dev ashamed
    with eidissolve_nd
    
    "{w=0.3}This is getting awkward.{w=0.3} She called me here for a reason, right?"
    
    show dev sad
    with eidissolve_nd
    
    "As it stands, we're both just sitting in silence as she nurses a cigar and I sip the soda hospitably forced onto me."
    
    show dev somber
    with eidissolve_nd
    
    D "Uh,{w=0.2} so-"
    
    show dev skeptical
    with eidissolve_nd
    
    "I get the ball rolling, hoping Sam will illuminate the meaning of our meeting. Instead she takes another long drag and holds it in."
    
    show dev neutral
    with eidissolve_nd
    
    "Just as I go to open my mouth again, Sam finally breaks the silence."
    
    show sam:
        transform_anchor True
        subpixel True
        yoffset 0.5 * 1500
        yanchor 0.5
        
        ease_cubic 1.2 rotate 0.0
        pause 0.2
        "sam left cigar neutral"
    show dev surprised
    with eidissolve_nd
    
    S "So, how's it going so far?{w=0.3} Adjusting to college life?"
    
    show sam cigar neutral left
    show dev sad
    with eidissolve_nd
    
    "I blink.{w=0.3} Despite being a perfectly reasonable ice-breaker, I find myself scrambling for a way to put the last two days into words."
    
    show dev skeptical
    with eidissolve_nd
    
    D "It's{cps=5}...{/cps} okay, I guess.{w=0.3} A bit overwhelming."
    
    show sam neutralconsidering
    with eidissolve_nd
    
    S "Yeah, that's common. Lots of new faces,{w=0.1} new freedom,{w=0.1} and new responsibilities.{w=0.3} What do you think about the campus?"
    
    show sam neutral
    show dev neutral
    with eidissolve_nd
    
    D "It's big.{w=0.2} And different.{w=0.1} I mean, I'm used to a place where everyone's human. This is a whole other world compared to home."
    "She nods, leaning back in her chair. The smoke swirls around her head like a lazy cloud."
    S "That can be tough. Have you met anyone yet?{w=0.3} Friends?"
    "I take a moment to recall all the colorful characters I've met in my short time here."
    
    show dev thinking
    with eidissolve_nd
    
    D "I think so?{w=0.3} I met this guy, Theo. He's been nice. And his sister, Rebecca, too. But, um,{w=0.3} I don't know if they're actually friends yet."
    
    show sam grin
    show dev skeptical
    with eidissolve_nd
    
    S "Making friends takes time. You've got to find your tribe, right?{w=0.3} Tell me a bit more about these Theo and Rebecca characters."
    
    show sam neutral
    show dev neutral
    with eidissolve_nd
    
    "I rub the back of my neck."
    D "They're fine, I guess. Theo seems very{cps=5}...{/cps} enthusiastic.{w=0.3} About basically everything. Certainly a lot different from my high school friends back home."
    
    show dev skeptical
    with eidissolve_nd

    D "We barely know each other and he already invited me to work on some big project."
    
    show sam skeptical
    show dev neutral
    with eidissolve_nd
    
    "She raises an eyebrow, intrigued."
    S "What kind of project?"
    D "He wants to make a video game."
    S "{w=0.3}Do you like video games?"
    
    show sam neutral
    show dev skeptical
    with eidissolve_nd
    
    D "Yeah{cps=5}...{/cps}?"
    
    show sam grin
    with eidissolve_nd
    
    S "Then why not?{w=0.3} Maybe it will help you figure out what you want to do for your future."
    
    show dev surprised
    with eidissolve_nd
    
    D "I-{w=0.3} what did-"
    
    show sam skeptical
    show dev neutral
    with eidissolve_nd
    
    S "Kid,{w=0.1} you joined a tech college with no major. You didn't even sign up for any electives.{w=0.3} It doesn't take a mind reader to figure out you're a bit lost."
    
    show sam grin
    with eidissolve_nd
    
    S "Take it from me, these things take time. Play it by ear, I say.{w=0.3} Last thing you want to do is over-commit and end up hating what you chose to do for the rest of your life."
    
    show sam neutral
    show dev ashamed
    with eidissolve_nd
    
    "I swallow down the nerves, unsure if one situation {i}is{/i} better than the other. I just want to get through my first semester without completely embarrassing myself at this point."
    "I sit back, sipping my soda, waiting for her next question."
    
    show sam skeptical
    show dev terrified
    with eidissolve_nd
    play ambience digital_alarm volume 8 loop
    
    "{b}BEEP BEEP BEEP!{/b}"
    
    stop ambience
    show sam neutral
    show dev shocked
    with eidissolve_nd
    
    "I jump as the alarm on my phone goes off. Looking at it, I'm reminded about my next class coming up soon."
    
    show dev yiik
    with eidissolve_nd
    
    "A class which happens to be on the opposite side of the campus."
    
    show dev annoyed
    with eidissolve_nd
    
    "Great.{w=0.3} I'll have to book it if I want to make it in time."
    
    show dev neutral
    with eidissolve_nd
    
    "I get up to leave."
    S "Before you go, I wanted to ask you about your home life."
    
    show dev skeptical
    with eidissolve_nd
    
    D "{cps=5}...{/cps}"
    D "Uh,{w=0.2} why exactly?"
    
    show sam neutralconsidering
    with eidissolve_nd
    
    S "In both of my questions you mentioned something about home. Your old town,{w=0.1} your old school.{w=0.3} Just wanted to know if you're homesick."
    
    show sam neutralclosed:
        hop(y=0.1)
    with eidissolve_nd
    
    "She shrugs."
    
    show sam neutral
    with eidissolve_nd
    
    S "It's a normal feeling for freshmen like you."
    
    show dev unimpressed
    with eidissolve_nd
    
    D "I don't feel homesick."
    
    show dev annoyed
    with eidissolve_nd
    
    S "Have you talked with your parents today?"
    
    show dev skeptical
    with eidissolve_nd
    
    D "No,{w=0.3} I haven't talked with them since I left home."
    
    show sam skeptical
    show dev annoyed
    with eidissolve_nd
    
    S "Really? {cps=5}...{/cps} Hmmm,{w=0.3} any reason why?{w=0.2} Family issues?"
    
    show sam neutral
    show dev skeptical
    with eidissolve_nd
    
    "I really need to go, and I {i}really{/i} don't want to have this conversation."
    
    show dev sad
    with eidissolve_nd
    
    D "I-{w=0.1} No, I just{cps=5}...{/cps} I've been pretty busy the last two days. Getting settled in classes and stuff{cps=5}...{/cps}"
    S "Hmmm, sure."
    
    show dev neutral
    with eidissolve_nd
    
    S "Give them a call kid, I'm sure they miss you as much as you miss them."
    
    show dev skeptical
    with eidissolve_nd
    
    D "Uh,{w=0.1} sure{cps=5}...{/cps} maybe."
    
    show dev neutral
    with eidissolve_nd
    
    "My thumbs circle each other.{w=0.3} Her innocent suggestion burns in my mind as I go to leave, but I have neither the time nor the mindset to meditate on it right now."
    "The smell of smoke and alcohol radiating off of her reminds of the worst parts of home, lessening my desire to spill my life story, even if I had the time."
    D "Is that all, Counselor Sam?{w=0.3} I really should get going to my next class."
    "She nods tiredly and dismisses me with a slow wave of her hand."
    
    show sam grin
    with eidissolve_nd
    
    S "Yeah,{w=0.3} you're good to go kid. And don't be a stranger,{w=0.1} I know my appearance might make it seem otherwise, but my door is always open."
    
    show sam neutral
    with eidissolve
    
    show dev left at moveoutleft(x=0.35)
    hide dev
    
    pause 2
    scene black with dissolve
    stop music fadeout 10
    
    window auto hide
    
    pause 1
    
    "I nod and leave her office.{w=0.3} Turning back, I see her return to her papers and the old computer by her side."

####PART 5####
    
    
    
    "And for the second time on my first day, I’m running late."
    "Any reasonable person would realize there’s no hope and just saunter into class.{w=0.3} But upon recalling how Mr. Hawthorn had \"welcomed\" Emily, I don’t want to test how well I’d hold up to such a dressing-down."
    "I run as fast as I can, skipping steps and trekking through stretches of grass, blowing right by several signs that clearly instruct me to \"KEEP OFF THE GRASS\"."
    
    play music violin_solo fadein 15
    
    "I’m gasping for air by the time I find myself standing before the door to the music room. My hand hovers over the knob and I’m about to turn it before{cps=5}...{/cps}"
    "My ears perk up at the gentle melody of a violin just inside. Damn it, class must already be in session."
    "My arm moves on its own to pull the door open, revealing rows of chairs set in a semicircle, centered around a podium and a whiteboard."
    
    show abimusic_1 behind black
    show abimusic_2 behind abimusic_1
    
    show abigail left behind abimusic_2:
        xpos 0.55
    
    show john left behind abimusic_2:
        xpos 0.9
    
    show dev happy behind abimusic_2:
        xpos 0.2
        ypos 0.1
    
    show music_room_day behind abigail
    hide black with Dissolve(1)
    show abimusic_1:
        pause 0.5
        ease_cubic 4 ypos 1.2
    show abimusic_2:
        pause 0.6
        ease_cubic 3.5 ypos 1.3
    window auto show

    pause .5
    

    "A gray triceratops girl stands alone behind the podium."
    "She lovingly holds a violin, one hand letting the bow travel gracefully across the strings. Her eyes are closed, and a small smile dances across her lips. Her body slowly sways to the rhythm of her melody."
    
    if AU:
        "I recognize the song.{w=0.3} It’s Lili Boulanger’s Nocturne violin solo. A moving piece that becomes more and more colorful, more and more{cps=5}...{/cps} full, as it continues."
        "It builds upon itself, the melancholic beginning swelling into a nostalgic triumph, never speeding, only expanding until it softly begins to trail away into silence."
    else:
        "I become conscious of my gaping expression.{w=0.3} My finger taps along out of sync as I try and fail to follow along with the tempo out of impulse."
        "I have no idea what song she’s playing, but{w=0.3} it’s beautiful."
    
    hide abimusic_1 with dissolve
    hide abimusic_2 with dissolve
    stop music fadeout 3
    
    "I walk to the closest, empty seat. As the girl reaches the finishing notes, an older man stands and walks to her."
    
    show abigail right
    show john:
        ease_cubic 0.75
    
    "He begins to applaud. Everyone else joins in,{w=0.1} me included."
    
    
    
    play music strings fadein 10
    show john grin:
        ease_cubic 1 xpos 0.75
        hop
    show abigail happy right:
        ease_cubic 1 xpos 0.5
    with eidissolve_nd
    
    Ju "Awesome Abigail, completely awesome. That was freaking perfect!"
    A "Thank you, Mr. Johblinsky, for letting me do a demonstration."
    
    show dev skeptical
    show john happy
    with eidissolve_nd
    
    "Her accent is strange.{w=0.3} She rolls her r’s, and her h’s are ultra silent, making her \"thank\" sound like \"tank\". Any word with an r sounds like the purr of a kitten as she speaks it."
    
    show dev neutral
    with eidissolve_nd
    
    "The teacher, Mr. Johblinsky, turns to the rest of the class.{w=0.3} No one seems to notice or care that I’m late."
    
    show abigail neutral:
        parallel:
            ease_cubic 1 xpos 0.9
        parallel:
            pause 0.5
            "abigail left"
    show john:
        ease_cubic 1 xpos 0.45
    show dev surprised
    with eidissolve_nd
    
    J "Oh,{w=0.1} you must be Dev!{w=0.3} Good of you to join us!"
    
    show dev sad
    with eidissolve_nd
    
    "I spoke too soon."
    J "Why don’t you show us some of your skills?{w=0.3} You {i}are{/i} the last to arrive, after all."
    if devnumba1:
        
        show john grin
        with eidissolve_nd
        
        J "I’m already digging the confidence, amigo."
        
        show dev ashamed
        show john devious
        with eidissolve_nd
        
        J "To be the best, you gotta think you’re the best."
        
        show john happy
        with eidissolve_nd
        
        "Much to my chagrin, Mr. Johblinsky points to his forehead, drawing everyone’s attention to the ill-conceived mark on my face."
    
    show dev neutral
    with eidissolve_nd
    
    "The teacher grins and waggles his eyebrows."
    
    show dev skeptical
    with eidissolve_nd
    
    J "And musicians always save the best for last."
    
    show dev sad
    with eidissolve_nd
    
    "He punches the air and makes air guitar gestures while whistling. It seems like my reputation as the only human will continue to precede me."
    
    show dev skeptical
    with eidissolve_nd
    
    "And considering the kind of character that the counselor is, I am wondering if Mr. Hawthorn was the exception and that I should just expect all of my professors to be this{cps=5}...{/cps} eccentric."
    D "Uh{cps=5}...{/cps} Okay, I guess."
    
    show dev neutral
    show john neutral
    with eidissolve_nd
    
    J "Go get whatever you want from the back of the room. No electric anything yet."
    
    show john annoyed
    with eidissolve_nd
    
    J "The electrician’s still gotta do some fuse-fixing or something before we plug in the real bangers.{w=0.3} The kind that will make other \"teaches\" write complaints about me again."
    
    show black with dissolve
    show dev:
        xpos 0.5
        ypos 0.0
    show john behind abigail:
        xpos 0.85
    show abigail left
    
    "I walk around the other students, pointedly avoiding their inquisitive looks.{w=0.3} Sure enough, there’s a pile of drums, many string instruments, a keyboard plopped against the wall, and many, many cases of varied shapes."
    "There also are amplifiers,{w=0.1} pedals,{w=0.1} and sound boards,{w=0.1} every cable neatly folded on top of one another."
    "With nowhere to currently plug them in, I take{nw}"
    if AU:
        show devmusic2 behind black
        extend" an acoustic guitar."
        hide black with dissolve
        "I pluck at the strings and turn the pegs until I tune it correctly.{w=0.3} I’m more than accustomed to what it should sound like, even if my instrument of choice during my music-making afternoons had been its electric variant."
        "Electric or acoustic though, this is the instrument that got me started on music when I was much younger."
        "My fingers rasp against the strings, letting the familiarity settle back in. It almost has a taste: of returning to a place I miss, the smell of grandma’s cooking, my grandfather teaching me to play{cps=5}...{/cps}"
        "Of sweat and small garage concerts with an audience of zero, or vinyls and CDs paid with cash from cutting the neighbors’ grass."
        "I’m deep into my thoughts as I make my way to the very front of the classroom."
        "The chords for \"Walkway to Heaven\" bloom from the tips of my fingers, inundating all of my senses and bringing me comfort."
        "This, I know."
        "The acoustic warmth that the guitar gives the melody turns it wistful, gives it a note of yearning and respite that reverberates on the walls."
        show black with dissolve
        pause 0.2
        hide devmusic2
        "Once I’m finished with the guitar solo, I receive a round of short applause. Mr. Johblinsky is clapping energetically, and Abigail nods approvingly at me."
        
        hide black with dissolve
        show dev somber
        show john happy
        with eidissolve_nd
        
        J "Your fretwork was a little jank at the start, but you did pretty good, Dev!"
        J "Can’t really go wrong with the classics, eh?"
        
        show dev happy
        with eidissolve_nd
        
        "He winks at me as he gives me a thumbs up."
        "My ears go warm and I take the guitar with me to an empty seat."
    else:
        show devmusic1 behind black
        extend" the familiar shape of a trombone case among the rest. I grab it and pull the zipper open, freeing the instrument."
        D "Uh,{w=0.1} I was first trombone in my high school band."
        hide black with dissolve
        "I walk slowly to the front of the class, thinking that even if it's not the sexiest instrument, at least I wasn’t  the first triangle in the band."
        "I briefly wonder if there’s something as sad as a second triangle in bigger school bands."
        "There I stand, in front of eager and expectant eyes, while I fumble with the braces and eye the mouthpiece. It looks dry and a bit dusty, so I thumb at it to remove some of the soot."
        J "Well?"
        "I bring the instrument to my mouth, pressing my lips together, and start playing \"First Nation Army\" starting notes, my arm arching back and forth methodically."
        "The results are{cps=5}...{/cps} Questionable on their own.{w=0.3} It would have been acceptable for a marching band making the rounds around a football field."
        "But I’m on my own, and my hand slips more than it should when landing on the notes."
        "Out of the corner of my eyes, I see the gray tricera from earlier cringe. My cheeks are burning."
        show black with dissolve
        pause 0.2
        hide devmusic1
        "I stop after a few seconds."
        
        hide black with dissolve
        
        pause 0.2
        show john happy:
            ease_cubic 1 xpos 0.7
        show dev sad
        with eidissolve_nd
        
        J "That was alright, Dev!{w=0.3} It’s good to know that you’re not going from absolute zero to hero here."
        "A student snickers."
        unknown "More like from zero point five to hero."
        "Mr. Johblinsky shushes them."
        
        show john right angry:
            hop
        with eidissolve_nd
        
        J "You can either show us the melody of your feet walking out of my classroom or zip it."
        "He makes a zipping motion with his fingers."
        
        show john left annoyed with eidissolve_nd
        
        J "Absolutely no making fun of anyone once you’re past that door and inside my realm, okay?"
        "The class replies with an echo-y \"okay\". I retake my seat and Mr. Johblinsky starts the class proper."
    
    show john neutral behind dev:
        ease_cubic 1 xpos 0.5
        pause 0.5
        ease_cubic 0.5 xpos 0.45
        block:
            pause 1
            "john right"
            hop
            pause 1.5
            ease_cubic 0.5 xpos 0.55
            hop
            pause 1
            "john left"
            pause 1.5
            "john right"
            pause 1
            "john left"
            hop
            pause 1
            ease_cubic 0.5 xpos 0.45
            pause 2
            "john right"
            pause 1.75
            "john left"
            repeat
    
    show dev neutral left:
        parallel:
            ease_cubic 1 xpos 0.2
        parallel:
            pause 0.5
            "dev right"
            easein_cubic 1.2 ypos 0.1
    
    show black behind dev:
        alpha 0
        ease_cubic 2 alpha 0.5
    with eidissolve_nd
    
    "Mr. Johblinsky uses the very first class to go over the schedule for the rest of the semester."
    "The class is otherwise uneventful."
    "This time, I take notes though.{w=0.3} Mostly upcoming expositions and events. Students are supposed to present a piece at the end of the course, either a composition made by oneself or an arrangement based on someone else’s music."
    "It could be a solo presentation with the teacher at the piano, or a duet with one of the students taking helm at the keys."
    "That, or go through a twenty page long written exam."
    "The class ends an hour and a half later.{w=0.3} I’m left with a treasure trove of information on the upcoming semester and feeling a little overwhelmed for the first day, honestly."
    "Abigail is staying to have a short talk with the teacher while the rest of us prepare to leave. Then, Mr. Johblinsky jumps up."
    
    hide black
    
    show john left shocked:
        ease_cubic 0.5 xpos 0.5
        hop
    
    show dev surprised right
    with eidissolve_nd
    
    J "Shucks! I’m late for a meeting. Gotta scram.{w=0.3} Don’t take anything from the classroom without my permission."
    
    show john:
        ease_cubic 1 xpos -0.25
    show dev surprised:
        pause 0.1
        "dev left surprised"
    
    "Then he makes a break for the door, disappearing around the corner."
    
    show john right angry:
        transform_anchor True
        subpixel True
        yoffset 0.0 * 1500
        yanchor 0.0
        
        xpos -0.10
        rotate 20
        easeout_cubic 3 xpos 0.05
    
    "Only for his head to reappear, peeking past the door frame, and his hand making ‘I see you’ gestures at the students still remaining."
    J "I {i}will{/i} notice if someone took anything. Consider this your only warning of my bodacious wrath when it comes to my babies."
    J "{w=0.3}Be{w=0.3}have."
    
    show john:
        ease_cubic 6 xpos -0.25
    
    "Then, he leaves.{w=0.3} For real this time."
    
    hide john
    show c_standing1 left:
        xpos 1.2
        matrixcolor ColorizeMatrix("#9b5c3e", "#ffffff")
    show c_standing2 left:
        xpos 1.2
        matrixcolor ColorizeMatrix("#9b3e4c", "#ffffff")
        
    show c_standing1 left:
        parallel:
            ease_cubic 3 xpos 0.75
        parallel:
            pause 2.9
            "c_standing1 right"
        parallel:
            pause 0.5
            block:
                easein_cubic 0.2 ypos -0.01
                pause 0.01
                easein_cubic 0.2 ypos 0.0
                pause 0.01
                easein_cubic 0.2 ypos -0.01
                pause 0.01
                easein_cubic 0.2 ypos 0.0
                pause 4
                easein_cubic 0.2 ypos -0.02
                pause 0.01
                easein_cubic 0.2 ypos 0.00
                pause 5
                repeat
    show c_standing2 left:
        ease_cubic 3 xpos 0.99
        pause 0.5
        block:
            pause 0.3
            easein_cubic 0.2 ypos -0.02
            pause 0.01
            easein_cubic 0.2 ypos 0.0
            pause 0.01
            easein_cubic 0.2 ypos -0.01
            pause 0.01
            easein_cubic 0.2 ypos 0.0
            pause 3
            easein_cubic 0.2 ypos -0.01
            pause 0.01
            easein_cubic 0.2 ypos 0.00
            pause 4
            repeat        
    
    show abigail neutral left:
        pause 1
        "abigail skeptical"
        pause 1.5
        "abigail left skeptical"
        pause 2.5
        "abigail left saddown"
    
    show dev neutral left:
        parallel:
            0.5
            ease_cubic 1.2 xpos 0.1
        parallel:
            easein_cubic 1 ypos 0.0
        parallel:
            pause 3
            "dev right skeptical"
    with eidissolve_nd
    
    "I’m in the middle of returning the instrument I used for my demonstration when I overhear a couple of students mocking Abigail’s accent."
    
    show dev mad right
    show abigail despair left
    with eidissolve_nd
    
    "They mock her strong r’s and her silent h’s while saying goodbye to her, calling her \"little miss perrrfect\". She turns her nose up at them as she packs her violin."
    "It makes my blood boil.{w=0.3} I guess I was right that this place is just like high school."
    menu:
        "It makes me want to do something.":
            show dev smug:
                hop
                pause 0.5
                "dev surprised" with eidissolve
                pause 1
                "dev unimpressed left"
            with eidissolve_nd
            "I rip a blank page from a nearby, unattended notebook. I hastily ball it up and throw it in the direction of the mean spirited group."
            
            show c_standing1 left:
                ypos 0.0
                pause 2
                "c_standing1 right"
                pause 1
                "c_standing1 left"
                ease_cubic 2.5 xpos -0.25
            show c_standing2 left:
                ypos 0.0
                pause 4
                hop
                ease_cubic 2.5 xpos -0.25
            
            "It hits its mark, bouncing off of the main taunter’s spiky head.{w=0.3} I’m quick to cross my arms and turn away to feign my innocence. They mutter more insults my way now, but leave with sneers on their faces."
                
        "I wait.":
            show dev annoyed
            with eidissolve_nd
            show c_standing1 right:
                pause 1
                "c_standing1 left"
                ease_cubic 2 xpos -0.15
            show c_standing2 left:
                pause 2
                hop
                ease_cubic 2 xpos -0.15
            "I let it pass, not wanting to meddle into something that’s decidedly not my business and that could put a bigger target on both of our backs."
            "Instead{w=0.2} I hang back. Maybe a kind comment will help?"
    
    hide c_standing1
    hide c_standing2
    
    show dev somber:
        ease_cubic 2 xpos 0.35
    show abigail despair left:
        ease_cubic 2 xpos 0.65
        "abigail left sad" with eidissolve
    with eidissolve_nd
    "I cough once the mean group leaves."
    
    show abigail skeptical
    with eidissolve_nd
    
    "Abigail glares at me."
    D "I{cps=5}...{/cps} I actually like your accent."
    
    show dev sad
    show abigail annoyed
    with eidissolve_nd
    
    "Abigail squints at me and I reconsider my words."
    
    show dev ashamed
    with eidissolve_nd
    
    D "What I mean is{cps=5}...{/cps} it’s{cps=5}...{/cps} sophisticated sounding.{w=0.3} Don’t, uh{cps=5}...{/cps} don’t let them get you down."
    
    show dev skeptical
    show abigail surprised
    with eidissolve_nd
    
    play sound phone_notification volume 3 loop
    
    "Something inside her skirt pocket begins pinging repeatedly.{w=0.3} She ignores it as she continues looking at me."
    
    stop sound fadeout 2
    show dev neutral
    show abigail skeptical
    with eidissolve_nd
    
    A "I wasn’t.{w=0.3} But thank you, I suppose. I{cps=5}...{/cps}"
    
    show dev surprised
    show abigail neutral
    with eidissolve_nd
    
    A "I liked your playing."
    if AU:
        show dev somber
        with eidissolve_nd
        D "Thanks,{w=0.2} I’m a bit rusty, but I used to play the guitar all the time when I was a kid.{w=0.3} Even had dreams of being some big rock star or something."
        show dev neutral
        show abigail sad
        with eidissolve_nd
        A "\"Had\"?{w=0.3} You do not any more?"
        D "Oh, uh,{w=0.1} no."
        A "Why not?"
        show dev thinking
        with eidissolve_nd
        D "I wasn’t all that good to be honest.{w=0.3} There were several other kids at my school that were {i}far{/i} better than me.{w=0.2} Guess I just kinda figured it wasn’t going to be my path in life."
        show dev happy
        show abigail neutral
        with eidissolve_nd
        A "That is a shame.{w=0.1} You seemed quite good to me, and that song you played, it was certainly interesting. What is it called? Who was the composer?"
        show dev neutral
        with eidissolve_nd
        D "\"Walkway to Heaven\" and, uh, I guess Led Blimp?"
        show abigail happy
        with eidissolve_nd
        A "Oooooo, and who is that?"
        show dev skeptical
        show abigail neutral
        with eidissolve_nd
        D "Led Blimp? The rock band? You’ve never heard of them?"
        show abigail saddown
        with eidissolve_nd
        "Her face drops."
        A "I was not{cps=5}...{/cps} I did not listen to much outside of classical music growing up.{w=0.3} But better late than never to broaden my knowledge, hm?"
    else:
        show dev somber
        with eidissolve_nd
        D "Thanks but,{w=0.2} I mean,{w=0.1} I wasn’t very good. Even Mr. Johblinsky seemed to notice."
        show abigail ashamed a_upset a_noblush
        with eidissolve_nd
        A "It was certainly an interesting instrument you played. It looks so cumbersome, I can’t imagine it is easy to play."
        show dev skeptical
        show abigail neutral
        with eidissolve_nd
        D "The trombone?{w=0.3} I mean,{w=0.1} I guess so. I take it you never played in high school pep rallies?"
        show abigail sad
        with eidissolve_nd
        "Her face drops."
        A "Oh, um{cps=5}...{/cps} I was homeschooled."
        show dev somber
        show abigail saddown
        with eidissolve_nd
        D "Ah. That’s{cps=5}...{/cps} cool."
    
    show dev thinking
    with eidissolve_nd
    
    "Taking a good look at her now, she’s prim, proper, and elegant. Standing ramrod straight, and with perfectly combed hair."
    
    show dev sad
    show abigail ashamed
    with eidissolve_nd
    
    "I have no idea how to reply in the ensuing silence."
    
    play sound phone_notification volume 3 loop
    show abigail angrydown
    with eidissolve_nd
    
    "Her phone keeps ringing off the hook, notifications pinging one after another."
    
    stop sound fadeout 2
    show dev ashamed
    with eidissolve_nd
    
    "It’s giving {i}me{/i} anxiety at this point."
    
    show dev skeptical
    show abigail annoyed
    with eidissolve_nd
    
    D "Are you{cps=5}...{/cps} going to pick up?"
    A "No,{w=0.3} I am not."
    
    play sound phone_notification volume 3 loop
    show abigail annoyeddown
    with eidissolve_nd
    
    "With her phone continuing to chime, she looks me up and down now, her frown deepening as she focuses on my shirt."
    
    stop sound fadeout 2
    show dev surprised
    with eidissolve_nd
    
    A "Your clothes{cps=5}...{/cps}"
    "I look down at myself. Sure, my shirt's a bit wrinkled and my jeans have seen better days,{w=0.3} but it's not like I'm planning on walking down a runway."
    
    show dev skeptical
    show abigail skeptical 
    with eidissolve_nd
    
    D "What’s wrong with them?"
    "She begins digging around in her bag before pulling out some sort of small spray bottle."
    
    show abigail neutral left:
        ease_cubic 1 xpos 0.62
    
    D "What are you-?"
    
    play sound spray
    show dev surprised
    with eidissolve_nd
    
    "Without warning she spritz a few sprays of some sort of mystery liquid onto my shirt."
    
    show dev yiik
    show abigail surprised
    with eidissolve_nd
    
    "{sc}{b}OH GOD, I’VE BEEN ACID ATTACKED!!!{/b}{/sc}"
    
    show dev furious f_angry:
        easeout_quad 0.5 xpos 0.3
    show abigail shocked:
        easeout_quad 0.5 xpos 0.7
    with eidissolve_nd
    
    D "{b}What the hell?{/b}"
    
    show dev mad
    with eidissolve_nd
    
    "We jump apart, her in embarrassment and me in shock."
    A "Sorry! Sorry! It is wrinkle-release spray. See watch{cps=5}...{/cps}"
    
    show dev behind abigail:
        pause 0.8
        "dev skeptical"
        pause 1.3
        "dev surprised"
    show abigail sad:
        parallel:
            ease_cubic 2 xpos 0.45
        parallel:
            pause 1.8
            easeout_back 0.2 ypos 0.03
            pause 0.2
            ease_cubic 0.4 ypos 0.0
        parallel:
            pause 2.5
            ease_cubic 1 xpos 0.65
    
    "She grabs the hem of my shirt and gives it a slight tug. When she lets go,{w=0.1} it's noticeably smoother than before."
    
    show dev surprised
    show abigail embarrassed
    with eidissolve_nd
    
    "Afterwards she wilts in embarrassment, her cheeks turning pink."
    
    show dev ashamed
    with eidissolve_nd
    
    "I find myself just as bashful for freaking out over something so small.{w=0.3} Something helpful even."
    
    show abigail somber
    with eidissolve_nd
    
    D "Huh.{w=0.3} Well{cps=5}...{/cps} thanks, I guess."
    
    show dev sad
    show abigail disappointed
    with eidissolve_nd
    
    A "Sorry again. I just{cps=5}...{/cps} thought I would help."
    
    show dev somber
    with eidissolve_nd
    
    D "It’s fine.{w=0.3} Just maybe a warning next time."
    
    show dev neutral
    show abigail sad
    with eidissolve_nd
    
    "She shakes her head fervently before holding out the offending spray bottle in both hands."
    
    show dev skeptical
    show abigail somber
    with eidissolve_nd
    
    A "No, no. It was rude of me, but please, take it for yourself.{w=0.3} I have several more back in my room. Think of it as my apology to you."
    "I gingerly take the bottle from her, inspecting it. I mean, I wouldn’t have thought of it myself, but it could clean me up on days that I find myself rushed."
    
    show dev happy
    show abigail neutral
    with eidissolve_nd
    
    D "Alright.{w=0.3} Yeah, thanks. Your name was Abigail, right?"
    
    show dev skeptical
    show abigail happy
    with eidissolve_nd
    
    A "Kyllä. I mean, yes. And you were{w=0.3} \"Dep\"?"
    
    show dev neutral
    show abigail neutral
    with eidissolve_nd
    
    D "It’s Dev,{w=0.2} actually. Nice to meet you."
    
    show abigail skeptical
    show dev somber:
        ease_cubic 1 xpos 0.4
    with eidissolve_nd
    
    "I timidly hold out my hand, not sure if it’s the proper etiquette or not here."
    
    show dev happy:
        pause 1.5
        easeout_back 0.2 ypos 0.01
        pause 0.2
        ease_cubic 0.4 ypos 0.0
    show abigail happy:
        parallel:
            ease_cubic 1 xpos 0.55
        parallel:
            pause 1.5
            easeout_back 0.2 ypos 0.01
            pause 0.2
            ease_cubic 0.4 ypos 0.0
        parallel:
            pause 2.5
            ease_cubic 1 xpos 0.65
        
    with eidissolve_nd
    
    "She lightly accepts the handshake with a smile and a nod."
    A "It is good to meet you too, Dev."
    if devnumba1:
        show dev skeptical
        show abigail skeptical
        with eidissolve_nd
        
        A "Um{cps=5}...{/cps}"
        A "I was not going to ask to not be rude, but{cps=5}...{/cps}"
        
        show dev happy
        show abigail somber
        with eidissolve_nd
        
        D "By all means, ask. I wouldn’t think you’re rude."
        
        show dev sad
        show abigail neutral
        with eidissolve_nd
        
        A "Why is there a number one on your forehead?"
        
        show abigail disappointed
        with eidissolve_nd
        
        "I sigh aloud at that."
        
        show dev ashamed
        with eidissolve_nd
        
        "I can’t delude myself anymore:{w=0.3} I got got."
        
        show dev sad
        with eidissolve_nd
        
        "But Abigail doesn’t need to know that, we just met!{w=0.3} I don’t need the image of me being a dork branded into her impression of me."
        
        show abigail skeptical
        with eidissolve_nd
        
        D "It’s{cps=5}...{/cps} a freshman thing."
        
        show abigail surprised
        with eidissolve_nd
        
        A "A \"freshman thing\"?"
        D "Yeah,{w=0.3} it’s a tradition{cps=5}...{/cps} or something."
        
        show abigail happy
        with eidissolve_nd
        
        A "Oh?"
        
        show abigail joy
        with eidissolve_nd
        
        "She seems to light up at that."
        
        show dev skeptical
        with eidissolve_nd
        
        A "I can’t believe I hadn’t heard of this! You Americans are so unique."
        
        show dev shocked
        show abigail surprised
        with eidissolve_nd
        
        A "Dev,{w=0.2} help me find a pen!"
        
        show dev terrified
        with eidissolve_nd
        
        D "Ah, no no!"
        
        show dev sad
        show abigail skeptical
        with eidissolve_nd
        
        "She looks back at me in confusion. Damn it, I still have to save face here."
        
        show dev somber
        with eidissolve_nd
        
        D "I mean,{w=0.1} the day’s almost over and it really wasn’t {i}that{/i} big a tradition."
        
        show dev happy
        with eidissolve_nd
        
        D "Did you see anyone else with it today?"
        
        show abigail sad
        with eidissolve_nd
        
        A "Oh.{w=0.3} No, I suppose I didn’t."
        
        show dev sad
        show abigail saddown
        with eidissolve_nd
        
        "She actually seems a bit disappointed at that, but she doesn’t need me literally painting a target on her forehead, so it’s for the best."
    
    play sound phone_notification volume 3 loop
    show dev skeptical
    show abigail annoyedconsidering
    with eidissolve_nd
    
    "Her phone beeps again, and this time a flicker of annoyance shows on her face. She fidgets with the strap of her violin case, clearly trying to ignore it, and I can only guess why.{w=0.3} Maybe I should ask about it?"
    
    menu:
        "Be nosy, ask her.":
            jump abi_be_nosy
        "Mind your own business.":
            jump abi_ignore
    
label abi_be_nosy:
    
    stop sound fadeout 2
    show dev somber
    show abigail annoyed
    with eidissolve_nd
    D "Is everything ok?{w=0.3} Kinda hard to ignore all that ringing."
    show abigail sad
    with eidissolve_nd
    A "It is{cps=5}...{/cps} fine.{w=0.3} Just my parents{cps=5}...{/cps} They can be rather,{w=0.3} how do you say{cps=5}...{/cps} \"clingy\"?"
    show dev neutral
    with eidissolve_nd
    D "Ah,{w=0.1} gotcha. "
    "I can’t help but remember my talk with the counselor, about my parents{cps=5}...{/cps}"
    show abigail neutral
    with eidissolve_nd
    D "I’m sure they just miss you.{w=0.3} You should answer them."
    show dev happy
    show abigail somber
    with eidissolve_nd
    "I offer a supportive smile."
    show abigail worried
    with eidissolve_nd
    A "You are{cps=5}...{/cps} probably right. "
    show dev neutral
    show abigail neutral
    with eidissolve_nd
    "She sighs, finally pulling out her phone and scrolling through it for a moment."
    show dev happy
    show abigail skeptical
    with eidissolve_nd
    A "Hmm, seems they wish to talk.{w=0.3} One moment please."
    show dev neutral
    show abigail neutral right:
        ease_cubic 1 xpos 0.75
    with eidissolve_nd
    "She moves the phone up to her head."
    A "Hello?{w=0.4} Yes, Mama{cps=5}...{/cps} No, I was in class, I still am-{w=0.4} I did not hear the texts{cps=5}...{/cps} Yes, I am fine{cps=5}...{/cps}"
    show abigail surprised
    with eidissolve_nd
    A "I was not-{w=0.4} I was not ignoring you."
    show dev skeptical
    show abigail sad
    with eidissolve_nd
    "She kinda was though."
    show dev sad
    show abigail disappointed left:
        pause 1
        "abigail right disappointed"
    with eidissolve_nd
    "Abigail glances at me and turns away, her voice even lower and now speaking in a foreign language."
    A "Usko minua, mie olin vaan luokassa enkä kuullu{cps=5}...{/cps} En mie tahallaa jättäny vastaamatta{cps=5}...{/cps} Mie sanoin jo, mie olen luokassa{cps=5}...{/cps}"
    A "Joo{cps=5}...{/cps} joo{cps=5}...{/cps} Mie soitan ku mie pääsen takas kämppään{cps=5}...{/cps} Joo{cps=5}...{/cps} Mieki sinua."
    show abigail saddown right
    "She hangs up the phone, still turned away."
    show abigail surprised
    with eidissolve_nd
    D "Trouble?"
    show abigail somber left:
        ease_cubic 1 xpos 0.65
    A "Hmmm?{w=0.3} No,{w=0.2} as I said, they can just be{cps=5}...{/cps} persistent{cps=5}...{/cps}"
    show dev somber
    show abigail neutral
    with eidissolve_nd
    A "Anyways,{w=0.1} I should hurry back to the dorms before they try to reach me again."
    D "Oh, right, heh. Don’t let me keep you."
    show dev happy
    show abigail happy
    with eidissolve_nd
    A "It was very nice meeting you, Dev. And thank you."
    show dev surprised
    show abigail neutral
    with eidissolve_nd
    D "What for?"
    "She shrugs at that."
    show abigail saddown
    with eidissolve_nd
    A "For just talking to me, I suppose.{w=0.3} Our peers haven't been so friendly."
    show dev somber
    show abigail sad
    with eidissolve_nd
    D "Right, I uh, noticed. But you’re welcome.{w=0.3} See you in class tomorrow?"
    show dev happy
    show abigail somber
    with eidissolve_nd
    
    scene black with dissolve
    
    "She gives me a nod as we both leave the classroom and part ways. Even though it was a short and kind of awkward interaction, she seems nice."
    
    stop music fadeout 10
    
    window auto hide
    
    pause 1
    
    jump chap2_part6
    
label abi_ignore:

    stop sound fadeout 2
    "I hold up the wrinkle-release spray to change the subject, joking."
    show dev happy
    show abigail happy:
        chuckle
    with eidissolve_nd
    D "Not exactly what you think of for \"back to school essentials\"."
    A "Oh, I suppose it isn’t.{w=0.3} I guess I just like things neat and tidy, hehe."
    show abigail somber
    with eidissolve_nd
    A "Something I got from my upbringing. And \"old habits are hard to die\" right? Hehe."
    show dev somber
    with eidissolve_nd
    D "Right."
    show abigail surprised
    with eidissolve_nd
    play sound phone_notification volume 5 loop
    "Her phone beeps once more, seemingly louder this time. She glances at it briefly before looking back at me."
    stop sound fadeout 2
    show abigail sad
    with eidissolve_nd
    D "Are you gonna get that?"
    A "Ah, no. It is probably just-"
    play sound phone_ring loop
    show dev surprised
    show abigail shocked
    with eidissolve_nd
    "Her phone rings, giving us both a start.{w=0.3} She winces slightly before reluctantly answering it."
    stop sound fadeout 2
    show dev neutral
    show abigail sad right:
        ease_cubic 1 xpos 0.7
    with eidissolve_nd
    A "Hello?{w=0.4} Yes, Mama{cps=5}...{/cps} No, I was in class{cps=5}...{/cps} I did not hear the texts{cps=5}...{/cps} Yes, I am fine{cps=5}...{/cps}"
    "Her voice softens as she continues talking to her mother. I feel a bit awkward just standing here."
    show dev ashamed
    with eidissolve_nd
    D "So should I go or{cps=5}...{/cps}?"
    show abigail skeptical left
    with eidissolve_nd
    A "Hmm?{w=0.3} Oh, just one moment."
    show dev sad
    show abigail sad right
    with eidissolve_nd
    A "No mama, that was{cps=5}...{/cps} No, it was just{w=0.3} the professor{cps=5}...{/cps} No, you don't need to put papa on{cps=5}...{/cps}"
    show abigail saddown
    with eidissolve_nd
    "She heaves a sigh away from the receiver to prepare herself."
    show abigail sad
    with eidissolve_nd
    A "Hello papa{cps=5}...{/cps} no I was-{cps=5}...{/cps} I wasn't{cps=5}...{/cps}"
    show dev skeptical
    show abigail disappointed left:
        pause 1
        "abigail right disappointed"
    with eidissolve_nd
    "Abigail glances at me and turns away, her voice even lower and now in another language."
    A "Usko minua, mie olin vaan luokassa enkä kuullu{cps=5}...{/cps} En mie tahallaa jättäny vastaamatta äitille{cps=5}...{/cps} En mie väittäny vastaan, mie yritin vaan selittää sille että-"
    show dev ashamed
    with eidissolve_nd
    "I shift my weight from one foot to the other, feeling more awkward by the second as Abigail continues her phone conversation in a language I don’t understand."
    "Her voice is low, and she keeps glancing at me as if she's worried about me overhearing something important.{w=0.3} Which is frankly giving me too much credit, with my menial grasp on the English language as it is."
    show dev somber
    with eidissolve_nd
    D "I think I’ll just head out since you’re busy.{w=0.3} See you tomorrow?"
    show abigail sad
    with eidissolve_nd
    "Abigail purses her lips, clearly disappointed at the disruption but unable to get out of it. She places the phone to her chest to reply."
    show abigail somber left
    with eidissolve_nd
    A "Yes, of course.{w=0.3} I will see you then, Dev."
    D "Alright, catch you later then."
    
    scene black with dissolve
    hide dev
    hide abigail
    
    "I give her a nod and start to back away. She waves me goodbye with her free hand before grimacing at whatever she’s hearing on the other end of the line."
    "I head out of the classroom, feeling a bit lighter after our interaction. Even though it was short and kind of awkward, it was nice to connect with someone else on campus."

    stop music fadeout 10
    
    window auto hide
    
    pause 1
    
    jump chap2_part6

####PART 6####
label chap2_part6:
    play music family_drama fadein 3.0
    
    show dev behind black:
        xpos 0.5
    show dormroom_dev_empty_day behind dev
    
    window auto show
    
    "I check my phone to see that Theo had texted me earlier saying he'd be in the library until it closed.{w=0.3} I stop by my room before heading there, figuring he could use some help with whatever's keeping him so late."
    "History homework, I imagine."   
    "And despite how Counselor Sam's whole vibe rubbed me the wrong way,{w=0.1} I think she was right about seizing the opportunity I have in making a game with him."  
    "Before any of that though, I figure I should at least try and call home."

    if devnumba1:

        "First thing I do when I get back to my room is scrub my forehead hard enough to strip chrome from a bumper."

        "After enough time, my skin is left spotless, save for the aching, bright red splotch of skin left in its wake."

        "Then, I get to thinking about Abigail’s change of mood earlier."
        
        $ devnumba1 = False
        $ devnumba2 = True
        show dev_phonehome_1 behind black
        hide black with Dissolve(1)

        "That, coupled with Counselor Sam’s advice, I find myself pulling out my phone and dialing my parents’ number."

    else:
        
        show dev_phonehome_1 behind black
        hide black with Dissolve(1)
        
        "When I get back to my dorm, I’m quick to pull out my phone and call home. Images of Abigail’s change in mood fresh in my mind."


    "Someone picks up the line, a beat of silence passing before they answer."
    
    show dev_phonehome_1_2 with dissolve
    hide dev_phonehome_1 with dissolve

    Dad "Hmmm{cps=5}...{/cps} hello?{w=0.3} Who is this?"

    D "H{w=0.1}-Hey dad, it's uh,{w=0.3} it's me."
    
    show dev_phonehome_1 with dissolve
    hide dev_phonehome_1_2 with dissolve

    "Another beat of silence. My palms begin to sweat."
    
    show dev_phonehome_1_3 with dissolve
    hide dev_phonehome_1 with dissolve

    D "H{w=0.1}-Hello?{w=0.1} Can you hear me?"

    Dad "Huh?{w=0.3} Oh, yeah{cps=5}...{/cps} who was this again?"

    D "It's me, Dad{cps=5}...{/cps} it's{w=0.1} Dev."

    Dad "O{w=0.1}-OH! Hey champ, how are you doing?{w=0.3} Me and your mom haven't heard from you since yesterday."
    
    show dev_phonehome_1 with dissolve
    hide dev_phonehome_1_3 with dissolve

    D "{cps=5}...{/cps} I didn't call you yesterday."
    
    show dev_phonehome_1_3 with dissolve
    hide dev_phonehome_1 with dissolve

    Dad "What?{w=0.3} Yeah you did, we talked about{cps=5}...{/cps} uh{cps=5}...{/cps}"

    Dad "Hmm, we definitely talked about{cps=5}...{/cps} um{cps=5}...{/cps}"

    "His words are a slurry of syllables crashing against one another."
    "Is he really?"

    show dev_phonehome_1_4 with dissolve
    hide dev_phonehome_1_3 with dissolve

    D "Dad,{w=0.3} we didn't talk yesterday."

    Dad "Hmm, yeah{cps=5}...{/cps} Heh, well,{w=0.3} it took you long enough to call. You know, I heard about how those cold-blooded girls go crazy for us warmbloods.{w=0.3} Bet you were too busy drowning in p-"

    D "{b}Dad!{/b}"

    "He is."

    D "Dad, are you drunk?"

    Dad "What?{w=0.3} I am {i}not{/i} drunk."

    D "You sound like you are."

    Dad "{cps=5}...{/cps}"

    D "{cps=5}...{/cps}"
    
    show dev_phonehome_2_2 with dissolve
    hide dev_phonehome_1_4 with dissolve

    D "Dad!"

    Dad "Hmm, what's up?"

    D "Are you drunk,{w=0.3} {i}again{/i}?"

    Dad "Look, Dev{cps=5}...{/cps} work was pretty rough today.{w=0.3} I just had one drink to relax and unwind."
    
    show dev_phonehome_2 with dissolve
    hide dev_phonehome_2_2 with dissolve
    
    D "Was that \"one drink\" before or after work this time?"

    Dad "{cps=5}...{/cps}"
    
    show dev_phonehome_2_2 with dissolve
    hide dev_phonehome_2 with dissolve
    
    D "God damn it, Dad! You promised!"

    Dad "Huh?{cps=5}...{/cps} Hold up one minute, Dev, I think your mom wants to talk to you{cps=5}...{/cps}"
    
    show dev_phonehome_2 with dissolve
    hide dev_phonehome_2_2 with dissolve
    
    "The sound of muffled static plays as the other end of the line is shuffled about."

    Dad "Sorry champ,{w=0.3} it actually looks like she's asleep on the couch."

    D "Is she asleep or is she passed out on the couch?"

    Dad "Look Dev, we{w=0.1} - me and your mom{w=0.1} - are not drunk, we only had a few drinks-"
    
    show dev_phonehome_2_2 with dissolve
    hide dev_phonehome_2 with dissolve

    D "I fucking knew it!"
    
    stop music fadeout 7
    
    show dev_phonehome_3 with dissolve
    hide dev_phonehome_2_2 with dissolve
    
    D "You know what dad, my day was pretty rough too, so I think I'm going to go to bed."

    Dad "A{w=0.1}-Alright{cps=5}...{/cps} talk to you later champ, I lov-"

    "I hang up."
    
    play music tears_of_the_past fadein 7.0
    
    show dev_phonehome_4 with dissolve
    show dev_phonehome_5 behind dev_phonehome_4
    hide dev_phonehome_3 with dissolve
    
    "I don't want to deal with this."

    hide dev_phonehome_4 with edissolve_long
    pause 7
    
    
    
    "I think I finally have an answer for counselor Sam's question:{w=0.3} I'm not homesick,{w=0.3} at all."
    "I feel envious of Emily, Rebecca and Abigail. I wish I could wriggle my fingers on a pencil, a keyboard or freaking maracas to be able to create {i}anything{/i},{w=0.3} make something of myself more than the child of a pair of drunks."
    "Counselor Sam, in all of her foul-smelling wisdom, is right about something.{w=0.3} I can't afford to let opportunities pass me by."
    "I couldn't do anything about the situation back home.{w=0.3} Still can't, I guess."
    
    show dormroom_dev_empty_night behind dev
    show dev annoyed left with eidissolve_nd:
        xpos 0.75
    hide dev_phonehome_5 with dissolve
    "But I can do something about my situation here."
    
    "I dial Theo's number."
    
    window auto hide
    show dormroom_dev_empty_night as back1:
        crop (0.0, 0.0, 0.5, 1.0)
        xanchor 0.0
        easemovey(1.0, t=1.0)
    show library behind dormroom_dev_empty_night, back1:
        xanchor 0.45
        sety(-1.0)
        easemovey(0.0, t=1.0)
    show theo behind back1:
        xpos 0.25
        sety(-1.0)
        easemovey(0.0, t=1.0)

    show dormroom_dev_empty_night:
        #crop (0.0, 0.0, 1.0, 1.0)
        xanchor 0.0
        xpos 0.5 crop (0.5, 0.0, 1.0, 1.0)

    pause 0.5
    
    show theo skeptical
    with eidissolve_nd
    
    T "Hey man,{w=0.1} what's wrong?" 

    show dev skeptical
    with eidissolve_nd

    D "{cps=5}...{/cps}Why do you assume something is wrong?"
    
    show theo grin
    with eidissolve_nd

    T "Well,{w=0.2} you are calling me rather than texting me like a normal person, so I only assumed-"
    
    show dev annoyed
    show theo skeptical
    with eidissolve_nd

    D "Whatever, listen, you were right, so{cps=5}...{/cps} I want to do it with you."

    "There's a pause."
    
    show dev surprised
    show theo crossed c_smugconsidering
    with eidissolve_nd

    T "{cps=5}...{/cps}Uh, you know, I am very flattered, but I don't think I'm interested in you that way buddy.{w=0.3} But thanks for the offer."
    
    show dev skeptical
    with eidissolve_nd

    "That came out wrong."
    
    show dev unimpressed
    with eidissolve_nd

    D "The game, Theo!{w=0.3} The game, I want to make the game with you."
    
    show dev skeptical
    show theo neutral
    with eidissolve_nd

    T "Oh really? That's cool, man{cps=5}...{/cps}"
    
    show dev sad
    show theo unimpressed
    with eidissolve_nd

    D "You don't sound as enthusiastic as last night."
    
    show dev neutral
    show theo ashamed a_upsetconsidering
    with eidissolve_nd

    T "No I am, it's just{w=0.3} - and I'm being serious this time{w=0.2} - is something wrong?{w=0.3} You sound pretty mad{cps=5}...{/cps} If this is about what I texted you this morning{cps=5}...{/cps}"
    
    show dev ashamed
    show theo sad
    with eidissolve_nd

    D "No, I{cps=5}...{/cps} Let's just say families are complicated."
    
    show dev sad
    show theo saddown
    with eidissolve_nd

    T "Right{cps=5}...{/cps}"
    
    show theo neutral
    with eidissolve_nd

    T "Hey,{w=0.3} Elliot should be back at the dorm and I'm nearly done with this tower of books I've got going on in the library, you want to meet us over at our dorm and hang out for a bit?{w=0.3} We never did finish Rock Ring."

    show dev skeptical
    show theo unimpressed
    with eidissolve_nd

    D "So you're still in the library. Do you mind me coming there?"
    
    show dev sad
    show theo skeptical
    with eidissolve_nd

    T "{cps=5}...{/cps}"
    
    show dev somber
    show theo joy j_cheerful
    with eidissolve_nd

    T "Absolutely not. Come on down, man!"
    
    window auto hide
    stop music fadeout 10
    pause .5

    scene black with dissolve
    pause .5
    hide dev
    hide theo
    
    # Change Scene
    
    if LUNCH:

        "This is my lightest day of the week in terms of the amount of lessons I have to attend, but my duties are not over,{w=0.3} I have a favor to repay."

    else:

        "Luckily,{w=0.3} today is a light class-load day. And I may not have taken him up on his offer, but it only feels right to help Theo out with his history assignments if he needs it."

        "The dude’s already done more than enough for me in other ways."
    
    play music to_many_books_to_many_feels fadein 10
    show library behind black
    show theo:
        xpos 0.65
        ypos 0.1
    hide black with dissolve  

    pause 0.5
    
    show dev at moveinright(0.15)
    with eidissolve_nd
    
    "Following the map in the CCC app, this time easily finding the library and Theo torturing himself in the middle of a very literal tower of books."
    
    show dev:
        ease_cubic 1.2 xpos 0.35
    
    show theo:
        pause 1
        "theo left happy" with eidissolve
    with eidissolve_nd

    "As I approach him, I see that more than half of the books on his table aren't even about any sort of history."
    
    show theo grin left
    with eidissolve_nd
    
    "He hears me get closer. His eyes twinkle when he sees me."

    if devnumba2:
    
        show dev surprised
        show theo crossed c_annoyed
        with eidissolve_nd
        "He points to my forehead, grinning ear to ear."

        T "You got rid of it!"
        
        show dev surprised left:
            hop
        show theo surprised right:
            hop(y=0.1)
        with eidissolve_nd

        "He's shushed and I laugh at his expression of despair."
        
        show dev smug right
        show theo ashamed a_upset left
        with eidissolve_nd

        D "They're going to kick you out for screaming."
        
        show dev annoyed
        show theo happy
        with eidissolve_nd

        D "It's the least you'd deserve for making me go through with this."
        
        show theo crossed c_smug
        with eidissolve_nd
        
        "He crosses his arms."
        
        show dev unimpressed
        with eidissolve_nd
        
        T "Worth it."
        
        show dev neutral
        show theo neutral
        with eidissolve_nd

        T "Sis texted me about the \"Number 1\" . I asked her to snap a picture of you for me too, but she told me to not be a creep."
        
        show dev smug
        with eidissolve_nd

        D "At least one of you has a good head on their shoulders."
        
        show theo cheerful
        with eidissolve_nd
        
        T "Yeah,{w=0.3} me."
        
        show dev happy
        show theo happy
        with eidissolve_nd
        
        "He flaps his wings happily."

        D "Yeah, you're all smiles now, but just wait till I figure out a good payback."
        
        show dev unimpressed
        show theo surprised
        with eidissolve_nd
        
        D "I only had a permanent marker so I had to scrub half my face off just to get rid of it."
        
        show theo cheerful:
            chuckle(y=0.1)
        with eidissolve_nd
        
        "That makes him cough a laughing fit into a closed fist."
        
        show theo happy
        with eidissolve_nd

        T "S{w=0.1}-Sure, dude. Of course."

    else:    
        show theo sad
        with eidissolve_nd
        
        T "Aw, man.{w=0.3} You didn't draw anything on your forehead."
        
        show dev unimpressed
        with eidissolve_nd

        D "I have some semblance of dignity to conserve. And I don't need help whittling it away any faster this year."

    show theo neutral
    with eidissolve_nd
    
    "I pick up a random book."
    
    show dev terrified
    show theo skeptical
    with eidissolve_nd

    "\"Advanced quantum mechanics\""
    
    show dev surprised
    with eidissolve_nd

    D "Theo, what the hell?{w=0.3} Is this for one of your classes?"
    
    show dev neutral:
        parallel:
            ease_cubic 1 xpos 0.4
        parallel:
            pause 0.5
            easein_cubic 1.2 ypos 0.1
        
    with eidissolve_nd

    "I sit in the chair next to him."
    
    show dev skeptical
    show theo thunk
    with eidissolve_nd

    T "Huh?{w=0.3} Oh, yeah, but that stuff was easy. History though? Who cares what dead people did{cps=5}...{/cps}"
    
    show theo neutral
    with eidissolve_nd

    D "Okay, fair enough.{w=0.3} But why didn’t you put any of them away when you were done?"
    
    show dev neutral
    show theo grin
    with eidissolve_nd

    T "That’s what the librarian and her assistants are here for."
    
    show dev annoyed
    with eidissolve_nd

    "I frown at him."
    
    show dev skeptical
    show theo unimpressed
    with eidissolve_nd

    D "Look, I’m going to help you as much as I can, that’s a given, buuuut{cps=5}...{/cps}"

    D "We’re putting these back in their rightful place, because my grandmama did not raise me that way."

    "My parents did, but I don’t want to be that way."
    
    show dev sad
    show theo neutral
    with eidissolve_nd

    "Mentioning her out loud makes me realize how much I miss grandma, especially in the wake of my phone call home.{w=0.3} I grab another book, this time about actual history, and ask Theo what he covered in class."
    
    show dev neutral
    with eidissolve_nd
    
    show black behind dev:
        alpha 0
        ease_cubic 1 alpha 0.5

    "Ottoman empire.{w=0.3} Easily enough located through the records. There’s more than enough information about it to go through, and we don’t have to cross reference many texts to find all the bullet points that will be in Theo’s next test."

    "I, too, have General History as one of my courses, so this will help me quite a lot. Theo hasn’t mentioned if the tutor for his course is the same as mine, and we’re too busy trying to overcome his poor information retention to focus on anything else."

    "To be fair to him,{w=0.3} it is an absurd amount of info, and I see why Theo asked for help in the first place."

    "I end up suggesting flash cards."
    
    show theo cheerful
    with eidissolve_nd

    "He seems happy with those."
    
    hide black
    
    show dev skeptical
    show theo happy
    with eidissolve_nd

    T "My sis once tried to help me that way, but{w=0.3} she isn’t half as patient with me like you are."
    
    show theo grin
    with eidissolve_nd
    
    "He grins at me."
    
    show dev happy
    with eidissolve_nd

    T "Seriously,{w=0.3} thanks, dude."
    
    show dev thinking
    show theo neutral
    with eidissolve_nd

    "Remembering how fondly Rebecca spoke of Theo, and how fondly he’s speaking of her now, I feel another pang of envy."

    "Although I am reminded of something she said{cps=5}...{/cps} or called me{cps=5}...{/cps}"
    
    show dev skeptical
    show theo surprised
    with eidissolve_nd
    
    D "Hey Theo,{w=0.3} what does \"skinnie\" mean?"
    
    show dev surprised behind theo
    show theo shocked:
        easein_bounce 0.5 xpos 0.5
    with eidissolve_nd

    T "Shhuush shhh!"
    
    show theo shocked right
    with eidissolve_nd

    "He quickly silences me, looking back and forth over the library."
    
    show dev sad
    show theo annoyed left:
        ease_cubic 1.2 xpos 0.65
    with eidissolve_nd

    T "You can’t say stuff like that out loud in here, not unless you want the librarian to bring campus security on us.{w=0.3} And trust me,{w=0.1} she will."
    
    show theo skeptical
    with eidissolve_nd
    
    T "Do you really not know what that word means?"
    
    show dev skeptical
    with eidissolve_nd

    D "I came from a mostly human town, I never heard anyone use that before."
    
    show dev neutral
    show theo unimpressed
    with eidissolve_nd
    
    T "Who called you it then?"
    
    show theo surprised
    with eidissolve_nd
    
    D "Your sister."
    
    show theo angrydown
    with eidissolve_nd
    
    T "Dang it, Rebecca{cps=5}...{/cps}"

    show dev skeptical
    show theo skeptical
    with eidissolve_nd
    
    D "I am assuming it isn’t some saurian nickname for humans like I thought?"
    
    show theo sad
    with eidissolve_nd

    T "No, it is. Just{w=0.3} not a very nice one exactly{cps=5}...{/cps}"
    
    show dev annoyed
    with eidissolve_nd

    D "So she was insulting me then?"
    
    show dev skeptical
    show theo thinking t_thunk
    with eidissolve_nd

    T "She has a{cps=5}...{/cps} unique way of talking to people.{w=0.3} I doubt she truly meant anything by it but{cps=5}...{/cps} Look I’ll talk to her about it ok?"
    
    show dev sad
    show theo unimpressed
    with eidissolve_nd

    D "It’s not that big a deal, it's fine.{w=0.3} I don’t want you two arguing on my behalf."
    
    show theo angry
    with eidissolve_nd

    T "She shouldn’t be talking to you like that. Trust me, it’s fine.{w=0.3} Let’s just{cps=5}...{/cps} forget about that for now ok?"

    D "Sure."
    
    show dev neutral
    show theo neutral
    with eidissolve_nd

    "He is right, I shouldn’t dwell on it. I mean it was a single argument, and despite it I can’t help but feel happy for how the day went ."
    
    show dev somber
    show theo skeptical
    with eidissolve_nd

    "Emily showing me her drawing.{w=0.1} Rebecca reading to and confiding in me.{w=0.1} Abigail playing a beautiful melody."
    
    show dev happy
    show theo ashamed a_upsetconsidering
    with eidissolve_nd

    "Each of them are great to talk to in different ways. Each of them is so talented in their respective craft: art, writing, and music.{w=0.3} It makes me think of how they could come all together in a{cps=5}...{/cps}"
    
    show dev shocked
    show theo sad
    with eidissolve_nd
    
    T "Dude."

    "I jump at his words."
    
    show dev surprised
    show theo neutral
    with eidissolve_nd
    
    D "Yeah?"
    
    show dev neutral
    show theo neutral
    with eidissolve_nd

    T "We haven’t known each other for long, but if you ever need to vent, I’m here, okay?"
    
    show dev skeptical
    show theo smugconsidering
    with eidissolve_nd

    T "Well,{w=0.2} maybe not {i}here{/i} here, because this is a library and if things get loud, we’ll be kicked out."
    
    show dev happy
    show theo happy
    with eidissolve_nd

    "I smile."

    D "We’re totally gonna do it."
    
    show dev surprised
    show theo grin
    with eidissolve_nd

    "Theo blanches."
    
    show dev annoyed
    show theo crossed c_smug
    with eidissolve_nd

    T "Again, Dev. I don’t like you in that way.{w=0.3} Sorry."
    
    show dev mad
    show theo c_smugconsidering
    with eidissolve_nd

    D "Not that, Theo! The video game!"
    
    show dev surprised left:
        hop(y=0.1)
    show theo surprised right:
        hop(0.1)
    with eidissolve_nd

    "Now I’m the one who's being sent some venomous shushes."
    
    show dev annoyed right
    show theo grin left
    with eidissolve_nd

    T "Dude, I know!{w=0.3} Just messing with you."
    
    show dev neutral
    show theo skeptical
    with eidissolve_nd

    T "Got to ask though, what made you so certain?{w=0.3} You didn’t seem that into the idea yesterday."
    
    show dev skeptical
    show theo neutral
    with eidissolve_nd

    D "I guess you could say I had some{cps=5}...{/cps} revelations."
    
    show dev sad
    show theo unimpressed
    with eidissolve_nd

    D "I don’t exactly have much going on, no hobbies,{w=0.3} not really sure what I want to do next."
    
    show dev annoyed
    with eidissolve_nd

    D "But what I {i}do{/i} know is that I like games and I can’t just pass up on opportunities, so{cps=5}...{/cps} I guess that’s why I want to give game design a try."
    
    show dev skeptical
    with eidissolve_nd
    
    "Theo blinks twice. An ear to ear grin appears on his face in an instant upon hearing that."
    
    show dev somber
    show theo joy j_cheerful
    with eidissolve_nd
    
    T "Hell yes, dude! This is gonna be sweet!"
    
    show dev surprised left:
        hop(y=0.1)
    show theo surprised right:
        hop(0.1)
    with eidissolve_nd

    "Cue another volley of violent shushes sent our way."
    
    show dev somber:
        chuckle(y=0.1)
    show theo ashamed a_embarrassed:
        chuckle(0.1)
    with eidissolve_nd

    "Both of us just laugh them off before returning to our silent studying for the time being. Game creation can always come later."

    window hide
    window auto

    scene black with Dissolve(1.0)
    
    pause 2.0
    
    show joke_end behind black
    hide black with Dissolve(1)
    
    pause 5
    
    scene black with Dissolve(1.0)
    
    pause 3
    
    return