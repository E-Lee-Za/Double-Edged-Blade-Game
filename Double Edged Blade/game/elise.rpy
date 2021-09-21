label elisestart:
    #First Year.
    $ currentyear = 1

    scene lsa outside day with fade

    elise "(Summer term at Laurum Secondary Academy...)"
    scene rest of the class with fade
    elise "(Life is rather slow around this time, and not much really goes on, to be honest.)"
    elise "(Sometimes I think I'm just waiting for something to happen.)"

    "Your class' form tutor arrives. You don't pay much mind, but instead wait for your name to be called for attendance."

    als "Good morning everyone! Sorry I'm late- Let's start off with registration, shall we?"
    als "Let's see..."
    "“Catherine?” “Here, Miss.”"
    "“Catia?” “Here, Miss.”"
    "“Antoine?” “Here, Miss.”"
    "The sound of names and responses becomes simple background noise to you."

    "“Elise?”"

    elise "Here, Miss."

    elise "(That's all I have to listen out for.)"
    
    scene blackboard with fade
    show ms alsudo neutral
    als "And that's everyone!"
    als "Now, today, I have some exciting news..."
    als "Tomorrow, a new student is joining our class!"

    elise "(!)"
    elise "(New student...?)"
    elise "(But there's only two weeks of school left...?)"

    show ms alsudo smile
    als "Now, we'll all make him feel welcome, alright?"
    als "That's all the news I have for today. It's time to pack up and go to lessons, have a great day everyone!"

    hide ms alsudo with easeoutright

    elise "(Since a new student is coming...maybe it would be a good idea to meet him...)"
    elise "(...before everyone else does...)"
    
    "You watch as everyone else leaves the room."

    show elise neutraler at left with easeinleft
    elise "Um...Miss?"

    show ms alsudo neutral at right with easeinright
    als "Hello, Elise! Need to ask something?"
    show elise surprise at left
    elise "Uh...yeah...so there's the new student coming in tomorrow..."
    elise "And usually a student gets the job of giving them a tour around the school..."
    elise "So I was wondering..."
    show elise nervous at left
    elise "...could I do the tour?"
    show ms alsudo smile at right
    als "Of course! And thank you for volunteering."
    show elise laughter at left
    elise "Thanks, miss!"
    als "See you later, Elise."
    hide elise with easeoutleft

    scene black with dissolve

    scene lsa outside day with dissolve

    show elise nervous with easeinleft

    elise "Ah...well, I just did that."
    elise "Why did I do that..."
    show elise panic
    elise "I'm not fit to talk to new people..."
    elise "What if I mess up?"
    show elise nervous
    elise "Well...I could just not worry about it."
    elise "That takes less energy to do, anyway."

    scene black with dissolve

    "And so arrives the next day."

    scene blackboard with dissolve

    elise "(Ms Alsudo hasn't arrived yet...)"
    elise "(Maybe she'll forget about the tour thing and I'll not make a fool of myself...)"

    "She arrives."

    elise "(Oh.)"

    show ms alsudo smile
    with easeinleft

    als "Everyone, this is the new student I mentioned yesterday!"
    "She turns towards someone unfamiliar."
    show ms alsudo neutral
    als "Would you like to introduce yourself?"

    show ms alsudo neutral at right
    with ease
    pause 0.5
    show ray nervous
    with easeinleft

    ray "Uh…hello, e-everyone,"
    show ray shy
    ray "Um...my name is Raymond, uh…i-it’s nice to meet you all..."
    ray "And...that’s--that’s all I have to say for now."
    show ray awkward
    als "Thank you, Raymond. Now, let’s see..."
    als "You can go sit next to Elise over there at the back, okay?"

    elise "(O h .)"

    hide ray with easeoutleft

    show awkward with fade

    als "Right, now that’s sorted, we can start with the register."

    "The teacher starts to call the register."
    "“Catherine?” “Here, Miss.”"
    "“Catia?” “Here, Miss.”"

    elise "(Alright. New person. Right next to me.)"
    elise "(Now, I could try to strike up a conversation...)"
    elise "(...ehhh, but pretending not to notice him is a lot less risky...just don’t look up...)"
    show awkward2
    ray "Hi."

    elise "(Ah, great.)"
    elise "(How are you supposed to do this…? Uh...)"
    elise "H-hi…"
    hide awkward2
    "You continue sketching, trying not to look up."

    elise "(Oh my goodness, I said that awkwardly...)"

    "“Johanna?” “Here, Miss.”"
    show awkward2
    ray "That’s a nice drawing you’re making."

    elise "O-oh...thank you."

    ray "It looks like a pair of wings!"

    elise "Well,uh...y-yes, it is...just some plans for something…"

    ray "Oh, what are you planning?"

    elise "(No...if I tell him what it is he’ll probably think it’s weird...)"
    elise "N-nothing important…(!)"
    hide awkward2
    "“Johanna?” “Here, Miss.”"
    "“Antoine?” “Here, Miss.”"
    elise "(Come on, get it together...what happened to 'getting to know someone new'?)"

    menu:
        "Attempt conversation":
            show awkward3
            "You place your pencil onto the table."
            elise "(Alright, let's try it.)"
            show awkward4
            elise "So uh...what did you say your name was?"

            "“Raymond?”"

            ray "Here, Miss."

            elise "Ah, nice to meet you, Raymond. My name is-"

            "“Elise?”"

            elise "Here, Miss."

            ray "A pleasure to meet you too, Elise."

            elise "(Hey, that worked!)"
        
        "Stay quiet":
            "..."
            "“Raymond?”"

            ray "Here, Miss."

            "“Elise?”"

            elise "Here, Miss."

    als "Right, now that’s sorted, Maribel, can you take this to the office, please?"

    "A student stands up to take the clipboard to the office. The class resumes its chatter."

    als "Raymond? Elise? Please can you come up here for a bit?"

    elise "(I guess she didn't forget. Ah...it's okay.)"
    "You and Raymond walk over to the teacher."
    
    scene blackboard with dissolve
    show ms alsudo neutral at right
    pause 0.5
    
    show elise neutraler with easeinleft:
        xalign 0.25

    show ray neutral at left with easeinleft
    pause 0.5

    als "Elise, you volunteered yesterday to show the new student around, right?"
    als "You can do that now, if you’d like."
    
    elise "Yes, I think we’ll do that now, Miss."

    als "Alright, you two can go around the school, just make sure to be back here before the end of form-time."

    show ray laughter at left
    
    show elise nervous:
        xalign 0.25
    "Raymond and Elise" "Thanks, Miss!"

    "The two of you walk outside of the classroom."

    show ray at offscreenleft
    show elise at offscreenleft
    with ease
    
    scene black with dissolve
    pause 0.5
    stop music fadeout 0.5
    queue music ["audio/who-is-this-stranger.mp3", "audio/stranger-piano.mp3"] loop
    scene firstyear with dissolve
    pause 2.1
    show firstyearbegins
    pause 1.5
    scene black with dissolve
    scene courtyard1 with dissolve
    show elise neutral at right
    show ray neutral at left
    with ease

    elise "So this is the Courtyard, where we all hang around outside of lesson time."
    elise "It’s usually quite easy to get to class from here, so there’s little chance of being late."

    show ray at offscreenleft
    show elise at offscreenright
    with ease

    "Click on a door to go towards it."

    call screen tourCourtyardE()

label tourArtE:
    scene artroom
    show elise neutral with easeinleft:
        xalign 0.25
    show ray neutral at left with easeinleft
    elise "This is the art studio, where our art lessons are. I come here quite often, I like drawing."
    show ray smile at left
    ray "You’re quite good at it too."
    show elise laughter:
        xalign 0.25
    elise "Why, thank you!"
    show elise neutral:
        xalign 0.25
    show mrs sketch neutral with easeinright:
        xalign 0.75
    show mr sketch smile at right with easeinright
    gary "Hello, Elise! Showing around a new student, are you?"
    show elise confident:
        xalign 0.25
    elise "Indeed I am!"
    ray "H-hi, nice to meet you!"
    show mrs sketch smile:
        xalign 0.75
    jodie "Lovely to meet you too. We’ll see you both in art class, okay?"
    show elise laughter:
        xalign 0.25
    elise "Okay, bye!"
    show ray at offscreenleft
    show elise at offscreenleft
    with ease

    scene black with dissolve

    $ seenArtE = True
    if not seenDtE:
        call screen tourCourtyardE()

    if seenDtE and seenArtE:
        scene courtyard2
        call screen tourCourtyard2E()


label tourDtE:
    scene workshop
    show ray smile with easeinleft:
        xalign 0.25  
    show elise neutral with easeinleft:
        xalign 0.5
      
    elise "These are the workshops, where we have our engineering classes, my favourite subject!"
    ray "Wow, I didn't have this while homeschooling…"

    show mr silversaw neutral at left
    with easeinleft

    silversaw "Ah, hello, Elise! Nice to see you again. Who’s your new friend?"
    show elise confident:
        xalign 0.5
    elise "Hi, Mr Silversaw! This is Raymond, he’s joining our class!"
    show ray smile:
        xalign 0.25
    ray "Uh...hello!"
    show mr silversaw laughter at left
    show elise neutral:
        xalign 0.5
    silversaw "Nice to meet you, Raymond. I think we have a workshop class today, I’m looking forward to seeing you both there."
    show mr silversaw neutral at left
    silversaw "Oh, and Elise, is your plan for your project finished?"
    show elise laughter:
        xalign 0.5
    elise "Yep! Just adding a couple more notes and it’ll be done."
    show mr silversaw laughter at left
    silversaw "Excellent!"
    show elise neutral:
        xalign 0.5
    show mr silversaw smile at left
    silversaw "Well now, I suppose you still have places to see, yes?"
    show elise laughter:
        xalign 0.5
    elise "Ah, that’s right! I’ll see you later, Sir!"

    scene black with dissolve

    $ seenDtE = True
    if not seenArtE:
        call screen tourCourtyardE()
    
    if seenDtE and seenArtE:
        scene courtyard2
        call screen tourCourtyard2E()

label tourLibraryE:
    show elise neutral at right
    show ray neutral at left
    elise "Over there's the library. If you're looking for info on basically anything, it's probably in there."
    show ray smile at left
    ray "That'll come in useful, I'm sure."

    call screen tourCourtyard2E()
    

label tourTheatreE:
    show elise neutral at right
    show ray neutral at left
    with ease
    elise "And that's the Theatre building."
    elise "There's some classrooms in there, and the theatre's upstairs..."
    show elise surprise at right
    elise "...except it's closed off for renovations right now, so I don't think we can go in there."
    show elise neutraler at right
    ray "Ah, that's too bad."
    ray "Speaking of which...should we head back to form now?"
    show elise nervous at right
    elise "...Yes, probably should."
    show ray neutral at offscreenleft
    show elise neutral at offscreenright
    with ease
    scene black with dissolve
    jump firstcontinuedE

label firstcontinuedE:
    scene blackboard with dissolve
    show ms alsudo neutral at right
      
    show elise neutral with easeinleft:
        xalign 0.25
    
    show ray smile at left with easeinleft

    als "Ah, you’re back! How was it?"
    ray "It was pretty good,"
    show ms alsudo smile at right
    als "Lovely! I hope you’ll enjoy your time here. Also, thank you, Elise, for volunteering, you've done a good job."
    show elise laughter:
        xalign 0.25
    elise "(I did a good job!)"
    elise "Thank you, Miss."
    hide ray with easeoutleft
    hide elise with easeoutleft
    "Ms Alsudo turns to the rest of the class."
    show ms alsudo neutral at center with ease
    als "Alright everyone, it’s time to pack up and go to your first lessons, have a great day everyone, and I’ll see you in PM registration!"
    hide ms alsudo with easeoutleft

    #add comic-style background here- i'll draw this later

    "You and Raymond collect your bags and head off to your first lesson. Your class timetables are nearly identical."
    scene black with dissolve
    "The rest of the day continues pretty normally, as you would expect."
    
    scene courtyard1 with dissolve
    "Lunchtime rolls around, and you suddenly remember something you had to attend to."
    "So you hastily pack your things and run to the workshop."

    scene workshop with fade

    show mr silversaw smile at right

    silversaw "Good afternoon, Elise! You look a little worn out, did you run all the way here?"
    show mr silversaw neutral at right
    show elise tired at left with easeinleft

    elise "Hah...hello, Sir...yeah, I did..."

    show elise nervous at left

    elise "Just...trying to maximise the time I have to work on this project!"

    show mr silversaw sadsmile at right

    silversaw "Hahah, smart idea! But don't tire yourself, okay?"

    elise "Okay...!"

    show mr silversaw smile2 at right

    silversaw "Good, good!"
    show elise neutraler at left
    show mr silversaw neutral at right

    silversaw "So, did you finish your sketch?"

    show elise laughter at left
    elise "Yep! I've brought it with me."

    "You reach into your bag for your sketch."
    "Looking past all of your books, that one piece of paper is not in sight."
    show elise nervous at left
    elise "Uh..."
    show mr silversaw sadsmile at right
    silversaw "Worry not, take your time."

    elise "It is…right here…"

    "You cannot find what you are looking for."
    show elise neutraler at left
    elise "Well…that’s strange."

    silversaw "Misplaced it?"

    elise "I’m sure I put it in here…"

    show mr silversaw neutral at right
    silversaw "Oh, look, Elise, some friends have come to pay a visit!"

    "You look up. Raymond is there with one of your other classmates, Johanna, who is holding a familiar piece of paper."
    show elise surprise at left
    elise "Oh- hi!"
    show elise neutraler with ease:
        xalign 0.75
    show johanna neutral with easeinleft:
        xalign 0.25
    show ray neutral at left with easeinleft

    johanna "Hey, Elise! Raymond and I just came to give you this- you left it behind in form time."

    "Johanna hands you your sketch."
    show elise surprise:
        xalign 0.75
    elise "I thought I had left it somewhere...thanks!"
    show johanna laughter:
        xalign 0.25
    johanna "Of course! Hey, y’know, this thing you’re working on, looks really cool too."
    show elise neutraler:
        xalign 0.75
    show johanna neutral:
        xalign 0.25
    "You glance back at the various broken parts of what were meant to be a pair of mechanical wings."
    show elise nervous:
        xalign 0.75
    elise "Heh, thanks...well, if I could get it to work…"
    show elise neutral:
        xalign 0.75
    
    show ray smile at left
    ray "Ah, this is what you were sketching in class."
    show elise nervous:
        xalign 0.75
    elise "I’d tried to test this out the other day...all fell apart."
    show elise neutraler:
        xalign 0.75
    show mr silversaw laughter at right
    silversaw "But you went back to your design, made a few amendments…"
    show mr silversaw neutral at right
    elise "Yep. I think I worked out the problem with this...I hope."
    show ray neutral at left
    ray "How long have you been trying to make it for?"
    show elise surprise:
        xalign 0.75
    elise "I started this a couple months ago, I think."
    show elise neutraler:
        xalign 0.75
    silversaw "Your improved design looks a lot better, we’ll start on it on Thursday. Lunchtime is almost over, so you should get back to class now."
    show elise laughter:
        xalign 0.75
    elise "Ah, it’s that time already, see you later, Sir!"
    johanna "See you!"
    show ray smile at left
    ray "Bye!"
    show mr silversaw laughter at right
    silversaw "Good day, all of you!"
    "You, Raymond and Johanna leave the workshop."
    hide ray
    hide elise
    hide johanna
    with easeoutleft

    scene black with dissolve
    "It’s now time to go home."
    scene left folder with dissolve
    "You're packing your things, when you realise something is not where it should be."
    elise "Ah, great, I left my folder in the workshop…"
    ray "We can quickly go and get it…"
    show it wont take long1 with dissolve
    "Outside the window, the rain is now quite heavy."
    show it wont take long2 with dissolve
    ray "...it won’t take long."
    scene courtyard1 rain with dissolve
    "The two of you run through the rain into the workshop classroom."
    scene workshop dark with dissolve
    "Looks like Mr Silversaw has already left for the day. You see a folder on one of the workbenches."

    elise "There it is!"
    scene drops papers with dissolve
    "You pick up your folder, at which point a strong breeze blows some loose papers out from it and scatters them on the floor, some sliding underneath the tool cupboard door."
    "You both pick up the pages scattered around, but when you get the one in the cupboard…"
    show black with dissolve
    stop music fadeout 1
    pause 1
    show door closes1
    pause 1
    show door closes2
    "The strong wind blows again, and slams the cupboard door shut, with both of you inside."

    pause 0.5

    play music "audio/brushed-under-the-carpet.mp3"

    elise "What was that-what was that?!"
    show black
    "Attempts to open the door prove futile."
    scene help with dissolve
    ray "Is anyone out there?! We’re trapped!"

    elise "Oh, Raymond, what do we do?"
    scene black with dissolve
    elise "The lights have been broken for a while...and it's dark..."
    scene trapped1 with dissolve
    ray "Well, in that case, I have just the thing for this situation…"
    
    "He pulls out a box of matches."

    elise "Why...why do you have those??"

    ray "You never know when you’ll need them."

    elise "You’re not going to start a fire, are you?"
    show trapped2 with dissolve
    "He lights the match."

    ray "Only a tiny one."

    "The two of you sit down, watching the flickering flame of the match."

    ray "Well, now...worst case scenario, perhaps Mr Silversaw will find us in the morning?"

    elise "He teaches part-time, so he won’t be in tomorrow."

    ray "Ah. There goes that idea."
    ray "Hmm, oh, well...."

    "You sit together in silence."
    "…"

    elise "(Did this have to happen?)"
    elise "(At this time?)"
    elise "(In a storm, too...it's dark...and nobody's around to get us out...)"
    show trapped3
    "The match goes out."
    "You’re in darkness for a few moments."
    pause 1
    show trapped4
    pause 0.5
    scene trapped1
    
    elise "AHH-! What was- what was-?!"

    ray "It’s just the storm outside. It’s alright, don’t worry-"
    scene black with dissolve
    scene she panic1 with dissolve
    elise "I’m scared, Raymond! What if something happens to us in here?!  What if nobody finds us? What if we don’t get out?"
    scene she panic1 with dissolve
    elise "I...I don't..."
    elise "(I can't...)"
    elise "(...think...my head hurts, and everything feels like ringing...it feels loud...)"
    ray "Elise, please, calm down!"
    ray "What is happening here?!"
    "You look up."
    show elisemagic1 at fading
    elise "What’s that?! What’s happening?!"
    show elisemagic2 at fading
    ray "Are you doing this?"
    elise "I don’t know!"
    ray "Can we put them down?"
    "As soon as he says that, a red glow appears to counter the blue, dropping all of the tools onto the floor."
    scene raymagic with dissolve
    elise "I mean, that works?"
    ray "Was that me?"

    elise "We can try that again…"
    elise "(Unwise.)"

    show black at fading
    show tryitray at fading
    "He gestures his hand upwards. A small blade appears in front of him, and flies forward into the wall."

    ray "Wow…"
    show tryitelise at fading
    "You try the same, but your blade flies backwards, almost hitting you."

    ray "We’d better be careful."
    
    elise "What do we do with this knowledge?"

    scene cupboard with dissolve

    ray "Perhaps...we can find a way out."

    "Try clicking some of the tools, to find a way out."

    call screen cupboardE()

label screwdriverE:
    "You try to pick the lock open."
    "It doesn't work."
    "The door is quite stuck in its place."
    call screen cupboardE()

#label lightswitchE:
#    "The light switch is broken."
#    call screen cupboardE()

label escapecupboardE:
    "You notice the knife lodged into the wall, and an idea pops into your head."
    
    elise "We can destroy the lock."
    elise "With what we just tried with all those blades..."
    scene breakout1 with dissolve
    elise "Though, I doubt how safe this is..."

    ray "It’s about as safe as freezing to death in a cupboard during a storm."

    show breakout2 at fading
    pause 1
    show black
    pause 2
    scene breakout3 with dissolve
    pause 3
    scene breakout4 with dissolve

    show elise surprise at right
    show ray neutral at left
    with ease

    elise "Huh, that worked! That actually worked!"
    show ray laughter at left
    ray "No more freezing to death in a cupboard during a storm!"
    show ray neutral at left
    show elise neutraler at right
    "You look down at the pile of broken wood, which was once the door."

    ray "Except...what do we do with that?"
    show elise surprise at right
    elise "We can explain that later. Let’s get out of here."
    show ray at offscreenleft
    show elise at offscreenright
    with ease
    scene black with dissolve
    "You both run through the rain, to the school gate. It’s now dark outside."
    scene lsa outside night

    ray "Well...that was interesting."

    elise "Hahaha! Well, not to worry, this won’t be a regular occurrence, I’m sure."
    ray "Yes, definitely."
    elise "Well, we’d better get going, before our parents worry too much."
    elise "See you tomorrow!"
    ray "See you tomorrow, Elise."

    scene black with dissolve
    pause 1

    "You arrive home. Your mother has been waiting for you."
    scene realismanorwallpaper with dissolve
    sara "My, you’ve come home late, Elise."
    show elise nervous with easeinleft
    elise "I was just working on my project in the workshop."
    sara "This late?"
    show elise neutraler
    elise "...yes."
    "Your mother gives you a puzzled look."
    sara  "Are you alright, Elise?"
    show elise tired
    elise "Yes, I’m fine."
    elise "Just a little tired. I think I’ll go to bed early tonight."

    stop music fadeout 1
    scene black with dissolve

    elise "(I feel unusually tired...this doesn't happen...)"
    elise "(I don't even have the energy to think anymore...)"

    scene breakout1 with dissolve

    "By now you've probably noticed the number in the corner of your screen, labelled 'Control'."
    "The higher it is, the more control you have over your powers, and vice-versa."
    "It increases when you feel calmer, and decreases when you aren't."
    "If it hits zero, you’ve completely lost control for good, and the game is over."
    "Keep it up and you’ll survive. Good luck."

    scene black with dissolve

    queue music ["audio/stranger-piano.mp3", "audio/who-is-this-stranger.mp3"] loop

    "It's the last week of school and today, there’s a school trip to the History Museum in the city."
    scene museum with dissolve
    show ms alsudo neutral with easeinright
    als "Okay, everyone, here we are, Scholite University History Museum!"
    als "In here you’ll find a lot to learn about the Regions on this island, and about the city, too."
    als "Now, we’ll split into two groups and you can explore around a bit."
    als "Let’s see…"
    hide ms alsudo with easeoutleft

    show ray neutral at left with easeinright
    als "Raymond..."
    show catherine neutral with easeinright:
        xalign 0.25
    als "Catherine..."
    show maribel neutral with easeinright
    als "Maribel..."
    show fritz neutral with easeinright:
        xalign 0.75
    als "and Fritz..."
    als "That's one group, and..."

    hide ray
    hide catherine
    hide maribel
    hide fritz
    with easeoutleft

    show elise neutral at right with easeinleft
    als "Elise..."
    show catia neutral with easeinleft:
        xalign 0.75
    als "Catia..."
    show antoine neutral with easeinleft
    als "Antoine..."
    show johanna neutral with easeinleft:
        xalign 0.25
    als "and Johanna..."
    als "In the other group."

    hide elise
    hide catia
    hide antoine
    hide johanna
    with easeoutright

    show ms alsudo smile with easeinright

    als "Alright, everyone, you’re free to look around, and we’ll meet back here at two o’clock."
    als "Enjoy!"

    hide ms alsudo with easeoutleft

    "Try clicking on the displays."

    call screen museumE()

label royalportraitsE:
    scene royalportraits with dissolve

    pause 3

    show elise neutral with easeinleft:
        xalign 0.25
    show catia neutral at left with easeinleft
    show johanna neutral with easeinright:
        xalign 0.75
    show antoine neutral at right with easeinright

    show elise surprise:
        xalign 0.25
    elise "Hey...that's my mother!"
    show elise neutraler
    show johanna neutral:
        xalign 0.75
    johanna "I almost thought that was you for a minute..."

    show catia smile at left
    catia "I thought you looked similar!"
    show catia neutral at left
    show antoine smile at right
    antoine "And that must be the Pseudeland Region's family on the left."
    show antoine neutral at right
    antoine "I wonder why the Etceter Region doesn't have a portrait? They're a part of this Isle too..."

    scene black with dissolve
    scene museum with dissolve
    call screen museumE()

label mapofscholiteE:
    scene mapofscholite with dissolve
    pause 3
    show elise neutral with easeinleft:
        xalign 0.25
    show catia neutral at left with easeinleft
    show johanna neutral with easeinright:
        xalign 0.75
    show antoine neutral at right with easeinright
    show elise laughter:
        xalign 0.25
    elise "Oooh, I can see where my home is on here! Realis!"
    antoine "And there’s our school, up in north Scholite City."
    show johanna surprise:
        xalign 0.75
    johanna "The Isle of Scholite seems so much bigger when you look at it as a whole..."
    scene black with dissolve
    scene museum with dissolve
    call screen museumE()

label sworddisplayE:
    scene sworddisplay with dissolve
    pause 3

    show elise neutraler with easeinleft:
        xalign 0.25
    show catia neutral at left with easeinleft
    show johanna neutral with easeinright:
        xalign 0.75
    show antoine neutral at right with easeinright

    johanna "They’re pretty well-polished, for having been here so long."
    catia "Shiny. And sharp."
    elise "(Sharp…very sharp.)"
    "Pay no attention to the sinking feeling inside of you."
    $ control -= 5
    antoine "Looks like it’s time to head back."
    "The clock has turned to 2 o’clock."

    scene black with dissolve
    scene museum with dissolve

    show ms alsudo smile with easeinright
    als "Alright, everyone, looks like you all found that interesting!"
    show ms alsudo neutral
    als "However, we’ll have to get going quickly, before we miss the train home."
    scene black with dissolve
    scene street with dissolve

    "You try to stay with the group and not get left behind."
    "…"
    "You somehow ended up a bit behind."
    "Looking behind you, there appears to be a sword from that display, now on the ground at the museum entrance."

    elise "(How did that…why…??)"

    "As the thought crosses your mind, a blue glow appears around the sword."
    "It flies right at you."

    show sword at flyfastleft
    pause 0.2

    $ control -= 10

    "You start running at full speed to the train station."
    scene trainstation day with dissolve

    "The class is already there, and the train has already arrived."

    "Looking behind you, the sword has now cloned itself into three."

    "You see Raymond standing at quite a distance from the group."

    elise "aaaaaaaaaaaaaaaAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA-"
    show elise panic at run
    pause 0.2
    show sword at flyfastleft
    pause 0.2
    show sword at flyfastleft
    pause 0.2
    show sword at flyfastleft

    show ray confused at right with easeinright
    ray "What happened??"
    show elise surprise at left with easeinleft
    elise "I don’t know, I looked behind me after you went ahead with the group, and there were three swords rushing at me with full speed!"
    show ray ohheck at right
    ray "Oh, goodness…"
    show ray neutral at right
    show elise neutraler at left
    elise "We should put these back where they belong."

    show sword at flyfastright

    show elise nervous at left
    elise "There, that should do it."
    show ray ohheck at right
    ray "Uh....where did everyone else go?"
    show elise neutraler at left
    show ray neutral at right
    "You notice that the train has left without you."
    show elise panic at left
    elise "We lost the group?! We lost the group!"
    show ray ohheck at right
    ray "Well, darn. How do we get back?"
    elise "Use the train??"
    ray "Yes, but..."
    ray "...which side of the platform did they get on?"
    elise "Uhh....there's a map? Do you know how to read train maps?"
    ray "Nope."
    show elise neutraler at left
    elise "I...suppose we’ll have to guess."
    elise "Eastbound or westbound train?"

    menu: 
        "Eastbound train":
            ray "Try the eastbound train?"
            scene train day with dissolve
            "You both board the train."
            "Now we wait."
            
            "The next station comes, and you get off the train."
            scene trainstation evening with dissolve
        
            elise "There they are!"
                
            "They’re near the platform."
                
            als "One, two, three, four, five, six…"

            "Ms Alsudo looks your way."

            als "...seven, eight. Alright, that’s everyone."

            ray "(That was almost a disaster...)"

        "Westbound train":
            
            ray "Try the westbound train?"
            
            "You both board the train."
            scene train day with dissolve
            "Now we wait."
            "The next station comes, and you get off the train."
            scene trainstation evening with dissolve
            elise "Uh….where are we?"

            ray "No sign of anyone here at all."
            
            elise "Try the other way?"

            "You board the other train."

            scene train evening with dissolve

            "The train is taking a long time."

            "You look outside. The city is unfamiliar."
            
            ray " Have you ever been here before?"

            elise "Nope."

            "In an unfamiliar place like this, you start to feel a little uneasy."

            $ control -= 10
        
            "The view outside now looks different."

            "It'll be late soon."

            ray "Wait, I usually pass by this station when coming back from school!"

            "!!"

            elise "You know the way from here?"

            ray "It's this station."

            "You leave the train and go upstairs to the station."
            scene trainstation evening with dissolve
            "The class is there."

            show ms alsudo surprise at right with easeinright
            als "You’re here! Where did you both disappear to??"
            show elise nervous with easeinleft:
                xalign 0.25

            show ray awkward at left with easeinleft
            elise "Uh...we kinda missed the train and had to catch up…"
            show ms alsudo neutral at right
            als "Well, as long as you’re here now, it’s alright."

            scene black with dissolve

    "The group returns to the school."

    scene lsa outside night with dissolve
    show elise neutral at right
    show ray smile at left
    with ease

    elise "So...last day of school in a couple more days."
    elise "Will you be in for that?"
    show ray neutral at left
    ray "Probably not...my parents are going out of the Isle for a week, and they don’t want me going out while they’re not home."
    show elise nervous at right
    elise "Ah...oh, well."
    show elise neutral at right
    elise "I suppose I’ll see you in September?"
    show ray smile at left
    ray "Indeed."
    show ray laughter at left
    ray "And, if you’re travelling near the Pseudeland region, maybe you’ll find me, hahah!"
    show elise confident at right
    elise "Ahah, maybe I will!"
    show elise laughter at right
    show ray smile at left
    elise "Well, anyway...bye for now."
    show elise neutral at right
    elise "And...stay safe."
    ray "You too, Elise."

    hide ray with easeoutleft

    show elise neutraler at right
    elise "(Stay safe?)"
    stop music fadeout 1
    scene black with dissolve
    elise "(Easier said than done.)"

    "Pay it no mind."

    scene end first elise with dissolve

    elise "(But some things are much more difficult to ignore.)"
    elise "(If I don't think about it, it'll go away, won't it?)"
    elise "(Won't it?)"

    scene black with dissolve

    "End: First Year."  

    $ currentyear = 1.5

    jump devmessage