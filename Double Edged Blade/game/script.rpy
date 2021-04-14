# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define ray = Character("Raymond", color="#990000")
define als = Character("Miss Alsudo", color="#ff0033")
define elise = Character("Elise", color="#000066")
define saw = Character("Mr Silversaw", color="#005522")
define jodie = Character("Mrs Sketch", color="#ff0066")
define gary = Character("Mr Sketch", color="#993366")
define johanna = Character("Johanna", color="#806dd5")


# The game starts here.

label start:
    

    play music "audio/first-prologue.mp3" fadeout 1

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    scene black

    ray "(Well, this is the place.)"

    scene outside
    with fade

    ray "(The Laurum Secondary Academy, according to what Father said, it’s the most exclusive private school in all the lands...)"
    ray "(...where nobility and royals like myself are educated.)"

    scene ray and alsudo

    ray "(Huh, so this is what a proper school is like.)"
    ray "(Well, it’s very much different from the study we have at home.)"

    als "And this is where you and the rest of your class come to be registered, every morning and afternoon."
    als "How about we go and meet your new classmates?"

    ray "(Ah, that’s the thing about proper schools...)"
    ray "(There’s other kids here too.)"

    scene blackboard

    show miss alsudo smile
    with dissolve

    als "Everyone, this is the new student I mentioned yesterday!"

    "The whole class and the teacher look your way."

    show miss alsudo neutral

    als "Would you like to introduce yourself?"

    show miss alsudo neutral at left
    with ease

    show ray nervous
    with easeinright

    ray "Uh…hello, e-everyone,"

    show ray awkward

    ray "Um...my name is Raymond, uh…i-it’s nice to meet you all...."
    ray "And...that’s--that’s all I have to say for now."

    scene class

    ray "(Oh yes, very smooth indeed, you fool.)"
    ray "(That’s one way to make a first impression. Just wait until they find your full title. Then you're really in for it.)"

    als "Thank you, Raymond. Now...let’s see..."
    als "You can go sit next to Elise over there at the back, okay?"
    
    "You look over to see a girl sitting alone in the back row. She looks up at the mention of her name."
    "You go to sit next to her. You notice she’s sketching something on a piece of paper."

    als "Right, now that’s sorted, we can start with the register."

    "The teacher starts to call the register."
    als '“Catherine?” “Here, Miss.”'
    als '“Casper?” “Here, Miss.”'

    scene awkward silent stares

    ray "(Well, there’s someone right here.)"
    ray "(What am I supposed to do? Say something?)"
    ray "(Maybe I should just...)"
    ray "Hi."

    "The girl looks up, seemingly a little startled."

    elise "H-hi…"

    "She continues sketching, while glancing at you occasionally."

    ray "(She looks a little anxious. Should I say something or stay quiet?)"

    menu:

        "Say something":

            ray "(What can I say to start a conversation…?)"
            ray "That’s a nice drawing you’re making."

            elise "O-oh...thank you."

            ray "It looks like a pair of wings!"

            elise "Well-uh...y-yes, it is...just some plans for something…"

            ray "Oh, what are you planning?"

            elise "N-nothing important…(!)"

            ray "(I think I might have made her even more nervous than before...darn.)"
            
            als '“Antoine?” “Here, Miss.”'

            "The two of you are silent for a while, listening to all the names of other classmates, waiting for your own."
            "You notice the girl glancing at you a little more, before placing her pencil onto the table."

            "She turns to face towards you."

            elise "So uh...what did you say your name was?"

            als 'Raymond?'

            ray 'Here, Miss.'

            elise 'Ah, nice to meet you, Raymond. My name is-'

            als "Elise?"

            elise "Here, Miss."

            ray "A pleasure to meet you too, Elise."

            ray "(The nervous smile on your face tells me that you’re trying your best.)"
            ray "(I admire that.)"


        "Stay quiet":
            "..."
            
            als '“Johanna?” “Here, Miss.”'
            als '“Antoine?” “Here, Miss.”'
            
            ray '(Alright then, Ray. Stay in this awkward silence you’ve brought upon yourself.)'

            "The two of you are silent for a while, listening to all the names of other classmates, waiting for your own."

            als "Raymond?"
            
            ray "Here, Miss."
            ray "(Darn. I can see the whole class looking at me.)"

            als "Elise?"
            
            elise "Here, Miss."

            ray "(I think that’s everyone.)"

    als "Right, now that’s sorted, Maribel, can you take this to the office, please?"

    "A student stands up to take the clipboard to the office. The class resumes its chatter."

    als "Raymond? Elise? Please can you come up here for a bit?"

    scene blackboard

    show miss alsudo neutral at right
    
    
    show elise neutral with easeinleft:
        xalign 0.25
    


    show ray smile at left with easeinleft



    "You and Elise walk over to the teacher."

    als "Elise, you had volunteered yesterday to show the new student around, right?"
    als "You can do that now, if you’d like."

    elise "Sure, I think we’ll do that now, Miss."

    als "Alright, you two can go around the school, just do make sure to be back here before the end of form-time."

    show ray laughter at left
    
    show elise laughter:
        xalign 0.25
        


    "Raymond and Elise" "Thanks, Miss!"

    "The two of you walk outside of the classroom."

    scene black
    with fade

    play music "audio/blessing.mp3" fadein 1

    scene first placeholder
    with fade

    pause 3
    
    scene courtyard1
    with fade

    show elise neutral at right

    show ray neutral at left

    elise "So this is the Courtyard, where we all hang around outside of lesson time."
    elise "It’s usually quite easy to get to class from here, so there’s little chance of being late."

    hide ray with easeoutleft
    hide elise with easeoutright

    "Click on a building to go towards it."

    call screen tourCourtyard()

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.

    # This ends the game.

    return

label tourArt:
    scene jodie and gary introduced
    elise "This is the art studio, where our art lessons are. I come here quite often, I like drawing."
    ray "You’re quite good at it too."
    elise "Why, thank you!"  
    gary "Hello, Elise! Showing around a new student, are you?"
    elise "Indeed I am!"
    jodie "How lovely. We’ll see you in art class, okay?"
    elise "Okay, bye!"

    
    $ seenArt = True
    if not seenDt:
        call screen tourCourtyard()

    if seenDt and seenArt:
        scene courtyard2
        call screen tourCourtyard2()


label tourDt:
    scene workshop
    show ray smile with easeinleft:
        xalign 0.25  
    show elise neutral with easeinleft:
        xalign 0.5
      
    elise "These are the workshops, where we have our design and engineering classes, my favourite subject!"
    ray "Wow, I never would have been taught this in homeschooling…"

    show mr silversaw neutral at left
    with easeinleft

    saw "Ah, hello, Elise! Nice to see you again. Who’s your new friend?"
    show elise smile:
        xalign 0.5
    elise "Hi, Sir! This is Raymond, he’s joining our class!"
    show ray smile:
        xalign 0.25
    ray "Uh...hello!"
    show mr silversaw laughter at left
    show elise smile:
        xalign 0.5
    saw "Nice to meet you, Raymond. I think we have a workshop class today, I’m looking forward to seeing you both there."
    show mr silversaw neutral at left
    saw "Oh, and Elise, is your plan for your project finished?"
    show elise laughter:
        xalign 0.5
    elise "Yep! Just adding a couple more notes and it’ll be done."
    show mr silversaw laughter at left
    saw "Excellent!"
    show elise neutral:
        xalign 0.5
    show mr silversaw smile at left
    saw "Well now, I think it’s almost time you both returned to your form room, yes?"
    show elise laughter:
        xalign 0.5
    elise "Ah, that’s right! I’ll see you later, Sir!"

    
    $ seenDt = True
    if persistent.seenArt == False:
        call screen tourCourtyard()
    
    if seenDt and seenArt:
        scene courtyard2
        call screen tourCourtyard2()

label tourPond:
    show elise neutral at right
    show ray neutral at left
    elise "That’s the pond, it’s very peaceful, isn’t it?"
    show ray smile at left
    ray "Indeed it is…"
    
    ray "...how many times do you suppose someone’s fallen into there?"
    show elise laughter at right
    elise "Hahaha! That’s happened at least once...luckily the water is shallow!"

    call screen tourCourtyard2()
    

label tourTheatre:
    scene corridor placeholder
    elise "This building has a bunch of classrooms, including our form room, and upstairs…"
    scene theatre placeholder
    elise "...is the school theatre! Many shows and events have taken place here."
    ray "Woah, what it must be like to perform here...in front of so many people…"
    elise "Ahah...I could never do that."
    ray "Neither would I."
    "…"
    ray "Should we head back to form?"
    elise "Yes, probably should."

    scene black
    with fade

    scene blackboard
    with fade

label backInForm:

    show miss alsudo neutral at right
      
    show elise neutral with easeinleft:
        xalign 0.25
    
    show ray smile at left with easeinleft

    als "Ah, you’re back! How was it?"
    ray "It was pretty good,"
    show miss alsudo smile at right
    als "Lovely! I hope you’ll enjoy your time here. Also, thank you, Elise, for volunteering, you've done a good job."
    show elise laughter:
        xalign 0.25
    "Elise smiles shyly."
    elise "Thank you, Miss."
    hide ray with easeoutleft
    hide elise with easeoutleft
    "Ms Alsudo turns to the rest of the class."
    show miss alsudo neutral at right
    als "Alright everyone, it’s time to pack up and go to your first lessons, have a great day everyone, and I’ll see you in PM registration!"
    
    scene black
    with fade

    #add comic-style background here- i'll draw this later

    "You and Elise collect your bags and head off to your first lesson. Your class timetables are nearly identical."

    "The rest of the day continues pretty normally, as you would expect."
    "You’re both still very quiet, occasionally asking one another for a bit of help."
    "Also, may I say, good job on having not broken your glasses yet."


    ###start the next scene plz

    scene notyet

    "Now it's lunchtime, and you're in the Courtyard."
    scene courtyard2
    "Everyone’s outside at this time."
    "You sit alone at a table. Everyone else seems to have friends they’re talking to, except you."
    "You probably would have stuck with Elise, but she ran off somewhere."
    "As that thought crosses your mind, you see someone walking towards you."
    "You’ve seen this girl before, she’s in your registration group."
    
    show johanna neutral at left
    with easeinleft

    johanna "Hey, Raymond!"

    show ray awkward at right
    with easeinright

    ray "H-hi...Johanna, was it?"

    show johanna laughter at left

    johanna "Yep, that’s me! Can I ask you something real quick?"

    ray "Um...okay…"

    show johanna surprise at left

    show ray neutral at right

    johanna "D'you know where Elise is? She left this behind in registration."

    "Johanna holds up the diagram of the mechanical wings Elise had been sketching."

    ray "Oh, um...I don’t know, but she said she’s usually in the art studio, or in the workshops?"

    show johanna laughter at left
    show ray smile at right

    johanna "Ah, okay, let’s go check there, then."

    hide johanna with easeoutleft
    hide ray with easeoutleft

    "The two of you go to the workshop classroom."

    scene oh look

    "The door is already open, and you see Elise and Mr Silversaw, the engineering teacher. Elise appears to be looking for something in her bag."

    elise "I’m sure I put it in here…"

    saw "Oh, look, Elise, some friends have come to pay a visit!"

    "Elise looks up and sees you and Johanna."

    elise "Oh- hi!"

    johanna "Hey, Elise! Raymond and I just came to give you this- you left it behind in form time."

    "Johanna hands Elise her sketch."

    elise "I thought I had left it somewhere...thanks!"

    johanna "Of course! Hey, y’know, this thing you’re working on, looks really cool too."

    "Elise glances behind her at the various broken parts of what appeared to be a pair of mechanical wings."

    elise "Heh, thanks...well, if I could get it to work…"

    ray "Ah, this is what you were sketching in class."

    elise "I’d tried to test this out the other day...all fell apart."

    saw "And you’ve gone back to your design, made a few amendments…"

    elise "Yep. I think I worked out the problem with this...I hope."

    ray "How long have you been trying to make it for?"

    elise "I started this a couple months ago, I think."

    saw "Hmm, your improved design looks a lot better, we’ll start on it on Thursday. Lunchtime is almost over, you should get back to class now."

    elise "Oh, it’s that time already, see you later, Sir!"

    "You, Elise and Johanna leave the workshop."

    "It’s now time to go home."
    "You pack up your stuff and are ready to go. Elise is looking through her bag, muttering to herself."

    elise "Ah, great, I left my folder in the workshop…"
    ray "We can quickly go and get it…"

    "You look out of the window. The rain seems to have become quite heavy."

    ray "...it won’t take long."

    "The two of you run through the rain into the workshop classroom."
    "Looks like Mr Silversaw has already left for the day. You see a folder on the teacher’s desk."

    elise "There it is!"

    "Elise picks up her folder, at which point a strong breeze blows some papers out from it and scatters them on the floor, some landing in the tool cupboard."

    "You both pick up the pages scattered around, but when you get the one in the cupboard…"
    "The strong wind blows again, and slams the cupboard door shut, with both of you inside."

    elise "What was that-what was that?!"

    "You try to open the door. It’s locked, and doesn’t open from inside."

    ray "Is anyone out there?! We’re trapped!"

    elise "Oh, Ray, what do we do?"

    ray "Don’t worry, Elise, we’ll find a way out...somehow. It’s not like anything can happen to us in here..."

    "And it’s at that exact moment that the lights go out and there’s a power cut. You had to say it, didn’t you?"

    ray "...great."

    elise "This is great!"

    ray "Well, I have just the thing for a situation like this…"

    "You pull out a box of matches from your pocket."

    elise "Why...why do you have those??"

    ray "You never know when you’ll need them."

    elise "You’re not going to start a fire, are you?"

    "You light the match."

    ray "Only a tiny one."



    "It's at this point that Eleeza stops writing."