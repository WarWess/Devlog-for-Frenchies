label chapter_1:

####PART 1####
    stop music fadeout 3.0
    
    pause 2.0

    play music moonlit_groove fadein 3.0
    pause 2.5
    
    scene black
    
    ##There is going to be a few more of these cgs, so its not just one static image the whole time, they are just not done yet.

    "Vous savez,{w=0.3} I never was too keen on the idea of going to college.{w=0.5} Sure,{w=0.3} it might be nice to go, but what for?"
    
    show devbusintro_1 with eDissolve(1)
    
    "I had no idea what I wanted to do with my life.{w=0.3} I still don't,{w=0.3} not really,{w=0.3} and practically speaking my grades limited me to only certain professions."
    
    "I wasn't going to be a surgeon or some nuclear scientist, that's for sure,{w=0.3} but I knew I still needed to do something with myself.{w=0.5} Else,{w=0.3} my parents would drag me to the nearest army recruitment office."
    
    show devbusintro_2 with eDissolve(1)
    
    "So, I applied everywhere I could."
    
    "The place I REALLY hoped I would get into was{cps=5}...{/cps}"
    
    menu:
        "Caveway Institute for Digital Arts":
            $ CIDA = True
            "I'm certainly no great artist,{w=0.3} but my high school art teacher said I had potential.{w=0.3} Plus learning is the point of college, right?"
            
        "Arthur University":
            $ AU = True
            "It has a whole bunch of really cool courses on music and sound. I've always loved music,{w=0.3} and I could play a mean trombone in band,{w=0.3} so it seemed like a good pick."
            
        "Volcano Tech School of Design":
            $ VTSD = True
            "Someone online told me to \"learn to code\" and{cps=5}...{/cps} it seemed like good advice!{w=0.3} I've even made some rough mods for Future Scrolls 4."
            
        "StegoTech University of Innovation":
            $ SUI = True
            "Paradise Extinction always really spoke to me,{w=0.3} like,{w=0.3} on an emotional level. Trying my hand at literature seemed perfect."
            
        "Lauren Institute of Culinary Arts":
            $ LICA = True
            "It's not the best cooking college a person could hope to go to, but not the worst.{w=0.3} So long as Gordon Raptsey stops making fun of my quiche online, then I feel like that is a success."
    
    show anim_devcg with eDissolve(1)
    
    "I even sent a few applications to some of the fancier colleges,{w=0.3} even if it was more as a joke."
    
    
    
    "One of those joke applications was to CCC,{w=0.5} Cretaceous College of Computing."
    
    pause 0.5
    
    show devbusintro_5 with eDissolve(1)
    
    "The punchline is that CCC accepted my application."
    
    "I'm not sure who was more surprised;{w=0.3} me,{w=0.6} or my parents."
    
    "After looking into it,{w=0.3} it turned out that apparently a bunch of humans won some big court case about unfair enrollment practices in the higher end colleges,{w=0.3} or something like that.{w=0.3} So now they are all scrambling to get as many humans in their school as possible."
    
    "Well,{w=0.3} I sure wasn't going to look a gift horse in the mouth.{w=0.3} Especially not a \'full scholarship with boarding and a monthly commissary allowance for any store on the campus\' shaped horse."
    
    "So, here I am,{w=0.3} on a bus,{w=0.3} heading straight to the CCC campus,{w=0.3} with only a duffle bag's worth of things to my name."
    
    "The driver interrupts my thoughts."
    
    show devbusintro_6 with eDissolve(1)
    
    unknown "We are now arriving at the Cretaceous College of Computing campus.{w=0.3} If you are getting off, please remember to take any personal possessions you may have brought, as well as any trash."
    
    unknown "From all of us at BlueAlbertosaur Busing,{w=0.3} we thank you for choosing us."
    
    window auto hide
    stop music fadeout 10
    pause .5

    scene black with dissolve
    pause .5
    
    ##Chefe is doing a animation of Dev getting off the bus, a dramatic pan up to his face, and a title drop.
    ##After the animation I would like to have a bunch of crowd characters plow into him, nearly knocking him down and trampling him.
    ##Can't seem to get this to work.
    show screen cutscene("devintro_skip")
    window auto hide
    pause .5
    
    play sound devintro_audio
    show anim_devintro behind black
    # Loading a video takes a second, so this is here so the fadein isn't choppyRR
    pause 0.2
    hide black with Dissolve(1) 
    pause 12
    play music fleeting_echoes fadein 2
    pause 6.4
    label devintro_skip hide:
    hide screen cutscene
    scene college_entrance_day_summer with dissolve
    pause .5
    show dev at moveinright(0.5) with eidissolve_nd
    
    #        #Under Construction: TODO add sounds
    
    stop sound
    play music fleeting_echoes fadein 2 if_changed
    play ambience crowd_talking volume 10 fadein 3 loop
    
    pause 3.0
    
    
    
    show c_chilling1:
        matrixcolor ColorizeMatrix("#7e3e9b", "#ffffff")
        xpos -0.2
    show c_selfie1:
        matrixcolor ColorizeMatrix("#9b3e4c", "#ffffff")
        xpos -0.2        
    show c_selfie2:
        matrixcolor ColorizeMatrix("#989b3e", "#ffffff")
        xpos -0.2
    show c_standing1:
        matrixcolor ColorizeMatrix("#559b3e", "#ffffff")
        xpos -0.2
    show c_standing2:
        matrixcolor ColorizeMatrix("#9b5c3e", "#ffffff")
        xpos -0.2
        
    show c_standing3:
        matrixcolor ColorizeMatrix("#4d892c", "#ffffff")
        xpos -0.2
    show c_chilling2:
        matrixcolor ColorizeMatrix("#19b7b5", "#ffffff")
        xpos -0.2
    show c_walking1:
        matrixcolor ColorizeMatrix("#d563a9", "#ffffff")
        xpos -0.2        
    show c_walking2:
        matrixcolor ColorizeMatrix("#26327f", "#ffffff")
        xpos -0.2
    show c_walking3:
        matrixcolor ColorizeMatrix("#7f7e36", "#ffffff")
        xpos -0.2  


    show c_chilling1 at quadmovex(1.7, 3.5)
    show c_selfie1 at movex(1.5, 4.7), walkerloop(0, 0.5, 0.0)
    show c_selfie2 at movex(1.5, 3.7), walkerloop(0, 0.5, 0.0)
    show c_standing1 at easemovex(1.8, 4.5)
    show c_standing2 at movex(1.8, 2.5)
    show c_standing3 at quadmovex(1.8, 3.5)
    show c_chilling2 at backmovex(1.4, 3.5)
    show c_walking1 at movex(1.3, 3.9)
    show c_walking2 at easemovex(1.3, 3.5)
    show c_walking3 at movex(2.0, 3.5)   
    
    pause 0.1
    
    play sound person_knocked_down volume 6
    show dev shocked left at rotate_bullet(t=0.7) with hpunch                                    
    
    stop ambience fadeout 8
    
    pause 4.5
    
    show dev annoyed left at moveinup(0.5, 0.0, 0.2, 0.75) with eidissolve_nd:
        resetrotate
        xoffset 0.0    
    
    
    
    "{cps=5}...{/cps}"    
        
    pause 1.0

    hide c_chilling1
    hide c_selfie1
    hide c_selfie2
    hide c_standing1
    hide c_standing2
    hide c_standing3
    hide c_chilling2
    hide c_walking1
    hide c_walking2
    hide c_walking3

    # Construction "finished" boss.
    
    "Rude."
    
    show dev left with eidissolve_nd
    pause 1
    show dev right with eidissolve_nd
    pause 1
    
    "Hmmm{cps=5}...{/cps}"
    
    "No other humans."
    
    show dev thinking with eidissolve_nd

    "Figured there would be more that got the same scholarship."
    
    "Oh well,{w=0.3} maybe they took some other bus,{w=0.3} or got here early?"
    
    #Make it so Dev is hidden, then this is semi zoomed in then pans up before zooming out back to Dev.
    #BG are default 1920x1080 so this might not look good, if not just ignore all this, maybe have Dev fade out here to show the BG?
    #scene college_entrance_day_summer
    
    show dev:
        ease_quad 1 xpos 0.2
    
    "Cretaceous College of Computing loomed before me."
    
    
    
    "It was{cps=5}...{/cps} "
    
    if CIDA:
        show dev thinking t_considering with eidissolve_nd
        "Imposing and brutalistic.{w=0.3} Concrete cubes among concrete cubes with rectangular glass windows."
        show dev thinking t_surprised with eidissolve_nd
        extend "The bleary color palette was completed by the greenery of the quasi megafauna that grew alongside the walkways and roads."
        show dev neutral with eidissolve_nd
        
    else:
        show dev neutral with eidissolve_nd
        "Wide,{w=0.1} big,{w=0.1} mostly square-ish.{w=0.3} Boring to look at except for the many palm trees and other plants all over the place."
    
    "The starting place for countless success stories.{w=0.3} If you can do well here,{w=0.3} then you are basically guaranteed success in life."
    
    "At least{w=0.3}, that is what their brochure said."
    
    "I squint against the sun,{w=0.3} taking in the sight of students milling about."
    
    show dev:
        ease_quad 1 xpos 0.5
    
    #Should probably have a CG or something for this, maybe a wider close-up version of the college entrance but with people
    
    "My hometown was populated by mostly humans.{w=0.3} I've seen other dinos before,{w=0.3} but not this many at the same time, same place.{w=0.3} Their scales shimmer in hues that my hometown's limited palette could never have imagined."
    
    show c_chilling1 behind dev:
        matrixcolor ColorizeMatrix("#7f7e36", "#ffffff")
        xpos -0.27
    show c_walking2 behind dev:
        matrixcolor ColorizeMatrix("#4d892c", "#ffffff")
        xpos -1.2
        
    show c_chilling1 at quadmovex(1.5, 5)
    show c_walking2 at quadmovex(1.5, 5)
    
    "I wonder if they think I'm an oddity.{w=0.3} The lawsuit thing was about no humans going here, maybe this is the first time they have seen a human before?{w=0.3} There are dino only towns as far as I know."
    
    #have a few people walk across the screen behind Dev
    #have Dev's vision follow them?
    
    show c_standing1 left behind dev:
        matrixcolor ColorizeMatrix("#d563a9", "#ffffff")
        xpos 1.35
    show c_standing2 left behind dev:
        matrixcolor ColorizeMatrix("#989b3e", "#ffffff")
        xpos 1.2
        
    show c_standing1 at quadmovex(-0.5, 5)
    show c_standing2 at quadmovex(-0.5, 5)
    
    pause 2.5
    
    show dev left
    with eidissolve_nd
    
    "Some raptors in letterman jackets snicker as they pass by."
    
    show dev ashamed with eidissolve_nd
    
    "The excitement that had bubbled within me during the bus ride now gives way to an unsettling apprehension."
    
    show dev neutral right with eidissolve_nd
    
    "I try to shrug it off."
    
    "I was told someone would be here to greet me,{w=0.3} but as minutes ticked by,{w=0.3} nobody came."
    
    "I scan the crowd again, looking for any sign of a welcome committee,{w=0.3} but I'm only met by the indifferent gazes of pterodactyls chilling on some benches and spinosaurus chatting animatedly in groups."
    
    show elliot angry left at moveinleft(0.7) with eidissolve_nd
    pause 0.2
    show dev concerned:
        ease_quad 0.5 xpos 0.3
    
    "Then, a green parasaur cuts through the throng with a purposeful stride.{w=0.3} His eyes are creased with annoyance.{w=0.3} I don't know who's reflecting the Sun more,{w=0.3} his gelled golden hair or my bald head."
    
    "His expression is sour enough to curdle milk,{w=0.3} and approaches with an air of someone who has far better things to do."
    
    show elliot skeptical with eidissolve_nd
    show dev surprised with eidissolve_nd
    
    Eu "Dev A. Loper?"
    
    "His voice has an authoritative ring to it that makes me stand up straighter."
    
    show dev happy with eidissolve_nd
    
    D "That's me."

    "I try for a smile."
    
    show elliot unimpressed with eidissolve_nd
    
    Eu "I'm the student union president,{w=0.3} Elliot."

    #Have an animation here where he moves close to Dev and both do a little bob to show him handing something to Dev
    show elliot skeptical left:
        ease_quad 0.5 xpos 0.4
        pause 0.2
        ###nudgeup(1.0, 1.0, 1.0)
        nudgeup()
        ease_quad 0.5 xpos 0.55
    show dev shocked with eidissolve_nd:
        pause 0.7
        nudgeup()

    "He thrusts a stack of papers into my hands—schedules,{w=0.3} maps,{w=0.3} pamphlets."
    
    E "The dean made me your welcome committee,{w=0.3} but I have a million other things I need to do, so let's get this over quick."

    show dev neutral with eidissolve_nd

    "He pulls out a paper from his pocket and begins reading it."
    
    #Have elliot pace back and forth to show he is being impatient
    show elliot annoyeddown right:
        ease_quad 1 xpos 0.8
    
    E "Hello and Welcome to Cretaceous College of Computing, and{cps=5}...{/cps}{nw=1}{nw} Bla{nw=0.5}{nw} bla{nw=0.5}{nw} bla{nw=0.5}{cps=5}...{/cps}{w}"
    
    show dev considering with eidissolve_nd
    
    "He actually says 'bla bla bla'."
    show dev surprised with eidissolve_nd
    extend " I feel my eyes getting bigger as he keeps talking,{w=0.3} trying to soak in all the info he's giving me."
    
    show elliot annoyeddown left:
        ease_quad 1 xpos 0.55
    
    E "We are happy to provide young and underprivileged humans such as yourselves a chance at becoming your best selves.{nw=2} {nw}Bla{nw=0.5} {nw}bla{nw=0.5} {nw}bla{nw=0.5}{cps=5}...{/cps}{p}"

    "It's not of much value, sadly."
    
    show elliot annoyeddown right:
        ease_quad 1 xpos 0.8
    
    E "The papers you have been given include detailed descriptions of all our facilities,{w=0.3} a map of the campus,{w=0.3} your schedule,{nw=1} {nw}bla{nw=0.5}{nw} bla{nw=0.5}{nw} bla{nw=0.5}{cps=5}...{/cps}{p}"

    E "{cps=5}...{/cps}"
    
    "He seems to be scanning the paper,{w=0.3} only to put it aside."
    
    show elliot unimpressed left:
        ease_quad 0.3 xpos 0.7

    E "Look, I'm sure you can figure out all of this stuff on your own."
    extend " I sure hope you can if you are planning on making it here."

    E "Do you have any questions?{w=0.25} Like I said, I need to get going."
    
    show dev shocked with eidissolve_nd
    
    D "Wha--?"
    
    show elliot annoyed with eidissolve_nd
    show dev sad with eidissolve_nd
    
    "I realize a moment too late that I'd blurted that out.{w=0.25} His claw taps impatiently on the top sheet, pointedly not remarking to my very insightful response."
    
    show dev skeptical with eidissolve_nd
    
    "My eyes dart across what turns out to be my schedule.{w=0.25} Most of it seems normal but{cps=5}...{/cps}Musical Theory? Advanced World History?"
    
    D "This is{cps=5}...{/cps}{w=0.25} I don't remember picking these{cps=5}...{/cps}"
    
    show elliot skeptical with eidissolve_nd
    
    "He gives a confused expression as he grabs my schedule and looks over the page before going through several other papers he is carrying."
    
    show elliot neutral with eidissolve_nd
    
    E "Hmmm, there may have been a mix up,{w=0.3} what major did you pick?"
    
    show dev neutral
    with eidissolve_nd
    
    D "\"General studies\"."
    
    show elliot surprised
    with eidissolve_nd

    E "{cps=5}...{/cps}"    
    
    D "{cps=5}...{/cps}"
    
    show dev surprised
    show elliot angry
    with eidissolve_nd
    
    "With a roll of his eyes, he tosses my schedule back."
    
    show dev skeptical
    show elliot annoyedconsidering
    with eidissolve_nd
    
    E "So you're the one that{cps=5}...{/cps}"
    
    "Elliot shakes his head."
    
    show dev neutral
    show elliot annoyed
    with eidissolve_nd
    
    E "This isn't a community college,{w=0.25} you were supposed to have a major.{w=0.25} We don't even {b}have{/b} a 'general studies' course."

    E "Well... we {i}didn't{/i}.{w=0.25} Somehow no one noticed the issue until two weeks ago or something, so they had to scramble to throw one together before the semester started."
    
    show dev sad
    show elliot angry
    with eidissolve_nd
    
    E "All{w=0.25} for{w=0.25} you{w=0.25}{cps=5}...{/cps}"
    
    show dev ashamed
    with eidissolve_nd

    D "{cps=5}...{/cps}"

    "Well{cps=5}...{/cps} That's a promising start."
    
    show elliot unimpressed
    with eidissolve_nd
    
    show dev sad
    with eidissolve_nd
    
    E "Well, if that's all,{w=0.3} I'm going to get going."
    
    show elliot annoyed right:
        ease_quad 1 xpos 0.8
    with eidissolve_nd
    
    "He gives what could best be described as a sarcastic wave before he starts walking off."
    
    show dev surprised
    with eidissolve_nd
    
    "Wait, he barely gave me any information at all, how was that an orientation?!" 
    
    menu:
        "H-hey! Where are the dorms?":
        
            show dev shocked with eidissolve_nd
            show elliot annoyed with eidissolve_nd
        
            "He turns towards me but continues walking away backwards."
            
            show dev shocked:
                ease_quad 0.5 xpos 0.5
            show elliot annoyed left:
                ease_quad 1 xpos 1.2
            
            E "I gave you a map, genius.{w=0.25} You can figure it out on your own."
            
            hide elliot
            
        "Who do I talk to about changing my classes?":
        
            show dev shocked with eidissolve_nd
            show elliot annoyed with eidissolve_nd
        
            "He turns towards me but continues walking away backwards."
            
            show dev shocked:
                ease_quad 0.5 xpos 0.5
            show elliot annoyed left:
                ease_quad 1 xpos 1.2
            
            E "Talk to the Dean,{w=0.3} but unless you have a good reason, you're stuck with them."
            
            hide elliot
            
        "Are there any human-specific resources I should know about?":
        
            show dev shocked with eidissolve_nd
            show elliot annoyed with eidissolve_nd
        
            "He shrugs and continues walking away without turning to look back."
            
            show dev shocked:
                ease_quad 0.5 xpos 0.5
            show elliot annoyed right:
                ease_quad 1 xpos 1.2
            
            E "You're the only human here,{w=0.3} you figure it out."
            
            hide elliot
            
        "Thanks!{w=0.5} You were a lot of help!":
            
            show dev annoyed with eidissolve_nd
            show elliot annoyed right:
                ease_quad 1 xpos 1.2
            
            "He completely ignores me.{w=0.25} I'm not sure he realized I was being sarcastic.{w=0.25} Or maybe he doesn't care."
            
            show dev annoyed:
                ease_quad 0.5 xpos 0.5
            
            hide elliot
    
    "And with that he is gone."
    
    show dev annoyed with eidissolve_nd
    
    "Great."
    
    show dev sad with eidissolve_nd
    
    "I am left amidst a sea of strangers."
    
    show dev neutral left with eidissolve_nd
    pause 1
    show dev neutral right with eidissolve_nd
    pause 1

    "I should probably start by finding my dorm, but{cps=5}...{/cps}"

    show dev unimpressed with eidissolve_nd

    "The map looks to be useless."
    
    "It is made up of nondescript boxes with little dark lines indicating roads or paths,{w=0.3} without any details or landmarks."
    
    "How is anyone supposed to find {i}anything{/i} with this thing?!"
    
    show dev annoyed with eidissolve_nd
    
    "Whatever."
    
    show dev somber at moveoutright_cs(1.85, m=0.15, t=1.5)
    #pause
    hide dev
    
    "How hard can it be to find one building?"
    
    #fade out background
    
    scene quad_1 with dissolve
    
    show dev left at moveinleft(0.5) with eidissolve_nd
    
    "..."
    
    show dev left at moveoutright(x=0.5, m=0.7, t=1)
    with eidissolve_nd
    hide dev
    
    scene quad_2 with dissolve
    
    show dev at moveinright(0.5)
    "..."
    show dev at moveoutright_cs(1.85, m=0.15, t=1.5)
    
    hide dev
    
    #Small cutscene of Dev looking around random points at the college.
    
    
####PART 2####

    ##Maybe have some visual gags in the bg?

    scene college_entrance_day_summer with dissolve
    
    show dev left at moveinleft(0.5) with eidissolve_nd
    
    "{cps=5}...{/cps}"

    show dev sad at rotate_funny(0.05, inv=1)
    
    "With the sun falling towards the horizon, my spirits fall with it."
    
    show dev sad at standup(0.0, 1.0, 0.5)

    "Years of gaming and surfing obscure websites have given me absolutely no useful abilities at deciphering these symbols on this so-called map."
    
    show dev left with eidissolve_nd

    "I check it again,{w=0.3} trying to convince myself that I was going the right way."

    pause 1
    show dev right with eidissolve_nd
    pause 1

    "Yet,{w=0.3} looking around,{w=0.3} I find myself right back where I had started."
    
    play ambience plane_flying fadein 3 volume 1 loop
    
    "{cps=5}...{/cps}"
    
    "I'm not even sure how I managed that."
    
    #A shadow overcoming Dev? Should have the sound of a Zero play in the background on loop.
    show dev skeptical with eidissolve_nd
    
    $renpy.music.set_volume(0.5, channel='music', delay=2)
    
    pause 0.5
    
    $renpy.music.set_volume(3, channel='ambience', delay=1)
    
    D "Huh?"
    
    $renpy.music.set_volume(6, channel='ambience', delay=1)
    
    "A loud whooshing noise makes me look up just in time to see a blur of red and blue heading straight for me."
    
    Tu "{b}Watch out!{fast}{/b}"
    
    stop ambience fadeout 1.5
    play sound stuka_siren_boom volume 0.3 fadein 0.5

    pause 1.5

    show dev shocked left:
        easein 0.3 xoffset 50

    pause 0.25
    
    #Cutscene of Theo crashing into Dev.
    show theo bullet:
        subpixel True
        rotate 40
        ypos -0.3
        xpos -0.3
        linear 0.3 ypos 1.2 xpos 1.2
    pause 0.1    

    show dev at rotate_bullet() with hpunch
    
    hide theo bullet
    hide dev
    show black
    pause 5
    
    stop ambience fadeout 2
    stop sound fadeout 2
    
    "Ow..."
    
    $renpy.music.set_volume(1, channel='music', delay=2)

    D "What the—"

    Tu "Sorry! Sorry!"
    
    hide black
    
    show theo shocked at moveinup(0.5, 0.0, 0.2, 0.75) with eidissolve_nd:
        pause 0.1
        resetrotate
        
    pause 0.3
    show theo shocked:
        ease_quad 0.75 xpos 0.4 ypos 0.0

    "The dinosaur untangles himself from me and stands up,{w=0.3} extending a clawed hand to help me up."

    Tu "Didn't see you there!"
    
    show theo shocked with eidissolve_nd:
        ypos 0.0
    
    show dev annoyed left at moveinup(0.5, 0.0, 0.2, 0.75) with eidissolve_nd:
        resetrotate
        xoffset 0.0
       
        
    pause 0.5
    show dev annoyed left:
        ease_quad 0.5 xpos 0.7 ypos 0.0
        
    show theo sad:
        ease_quad 0.5 xpos 0.3 ypos 0.0
        

    "I took his hand,{w=0.3} wincing as I got back on my feet."
    
    show theo ashamed a_upset with eidissolve_nd
    
    D "Yeah,{w=0.2} clearly."
    
    "The dinosaur in front of me was a pterodactyl with red feathers and a sheepish grin.{w=0.3} He rubbed the back of his neck, looking genuinely embarrassed."
    
    show theo ashamed a_upsetconsidering with eidissolve_nd
    show dev neutral with eidissolve_nd

    Tu "Super sorry about that, was practicing gliding and totally didn't see you walk into my path."
    
    show theo ashamed a_surprised with eidissolve_nd
    show dev furious f_annoyed with eidissolve_nd

    D "You think you could maybe practice somewhere that's {b}not{/b} right in the middle of campus?"

    "His wings drooped a bit,{w=0.3} his grin faltering."
    
    show theo sad with eidissolve_nd
    show dev annoyed with eidissolve_nd

    Tu "Yeah, you're right.{w=0.2} My bad.{w=0.3} Are you okay? Did I hurt you?"

    D "My shoulder hurts a bit,{w=0.3} but{w=0.2} I'll live."

    "He looked relieved but still concerned."
    
    show theo happy with eidissolve_nd

    T "Let me make it up to you. Need help finding something? You look kinda lost. I'm Theo by the way."
    
    show dev neutral with eidissolve_nd

    D "Dev,{w=0.2} and you could say that.{w=0.3} I'm looking for the dorms."
    
    show theo considering with eidissolve_nd

    T "The dorms?{w=0.3} Didn't orientation show you all that?"
    
    show dev unimpressed with eidissolve_nd

    D "If by \"orientation\" you mean \"dumped a bunch of papers on me then bailed\",{w=0.3} then no."
    
    show dev with eidissolve_nd
    show theo grin open with eidissolve_nd

    T "Heh,{w=0.3} well then, lucky for you I'm an expert navigator,{w=0.2} so consider me your personal tour guide."

    show theo:
        ease_quad 0.15 xpos 0.65 
        ease_quad 0.15 xpos 0.40
    pause 0.15
    show dev shocked at hitx(0.75)

    #have dev bounce a bit here

    "Theo clapped a wing on my back,{w=0.3} almost knocking me off balance."

    show theo grin closed with eidissolve_nd

    T "C'mon then, let's find your place!"
    
    scene quad_1 with dissolve
    
    show dev at moveinright(x=1.5, m=1.6, t=25) with eidissolve_nd:
        pause 2
        walkerloop
    
    show theo happy closed at moveinright(x=0.7, m=0.8, t=1) with eidissolve:
        block:
            pause 1
            jumping
            pause 2
        block:
            xzoom -1
            quadmovex(0.2)
            jumping
            pause 2
        block:
            xzoom 1
            quadmovex(1.5)
    
    "With Theo's guidance, the cryptic map started to make sense."
    
    "He pointed out various landmarks that could be found on it{w=0.3}—a statue here,{w=0.3} a particularly gnarled tree there{w=0.2}—and eventually we found our way to the dormitories."
    
    scene quad_2 with dissolve
    
    show theo grin open at moveinright(x=0.7, m=0.8, t=1) with eidissolve

    T "That's the common room—great for all-nighters.{nw=1.5}"
    
    show dev at moveinright(x=0.4, m=0.6, t=10) with eidissolve_nd:
        pause 2
        walker(r=8)
    show theo grin closed left with eidissolve:
        quadmovex(0.2)
        jumping(r=3)
        pause 2
        xzoom -1
        quadmovex(0.6)
    
    extend " Over there's the laundry—would recommend going early if you don't want to battle for a washer."
        
    show theo happy right with eidissolve
        
    T "And here we are!"

    "We reached what looked like the right building{w=0.3}—two stories of brick and stone standing sentinel at the edge of campus."

    "Theo pushed open the heavy door with a flourish."
    
    scene dorm_hallway with dissolve
    show dev at moveinright(0.4, m=0.5) with eidissolve_nd
    show theo happy at moveinright(0.6, m=0.7) with eidissolve_nd:
        pause 1
        xzoom -1

    T "This is it, what's your dorm number?"

    "I double check the paper."

    D "{w=0.3}482."

    "We navigate through a massive collection of dinosaurs,{w=0.3} milling about or talking with friends."

    T "478{cps=5}...{/cps} 480{cps=5}...{/cps} There,{w=0.2} 482! Your home away from home."
    
    scene dormroom_dev_empty_day with dissolve
    show dev at moveinright(0.3) with eidissolve_nd
    show theo happy at moveinright(0.7) with eidissolve_nd

    "The room was larger than I expected;{w=0.3} two beds on opposite walls with desks beneath lofted bunks."
    
    show theo neutral left with eidissolve_nd

    T "Guess this palace is all yours."

    D "Seems so."
    
    show theo happy left with eidissolve_nd

    T "Lucky!"

    show dev somber with eidissolve_nd
    show theo skeptical left with eidissolve_nd

    D "Maybe they saw who they were rooming with and bailed."

    show theo happy left with eidissolve_nd

    "Theo shrugged off my self-deprecation joke with another easy smile."

    T "Their loss!{w=0.3} More space for you. Besides,{w=0.2} who needs roommates when you've got neighbors like me?"
    
    show dev shocked with eidissolve_nd
    
    D "We're neighbors?"

    T "Well{cps=5}...{/cps} no,{w=0.2} but I'm only one floor down."
    show theo grin left with eidissolve_nd
    extend " That's practically neighbors, right?"
    
    show dev neutral with eidissolve_nd
    
    "Well,{w=0.3} can't argue with that."

    D "Do you have a roommate?"

    T "Duh. Everyone does."
    
    show theo considering left with eidissolve_nd

    "I gesture to the other half of my new room."

    show theo ashamed a_embarrassed left with eidissolve_nd

    T "Almost everyone."
    
    show theo neutral left with eidissolve_nd

    D "What are they like?"
    
    show theo neutralconsidering left with eidissolve_nd

    T "He's an{w=0.5} acquired taste kind of guy,{w=0.3} but grows on you eventually."
    
    show theo neutral left with eidissolve_nd

    "I toss my bag onto the nearest bed and glance around at the empty space."

    "Place is kind of depressing as it is."
    
    menu:
        "A roommate sounds neat. Bummer.":
            "It would certainly liven the place up a bit{w=0.3}, plus I would only have to worry about decorating my side.{w=0.3} In any case, I should get some posters or something."
        "But at least I have the entire place to myself.":
            "In any case,{w=0.3} I should get some posters or something.{w=0.3} Guess I won't be having any arguments about decor,{w=0.3} considering the lack of another being capable of voicing their opinion on what my room should look like."

    show theo happy left with eidissolve_nd

    T "Hey, you hungry?{w=0.3} Cafeteria food isn't half bad if you know what to avoid."

    show dev neutral with eidissolve_nd:
        hitx(0.3, i=1.2, s=1.5)
    show theo surprised left with eidissolve_nd

    "As if on cue,{w=0.3} my stomach roars."
    
    show dev somber with eidissolve_nd
    show theo grin left with eidissolve_nd

    D "Starving."
    
    window auto hide
    stop music fadeout 10
    pause .5

    scene black with dissolve
    pause .5
    
####PART 3####
    
    play music moonlit_reverie fadein 3.0
    play ambience school_cafeteria_ambience volume 2 fadein 3.0 loop
    
    show cafeteria_summer behind black
    hide black with Dissolve(1)
    window auto show

    pause .5
    
    show dev at moveinright(0.3, m=0.5) with eidissolve_nd
    show theo neutral at moveinright(0.7, m=0.7) with eidissolve_nd:
        pause 1
        xzoom -1
    
    "We walk side by side,{w=0.3} my stomach growling louder with each step toward the cafeteria."

    "Inside, the hall buzzes with a hundred conversations,{w=0.3} the scent of sizzling meat and overcooked vegetables heavy in the air."
    
    show dev sad with eidissolve_nd

    D "I didn't expect it to be this{cps=5}...{/cps} lively."
    
    show theo grin left with eidissolve_nd:
        xzoom 1

    T "Pffft"
    
    show theo happy left with eidissolve_nd

    T "Wait until you see the feeding frenzy during finals."
    
    show dev skeptical
    with eidissolve_nd

    D "So{w=0.3} you've been here before?"

    T "Yep,{w=0.1} second year."
    
    show dev surprised
    with eidissolve_nd

    D "Oh.{w=0.3} Neat!"

    "I take a look at the prices next to the stuff on the menu."
    
    show dev yiik
    with eidissolve_nd

    "Sweet Raptor Jesus{cps=5}...{/cps}"

    "$5 for a single bottle of water? {b}$7{/b} for small fries?"
    
    show dev ashamed
    with eidissolve_nd

    D "Well, crap{cps=5}...{/cps}"
    
    show theo skeptical left
    with eidissolve_nd

    T "What's up?"
    
    show dev sad with eidissolve_nd

    D "I knew the prices here would be bad, not this bad!"

    D "I'm running on fumes here,{w=0.1} financially speaking.{w=0.3} One meal is gonna wipe out the cash I have on me."

    D "I think I might just hit up the vending machines, gotta wait for the allowance to kick in."

    show theo grin open left with eidissolve_nd
    
    "Theo claps me on the back."

    T "Don't sweat it. My treat."
    
    show theo grin closed left with eidissolve_nd

    D "I can't let you do that, we only just met."

    D "I don't like the idea of owing a stranger."
    
    show theo surprised left with eidissolve_nd

    "Theo gasps dramatically."
    
    show theo sad left with eidissolve_nd

    T "A stranger?{w=0.3} After all that bonding together we did,"
    
    show theo considering left with eidissolve_nd
    
    extend " finding your room, entering your room{w=0.3}, exiting your room{cps=5}...{/cps}"
    
    show dev happy with eidissolve_nd:
        chuckle
    
    D "Heh."
    
    show dev thinking t_happy with eidissolve_nd

    D "Finding the cafeteria, entering the cafeteria{cps=5}...{/cps}"
    
    show theo grin left with eidissolve_nd:
        chuckle

    "He laughs too. I feel a knot undo itself inside my chest.{w=0.3} Socializing.{w=0.1} Not that hard, right?"
    
    show theo neutral left with eidissolve_nd
    show dev neutral with eidissolve_nd
    
    T "But no, I get you{cps=5}...{/cps}"
    
    show theo considering left with eidissolve_nd

    T "Hmm,{w=0.3} you know how to read?"
    
    show theo neutral left with eidissolve_nd
    show dev annoyed with eidissolve_nd

    "What kind of question is that?"
    
    show dev skeptical with eidissolve_nd

    D "Yes{cps=5}...{/cps}?"
    
    show theo happy left with eidissolve_nd
    show dev neutral with eidissolve_nd

    T "You can pay me back by helping me out on my next History assignment. Can barely pay attention during class."
    
    show dev sad with eidissolve_nd

    "I guess it's a fair deal{cps=5}...{/cps}{w=0.3} but I don't know{cps=5}...{/cps}"
    
    menu:
        "Take the deal, my stomach guides me more than my pride!":
            $ LUNCH = True
            pause 0.5
            jump eager_deal
            
        "Not like I have a better option{cps=5}...{/cps} Take the deal.":
            $ LUNCH = True
            pause 0.5
            jump reluctant_deal
            
        "I need to be able to take care of myself, reject the offer.":
            $ LUNCH = False
            pause 0.5
            jump firm_deal
            
        "He seems so genuine but{cps=5}...{/cps} I can't, reject the offer.":
            $ LUNCH = False
            pause 0.5
            jump kind_deal

label eager_deal:

    show dev shocked with eidissolve_nd:
        nudgeright(0.4)
    show theo shocked with eidissolve_nd:
        pause 0.2
        nudgeright(0.8)

    D "YES, PLEASE."

    "Theo is visibly taken aback by my outburst. My ears start to burn."
    
    show dev shocked at quadmovex(0.3, t=1)
        
    show theo shocked with eidissolve_nd:
        pause 0.3
        quadmovex(0.7, t=1)
        
    show dev sad with eidissolve_nd

    "Oh, no. {w=2} Now he's going to think I'm some kind of deadbeat or freeloader or{cps=5}...{/cps} I'm already a full scholarship student{cps=5}...{/cps}"

    "Does Theo know that already? Is this affecting his image of me?"
    
    show theo surprised with eidissolve_nd

    T "O-okay, dude."
    
    show dev sad with eidissolve_nd:
        hitx(0.3, i=1.2, s=1.5)
        ypos 0.0
    show theo grin left with eidissolve_nd:
        pause 0.5
        chuckle

    "My stomach rumbles, my shame increases. Theo, on the other hand, start laughing so hard he's got to hold his ribs."

    D "Sorry."
    
    show theo happy with eidissolve_nd

    "He's smiling again."

    show dev neutral with eidissolve_nd

    T "No, no, dude, I get it. C'mon, I'm starving too."
    
    show theo neutral right at moveoutright_cs(1.0)
    show theo neutral right with eidissolve_nd
    hide theo
    
    show dev neutral at moveoutright_cs(0.5)
    show dev neutral with eidissolve_nd
    hide dev

    jump accept_deal
    
label reluctant_deal:

    show dev sad with eidissolve_nd

    D "{cps=5}...{/cps}"
    
    show theo happy with eidissolve_nd

    "Theo wiggles his eyebrows."

    T "C'mon~"

    D "Fine. Yes. Thank you.{w=0.3} But I'll pay you back as soon as my allowance comes."

    T "Eh don't be stubborn, Dev. We already have an agreement going on.{w=0.3} Plus you've got no idea, but you'll end up wishing you hadn't sold your soul for a lunch meal."

    show dev shocked with eidissolve_nd

    "That makes me pause.{w=0.3} What kind of history assignments does this guy have?"
    
    show dev sad with eidissolve_nd

    "I was never super great at history so I hope I didn't just enter some sort of Faustian deal for a sandwich?"
    
    show dev neutral with eidissolve_nd

    "Well,{w=0.3} aren't all friendships something like that in the end? I'm not that experienced on the topic, but I relax and follow Theo to the lunch queue."
    
    show theo neutral right at moveoutright_cs(1.0)
    show theo neutral right with eidissolve_nd
    hide theo
    
    show dev neutral at moveoutright_cs(0.5)
    show dev neutral with eidissolve_nd
    hide dev
    
    jump accept_deal

label firm_deal:

    show dev neutral with eidissolve_nd
    show theo surprised with eidissolve_nd
    
    D "No."
    
    "Theo seems taken aback by my direct denial."
    
    show theo sad  with eidissolve_nd
    
    T "Are you sure, dude? I swear it's no problem."
    
    D "No, thank you."
    
    show theo saddown with eidissolve_nd
    
    T "Oh,{w=0.3} okay."
    
    "He deflates at my response."
    
    show dev sad with eidissolve_nd
    
    "Maybe it was pride or maybe just that gnawing gut feeling that I had to fend for myself, but{w=0.3} I couldn't accept this charity. Not now."
    
    "I'm already on a full scholarship, already at the receiving end of too much goodwill I might as well not deserve to already be freeloading from someone I just met."
    
    "I hope he doesn't take this the wrong way and that we can continue to be friends, he's nice."
    
    show theo sad  with eidissolve_nd       
    show dev somber with eidissolve_nd
    
    D "I{cps=5}...{/cps} I appreciate the offer,{w=0.3} I didn't mean to offend or anything."
    
    show theo skeptical with eidissolve_nd
    
    "Theo raises an eyebrow at me."
    
    D "I could still help you with your history assignment though{cps=5}...{/cps}"
    
    show theo surprised with eidissolve_nd
    
    "Theo raises his eyebrow higher before breaking into a chuckle"
    
    show dev surprised with eidissolve_nd
    show theo grin with eidissolve_nd:
        chuckle
    
    T "Dang dude don't sweat it. I'm not {cps=7}'offended'{/cps}{w=0.3}, I get it. "
    
    show dev somber with eidissolve_nd
    
    D "Right{cps=5}...{/cps}"
    
    show theo neutral with eidissolve_nd
    show dev neutral with eidissolve_nd
    
    T "The vending machines are by the east wall, by the way."

    show theo neutral right at moveoutright_cs(1.0)
    show theo neutral right with eidissolve_nd
    hide theo
    
    show dev neutral at moveoutright_cs(0.5)
    show dev neutral with eidissolve_nd
    hide dev

    jump deny_deal
    
label kind_deal:

    show dev sad with eidissolve_nd
    show theo happy with eidissolve_nd

    "I hesitate, the weight of my wallet—or rather, the lack of it—pressing on my mind."
    
    "Theo's offer was generous, but{w=0.3} something about accepting it doesn't sit right with me."
    
    show theo unimpressed with eidissolve_nd
    
    D "Appreciate it, seriously, dude, but I'll manage.{w=0.3} Got to learn to survive on a budget sooner or later, right?"
    
    show theo skeptical with eidissolve_nd
    
    "Theo raises an eyebrow."
    
    T "You sure, man? It's really not that big a deal."
    
    "He doesn't seem accustomed to being denied this way. I feel extra bad for him, and for me, but I can't accept his offering."
    
    "A full ride through college and an allowance are more than enough to ask from the world."
    
    show dev somber with eidissolve_nd
    
    D "Yeah I'm sure,{w=0.3} I can just get some snacks from the vending machines for today."
    
    show theo sad with eidissolve_nd
    
    T "{cps=5}...{/cps}"
    
    show theo neutral with eidissolve_nd
    show dev neutral with eidissolve_nd
    
    T "Suit yourself, man. The vending machines are by the east wall."
    
    show theo neutral right at moveoutright_cs(1.0)
    show theo neutral right with eidissolve_nd
    hide theo
    
    show dev neutral at moveoutright_cs(0.5)
    show dev neutral with eidissolve_nd
    hide dev    

    jump deny_deal

label accept_deal:

    scene buffet with dissolve

    "We walk over to get our food when I notice there are two serving areas, marked as 'herbivore' and 'carnivore' respectively."
    
    "The herbivore side is full of leafy concoctions—towering salads,{w=0.2} steamed veggies,{w=0.2} and grains in every flavor."
    
    "But then there is the carnivore side—burgers,{w=0.2} strips of bacon,{w=0.2} sausages."
    
    "Theo heads straight for the carnivore section, grabbing a tray and piling on a little bit of everything."
    
    if LICA:
        "Checking out what they offer{cps=5}...{/cps} all the meat looks overcooked as charcoal and that the vegetables are drier than the freaking desert, and so{w=0.2} much{w=0.2} grease{cps=5}...{/cps}"
        "I've done better work back on my crappy kitchen stove."
        "Still,{w=0.3} I keep my mouth shut and grab a handful of anything that looks ok and end up with a medium filet mignon with a side of Caesar's salad and a small bowl of crème brulée."
        "Theo has already stacked his tray with various meats by the time I join him in line. He has this huge drumstick in one hand, nibbling on it as we move forward."
        T "Dang,{w=0.3} you got your plate looking fancy!"
        "Fancy?"
        T "You can grab more if you want, I don't mind."
        D "Nah, I'm good.{w=0.3} This was all I could find that looked even edible."
        T "Uh{cps=5}...{/cps} sure, ok{cps=5}...{/cps}"
           
    else:
        "I grab and fill my tray with{cps=5}...{/cps}"  
        menu:
            "Steamed vegetables and veggie pizza. Mom taught me to love my greens.":
                $ CHEESE = False
                "Theo has already stacked his tray with various meats by the time I join him in line. He has this huge drumstick in one hand, nibbling on it as we move forward."
                T "You humans can eat anything and you still choose to eat grass?{w=0.3} For shame{cps=5}...{/cps}"
                T "You sure you don't want some of this meaty goodness?"
                D "Nah, I'm good."
            "A bacon cheeseburger, fries and meatballs, all between the same buns. I'm given disposable gloves to handle the burger.":
                $ CHEESE = False
                "Theo has already stacked his tray with various meats by the time I join him in line. He has this huge drumstick in one hand, nibbling on it as we move forward."
                T "Oh dude, Samezies!"
                T "You can grab more if you want by the way, I don't mind."
                D "Nah, I'm good."
            "A mix of everything. A varied diet is a healthy diet.":
                $ CHEESE = False
                "Theo has already stacked his tray with various meats by the time I join him in line. He has this huge drumstick in one hand, nibbling on it as we move forward."
                T "Man, this is good stuff. Are you sure you're good with only that?"
                T "You can grab more if you want, I don't mind."
                D "Nah, I'm good."
            "A bowl of cheese and nothing more. Just cheese.":
                $ CHEESE = True
                "Theo has already stacked his tray with various meats by the time I join him in line. He has this huge drumstick in one hand, nibbling on it as we move forward."
                T "{cps=5}...{/cps}"
                T "You sure that is all you want?"
                D "Yes."
                T "You can get what you want obviously I just thi-{nw}"
                D "I'm good."
    
    "He shrugs and continues eating."
    
    "I take a bite of my meal with one hand while the other holds the tray.{w=0.3} The food tastes slightly bitter because it was a gift, no matter the supposed payment I would have to give in the form of helping Theo with his school work."
    
    "For all I know, he might just be messing with me about how bad his history assignments are."
    
    "In any case,{w=0.3} the food finds a way to battle past the bitterness and fill me with comfort. And so does Theo's happy mood."
    
    "We reach the cashier and Theo flashes his credit card for both our meals, gesturing for me to follow him to find seats in the crowded dining hall."    

    jump introducing_becca
    
label deny_deal:

    scene vending with dissolve
    
    $renpy.music.set_volume(0.25, channel='ambience', delay=2)

    "I nod and make my way through the crowd, the noise fading as I leave the main hall."
    
    "Following Theo's direction, I spot the fluorescent lights of the vending machines."
    
    "Surprisingly, despite there being quite a few machines, my choices are limited;{w=0.3} they all seem to hold basically the same stuff."
    
    "I feed several dollars into one of the machines, mourning the feel of my lighter pockets."
    
    if LICA:
        "Nothing looks all that good on its own, but{cps=5}...{/cps} cheddar popcorn, pretzels, mixed nuts, raisins, and some chocolate bites. Its not exactly high culinary arts, but I could make a trail mix from that. Would probably last me all day even."
        $renpy.music.set_volume(0.5, channel='ambience', delay=2)
        "With my meager dinner in hand, I walk back to where Theo waits, his plate piled high with what looks like half the menu."    
        "All of which is meat."    
        "As I approach, he eyes my selection."
        T "Dang,{w=0.3} you buy out a whole machine!"
        D "Going to make a trail mix."
        "He gives me a grin."
        T "Well look at mister '\master chef'\ over here!{w=0.3} Anyways lets go grab a seat."
    
    else:
        "I choose{cps=5}...{/cps}"
        menu:
            "A Stone Tart, strawberry flavored. Not my favorite and very artificial, but it's the only brand name I recognize.":
                $renpy.music.set_volume(0.5, channel='ambience', delay=2)
                "With my meager dinner in hand, I walk back to where Theo waits, his plate piled high with what looks like half the menu."        
                "All of which is meat."       
                "As I approach, he eyes my selection."        
                T "Bit of a sweet tooth huh?"        
                "There's a note of hurt in his sarcasm."        
                "Guess things weren't off to a great start."        
                D "Yep."
            "Paleo Potato Chips, extra spicy and with meat flakes. If I'm going to spend this much money on trash, at least I'll go with a banger.":
                $renpy.music.set_volume(0.5, channel='ambience', delay=2)
                "With my meager dinner in hand, I walk back to where Theo waits, his plate piled high with what looks like half the menu."        
                "All of which is meat."       
                "As I approach, he eyes my selection."        
                T "Feast fit for a king?"        
                "There's a note of hurt in his sarcasm."        
                "Guess things weren't off to a great start."        
                D "Yep."
            "Beef jerky. I'd rather not put chemically enhanced sugar in my system.":
                $renpy.music.set_volume(0.5, channel='ambience', delay=2)
                "With my meager dinner in hand, I walk back to where Theo waits, his plate piled high with what looks like half the menu."        
                "All of which is meat."       
                "As I approach, he eyes my selection."        
                T "Guess I can't completely fault you,{w=0.3} use to be obsessed with Bob Link's in high school."        
                "There's a note of hurt in his voice."        
                "Guess things weren't off to a great start."        
                D "Yep."

    jump introducing_becca

label introducing_becca:
    
    #add the cg of rebecca once its done.
    scene cafeteria_summer with dissolve
        
    show theo at moveinright(0.4) with eidissolve_nd
    show dev at moveinright(0.2) with eidissolve_nd
    show rebecca left at moveinleft(0.7) with eidissolve_nd:
        setx(0.7)
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
    show rebecca neutraldown with eidissolve_nd
    
    $renpy.music.set_volume(0.25, channel='ambience', delay=2)
    
    "We maneuver through the crowd, and Theo leads me to a quieter corner where a girl{w=0.3} with spiky hair and spikier clothes sits alone{w=0.1}, her eyes glued to a laptop screen. A half-eaten sandwich lies forgotten beside her."
    
    show theo grin with eidissolve_nd
    
    T "And this here is my amazing{w=0.1}, awesome{w=0.1}, beautiful{w=0.1} sister Rebecca!"
    
    show rebecca angry :
        backmovey(0.1)
    with eidissolve_nd
    
    "The dino snaps her head towards Theo in an angry snarl.{w=0.3} Her fangs are even spikier."
    
    R "Theo I swear,{w=0.3} I don't want to meet another one of your new-"
    
    show rebecca surprised with eidissolve_nd
    
    "Her eyes flick up briefly before staring at me."
    
    D "{cps=5}...{/cps}"
    
    "{cps=5}...{/cps}{w=0.3} I should probably say something."
    
    show theo happy
    show dev somber
    with eidissolve_nd
    
    D "Uh{w=0.3}, hi{cps=5}...{/cps} I'm Dev."
    
    "Smooth Dev{w=0.1}, real smooth."
    
    show rebecca skeptical with eidissolve_nd
    
    R "{cps=5}...{/cps}{nw=0.2}"
    
    show theo skeptical
    show dev surprised 
    with eidissolve_nd
    
    extend " You're{w=0.3} a human{cps=5}...{/cps} "    

    show theo angry with eidissolve_nd
    
    "An uncomfortable laugh escapes my mouth."
    
    show dev skeptical 
    with eidissolve_nd
    
    D "Last I checked{cps=5}...{/cps} Is that an issue?"
    
    show rebecca neutraldown 
    with eidissolve_nd
    
    R "{cps=5}...{/cps}"
    
    show rebecca neutral
    show dev neutral
    show theo unimpressed
    with eidissolve_nd
    
    R "No."
    
    show rebecca neutraldown with eidissolve_nd:
        setx(0.7)
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
    
    
    "And with that, she turns away. Her fingers are already dancing across the keys."
    
    show dev sad with eidissolve_nd
    
    "I sigh."
    
    show theo neutral left with eidissolve_nd
    
    T "Don't worry{w=0.3}, the fact she is even talking to you means she likes you."
    
    show rebecca:
        backmovey(0.1)
    show rebecca angry with eidissolve_nd
    show dev skeptical with eidissolve_nd
    show theo grin with eidissolve_nd
    
    "Judging by the absolute death glare she is giving Theo I question whether that is true."
    
    show rebecca neutraldown with eidissolve_nd:
        setx(0.7)
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
    show dev neutral with eidissolve_nd
    show theo neutralconsidering with eidissolve_nd
    
    T "You don't really see humans here{w=0.2}, or even in town."
    
    show theo neutral with eidissolve_nd
    
    T "Was like that even last year."
    
    show dev shocked with eidissolve_nd
    
    D "Really?"
    
    show theo happy with eidissolve_nd
    
    T "Yep{w=0.3}, you're a bit of a rarity at CCC."
    
    show dev thinking with eidissolve_nd
    
    "I remember Elliot's comment about me being the only human here.{w=0.2} Huh{w=0.3}, did no one else apply the same scholarship I got?"
    
    show dev neutral with eidissolve_nd
    
    D "Well{w=0.3}, no one really seems to care if that is the case."
    
    R "People have far more to worry about here than some random human walking around."
    
    show dev sad with eidissolve_nd
    
    "Harsh{w=0.3}, but fair{cps=5}...{/cps}"
    
    "Despite her comments, her gaze remains fixed on her screen. The steady click-click-click of her typing somehow cuts through the noise."
    
    show dev thinking
    show theo neutral right
    with eidissolve_nd
    
    "I try to focus on my food, but my thoughts keep drifting."
    
    "It was weird to be sitting here, sharing a meal with two near-strangers{w=0.3}, one of whom seemed as though she'd rather be alone and another who couldn't wait to spend the rest of his day dragging me all over the campus."
    
    "I've never really been this far from home before, and this is going to be my life for the next several years."
    
    show dev neutral
    show theo neutral left
    with eidissolve_nd
    
    T "So{w=0.2}, Dev{w=0.2}, what brought you to CCC?"
    
    D "Scholarship."
    
    show theo cheerful with eidissolve_nd
    
    T "Really?{w=0.2} That's sick dude!"
    
    show rebecca skeptical
    show theo happy
    with eidissolve_nd
    
    R "Lucky you{cps=5}...{/cps}"
    
    show rebecca neutraldown
    show dev somber
    with eidissolve_nd
    
    T "What was the scholarship for{w=0.2}, you some sort of genius or sports star!"
    
    show dev:
        pause 0.1
        nudgeleft(x=0.2, t=1)
    show theo happy:
        nudgeleft(x=0.4, t=1)
    with eidissolve_nd
    
    "He gives me a playful nudge."
    
    show theo skeptical
    show dev thinking t_skeptical
    show rebecca neutral
    with eidissolve_nd
    
    D "For being human I think{cps=5}...{/cps}?{nw=0.3}"
    show dev neutral with eidissolve_nd
    extend " I don't really fully understand it myself to be honest."

    "They both look at me with a confused expression."

    D "I looked it up and it seemed to be something to try and get more humans in these fancier colleges. There was even some big lawsuit about it."
    
    show theo considering
    show rebecca neutraldown
    with eidissolve_nd
    
    T "But you're the only one here."
    
    show dev skeptical
    show theo skeptical
    with eidissolve_nd

    D "I know{cps=5}...{/cps} I mean{w=0.3} it's weird enough no one else got the scholarship, but{w=0.3} you'd think even without it there would be more humans here."
    
    show rebecca skeptical with eidissolve_nd
    
    R "Not really. Dinosaurs are just better suited for college than humans."

    show theo angry right with eidissolve_nd

    T "{cps=6}Rebecca...{/cps}"
    
    show rebecca grin:
        backmovey(0.1)
    with eidissolve_nd
    
    R "It's true. Our memory and attention span are better. Makes cramming for SATs and entry exams a breeze compared to humans."
    
    show dev annoyed with eidissolve_nd

    D "That's{cps=5}...{/cps}{w=0.3} I don't think that's true{cps=5}...{/cps}"
    
    show theo unimpressed left with eidissolve_nd
    
    T "It's not{w=0.3}, she is just messing with you."
    
    show dev skeptical
    show rebecca devious
    show theo considering
    with eidissolve_nd
    
    R "Am I?"
    
    show rebecca:
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
    show rebecca grindown
    show theo skeptical
    with eidissolve_nd
    
    D "{cps=5}...{/cps}"
    
    show rebecca neutraldown with eidissolve_nd
    
    D "Right{cps=5}...{/cps} Well{cps=5}...{/cps}{nw=0.5}"
    show dev neutral
    show theo unimpressed
    with eidissolve_nd
    extend" It doesn't help that it's all so different here.{w=0.3} And I don't really know anyone."
    
    show theo cheerful:
        chuckle
    with eidissolve_nd
    
    "Theo laughs, momentarily confusing me."
    
    show theo happy with eidissolve_nd
    
    T "You know me!{w=0.3} And now you know Rebecca.{w=0.2} Are you saying we're no one?"
    
    show theo grin:
        nudgeleft(x=0.6, t=2)
    show rebecca angry:
        nudgeleft(x=0.7, t=1)
    with eidissolve_nd
    
    "He nudges his sister with an elbow but earns only an annoyed glance."
    
    show theo:
        easein_cubic 1.5 xpos 0.5
    show theo happy
    show dev happy
    show rebecca:
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
    show rebecca neutraldown
    with eidissolve_nd
    
    D "No, of course not."
    
    show dev thinking with eidissolve_nd
    
    D "But there's more to college than just meeting people{w=0.3}, isn't there?"
    
    show dev neutral with eidissolve_nd
    
    T "Making friends is just the beginning. You'll find your groove{w=0.2}, dive into projects{w=0.2}, and before you know it{w=0.1}, you're part of the fabric here."
    
    show rebecca annoyeddown with eidissolve_nd:
        backmovey(0.1)
    
    "Rebecca suddenly stops typing and looks up at her brother with a scowl."
    
    show theo right:
        easein_cubic 1.5 xpos 0.45
    show theo unimpressed
    show rebecca angry
    with eidissolve_nd
    
    R "He just met us{w=0.2}, so just stop acting like we've known each other for years or something."
    
    show dev skeptical with eidissolve_nd
    
    "I mean{w=0.3}, she isn't wrong, but{cps=5}...{/cps} it still seems a bit rude."
    
    show dev neutral
    show theo happy left
    with eidissolve_nd
    
    T "Ehh, don't mind miss grumpy. She gets like this sometimes, but she doesn't mean anything by it."
    
    show dev surprised
    show theo surprised right     
    show rebecca gritting:
        hop(y=0.1)
    with eidissolve_nd
    
    R "Stop acting like I'm not here{cps=5}...{/cps} or like I'm a child!"
    
    show dev skeptical
    show theo grin right
    show rebecca annoyed
    with eidissolve_nd    
    
    T "Becca, your warm and fuzzy welcome is exactly why I brought Dev here.{w=0.3} Wanted him to feel right at home."
    
    show dev neutral
    show rebecca annoyedconsidering
    with eidissolve_nd     
    
    R "{cps=5}...{/cps}"
    
    show theo grin left
    show rebecca:
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
    show rebecca neutraldown
    with eidissolve_nd 
    
    T "Anyway{w=0.3}, all I'm trying to say is to not let the college scare you. You'll find your way."
    
    show theo neutralconsidering
    show rebecca annoyeddown
    with eidissolve_nd 
    
    "Rebecca snorts but says nothing."
    
    show theo neutral
    show rebecca neutral
    with eidissolve_nd 
    
    T "Or Becca{w=0.3}—don't let her scare you, either."
    
    show theo neutral right
    show rebecca devious:
        backmovey(0.1)
    with eidissolve_nd
    
    R "Theo, if he runs off because of me, he isn't going to last here long anyway."
    
    show theo neutral
    show dev thinking t_skeptical
    show rebecca:
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
    show rebecca neutraldown
    with eidissolve_nd
    
    "She seems{cps=5}...{/cps}"
    
    "{cps=5}...{/cps}"
    
    show dev sad with eidissolve_nd
    
    "Actually{w=0.5}, I don't know what to make of her."
    
    show dev neutral with eidissolve_nd
    
    "She has been focused on her laptop nearly this whole time, typing up a storm about{cps=5}...{/cps} something."
    
    "I'm not at a good angle to really see what it is{w=0.3}, and I don't want to seem like I'm spying."
    
    show dev skeptical with eidissolve_nd
    
    "Maybe I should just ask."
    
    show dev somber with eidissolve_nd
    
    "A sort of icebreaker{w=0.3}, even if she doesn't exactly seem like she likes me{cps=5}...{/cps}"
    
    menu:
        "Invade her privacy and ask what she is writing.":
            $ beccainvade = True
            show dev happy with eidissolve_nd
            D "So{w=0.3}, what are you writing?"
            show rebecca surprised:
                sety(0.1)
            with eidissolve_nd
            "Rebecca's eyes flick up, wide for a moment{nw}"
            show rebecca angry
            extend" before turning into a sharp scowl."
            show rebecca angry with eidissolve_nd
            R "Mind your own business."
            show dev skeptical
            show rebecca neutraldown:
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
            "Okay{w=0.5}, guess I struck a nerve."
            show dev neutral with eidissolve_nd
            "I shrug{w=0.3}, focus back on my food, but I can't help but feel a little stung. I was just trying to make conversation{cps=5}...{/cps}"
            "Theo is done with his plate, wiping his mouth with the back of his hand."
            show theo cheerful left with eidissolve_nd
            "He leans back in his chair, eyes catching mine for a moment before they shift to Rebecca.{w=0.3} He gives me a sly grin."
            show theo:
                moveoutdown
            hide theo
            pause 0.2
            show theo grin left:
                moveinup(x=0.68, t=2)
                rotate_funny(0.05, inv=-1)
            show theo behind rebecca
            with eidissolve_nd
            "With cat-like stealth, Theo slides up behind Rebecca, peering over her shoulder."
            show rebecca shocked with eidissolve_nd:
                sety(0.1)
            T "{i}\"The Chimera launch themselves at you once again, a writhing mass of bodies holding you in place, the strength of a half-dozen arms finally overpowering yours—\"{/i}"        
            show theo right:
                pause 0.1
                sety(0)
                resetrotate
                nudgeleft(x=0.45)
                
            show theo fear f_shocked
            show rebecca:
                nudgeleft(x=0.7)
            show rebecca gritting
            show rebecca blush
            with eidissolve_nd
            "Rebecca's cheeks flare red as she whirls around, shoving him away."
            show theo surprised with eidissolve_nd
            show rebecca pissed with eidissolve_nd
            R "Theo! Get out of my stuff!"
            "Her voice is half an octave higher than before."
            show theo cheerful with eidissolve_nd:
                chuckle
            show theo happy with eidissolve_nd
            T "Aww don't be like that Becca{w=0.3}, it was just getting good!"
            show theo skeptical with eidissolve_nd
            show rebecca annoyed with eidissolve_nd:
                linear 0.5  ypos 0.0 xpos 0.6
            "She glares at him with enough intensity to start a fire,{nw=1.0}"
            show theo shocked:
                linear 0.01  ypos 0.0 xpos 0.43
                linear 0.5  ypos 0.0 xpos 0.45
            show rebecca annoyed:
                linear 0.01  ypos 0.0 xpos 0.58
                linear 0.5  ypos 0.0 xpos 0.6
            with eidissolve
            extend" before flicking him on the snoot."
            show theo sad with eidissolve_nd
            T "Ow!"
            show rebecca sass s_angry with eidissolve_nd:
                easeout_quad 0.5 xpos 0.7
            show rebecca noblush with eidissolve_nd
            R "It's not for you to read{w=0.3}—or anyone else here, for that matter."
            show theo ashamed a_saddown with eidissolve_nd
            show rebecca s_angrydown with eidissolve_nd:
                easeout_cubic 0.5 ypos 0.1
            "She slams her laptop shut, her gaze now fixed on the table between us."
            show dev sad with eidissolve_nd
            "{w=0.5}I can't help but feel a twinge of guilt for having sparked this exchange."
            show rebecca angry with eidissolve_nd
            "I clear my throat."
            if SUI:
                show theo sad left with eidissolve_nd
                show dev somber with eidissolve_nd
                
                D "Didn't mean to pry, I don't know if I'd survive having someone else read my writings out loud. It's just that I like learning from other people's work and what I heard sounded good. I like your flow.."
                show dev neutral with eidissolve_nd
                show rebecca surprised with eidissolve_nd
                R "Wait, so you write too?"
                "I shrug."
                show dev happy with eidissolve_nd
                D "A bit. I'm not very good, though."
            else:
                show theo sad left with eidissolve_nd
                show dev happy with eidissolve_nd
                D "Well I thought it sounded pretty cool{cps=5}...{/cps}{nw=0.3}"
                show rebecca neutral with eidissolve_nd
                extend" I didn't mean to pry."
            show theo unimpressed right with eidissolve_nd
            show rebecca neutraldown with eidissolve_nd
            R "{cps=5}...{/cps}"
            "Rebecca shakes her head, and after a moment of hesitation{w=0.3}, reopens her laptop."
            show theo neutral with eidissolve_nd
            show rebecca neutral with eidissolve_nd
            R "It's fine.{w=0.3} Just{cps=5}...{/cps} forget it."
            show rebecca neutral with eidissolve_nd

        "Don't be nosy and mind my own business.":
            $ beccainvade = False
            show dev neutral with eidissolve_nd
            "It's probably best I leave her be."
            show theo thinking t_smug with eidissolve_nd
            T "So{w=0.3}, what's got you so invested in writing now, I'm sure Dev would like to know too."
            show rebecca sass s_annoyed with eidissolve_nd:
                sety(0.1)
            show theo neutralconsidering with eidissolve_nd
            show dev annoyed with eidissolve_nd
            D "Dude{cps=5}...{/cps}"
            show theo grin left with eidissolve
            T "C'mon, don't tell me you aren't curious."
            "I shrug."
            show theo unimpressed with eidissolve_nd
            show dev unimpressed with eidissolve_nd
            show rebecca surprised with eidissolve_nd
            D "It's not our business."
            show rebecca angry with eidissolve_nd
            R "He's right, it's not."
            "While it's true that curiosity is killing me, if we'd exchanged places, I'd be just as annoyed."
            show theo crossed c_sad with eidissolve_nd
            T "Two against one! It's not fair."
            "Theo places a hand on his chest, dramatically feigning being hurt by my betrayal to our newly formed friendship."
            show dev happy:
                chuckle
            pause 0.5
            show rebecca surprised with eidissolve_nd
            show dev smug with eidissolve_nd
            D "Do you try to peek at other people's phones when they're not looking too?"
            show theo:
                block:
                    xzoom -1
                    pause 1.3
                    xzoom 1
                    pause 1.3
                    repeat
            show theo surprised with eidissolve_nd
            show rebecca devious with eidissolve_nd
            "Theo's mouth hangs open while Rebecca{w=0.3}, surprisingly, snickers at my remark."
            T "I don't- I wouldn't- ah!"
            show theo surprised right with eidissolve_nd:
                xzoom 1
            show rebecca cheerful with eidissolve_nd
            show dev happy with eidissolve_nd
            R "He totally does that."
            show theo grin with eidissolve_nd
            show rebecca pissed p_shocked p_spiky with eidissolve_nd
            T "Well then, keep your secrets Becca, bet it's more fanfiction about colorful horses anyways."
            show theo neutralconsidering with eidissolve_nd
            show dev skeptical with eidissolve_nd
            D "{cps=5}...{/cps}wha-"
            show rebecca point po_angry with eidissolve_nd
            R "{b}Don't!{/b}"
            show rebecca grumpy with eidissolve_nd

    ###maybe have the camera zoomed in slightly with everyone scaled down, then when elliot shows have it zoom out a bit while he shows up?
   
    
    show dev neutral with eidissolve_nd
    show theo neutral with eidissolve_nd

    "As I poke at the few last crumbs of my meal, a new face suddenly strides up to our table."
    
    show elliot annoyedconsidering at moveinright(x=0.15) with eidissolve_nd
    show dev left with eidissolve_nd:
        movex(x=0.4)
    show theo skeptical left with eidissolve_nd:
        movex(x=0.6)
    show rebecca surprised with eidissolve_nd:
        movex(x=0.8)
    
    E "Raptor Jesus, those assholes can't give me one moment of-"
    
    show theo happy with eidissolve_nd
    show elliot surprised with eidissolve_nd
    show dev surprised with eidissolve_nd
    show rebecca neutraldown with eidissolve_nd:
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
    
    E "{cps=5}...{/cps}"
    
    D "{cps=5}...{/cps}"
    
    "I'm not sure which one of us is more confused about the other's presence."
    
    show theo grin with eidissolve_nd
    
    T "Elliot!{w=0.3} What's up man? Have you met Dev yet?"
    
    show elliot angry with eidissolve_nd
    
    "Finally breaking off the stare, Elliot's face drops with a grimace."
    
    show dev skeptical with eidissolve_nd
    
    "Of course my newest friend would also happen to be friends with the guy that left me to get lost in campus. All things considered{w=0.3}, it makes sense that overwhelmingly friendly Theo would be friends with basically anyone."
    
    show dev annoyed with eidissolve_nd
    
    E "What the hell is he doing here?"
    
    show rebecca annoyed with eidissolve_nd:
                sety(0.1)
    
    R "He was invited.{w=0.3} Unlike you."
    
    show dev surprised with eidissolve_nd
    show rebecca neutraldown with eidissolve_nd:
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
    
    "Rebecca coming up to my defense surprises me.{w=0.3} She must dislike Elliot more than she dislikes this random human her brother dragged along."
    
    show theo cheerful with eidissolve_nd
    show dev neutral with eidissolve_nd
    
    
    T "So you two DO know each other!"
    
    show dev unimpressed with eidissolve_nd
    
    D "He was the 'orientation' I mentioned to you when we met."
    
    show theo unimpressed with eidissolve_nd
    show elliot surprised with eidissolve_nd
    
    T "Really?{w=0.3} You know he spent like an hour trying to find the dorms, right?{w=0.3} You really just left him hanging?"
    
    show elliot unimpressed with eidissolve_nd
    
    E "{cps=5}...{/cps}{w=0.3} I gave him a map."
    
    ##zoom in on the two
    show cafeteria_summer:
        easein_quad .25:
            zpos +389
    camera:
        perspective True
        easein_quad .25:
            zpos -189
            xpos -200
            ypos -45
    show theo crossed c_skeptical:
        movex(x=0.4)
    show dev surprised at movex(x=0.65) 
    show rebecca at movex(x=0.85) 
    
    T "Elliot{cps=5}...{/cps}"
    
    show elliot considering with eidissolve_nd
    
    E "Look{w=0.3}, I had another{cps=5}...{/cps} I had stuff to deal with."
    
    show cafeteria_summer:
        easein_quad .25:
            zpos +589
    camera:
        perspective True
        easein_quad .25:
            zpos -289
            xpos -300
            ypos -55
    
    show theo c_angry at movey(y=-0.05) 
    show dev neutral at movex(x=0.9) 
    show elliot surprised at movex(x=0.22) 
        
    T "{cps=5}Elliot...{/cps}"
    
    show elliot annoyed with eidissolve_nd
    
    E "Ok, fine{w=0.3}, I'm sorry!{w=0.5} Damn{cps=5}...{/cps}"
    
    show theo unimpressed with eidissolve_nd
    
    T "{cps=5}...{/cps}"
    
    show cafeteria_summer:
        easein_quad 1.0:
            zpos 0
    camera:
        perspective True
        easein_quad 1.0:
            zpos 0
            xpos 0
            ypos 0
    
    show theo:
        movey(y=0)
        movex(x=0.4)
    show dev at movex(x=0.6)  
    show rebecca skeptical at movex(x=0.8) 
    show elliot unimpressed at movex(x=0.15) 

    pause 1.0

    show theo joy j_cheerful with eidissolve_nd

    T "Well, the important thing is that you learn from your mistakes!"
    
    show elliot annoyedconsidering with eidissolve_nd
    
    E "Sure{cps=5}...{/cps} Thanks Dad."
    
    show elliot neutral with eidissolve_nd
    show theo happy with eidissolve_nd
    
    T "Anytime!"
    
    show elliot unimpressed with eidissolve_nd
    show rebecca skeptical with eidissolve_nd:
        sety(0.1)
    
    R "Why are you even here?"
    
    show elliot skeptical with eidissolve_nd
    
    E "Because Theo texted me he was eating{cps=5}...{/cps} and I always sit here?"
    
    show theo thinking t_thunk with eidissolve_nd
    show rebecca annoyedconsidering with eidissolve_nd
    R "Unfortunately{cps=5}...{/cps}"
    
    show theo cheerful with eidissolve_nd:        
        block:
            subpixel True
            xzoom (-1)
            easein_cubic (0.7/2) ypos 0.0 - 0.08
            easeout_cubic (0.7/2) ypos 0.0
            easein_cubic (0.7/2) ypos 0.0 - 0.07
            easeout_cubic (0.7/2) ypos 0.0
            pause 0.1
            xzoom (1)
            easein_cubic (0.7/2) ypos 0.0 - 0.08
            easeout_cubic (0.7/2) ypos 0.0
            easein_cubic (0.7/2) ypos 0.0 - 0.07
            easeout_cubic (0.7/2) ypos 0.0
            pause 0.1
            repeat
        
    show rebecca annoyed with eidissolve_nd
    show dev thinking t_annoyed with eidissolve_nd
    
    "Truthfully{w=0.3}, I'm still a bit annoyed about what Elliot pulled. However, not only has the conversation already moved on, but Theo's eyes light up like he's just had the best idea."
    
    show rebecca neutral 
    show elliot neutral 
    show dev neutral  
    show theo right grin:
        xzoom (1)
        sety(0.0)
    with eidissolve_nd        
    
    
    T "I think it's time for proper introductions!"
    
    show rebecca annoyed with eidissolve_nd
    show elliot annoyedconsidering with eidissolve_nd    
    show theo left happy with eidissolve_nd
    
    E "Theo{w=0.5}, we've all met before."
    
    show theo right happy with eidissolve_nd
    show rebecca angry with eidissolve_nd
    show elliot unimpressed with eidissolve_nd
    
    R "Yeah, what is this{w=0.3}, elementary school?"
    
    show rebecca annoyed with eidissolve_nd
    
    T "Nah, nah, this is different!{w=0.3} Dev's new here. It's only fair."
    
    "I glance around the table.{w=0.3} Despite his enthusiasm, it's clear he's the only one on board with doing this."
    
    show dev skeptical with eidissolve_nd
    
    "Not to mention{w=0.3}, it's a bit childish{cps=5}...{/cps}"
    
    show dev sad with eidissolve_nd
    
    D "I mean{w=0.3}, I already know your names..."
    
    show theo considering with eidissolve_nd
    
    "Theo waves a hand dismissively."
    
    show theo happy with eidissolve_nd
    
    "He points to himself with both thumbs, grinning."
    
    show theo cheerful with eidissolve_nd
    
    T "I'm Theodore Chase, but you can call me Theo.{w=0.3} Second year here at CCC and future creator of the next big indie game!"
    
    show theo neutralconsidering with eidissolve_nd
    
    T "Our dad is a microraptor, and our mom is a pterodactyl, which I take after both of them. Which is why I look all {cps=5}fUnKy{/cps}."
    
    show theo skeptical with eidissolve_nd
    show rebecca devious with eidissolve_nd
    
    R "A genetic {cps=100}{b}freak{/b} {/cps}is what you mean."
    
    show rebecca neutral with eidissolve_nd
    show theo smug with eidissolve_nd
    
    T "You're just jealous you only took after dad."
    
    show theo happy with eidissolve_nd
    
    T "I like meat, video games, programming, FND let's plays, and{nw=0.5}"
    show theo considering with eidissolve_nd
    extend" {cps=5}uhhhh...{/cps}"
    
    
    show rebecca neutraldown with eidissolve_nd:
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
    
    show theo cheerful with eidissolve_nd
    T "I think that's it."
    
    show dev thinking with eidissolve_nd
    show theo neutral with eidissolve_nd
    
    "For all the hassle he caused about introducing oneself properly, he sure gave the rest of us a very underwhelming presentation. Eh{w=0.3}, I give it a six point five out of ten. Sufficient{w=0.3}, but won't be entering any lists for the best of anything this year."
    
    show dev neutral with eidissolve_nd
    show theo skeptical with eidissolve_nd
    show rebecca sass s_annoyed with eidissolve_nd:
        sety(0.1)
    
    "He looks to his sister.{w=0.3} The glare he receives in response could melt steel."
    
    show theo unimpressed with eidissolve_nd:
        xzoom (-1)
    show elliot annoyeddown with eidissolve_nd
    show rebecca neutraldown with eidissolve_nd:
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
    
    "Elliot is just picking at his food{w=0.3}, seemingly ignoring Theo."
    
    show theo happy with eidissolve_nd:
        xzoom (1)
    show dev with eidissolve_nd
    
    "Finally, he turns to me."
    
    show theo grin with eidissolve_nd
    
    D "{cps=5}...{/cps}"
    
    show theo cheerful with eidissolve_nd
    
    T "{cps=5}...{/cps}"
    
    show dev sad with eidissolve_nd
    
    "Crap{cps=5}...{/cps}"
    
    show theo happy with eidissolve_nd
    
    T "Come {cps=6}ooooonnnn...{/cps}"
    
    T "Show these two how it's done{w=0.3}, don't hold anything back!"
    
    D "I would really prefer not to{cps=5}...{/cps}"
    
    show theo skeptical with eidissolve_nd
    
    T "This is a safe space Dev, you can be honest with us."
    
    show theo sad with eidissolve_nd
    
    T "Also{w=0.3}, please throw me a bone{w=0.3}, you can't leave me hanging after revealing all my darkest secrets like that."
    
    "It's becoming increasingly difficult to say no to the guy."
    
    D "{cps=5}...{/cps}"
    
    show dev annoyed with eidissolve_nd
    show theo cheerful with eidissolve_nd
    
    D "Fine{cps=5}...{/cps}"
    
    menu:
        "Introduce yourself.":
            show dev thinking with eidissolve_nd
            D "My name is Dev Loper and this is my first year here.{w=0.3} I don't really know what I want to do in the future."
            D "I guess I like video games as well, and{w=0.3} YouSnoot shorts{cps=5}...{/cps}{nw}"
            show dev neutral with eidissolve_nd
            extend" not sure what else{cps=5}...{/cps}"
            T "That was great!"

        "Keep it brief.":
            show theo happy with eidissolve_nd
            show dev thinking t_considering with eidissolve_nd
            D "My name is Dev Loper and this is my first year here."
            show theo neutral with eidissolve_nd
            show dev neutral with eidissolve_nd
            T "{cps=5}...{/cps}"
            show theo skeptical with eidissolve_nd
            T "Was{cps=5}...{/cps}was that it?"
            D "Yeah."
            show theo ashamed a_upset with eidissolve_nd
            T "That wasn't much of an introduction{cps=5}...{/cps}"
            show theo unimpressed with eidissolve_nd
            show rebecca skeptical with eidissolve_nd
            R "Theo{w=0.3}, we are strangers{w=0.3}, normal people don't like throwing their life story at the feet of strangers."
            show rebecca neutraldown
            show theo neutral 
            with eidissolve_nd

        "Well he asked for it , tell them EVERYTHING!":
            show dev neutral
            show theo neutral
            with eidissolve_nd
            D "Well{w=0.3}, I'm Dev A. Loper. As you know{w=0.3}, I'm a freshman here, and yeah{w=0.3}, I got in on a scholarship for{cps=5}...{/cps} reasons that are still kind of beyond me."
            show dev somber
            show theo unimpressed
            with eidissolve_nd
            D "I'm not exactly sure what I'm doing here, to be honest.{w=0.3} I like games,{w=0.1} tech stuff{cps=5}...{/cps} but there's no grand plan or anything."
            show dev sad
            show rebecca skeptical
            show theo skeptical
            with eidissolve_nd
            D "I guess you could say I'm sort of winging it?{w=0.3} Which sounds really bad out loud now that I'm saying it."
            show dev somber
            show rebecca grumpy
            show elliot skeptical
            show theo ashamed a_embarrassed
            with eidissolve_nd
            D "Back home I wasn't exactly{cps=5}...{/cps} well,{w=0.3} let's just say social circles and I didn't really overlap. The 'fitting in' part of life's always been a bit of a challenge."
            show dev sad
            show rebecca annoyed
            show elliot annoyeddown
            show theo ashamed a_upset
            with eidissolve_nd
            D "And here? Well,{w=0.3} it's like that,{w=0.3} but with a side of \"Oh hey, you're different from literally everyone else.\" So there's that."
            show dev ashamed
            show rebecca annoyeddown
            show theo ashamed a_upsetconsidering
            with eidissolve_nd
            D "Honestly?{w=0.3} Sometimes it feels like everyone's got their act together but me. Like there's this secret to life that everyone knows but forgot to tell me about."
            show dev neutral
            show theo sad
            with eidissolve_nd
            T "{cps=5}...{/cps}"
            show theo ashamed a_embarrassed
            with eidissolve_nd
            T "O-ok,{w=0.3} that was good, really{w=0.3} uh{w=0.3}, really took that '\everything'\ to heart."
            show dev happy right
            show theo skeptical
            show rebecca angry
            with eidissolve_nd
            R "Yeah, thanks for trauma dumping on us{w=0.3}, it was great."
            show dev happy left
            show theo thinking t_skeptical
            show rebecca angry
            with eidissolve_nd
            E "{cps=5}...{/cps}"
            show dev smug left
            show rebecca angrydown
            show theo crossed c_happy
            with eidissolve_nd
            E "Wait is he done?{w=0.3} I zoned out there for a moment."
            show dev happy
            show theo crossed c_grin
            show rebecca surprised
            show elliot skeptical
            with eidissolve_nd
            T "I think he was messing with us."
            show theo happy
            show rebecca devious
            show elliot surprised
            with eidissolve_nd
            E "{cps=5}...{/cps}"
            show elliot annoyedconsidering
            extend" whatever."
            show rebecca neutraldown
            show dev neutral
            show theo neutral
            show elliot annoyeddown
            with eidissolve_nd

    show dev thinking with eidissolve_nd

    D "Oh, right.{w=0.3} I forgot to add. I'm human?"

    show rebecca skeptical with eidissolve_nd
    show dev sad right with eidissolve_nd
    
    R "We noticed."

    show elliot annoyedconsidering with eidissolve_nd
    show dev sad left with eidissolve_nd
    
    E "Are you{cps=5}...{/cps} actually asking us if you are?"

    D "No? I just{cps=5}...{/cps} because he{cps=5}...{/cps}"
    
    show rebecca neutraldown with eidissolve_nd
    show dev annoyed with eidissolve_nd
    
    D "Nevermind{cps=5}...{/cps}"

    show dev sad left
    show rebecca ugh
    with eidissolve_nd
    
    "There's a moment of silence.{w=0.3} Rebecca sighs in that kind of disappointment you hear from your parents when they tell you they're not angry but, again, disappointed."
    
    "It's just as discouraging."

    show theo grin right with eidissolve_nd

    pause 0.75

    show theo grin left with eidissolve_nd
    
    "Theo looks at Rebecca and Elliot expectantly."

    show rebecca annoyeddown with eidissolve_nd
    
    R "{cps=5}...{/cps}"
    
    E "{cps=5}...{/cps}"
    
    T "Come on{w=0.3}, both me and Dev did it!"

    show rebecca neutraldown with eidissolve_nd
    show elliot unimpressed
    show dev neutral
    with eidissolve_nd
    
    E "Fine{w=0.3}, if it'll get you off this bit."
    
    show elliot considering:
        pause 0.25
        ease 0.2 ypos -0.05
        ease 0.2 ypos 0.0
    with eidissolve_nd

    "He clears his throat rather sarcastically."

    show elliot smug with eidissolve_nd
    
    E "Hello class{w=0.3}, I'm 23 years old{w=0.3}, and my name is Elliot Reddington of the Reddington family{cps=5}...{/cps}"
    
    show elliot unimpressed
    show theo skeptical right
    with eidissolve_nd
    
    E "{cps=5}...{/cps}"
    
    pause 1

    show elliot skeptical with eidissolve_nd
    
    E "Nothing{w=0.3}, really?"
    
    show rebecca skeptical left
    show dev neutral right
    with eidissolve_nd

    pause 0.75

    show dev neutral left with eidissolve_nd

    pause 0.5
    
    "I look around and find both Theo and Rebecca are also looking at me."
    
    show dev sad left with eidissolve_nd
    
    D "Wait-{w=0.3} Was I supposed to know who the Reddingtons are?"

    show elliot skeptical with eidissolve_nd
    
    E "People typically have a reaction when they find out I am a Reddington."
    
    "I shrug."
    
    show elliot annoyed
    show rebecca neutraldown
    with eidissolve_nd

    E "You know{w=0.3}, like the real estate company?"
    
    D "{cps=5}...{/cps}"

    show elliot angry with eidissolve_nd
    
    E "What about Red Origin, the freaking space company?"
    
    show dev ashamed
    with eidissolve_nd
    
    D "{cps=5}...{/cps}"
    
    show elliot surprised
    show theo surprised
    with eidissolve_nd
    
    "Rebecca seems to have lost interest in the conversation but Elliot and Theo continue to stare at me.{w=0.3} I shrug again, thinking how much I'd rather have the earth swallow me up right here, right now."

    show elliot annoyedconsidering with eidissolve_nd
    
    E "Whatever{w=0.3}, that's all you get."

    show dev neutral
    show theo ashamed a_embarrassed
    with eidissolve_nd
    
    T "O-ok{w=0.3}, that was good{cps=5}...{/cps} "
    
    show dev neutral right
    show theo happy right 
    with eidissolve_nd
    
    T "Rebecca?"

    show rebecca annoyedconsidering with eidissolve_nd
    
    "She sighs."

    show rebecca annoyeddown with eidissolve_nd
    
    R "You know my name already, and you know I'm his sister."
    
    show dev happy
    show rebecca surprised
    with eidissolve_nd
    
    D "And that you're a fast typer."

    show rebecca grin with eidissolve_nd
    
    "Rebecca stares at me, bemused."

    show rebecca grindown with dissolve_nd
    
    R "That, too.{w=0.3} Sure.{w=0.3} You know that.{nw}"
    show dev neutral
    show rebecca neutraldown
    with eidissolve_nd
    extend" Guess I'm done with my presentation."
    
    show theo skeptical with dissolve_nd
    
    T "{cps=5}...{/cps}"
    
    D "{cps=5}...{/cps}"

    show theo happy left
    show dev left
    with eidissolve_nd
    
    T "Right{cps=5}...{/cps} Well{w=0.3}, now we're no longer strangers!"

    window hide
    window auto

    #black backdrop to illustrate the passage of time as Dev monologues to himself, with Dev in front of the black tint

    #lower music volume
    
    $renpy.music.set_volume(0.2, channel='music', delay=2)
    $renpy.music.set_volume(0.0, channel='ambience', delay=2)

    show black behind dev:
        alpha 0.5
    show theo behind black
    show rebecca behind black
    show elliot behind black
    with Dissolve(1.0)

    pause 1.0
    
    "Small talk fills the rest of our lunch{w=0.3}, it's still awkward but{w=0.3}, maybe not as much as before."

    show theo cheerful left

    "It's mostly Theo driving the conversation{w=0.3}, with Elliot occasionally jumping in with a sarcastic remark or two."

    show theo neutral left
    show rebecca devious left
    with eidissolve
    
    "Rebecca stays mostly quiet{w=0.3}, only offering a word when directly spoken to or when she has a sharp comment."

    show rebecca neutraldown left
    with eidissolve
    
    "I find myself chiming in more than I expected."
    
    "We talk about classes, professors known for their impossible exams, and the best spots on campus to grab a midnight snack."
    
    "It's all pretty mundane stuff, but{w=0.3} it feels good{w=0.3}—normal, even."
    
    "Maybe Theo had a point after all when he forced us through those introductions."
    
    $renpy.music.set_volume(1.0, channel='music', delay=2)
    $renpy.music.set_volume(0.25, channel='ambience', delay=2)
    
    window hide
    window auto

    hide black with eidissolve

    pause 1.0

    show theo grin right:
        ease 0.5 ypos -0.1
        easeout 0.15 ypos -0.05

    pause 0.6

    with vpunch

    show dev surprised left
    show elliot neutral right
    with eidissolve
    
    stop ambience fadeout 5
    
    "As the cafeteria starts to empty and the noise level drops, Theo slaps his hands on the table, startling me."
    
    T "Hey Dev, you wanna come over and play some games?{w=0.3} I've got a pretty sweet setup back at my dorm. Elliot can vouch for it."

    show elliot smug right with eidissolve
    
    "Elliot nods, grinning."

    show dev neutral with eidissolve
    
    E "Yeah, he's not lying{w=0.3}, well except about it being 'his'."

    show theo cheerful left with eidissolve
    
    T "The games are mine{w=0.3}, the TV and console are his{cps=5}...{/cps}"
    
    show theo happy right
    show rebecca skeptical
    show dev right
    with eidissolve
    
    "Rebecca snorts."
    
    R "Only reason to ever go to their room."

    show dev neutral left
    show theo shocked
    with eidissolve
    
    D "Oh, so you're the acquired taste roommate."
    
    show elliot surprised
    show theo ashamed a_embarrassed left
    show rebecca cheerful:
        chuckle(0.1)
    with eidissolve

    E "The {b}WHAT{/b}?"
    
    "Theo blanches. Elliot looks alarmed."
    
    show rebecca grin:
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
    with eidissolve
    
    "Rebecca simply snorts again."
    
    show elliot angry
    show theo ashamed a_smugconsidering
    show rebecca grindown
    show dev thinking
    with eidissolve
    
    "I hesitate{w=0.3}, but only for a moment. It sounds like fun, and honestly{w=0.3}, I could use a break from all the stress of today."
    
    show elliot annoyed
    show theo happy right
    show dev happy
    with eidissolve
    
    D "Yeah, sure, that sounds great."
    
    show theo cheerful
    with eidissolve
    
    T "Awesome!{w=0.3} You're gonna love it."

    window hide
    window auto

    scene black with Dissolve(1.0)
    
    stop ambience fadeout 5
    stop music fadeout 5
    pause 2.0

####PART 4####
    
    play music fleeting_echoes fadein 3.0
    
    "Theo, Elliot, and myself shuffle into their dorm room, while Rebecca goes off to do her own thing without saying goodbye. I asked Theo about it, but he said she does that when she's had her fill of socializing for the moment."
    
    show dormroom_theo_nightlight behind black
    show dormroom_theo_night behind dormroom_theo_nightlight    
    hide black with Dissolve(1)
    window auto show
    
    show theo cheerful at moveinright(x=0.2, m=0.5) with eidissolve_nd
    show theo behind elliot
    pause 0.5
    show theo left with eidissolve_nd
    pause 1.5
    show theo happy
    show dev at moveinright(x=0.45, m=0.45, t=2)
    show elliot unimpressed at moveinright(x=0.7, m=0.7, t=2)
    show theo right
    with eidissolve_nd
    pause 1.5
    show dev left
    show elliot left
    with eidissolve_nd

    #show theo cheerful enter from right, then dev neutral and elliot unimpressed. Theo stops and faces right as if to drop his backback off or some shit, then proceeds over to the left

    "Their room mirrors mine in size,{w=0.3} but feels entirely different."

    #Dev turns left and right as he reads the next line
    show dev neutral right with eidissolve_nd

    pause 1

    show dev neutral left with eidissolve_nd

    pause 0.5
    
    "Posters of old-school video games plaster the walls,{w=0.3} and there's a vibe here."
    
    show dev thinking right with eidissolve_nd
    
    "Two vibes, actually."
    
    "Elliot's half is meticulously clean with everything in its place, while Theo's side is a storm of sketches and scattered game cases where one can't even take a step without looking down first."
    
    show dev neutral with eidissolve_nd
    
    "Well,{w=0.3} I guess you can try walking in blind,{w=0.3} but stepping on these cases would be just as bad as stepping on a LEGO. If not for Elliot's tidy half, I wouldn't know the color of the floor."
    
    "I'm not sure if I've ever seen anything that demonstrates the duality of order and chaos so perfectly."
    
    #oh nvm the backpack thing, I don't have any sprites for backpackless theo

    #"Theo tosses his backpack onto his bed, sending a few papers fluttering to the floor."
    #"He doesn't seem to notice—or care—as he grabs a couple of controllers and tosses one my way."
    "Theo grabs a couple of controllers and tosses one my way."

    show theo crossed c_smug
    show elliot neutral
    with eidissolve_nd
    
    T "Get ready to get schooled."

    #elliot devious sinks down a little in the corner on his side
    show elliot:
        easein_cubic 1 xpos 0.71
        easein_cubic 1 ypos 0.1

    "Elliot settles into his desk chair,{w=0.3} swiveling to face us."
    
    show elliot smug
    show theo neutral
    with eidissolve_nd
    
    E "I'd join,{w=0.3} but I've seen how this ends.{nw=0.5}"
    show elliot neutral with eidissolve_nd
    extend" I'll just enjoy the show."
    
    
    show dev neutral:
        easein_cubic 1 xpos 0.44
        easein_cubic 1 ypos 0.12
    
    pause 0.2
    #Dev / Theo sink down a little, facing the left side by side
        
    show theo left
    show theo:
        easein_cubic 2 xpos 0
    
    pause 1.5
    
    play sound light_switch
    hide dormroom_theo_nightlight with eidissolve_nd
    
    show dev with eidissolve_nd:
        matrixcolor BrightnessMatrix(-0.3)
    show elliot with eidissolve_nd:
        matrixcolor BrightnessMatrix(-0.3)
    show theo with eidissolve_nd:
        matrixcolor BrightnessMatrix(-0.3)
    pause 1
    #hide black
    show theo right:
        easein_cubic 1 xpos 0.23
        easein_cubic 1 ypos 0.1
    pause 2
    
    show dev:
        matrixcolor BrightnessMatrix(0.1)
        pause 1.2
        easein 0.08 matrixcolor BrightnessMatrix(0.06)
        pause 1.6
        matrixcolor BrightnessMatrix(0.08)
        pause 0.86
        easein 0.08 matrixcolor BrightnessMatrix(0.04)
        pause 0.36
        matrixcolor BrightnessMatrix(0.1)
        pause 1.26
        matrixcolor BrightnessMatrix(0.08)
        pause 0.86
        easein 0.08 matrixcolor BrightnessMatrix(0.06)
        pause 1.6
        repeat
    show elliot:
        matrixcolor BrightnessMatrix(0.1)
        pause 1.2
        easein 0.08 matrixcolor BrightnessMatrix(0.06)
        pause 1.6
        matrixcolor BrightnessMatrix(0.08)
        pause 0.86
        easein 0.08 matrixcolor BrightnessMatrix(0.04)
        pause 0.36
        matrixcolor BrightnessMatrix(0.1)
        pause 1.26
        matrixcolor BrightnessMatrix(0.08)
        pause 0.86
        easein 0.08 matrixcolor BrightnessMatrix(0.06)
        pause 1.6
        repeat
    show theo:
        matrixcolor BrightnessMatrix(0.1)
        pause 1.2
        easein 0.08 matrixcolor BrightnessMatrix(0.06)
        pause 1.6
        matrixcolor BrightnessMatrix(0.08)
        pause 0.86
        easein 0.08 matrixcolor BrightnessMatrix(0.04)
        pause 0.36
        matrixcolor BrightnessMatrix(0.1)
        pause 1.26
        matrixcolor BrightnessMatrix(0.08)
        pause 0.86
        easein 0.08 matrixcolor BrightnessMatrix(0.06)
        pause 1.6
        repeat
    with eidissolve_nd
    
    pause 1
    play music hyperpunchsisters_theme fadein 2.0
    
    "Theo launches a game I recognize but haven't played in a while."

    #Safety xpos to make sure they stay in place :)
    show dev considering with eidissolve_nd:
        xpos 0.44 ypos 0.12
    show theo:
        xpos 0.23 ypos 0.1
    show elliot:
        xpos 0.71 ypos 0.1
    
    "Hyper Punch Sisters,{w=0.3} everyone in middle school had it."
    
    "I think we even had a fighting game club where it was the only thing anyone played."
    
    show dev thinking with eidissolve_nd
    
    "It's all quick reflexes and strategy—two things I'm decent but rusty at. I choose a{cps=5}...{/cps}"
    
    menu:
        "Fast but weak character.{w=0.3} I'd practiced stringing combos together during my school years.":
            pass
        "Well rounded character.{w=0.3} Can barely remember how to hold the controller, this will help me get back in gaming shape.":
            pass
        "Strong but slow character.{w=0.3} I'm going to spam the same two buttons and hope for the best.":
            pass

    show theo skeptical
    show dev neutral
    with eidissolve_nd

    "We dive into the first match, and Theo's character is a non-stop flurry of movement. Twitching back and forth or randomly crouching."
    
    show theo smug
    show dev sad
    with eidissolve_nd
    
    "I{cps=5}...{/cps} may be in over my head here{cps=5}...{/cps}"
    
    show theo neutralconsidering
    show dev neutral
    show elliot skeptical
    with eidissolve_nd
    
    T "Okay, okay, warm-up round doesn't count."
    
    show theo happy
    show dev somber
    show elliot neutral
    with eidissolve_nd
    
    "I'm grateful for the mulligan as I try to shake off the nerves and focus on the screen."
    
    show theo angry
    show dev annoyed
    with eidissolve_nd
    
    "There's a rhythm to the game that feels familiar even when you're out of practice—a pattern to attacks, dodges, and counters that you start to feel more than you think about."
    
    show elliot smug with eidissolve_nd
    
    "Elliot watches us with an amused smirk,{w=0.3} calling out pointers that are half helpful, half trolling."
    
    show theo cheerful:        
        ypos 0.0
        block:
            subpixel True
            xzoom (-1)
            easein_cubic (0.7/2) ypos 0.0 - 0.08
            easeout_cubic (0.7/2) ypos 0.0
            easein_cubic (0.7/2) ypos 0.0 - 0.07
            easeout_cubic (0.7/2) ypos 0.0
            pause 0.1
            xzoom (1)
            easein_cubic (0.7/2) ypos 0.0 - 0.08
            easeout_cubic (0.7/2) ypos 0.0
            easein_cubic (0.7/2) ypos 0.0 - 0.07
            easeout_cubic (0.7/2) ypos 0.0
            pause 0.1
            repeat
    show dev sad
    with eidissolve_nd
    
    "The match ends with my character face-down on the virtual battlefield.{w=0.3} Theo whoops in victory,{w=0.3} but offers a good-natured nod."
    
    show dev yiik
    show theo embarrassed:
        xzoom 1
        ypos 0.0
    with eidissolve_nd
    
    "We play a few more rounds,{w=0.3} all of which I lose spectacularly."
    
    show dev:
        matrixcolor BrightnessMatrix(0.1)
    show elliot:
        matrixcolor BrightnessMatrix(0.1)
    show theo:
        matrixcolor BrightnessMatrix(0.1)
    show dev sad:
        rotate_funny(h=0.3, t=5, inv=-1)
    
    with eidissolve_nd
    play music fleeting_echoes fadein 1.0
    
    T "Not bad for a newbie."
    
    show theo embarrassed:
        easein_cubic 1 ypos 0.1
    with eidissolve_nd
    
    D "I'm not,{w=0.3} I used to play this all the time{cps=5}...{/cps} I was one of the top players in my middle school{cps=5}...{/cps}"
    
    show theo ashamed a_upsetconsidering
    show elliot surprised
    with eidissolve_nd
    
    T "{cps=5}...{/cps}"
    
    show elliot unimpressed
    show theo upset
    with eidissolve_nd
    
    E "Rough{cps=5}...{/cps}"
    
    show elliot neutral
    show theo cheerful
    show dev somber:
        resetrotate
        easein_cubic 1 ypos 0.1
    with eidissolve_nd
    
    T "Ah, well,{w=0.3} you'll shake the rust off eventually, I'm sure!"
    
    show dev skeptical with eidissolve_nd
    
    "I'm less convinced about that than he is, but I nod anyway."
    
    show theo neutral
    show dev neutral
    with eidissolve_nd
    
    D "What other games do you have?"
    
    show theo happy with eidissolve_nd
    
    "He motions to the floor around him."
    
    T "Loads! Name it and I probably have it. Got a bunch downloaded too."
    
    show dev thinking with eidissolve_nd
    
    D "Do you have Rock Ring 3? We could play co-op."
    
    show theo sad
    show dev neutral
    with eidissolve_nd
    
    T "No I don't."
    
    show dev thinking
    with eidissolve_nd
    
    D "Oh{cps=5}...{/cps}well maybe-{nw=1}"
    
    show dev surprised
    show dev behind theo
    show theo joy j_cheerful:
        hop(y=0.1)
    with eidissolve_nd
    
    T "But I do have the MGC!"
    
    show elliot skeptical
    show theo skeptical
    show dev neutral
    with eidissolve_nd
    
    E "Isn't that broken?"
    
    show theo considering with eidissolve_nd
    
    T "Nah they fixed it."
    
    show theo behind dev
    show theo happy
    show elliot neutral
    with eidissolve_nd
    
    T "We should play Rock Ring Harvest though, way cooler."
    
    show dev thinking with eidissolve_nd
    
    "Personally, I would still prefer 3,{w=0.3} but Harvest is also good. Anything but 4,{w=0.2} or Raptor Jesus forbid, 5{cps=5}...{/cps}"
    
    show theo skeptical
    show dev sad:
        shudder(x=0.44)
    with eidissolve_nd
    
    "I can't help but involuntarily shudder."
    
    show theo happy
    show dev neutral
    with eidissolve_nd
    
    D "That's fine."
    
    show theo smug
    show dev skeptical
    show elliot unimpressed
    with eidissolve_nd
    
    T "Elliot, you joining now that I can't whoop your butt?"
    
    show elliot considering with eidissolve_nd
    
    E "Yeah sure,{w=0.4} a mission or two."
    
    show theo neutral
    show dev neutral
    show elliot neutral
    show dev:
        matrixcolor BrightnessMatrix(0.1)
        pause 1.2
        easein 0.08 matrixcolor BrightnessMatrix(0.06)
        pause 1.6
        matrixcolor BrightnessMatrix(0.08)
        pause 0.86
        easein 0.08 matrixcolor BrightnessMatrix(0.04)
        pause 0.36
        matrixcolor BrightnessMatrix(0.1)
        pause 1.26
        matrixcolor BrightnessMatrix(0.08)
        pause 0.86
        easein 0.08 matrixcolor BrightnessMatrix(0.06)
        pause 1.6
        repeat
    show elliot:
        matrixcolor BrightnessMatrix(0.1)
        pause 1.2
        easein 0.08 matrixcolor BrightnessMatrix(0.06)
        pause 1.6
        matrixcolor BrightnessMatrix(0.08)
        pause 0.86
        easein 0.08 matrixcolor BrightnessMatrix(0.04)
        pause 0.36
        matrixcolor BrightnessMatrix(0.1)
        pause 1.26
        matrixcolor BrightnessMatrix(0.08)
        pause 0.86
        easein 0.08 matrixcolor BrightnessMatrix(0.06)
        pause 1.6
        repeat
    show theo:
        matrixcolor BrightnessMatrix(0.1)
        pause 1.2
        easein 0.08 matrixcolor BrightnessMatrix(0.06)
        pause 1.6
        matrixcolor BrightnessMatrix(0.08)
        pause 0.86
        easein 0.08 matrixcolor BrightnessMatrix(0.04)
        pause 0.36
        matrixcolor BrightnessMatrix(0.1)
        pause 1.26
        matrixcolor BrightnessMatrix(0.08)
        pause 0.86
        easein 0.08 matrixcolor BrightnessMatrix(0.06)
        pause 1.6
        repeat
    with eidissolve_nd
   
    with eidissolve_nd
    
    play music rockringharvest_theme fadein 2.0
    
    "The room hums with the low buzz of the console as it springs to life,{w=0.3} the screen flashing the familiar logo of 'Rock Ring Harvest',{w=0.3} the bombastic orchestra of the opening theme filling the room."
    
    "It's been a while since I've played any Rock Rings,{w=0.3} but I still have nostalgic memories about this franchise."
    
    show theo cheerful
    show dev neutral
    show elliot grin
    with eidissolve_nd
    
    "Theo's animated as ever, while Elliot sits more reserved but with a spark of anticipation in his eyes."
    
    "We dive into co-op mode."
    
    T "Okay guys, which difficulty, '\hunter'\ or '\gatherer'\?"
    
    show dev annoyed
    show elliot devious
    with eidissolve_nd
    
    E "Both of those might be a bit advanced for Dev, we should do '\weaver'\-"
    
    show theo skeptical
    show dev annoyed
    show elliot skeptical
    with eidissolve_nd
    
    D "I've played this before,{w=0.3} pick '\hunter'\."
    
    show theo smug
    show dev annoyed
    show elliot skeptical
    with eidissolve_nd
    
    T "Ohoho, watch out, we've got a {b}badass{/b} over here."
    
    show theo neutral
    show dev neutral
    show elliot neutral right:
        easein_cubic 1 xpos 0.65
    with eidissolve_nd
    
    "We charge through the first few enemies with surprising ease. My shots are a little off at first, but it doesn't take long to find my groove."
    
    "I may have played a lot of HPS, but I {i}{cps=5}breathed{/cps}{/i} Rock Ring."
    
    "Theo's character bounds ahead,{w=0.3}  fearless, sometimes too much so—he gets taken down more than once."
    
    "Elliot plays far more defensively,{w=0.3}  always behind cover and only using precision weapons."
    
    show theo surprised
    show dev surprised
    show elliot surprised:
        hop(y=0.1)
    with eidissolve_nd
    
    E "Watch out!"
    
    show theo angry
    show dev annoyed
    show elliot angry
    with eidissolve_nd
    
    "Thanks to his callout, it only takes me a split second to spot the group of enemies ambushing us from the side."
    
    "I swivel my character and open fire, the controller vibrating in my hands with each shot."
    
    show dev smug
    show elliot devious
    show theo cheerful:        
        ypos 0.0
        block:
            subpixel True
            xzoom (-1)
            easein_cubic (0.7/2) ypos 0.0 - 0.08
            easeout_cubic (0.7/2) ypos 0.0
            easein_cubic (0.7/2) ypos 0.0 - 0.07
            easeout_cubic (0.7/2) ypos 0.0
            pause 0.1
            xzoom (1)
            easein_cubic (0.7/2) ypos 0.0 - 0.08
            easeout_cubic (0.7/2) ypos 0.0
            easein_cubic (0.7/2) ypos 0.0 - 0.07
            easeout_cubic (0.7/2) ypos 0.0
            pause 0.1
            repeat
    with eidissolve_nd
    
    "Theo lets out a whoop as he tosses a rock at a large enemy's face, killing him instantly."
    
    show theo:
        xzoom 1
        ypos 0.0
    show theo happy:
        easein_cubic 1 ypos 0.1
    show dev happy
    show elliot happy
    with eidissolve_nd
    
    "Rocks were always a bit OP,{w=0.3}  but that's just part of Rock Ring's charm."
    
    "By the third mission we're perfectly in sync,{w=0.3}  moving as one unit through the map, covering each other's backs and sharing ammo when it runs low."
    
    "The game's score swells around us—a soundtrack to accompany us victory after victory."
    
    show theo happy
    show dev skeptical
    show elliot considering left:
        easein_cubic 1 xpos 0.68
    with eidissolve_nd
    
    E "Not bad.{w=0.3}  For a human."
    
    show theo cheerful
    show dev happy
    show elliot smug
    with eidissolve_nd
    
    T "Question mark."
    
    stop music
    play sound phone_notification volume 3
    
    show theo skeptical
    show dev surprised
    show elliot shocked:
        shudder(x=0.68)
    with eidissolve_nd
    pause 1
    show elliot annoyeddown with eidissolve_nd
    
    "I hear a ping from Elliot's direction.{w=0.3}  His face sours as he checks his phone."
    
    show theo skeptical
    show dev skeptical
    show elliot annoyeddown right:
        easein_cubic 1.5 ypos 0 xpos 0.75
    with eidissolve_nd
    
    E "Damn it{cps=5}...{/cps}"
    show elliot annoyed left:
        easein_cubic 1 xpos 0.72
    with eidissolve_nd
    extend" I got to leave."
    
    show theo surprised
    show dev neutral
    with eidissolve_nd
    
    T "Now?{w=0.3}  It's like 10pm, where are you going now?"
    
    show theo upsetconsidering
    show dev skeptical
    show elliot annoyedconsidering
    with eidissolve_nd
    
    E "My parents are here."
    
    show theo upset
    show dev neutral
    show elliot angry
    with eidissolve_nd
    
    E "I was hoping to avoid this, but they want to meet up with me before they leave."
    
    show theo sad
    show elliot unimpressed
    with eidissolve_nd
    
    T "Is that why you've been all stressed all day?"
    
    show elliot annoyed with eidissolve_nd
    
    "He doesn't answer, simply shrugging."
    
    show elliot annoyed:
        easein_cubic 3.5 xpos 0.1
    show theo sad:
        easein_cubic 2 xpos 0.4
    show dev neutral:
        easein_cubic 2 xpos 0.65
    pause 0.3
    show theo left
    show dev left
    pause 3.5
    show elliot annoyeddown right
    with eidissolve_nd
    
    E "I'll probably be gone for a few hours, so don't wait up."
    
    show elliot left:
        xpos 0.1
    show elliot at moveoutleft(x=-0.3)
    hide elliot
    with eidissolve_nd
    
    "The door clicks shut behind Elliot, and the room suddenly feels quieter, even with the game's action-packed music still playing in the background."
    
    hide gradient_black
    show theo saddown right:
        easein_cubic 2 xpos 0.38
    with eidissolve_nd
    
    "Theo pauses the game and turns to me,{w=0.3}  his expression shifting from focused to something more thoughtful."
    
    show dev ashamed
    pause 1
    show dev right
    with eidissolve_nd
    
    D "{cps=5}...{/cps} "
    
    play music echoes_of_the_street fadein 3  
    show dev sad left
    show theo sad
    with eidissolve_nd
    
    D "I assume I'm better off not knowing?"
    
    show theo saddown:
        easein_cubic 0.5 ypos 0.08
        pause 0.1
        easein_cubic 0.5 ypos 0.1
    with eidissolve_nd
    
    "Theo shrugs."
    
    show theo sad with eidissolve_nd
    
    T "Family dynamics can be{cps=5}...{/cps} complicated, even more so when your parents are big time CEOs."
    
    show dev ashamed
    show theo ashamed a_upsetconsidering
    with eidissolve_nd
    
    "There is an awkward pause,{w=0.3}  but thankfully Theo fills it in soon enough."
    
    show dev neutral
    show theo neutral
    with eidissolve_nd
    
    T "You know, I've always wanted to make games. Not just play them."
    
    show dev somber
    show theo neutral
    with eidissolve_nd
    
    "I accept the change of topic with a nod."
    
    show dev thinking
    with eidissolve_nd
    
    D "Who hasn't dreamt of making their own game?"
    
    show dev neutral
    show theo thinking t_thunk
    with eidissolve_nd
    
    T "I want to create that next big '\something'\. Not just for fame, but that new mechanic or system that pushes the whole industry, you know?"
    
    show dev skeptical
    show theo neutral
    with eidissolve_nd
    
    "His expression and tone are serious,{w=0.3}  but I can tell it's not because of what happened with Elliot—it might've started as just a change of topic,{w=0.3}  but clearly this is something he really cares about."
    
    show dev happy
    show theo neutralconsidering
    with eidissolve_nd
    
    D "I think I do, yeah."
    
    show theo crossed c_smug:
        rotate_funny(h=0.1, t=5, inv=-2.5)
    with eidissolve_nd
    
    "He leans back against his bed frame,{w=0.3}  arms crossed over his chest as he looks up at the ceiling."
    
    show theo c_surprised
    with eidissolve_nd
    
    T "It's like this big dream I've got."
    
    show dev surprised
    show theo happy:
        resetrotate
    with eidissolve_nd
    
    T "What about you?{w=0.3}  Was making games always just a passing interest, or something more?"
    
    show dev thinking
    with eidissolve_nd
    
    "The question catches me off guard, and I pause for a moment to think."
    
    "Like with so many others, the idea of making my own game has crossed my mind more than once, but I've never stopped to think about why I'd want to make one."
    
    show dev skeptical
    show theo unimpressed
    with eidissolve_nd
    
    D "Honestly, I've never really thought about it."
    
    show dev neutral
    show theo neutral
    with eidissolve_nd
    
    D "It's definitely never been about becoming rich or famous or anything like that{cps=5}...{/cps}"
    
    D "{cps=5}...{/cps} so I guess if I had to say anything, it'd be about the same as you? You know, creating something and leaving a mark in the world? Something lasting{cps=5}...{/cps}"
    
    show theo surprised
    with eidissolve_nd
    
    "Theo's eyes light up, his energy shifting as if he's just downed an entire pot of coffee."
    
    show theo grin with eidissolve_nd
    
    T "{b}Really?{/b}"
    
    "He is practically shouting, nearly knocking over his soda can in his sudden enthusiasm. I nod."
    
    show theo cheerful:
        easein_cubic 0.1 xpos 0.45
    with eidissolve_nd
    
    T "Dude, we should totally do it!"
    
    "The guy can go from zero to sixty in nothing flat!"
    
    show dev somber
    show theo skeptical:
        easein_cubic 2 xpos 0.38
    with eidissolve_nd
    
    D "Whoa, slow down, man."
    
    show dev happy:
        chuckle(y=0.1)
    show theo neutral
    with eidissolve_nd
    
    "I laugh, trying to temper his excitement with a dose of reality."
    
    show theo happy
    with eidissolve_nd
    
    D "I mean, it'd be awesome, but this is a lot to put on someone you just met."
    
    show dev neutral
    show theo skeptical
    with eidissolve_nd
    
    D "Shouldn't you ask Elliot, or someone you know is able to contribute? Even I don't know what I could bring to the table."
    
    show theo neutralconsidering
    with eidissolve_nd
    
    T "We tried before but{cps=5}...{/cps}"
    show theo neutral
    with eidissolve_nd
    extend"nah forget about that, listen!"
    
    show theo happy
    with eidissolve_nd
    
    T "We share the same passion, right? We both love games. We could make something amazing together!"
    
    show dev happy
    show theo grin
    with eidissolve_nd
    
    "I can't help but smile at his conviction.{w=0.3} It's infectious and sort of makes me believe that maybe,{w=0.3} just maybe{w=0.3}, we could pull something like this off."
    
    "And even if not,{w=0.3} it might still be fun."
    
    show dev thinking
    with eidissolve_nd
    
    D "We do have similar interests."

    show dev t_skeptical
    show theo skeptical
    with eidissolve_nd
    
    D "But is that enough to start?"
    
    show dev neutral
    show theo cheerful
    with eidissolve_nd
    
    T "Dude, great games started development with less than that."
    
    show dev sad
    show theo neutral
    with eidissolve_nd
    
    D "But where would we even start{cps=5}...{/cps} What would it even be about?"
    
    show dev thinking
    with eidissolve_nd
    
    D "More importantly, {b}how{/b} would we even make it?"
    
    show dev skeptical
    show theo crossed c_smug
    with eidissolve_nd
    
    T "Don't worry about that, I've been programming since I can remember."
    
    if VTSD:
        show dev thinking t_skeptical
        show theo neutral
        with eidissolve_nd
        D "Well{cps=5}...{/cps} I did make some mods for FS 4. But I wouldn't call myself a programmer."
        show dev neutral
        show theo grin
        with eidissolve_nd
        T "Sweet, man, then this is a match made in Heaven. Don't worry, I'll do the heavy lifting on that end."
    else:
        show dev thinking t_skeptical
        show theo skeptical
        with eidissolve_nd
        D "I knew I should have learned to code for real the first time an internet rando told me to."
        show dev neutral
        show theo happy
        with eidissolve_nd
        T "Haha, I told you, don't worry about that."
    
    show dev neutral
    show theo happy
    with eidissolve_nd
    
    T "All I need to know is {i}what{/i} it is, and I promise I can make it work."
    
    show theo thinking t_thunk
    with eidissolve_nd
    
    T "Which as for what, it could be an epic adventure, or a chill walking sim, or something—anything!"
    
    show theo thinking t_grin
    with eidissolve_nd
    
    T "Those are just details we can figure out along the way."
    
    show theo cheerful
    with eidissolve_nd
    
    "Theo claps his hands together in delight, a grin stretching across his face."
    
    "I lean back and run a hand over my bald head."
    
    "The idea is wild, but how hard could it be?"
    
    stop music fadeout 3
    scene black with Dissolve(3.0)
    
    "Theo continues to rattle off ideas,{w=0.3} barely pausing for breaths between each new thought,{w=0.3} but my mind is too focused on the practical problems to pay them enough attention."
    
    "Eventually it starts to get late,{w=0.3} and I head out,{w=0.3} promising him I'll think about it."
    
    "As I leave Theo's room and walk back towards my own, the halls of CCC are quiet, but given the storm of problems and potential solutions that's raging in my head, that suits me just fine."
    
    show dorm_hallway behind black
    hide theo
    hide dev
    
    "I'm no programmer.{w=0.3} Heck,{w=0.3} I've never designed anything more complex than a custom character in a game's character creator."
    
    hide black with Dissolve(1.0)
    play music halfway_to_home fadein 3
    
    show dev at moveinright(x=0.2, m=0.45, t=10)
    with eidissolve_nd
    
    "And yet,{w=0.3} as I walk down the corridor, my mind races with possibilities and doubts."
    
    show dev sad
    with eidissolve_nd
    
    "Making a game with Theo?{w=0.3} The thought is daunting."
    
    show dev:
        movex(x=0.5, t=20)
    show dev thinking
    with eidissolve_nd
    
    "It's not just about coming up with an idea but building it from scratch, debugging it{cps=5}...{/cps}{w=0.5} Stuff I know nothing about. But Theo seems convinced we can do it."
    
    show dev neutral
    with eidissolve_nd
    
    "It's not completely impossible,{w=0.3} I guess—you do read about a viral hit of a game that's made by one guy every now and then."
    
    "And half of those have graphics that look like a child made them,{w=0.3} and have some royalty free music as its soundtrack, if even that."
    
    show dev:
        movex(x=0.7, t=20)
    
    "If it's both me and Theo then we have, like, twice the chance of success, right?"
    
    "But then there's the time commitment,{w=0.3} the effort. And what if it fails?{w=0.3} What if we spend months on this and nothing comes out of it?"
    
    show dev at moveoutright(x=1.2, m=0.45, t=20) with eidissolve_nd
    scene black with Dissolve(3.0)
    show dormroom_dev_empty_nightlight behind black
    
    "College is already going to be tough enough without adding game development into my schedule."
    
    hide black with Dissolve(1.0)
    show dev at moveinright(x=0.5, m=0.45, t=5)
    
    "I open the door to my dorm and flick on the light.{w=0.3} The room greets me with its emptiness."
    
    show dev sad
    with eidissolve_nd
    
    "I really, really need to get some posters or something{cps=5}...{/cps}"
    
    show dev thinking:
        easein_cubic 5 xpos 0.7
        pause 1
        xzoom -1
        easein_cubic 5 xpos 0.2
        pause 1
        xzoom 1
        repeat
    with eidissolve_nd
    
    "I pace around the room.{w=0.3} Pros and cons begin to ping-pong in my head."
    
    "Pro:{w=0.3} It could be cool working with Theo,{w=0.3} his passion for this is certainly infectious.{w=0.3} His passion for everything is infectious."
    
    "Con:{w=0.3} I've got zero experience.{w=0.3} What if I drag us down?"
    
    "Pro:{w=0.3} If we actually pull this off, it could be amazing—a real achievement."
    
    "Con:{w=0.3} It's risky.{w=0.3} Games flop all the time,{w=0.3} even those made by professionals."
    
    show dev unimpressed:
        easein_cubic 5 xpos 0.5
    with eidissolve_nd
    
    "Man,{w=0.3} college is supposed to be about figuring out your future,{w=0.3} not jumping headfirst into some crazy project on day one."
    
    show dev neutral left
    pause 0.5
    show dev right
    with eidissolve_nd
    
    "I glance at the empty bed on the other side of the room and stare at it for a while.{w=0.3} There's silence.{w=0.3} This late into the night, not even the other students seem to be making much noise at all, and I'm left alone with my thoughts."
    
    show dev ashamed
    with eidissolve_nd
    
    "I'm alone,{w=0.3} period."
    
    show dev somber
    with eidissolve_nd
    
    "Flashes from my brief time with Theo and Elliot appear in my mind.{w=0.3} I realize that in the last 24 hours, I haven't given even one thought to my life before CCC beyond thinking of my parents, my indecision, and hobbies."
    
    show dev skeptical right
    with eidissolve_nd
    
    "Not one name from high school pops up in my head."
    
    show dev sad
    with eidissolve_nd
    
    "{cps=5}...{/cps}"
    
    "I've been alone for a while, haven't I?"
    
    show dev thinking
    with eidissolve_nd
    
    "But not this afternoon.{w=0.3} I wasn't alone with Theo, Elliot, and Rebecca. That was fun."
    
    show dev neutral
    with eidissolve_nd
    
    "Maybe{cps=5}...{/cps}"
    
    "I add another item to the pros and cons list."
    
    show dev happy
    with eidissolve_nd
    
    "Pro: It'd be fun{cps=5}...{/cps}"
    
    show dev neutral
    with eidissolve_nd
    
    scene black with Dissolve(3.0)
    
    "I need to sleep on this.{w=0.3} Maybe things will be clearer in the morning{cps=5}...{/cps} or maybe they'll be exactly the same,{w=0.3} and I'll still have no clue what I'm doing or what I'll want to do."
    
    window hide
    window auto
    
    stop music fadeout 3
    
    scene black with Dissolve(1.0)
    
    pause 5.0
    
    return
    
