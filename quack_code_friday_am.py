import sys, time, os, random
from running_duck import running_duck
from lazers import lazer_shot_left, lazer_shot_right

def clear():
    os.system("cls" if os.name == "nt" else "clear")

os.system("")

bread_counter = 0

forest_bread = False
beach_bread = False
space_bread = False
temple_bread = False

forest_loop = False
beach_loop = False
space_loop = False
temple_loop = False

winner = False

class style():
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'

def typewriter(message):
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        if char == "\n":
            time.sleep(0.2)
        elif char == "." or char == "?" or char == "!":
            time.sleep(0.1)
        else:
            time.sleep(0.01)

def forest_fight():
    goblin_health = 10
    duck_health = 10

    possible_damage = [2,3,4,5]
    damage = random.choice(possible_damage)

    current_turn = "duck"



    while goblin_health > 0 and duck_health > 0:
        if current_turn == "duck":
            go = input("\nPress A to attack the Goblin\n>>>   ")
            if go.lower() == "a":
                damage = random.choice(possible_damage)
                goblin_health = goblin_health - damage
                if goblin_health < 0:
                    goblin_health = 0
                typewriter(f"\n\nYou've attacked the Goblin and managed to do {damage} points worth of damage!")
                if goblin_health == 0:
                    typewriter(style.GREEN + "\n\n          aarrrghhh, you vicious little duck!" + style.WHITE)
                else:
                    typewriter(f"\nThe Goblin's health is now only {goblin_health} points.")
                current_turn = "goblin"
            else:
                typewriter("Why aren't you attacking???")
                #run fight again
        elif current_turn == "goblin":
                damage = random.choice(possible_damage)
                duck_health = duck_health - damage
                if duck_health < 0:
                    duck_health = 0
                typewriter(f"\n\nThe Goblin attacked you back and managed to do {damage} points worth of damage!")
                if duck_health == 0:
                    print(style.CYAN + "\n\n         Quuuaaaackkkk!!!!!!" + style.WHITE)
                else:
                    typewriter(f"\nBe careful! You have only {duck_health} health points remaining!!!")
                current_turn = "duck"

    if duck_health == 0:
        typewriter("\n\nThe Goblin has made Crispy Duck Pancakes out of you!")
        typewriter(style.GREEN + "\nI think you'd better flap off back to your pond little duck!  HAHAHA!" + style.WHITE)
        typewriter(style.RED + ''' 

                        You Lose
                    G A M E   O V E R
                    ''' + style.WHITE)
        sys.exit()
    elif goblin_health == 0:
        typewriter("\n\nYou have defeated the Goblin! He looks completely ducked up.")
        time.sleep(2)
        typewriter("\nThe Goblin defeatedly beckons you over...")
        time.sleep(2)
        typewriter(style.GREEN + "\nYou Little duck, you have defeated me and done me great mischief.  \nHowever, I can tell that you are alone and scared in this strange forest.  \nTo ensure that you don't keep roaming this forest and ducking up all my Goblin friends,\n I'd like to direct you to a much nicer place where you'll feel like a much better duck.  \nPlease be nicer to the people you meet there than you have been to me. ")
        typewriter('''
        Take this piece of bread as a token of my surrender.
        You may find it useful later in your journey.
        ''')
        global bread_counter
        bread_counter += 1
        global forest_bread
        forest_bread = True
        print(style.WHITE + f"\nYou have {bread_counter} pieces of bread.")
        time.sleep(2)
        typewriter(style.GREEN + "\nNow, walk over there and step into that strange patch of light..." + style.WHITE)
        time.sleep(3)
        if forest_loop == True and bread_counter == 3:
            print("\nYou feel a magical power within you now that you have 3 pieces of bread...")
            print("\nYou feel a surge of ambition and excitement,\n and the strange forest starts to blur at the edge of your vision.")
            print("\nThe world blurs around you, and as it comes back into focus \nyou find yourself back on top of the mountain at the mystical temple...")
            temple_scene()
        else:
            if beach_bread == True:
                space_scene()
            else:
                #run duck animation
                running_duck() 
                #run beach scene function
                beach_scene()

def beach_fight():
    pirate_health = 10
    duck_health = 10

    possible_damage = [2,3,4,5]
    damage = random.choice(possible_damage)

    current_turn = "duck"



    while pirate_health > 0 and duck_health > 0:
        if current_turn == "duck":
            go = input("\nPress A to attack the pirate\n>>>   ")
            if go.lower() == "a":
                damage = random.choice(possible_damage)
                pirate_health = pirate_health - damage
                if pirate_health < 0:
                    pirate_health = 0
                typewriter(f"\n\nYou've attacked the pirate and managed to do {damage} points worth of damage!")
                if pirate_health == 0:
                    typewriter(style.YELLOW + "\n\n          AAARRRGGGHHHHH, shiver me timbers!" + style.WHITE)
                else:
                    typewriter(f"\nThe pirate's health is now only {pirate_health} points.")
                current_turn = "pirate"
            else:
                print("Why aren't you attacking???")
        elif current_turn == "pirate":
                damage = random.choice(possible_damage)
                duck_health = duck_health - damage
                if duck_health < 0:
                    duck_health = 0
                typewriter(f"\n\nThe pirate attacked you back and managed to do {damage} points worth of damage!")
                if duck_health == 0:
                    print(style.CYAN + "\n\n         Quuuaaaackkkk!!!!!!" + style.WHITE)
                else:
                    typewriter(f"\nBe careful! You have only {duck_health} health points remaining!!!")
                current_turn = "duck"

    if duck_health == 0:
        typewriter("\n\nThe pirate has shivered your timbers!")
        typewriter(style.YELLOW + "\nI think you'd better get quacking back to your pond little duck!  HAHAHA!" + style.WHITE)
        typewriter(style.RED + '''   

                        You Lose
                    G A M E   O V E R
                    ''' + style.WHITE)
        sys.exit()
    elif pirate_health == 0:
        typewriter("\n\nYou have defeated the pirate!")
        typewriter("\nThe pirate defeatedly beckons you over...")
        typewriter(style.YELLOW + "\nAAAAARRGGHHH me little duck!  You've shown me who the captain is!\nI'll be glad to see the back of you, so I will show you how to get off this island...")
        typewriter('''
        As a good pirate I will give you some treasure for your bravery.
        Take this piece of bread as a token of my surrender.
        You may find it useful later in your journey.
        ''')
        global bread_counter
        bread_counter += 1
        global beach_bread
        beach_bread = True
        print(style.WHITE + f"\nYou have {bread_counter} pieces of bread.")
        typewriter(style.YELLOW + "\nWalk over there and swashbuckle yourself into that strange patch of light..." + style.WHITE)
        time.sleep(3)
        if beach_loop == True and bread_counter == 3:
            print("\nYou feel a magical power within you now that you have 3 pieces of bread...")
            print("\nYou feel a surge of ambition and excitement,\n and the beach starts to blur at the edge of your vision.")
            print("\nThe world blurs around you, and as it comes back into focus \nyou find yourself back on top of the mountain at the mystical temple...")
            temple_scene()
        else:
            if space_bread == True:
                temple_scene()
            else:
                #run duck animation
                running_duck() 
                #run beach scene function
                space_scene()

def space_fight():
    alien_health = 10
    duck_health = 10

    possible_damage = [2,3,4,5]
    damage = random.choice(possible_damage)

    current_turn = "duck"

    typewriter("\nLooking around for a weapon, you find a space lazer gun nearby and pick it up to take on the alien!!!\n Get Zapping!")

    while alien_health > 0 and duck_health > 0:
        if current_turn == "duck":
            go = input("\nPress A to attack the alien\n>>>   ")
            if go.lower() == "a":
                lazer_shot_left()
                damage = random.choice(possible_damage)
                alien_health = alien_health - damage
                if alien_health < 0:
                    alien_health = 0
                typewriter(f"\n\nYou've attacked the alien and managed to do {damage} points worth of damage!")
                if alien_health == 0:
                    print(style.MAGENTA + "\n\n          eeeeeeekkkkkkkkkkk!!! ghjdbhjdssdgdsab!!!!" + style.WHITE)
                else:
                    typewriter(f"\nThe alien's health is now only {alien_health} points.")
                current_turn = "alien"
            else:
                typewriter("\nWhy aren't you attacking???")
        elif current_turn == "alien":
                lazer_shot_right()
                damage = random.choice(possible_damage)
                duck_health = duck_health - damage
                if duck_health < 0:
                    duck_health = 0
                typewriter(f"\n\nThe alien attacked you back and managed to do {damage} points worth of damage!")
                if duck_health == 0:
                    print(style.CYAN + "\n\n         Quuuaaaackkkk!!!!!!" + style.WHITE)
                else:
                    typewriter(f"\nBe careful! You have only {duck_health} health points remaining!!!")
                current_turn = "duck"

    if duck_health == 0:
        typewriter("\n\nThe alien has scrambled your particles!")
        typewriter(style.MAGENTA + "\nI think you'd better transport back to your pond little duck!  HeeHeee!" + style.WHITE)
        typewriter(style.RED + '''  

                        You Lose
                    G A M E   O V E R
                    ''' + style.WHITE)
        sys.exit()
    elif alien_health == 0:
        typewriter("\n\nYou have defeated the alien!")
        typewriter("\nThe alien wearily beckons you over...")
        typewriter(style.MAGENTA + "\nStrange little lifeform!  You've defeated me and shown the strength of your weird little species! \n I'll be glad to see the back of you, so I will guide you towards your goal.")
        typewriter('''
        Take this piece of bread as a souvenir of your time on this planet.
        You may find it useful later in your journey.
        ''')
        global bread_counter
        bread_counter += 1
        global space_bread
        space_bread = True
        print(style.WHITE + f"\nYou have {bread_counter} pieces of bread.")
        typewriter(style.MAGENTA + "\nWalk over to the space pod there, you will be transported to another dimension..." + style.WHITE)
        time.sleep(2)
        running_duck()
        temple_scene()

def beach_scene():
    typewriter(style.CYAN + "Where am I? It's so bright, and whats this on my webbed feet? Sand...I am on a desert island! \nI need to go and find some shade, it's too hot. \nI see a palm tree in the distance I will go and sit in the shade.")
    print("")
    typewriter(style.WHITE + "\nThe duck walked towards the tree. Suddenly a voice rang out:")
    print(style.YELLOW + '''
                 _____
              .-" .-. "-.
            _/ '=(0.0)=' \_
          /`   .='|m|'=.   \\
          \________________/
      .--.__///`'-,__~\\\\\\\\~`
     / /6|__\// a (__)-\\\\\\\\
     \ \/--`((   ._\   ,)))
     /  \\\\  ))\  -==-  (O)(
    /    )\((((\   .  /)))))
   /  _.' /  __(`~~~~`)__
  //"\\,-'-"`   `~~~~\\~~`"-.
 //  /`"              `      `\\
//
''')
    typewriter(style.YELLOW +
    "\n\nShiver me timbers! What is this I see before me? A duck!")
    typewriter(style.CYAN + '''

    !!! What should Mike do?
    ''')
    typewriter(style.WHITE + "\nA   " + style.CYAN +  "RUN!")
    typewriter(style.WHITE + "\nB   " + style.CYAN + "Talk to him and his cute parrot.")
    typewriter(style.WHITE + "\nC   " + style.CYAN + "Quack quack ATTACK!")
    print("\n")
    typewriter(style.WHITE + "\nchoose - A, B, or C")
    def beach_decision():
        beach_choice = input("\n>>>   ").lower()
        if beach_choice == "a":
            running_duck()
            print("\nMike escaped!")
            typewriter('''
            Mike the duck runs off along the beach on the edge of the golden sand...
            He enjoys the feeling of the sea breeze ruffling his feathers...
            The beach seems to go on for ever, but he begins to realise that it is curving slightly.
            Eventually he spots something in the distance ahead...
            It's the pirate agan!
            He must have run all the way around the island!!!
            What should he do now???
            ''')
            typewriter(style.WHITE + "\nA   " + style.CYAN +  "RUN!")
            typewriter(style.WHITE + "\nB   " + style.CYAN + "Talk to him and his cute parrot.")
            typewriter(style.WHITE + "\nC   " + style.CYAN + "Quack quack ATTACK!")
            print("\n")
            typewriter(style.WHITE + "\nchoose - A, B, or C")
            beach_decision()
        elif beach_choice == "b":
            typewriter(style.CYAN + "\nHello pirate, I thought I was alone on this island, \ndo you know where we are or how to get off of here?")
        elif beach_choice == "c":
            print(style.CYAN + "\nQUACK QUACK ATTACK" + style.WHITE)
            beach_fight()
        else:
            typewriter("Choose - A,B, or C")
            beach_decision()
    
    beach_decision()
    print("\n")
    typewriter(style.YELLOW + 
    "\nArrggh I do, why don't you take a look in that there olde treasure chest? ")
    typewriter(style.WHITE + 
    "\n\nThe duck slowly opened the chest to reveal a weathered piece of paper that read:\nWhich brand of rum is named after a 17th-century Welsh pirate?"
    '')
    print("")
    typewriter(style.WHITE + "\nA) Malibu.")
    typewriter(style.WHITE + "\nB) Bacardi.")
    typewriter(style.WHITE + "\nC) Captain Morgan")
    print("\n")
    typewriter(style.WHITE + "\n Choose - A, B, or C")
    def beach_quiz():
        beach_choice = input("\n>>>   ").lower()
        if beach_choice == "c":
            typewriter(style.YELLOW + "\nWell done duck, here is another piece of bread, and remember...\n")
            global bread_counter
            global beach_bread
            bread_counter += 1
            beach_bread = True
            print(style.WHITE + "\nZAP!")
            typewriter("\nMike is pulled into a portal before he can hear the pirate's advice")
            print(f"\nYou have {bread_counter} pieces of bread.")
            time.sleep(2)
            if beach_loop == True and bread_counter == 3:
                print("\nYou feel a magical power within you now that you have 3 pieces of bread...")
                print("\nYou feel a surge of ambition and excitement,\n and the beach starts to blur at the edge of your vision.")
                print("\nThe world blurs around you, and as it comes back into focus \nyou find yourself back on top of the mountain at the mystical temple...")
                temple_scene()
            else:
                if space_bread == True:
                    temple_scene()
                else:
                    #run duck animation
                    running_duck() 
                    #run beach scene function
                    space_scene()
        elif beach_choice == "b":
            typewriter(style.YELLOW + "\nUnlucky ducky! No treasure for you, which is a shame as...\n")
            print(style.WHITE + "\nZAP!")
            typewriter("\nMike is pulled into a portal before he can hear the pirates advice")
            time.sleep(2)
            space_scene()
        elif beach_choice == "a":
            typewriter(style.YELLOW + "\nUnlucky ducky! No treasure for you, which is a shame as...\n")
            print(style.WHITE + "\nZAP!")
            typewriter("\nMike is pulled into a portal before he can hear the pirates advice")
            time.sleep(2)
            space_scene()
        else:
            typewriter("Choose - A,B, or C")
            beach_quiz()
    beach_quiz()

def space_scene():
    typewriter(style.WHITE + '''

    Mike is whooshed away in a tunnel of light and wakes up floating, yes floating, in space.  
    Floating near to a crater, he crash lands and looks inside the crater and to his shock he spots an Alien.
    ''')
    print(style.MAGENTA + '''            
.     .       .  .   . .   .   . .    +  .
  .     .  :     .    .. :. .___---------___.
       .  .   .    .  :.:. _".^ .^ ^.  '.. :"-_. .
    .  :       .  .  .:../:            . .^  :.:\.
        .   . :: +. :.:/: .   .    .        . . .:\\
 .  :    .     . _ :::/:               .  ^ .  . .:\\
  .. . .   . - : :.:./.                        .  .:\\
  .      .     . :..|:                    .  .  ^. .:|
    .       . : : ..||        .                . . !:|
  .     . . . ::. ::\(                           . :)/
 .   .     : . : .:.|. ######              .#######::|
  :.. .  :-  : .:  ::|.#######           ..########:|
 .  .  .  ..  .  .. :\ ########          :######## :/
  .        .+ :: : -.:\ ########       . ########.:/
    .  .+   . . . . :.:\. #######       #######..:/
      :: . . . . ::.:..:.\           .   .   ..:/
   .   .   .  .. :  -::::.\.       | |     . .:/
      .  :  .  .  .-:.":.::.\             ..:/
 .      -.   . . . .: .:::.:.\.           .:/
.   .   .  :      : ....::_:..:\   ___.  :/
   .   .  .   .:. .. .  .: :.:.:\       :/
     +   .   .   : . ::. :.:. .:.|\  .:/|
     .         +   .  .  ...:: ..|  --.:|
.      . . .   .  .  . ... :..:.."(  ..)"
 .   .       .      :  .   .: ::/  .  .::\\

 ''')
    typewriter(style.MAGENTA + "\nHello!," + style.WHITE + " says the alien, " + style.MAGENTA + "you can call me Alan, dont be scared.  \nYou have travelled far you must be hungry, i can offer you some bread if you follow the path to that pod over their and answer a question...")
    typewriter(style.CYAN + '''

    "O M G thats an Alien, what do I do? - Do I run away, talk to him or fight him???"
    ''')
    typewriter(style.WHITE + "\nA   " + style.CYAN +  "I am going to run and hide")
    typewriter(style.WHITE + "\nB   " + style.CYAN + "I am going to be brave and go and talk to him.")
    typewriter(style.WHITE + "\nC   " + style.CYAN + "Hey Alien!!! (lets fight!)")
    typewriter(style.WHITE + "\nChoose - A, B, or C")

    def space_decision():
        space_choice = input("\n>>>   ").lower()
        if space_choice == "a":
            print("\nYou've chosen to run away!")
            #need to slow this bit down
            typewriter("You run away from the crater and are lost on the planet")
            #run function that loops back to start of space
            #more dialogue here...................
            typewriter("\nYou start to feel a strange sensation, a feeling of weightlessness...")
            typewriter("\nYou realise you've begun to float above the ground.  Flapping your wings causes you to move through the air, \n but soon you begin to lose control of this strange flight. \n You get stuck in a spin, and seem to be moving at an unfathomable speed through the atmosphere of this strange world...")
            typewriter("\nAfter a few minutes of intense inter-galactical chaos, you feel gravity being restored,\n and you coming crashing back down onto the planet's surface...")
            typewriter("\nRegaining your senses, you realise that you are back where you started at the crater,\n with the Alien looking down at you!")
            typewriter(style.CYAN + '''

            What is a duck to do?!?
            ''')
            typewriter(style.WHITE + "\nA   " + style.CYAN +  "I am going to run and hide")
            typewriter(style.WHITE + "\nB   " + style.CYAN + "I am going to be brave and go and talk to him.")
            typewriter(style.WHITE + "\nC   " + style.CYAN + "Hey Alien!!! (lets fight!)")
            typewriter(style.WHITE + "\nChoose - A, B, or C")
            space_decision()
        elif space_choice == "b":
            typewriter(style.CYAN + '''\n   Hello Alan the Alien!''')
            #continue to alien question
        elif space_choice == "c":
            print("\nHey Alan the alien (fight!!)")
            space_fight()
        else:
            typewriter("Choose - A,B, or C")
            space_decision()
        
        print("\n")
        typewriter(style.MAGENTA + '''
        "Hello little Duck!!!"
        "This planet is called Quaklar it must seem like a strange place for a little duck to be, dont be scared! 
        If you can answer this question you will be transported from here to somewhere very mystical and calming."
        "The Question is ;"
    
           
         On average how far away is the moon from the earth in miles??
        ''')
            
        typewriter(style.WHITE + "\n    A) " +style.MAGENTA + "200.000 miles")
        typewriter(style.WHITE + "\n    B) " +style.MAGENTA + "238.000 miles")
        typewriter(style.WHITE + "\n    C) " +style.MAGENTA + "140.000 miles")

    space_decision()

    def space_quiz_reply():
        typewriter(style.WHITE + "\n\n  Answer A,B, or C...")
        space_answer = input("\n>>>   ")
        if space_answer.lower() == "a":
                typewriter(style.MAGENTA + '''"That is the wrong answer! how ever little duck I like you so I am going to help you get to the next level but with out any bread which i know you love so much, oh well.."
                "Get inside this pod and I will send you off to your next destination "
                ''')
                time.sleep(2)
                running_duck()
                temple_scene()
        elif  space_answer.lower() == "b":
            global bread_counter
            global space_bread
            bread_counter += 1
            space_bread = True
            typewriter(style.MAGENTA + '''
            "Wow you are correct you are wiser than your young years duck!" 
            "Here is another piece of bread , and remember don't eat it all! Get inside this pod and I will send you off to your next destination "
            ''' + style.WHITE)
            print(f"You have {bread_counter} pieces of bread.")
            time.sleep(2)
            running_duck()
            temple_scene()
        elif space_answer.lower() == "c":
            typewriter(style.MAGENTA + '''"That is the wrong answer!  how ever little duck I like you so I am going to help you get to the next level but with out any bread which i know you love so much, oh well.."
            "Get inside this pod and I will send you off to your next destination "
            ''')  
            time.sleep(2)  
            running_duck()
            temple_scene()
        else: 
            space_quiz_reply()

    space_quiz_reply()

def temple_scene():
    global bread_counter
    print(f"You have {bread_counter} pieces of bread.")
    typewriter(style.WHITE + "Mike the duck wakes, piped music plays in the distance and he feels a sense of peace wash over him. \nHe looks around and finds himself at the summit of a mountain, atop which is a magnificent temple.")
    print( style.RED + '''

   `,.      .   .        *   .    .      .  _    ..          .
     \,~-.         *           .    .       ))       *    .
          \ *          .   .   |    *  . .  ~    .      .  .  ,
 ,           `-.  .            :               *           ,-
  -             `-.        *._/_\_.       .       .   ,-'
  -                 `-_.,     |n|     .      .       ;
    -                    \ ._/_,_\_.  .          . ,'         ,
     -                    `-.|.n.|      .   ,-.__,'         -
      -                   ._/_,_,_\_.    ,-'              -
      -                     |..n..|-`'-'                -
       -                 ._/_,_,_,_\_.                 -
         -               ,-|...n...|                  -
           -         ,-'._/_,_,_,_,_\_.              -
             -  ,-=-'     |....n....|              -
              -;       ._/_,_,_,_,_,_\_.         -
             ,-          |.....n.....|          -
           ,;         ._/_,_,_,_,_,_,_\_.         -
  `,  '.  `.  ".  `,  '.| n   ,-.   n |  ",  `.  `,  '.  `,  ',
,.:;..;;..;;.,:;,.;:,o__|__o !.|.! o__|__o;,.:;.,;;,,:;,.:;,;;:
 ][  ][  ][  ][  ][  |_i_i_H_|_|_|_H_i_i_|  ][  ][  ][  ][  ][
                     |     //=====\\     |
                     |____//=======\\____|
                         //=========\\

    ''')
    typewriter(style.WHITE + "\nMike waddles through thick undergrowth towards the temple. Outside there is a wise old monk. \nBefore Mike has a chance to run or strike the monk begins to speak.")
    typewriter(style.RED + "\nI have been waiting for you, Mike the Duck. I have the final piece you need to complete your quest and thus find the magic bathtub of your dreams.")
    typewriter(style.RED + "\nAll you must do is answer this one final question. Look deep into your soul for the answer, for it is by far the most difficult yet.\nThe Monk looked Mike straight in the eye and asked")
    
    print("\n")
    typewriter(style.RED + "....Which is the best bread?")
    print("\n")
    typewriter(style.WHITE + "\nA) Sourdough.")
    typewriter(style.WHITE + "\nB) Baguette.")
    typewriter(style.WHITE + "\nC) Focaccia")
    print("")
    typewriter(style.WHITE + "\n Choose - A, B, or C")
    def temple_decision():
        global bread_counter
        temple_choice = input("\n>>>   ").lower()
        if temple_choice == "a":
            typewriter(style.RED + "You FOOL. Sourdough isn't even in the top 10. Good luck defeating the Guardian of the Magic Bathtub now!!")
            #go to python battle
            python_scene()
        elif temple_choice == "b" and bread_counter >= 3:
            typewriter(style.RED + "I knew to have faith in you. Here, take this, Quackscaliber, the legendary baguette sword! This sword belonged to my father wh-")
            typewriter(style.CYAN + "\nOK thanks bye!")
            typewriter(style.WHITE + "\nMike hurried onwards past the monk.")
            bread_counter = bread_counter + 1
            global temple_bread
            temple_bread = True
            global winner
            winner = True
            #go to python battle
            python_scene()
        elif temple_choice == "b" and bread_counter < 3:
            typewriter(style.RED + "I knew to have faith in you. However all I can offer you is this.")
            typewriter(style.WHITE + "\nMike acquired Slightly Mouldy Bread Slice.")
            typewriter(style.RED + "\nTo be a true hero one needs more bread. Good luck defeating the Guardian of the Magic Bathtub..." + style.WHITE)
            #go to python battle
            python_scene()
        elif temple_choice == "c":
            typewriter(style.RED + "...That's your actual answer? Okay, well good luck defeating the Guardian of the Magic Bathtub now!!" + style.WHITE)
            #go to python battle
            python_scene()
        else:
            typewriter("Choose - A,B, or C")
            temple_decision()
            
    temple_decision()

def python_scene():
    global bread_counter
    global forest_bread
    global beach_bread
    global space_bread
    global temple_bread
    global winner
    
    print(style.WHITE + f"\nYou have {bread_counter} pieces of bread")
    print(f'''

    Forest bread? {forest_bread}
    Beach bread? {beach_bread}
    Space bread? {space_bread}
    Temple bread? {temple_bread}
    Winner? {winner}
    ''')
    time.sleep(4)
    
    typewriter(style.WHITE + "The final battle is nigh. Mike paces slowly through a dimly lit corridor. \nWhen a cackle rings out ahead.")
    typewriter(style.GREEN + "\nFoolish little duck. You're not in your little pond anymore. You shall never defeat I! The Guardian of the Magic Bathtub!")
    typewriter(style.WHITE + "\nUndeterred, Mike pressed on to the centre of the temple. Eventually finding himself in a large chamber.")
    typewriter(style.WHITE + "\n.  .  .  .  .")
    typewriter(style.WHITE + "\nCRASH!! A huge figure emerges from the shadows...\nThe Guardian of the Magic Bathtub...\nPYTHON!!!")
    print(style.GREEN + '''

           /^\/^\\
         _|__|  O|
\/     /~     \_/ \\
 \____|__________/  \\
        \_______      \\                  \\
                `\     \                  \\\\
                  |     |                  \\\\
                 /      /                    \\\\
                /     /                       \\\\
              /      /                         \ \\
             /     /                            \  \\
           /     /             _----_            \  \\
          /     /           _-~      ~-_         |   |
         (      (        _-~    _--_    ~-_     _/   |
          \      ~-____-~    _-~    ~-_    ~-_-~    /
            ~-_           _-~          ~-_       _-~
               ~--______-~                ~-___-~
    
''')
    typewriter(style.GREEN + "\nHA HA HA Come then puny duckling, I'll defend the Magic Bathtub with my life!")
    typewriter(style.WHITE + "\nThe giant python lunges towards Mike, who narrowly darts out of the way.")
    typewriter(style.CYAN + "\nQUACK! I have to do something...wait a second...")
    def python_battle():
        global winner
        if winner == True:
            typewriter(style.WHITE + "\nMike reached for Quackscaliber, the legendary baguette sword!! \nPython recoiled in anger.")
            typewriter(style.GREEN + "\nNO! Not that BREADFUL SWORD!!")
            time.sleep(2)
            typewriter(style.WHITE + "\nMike ran full speed towards Python!")
            time.sleep(1)
            typewriter(style.CYAN + "\nFinal attack!! Mighty Mallard Hoi Sin Stab Mark 3!!!")
            time.sleep(2)
            typewriter(style.WHITE + "\nB  O  O  P")
            time.sleep(2)
            typewriter(style.GREEN + "\n...Owww! :( FINE have the silly BATHTUB I don't give a duck!")
            time.sleep(4)
            credits_scene()
        else:
            typewriter(style.WHITE + "\nMike reached for....the slightly mouldy piece of bread\n...It's looking worse actually\n....Should probably just throw that away.")
            typewriter(style.WHITE + "\nMike threw the Very Mouldy Slice")
            typewriter(style.WHITE + "\nSplat...The bread missed. Awkward.")
            typewriter(style.WHITE + "\nThe Python easily overpowered Mike\nMike became crispy duck pancakes.")
            typewriter(style.RED + ''' 
                     
                                 You Lose
                            G A M E   O V E R
                                    ''' + style.WHITE)
            continue_game()
        sys.exit()
    python_battle()

   
#############################################################
def continue_game():
    if forest_bread == False:
            typewriter("\nWould you like to go back to the forest to try and find more bread?\n  Y or N?")
            loop_answer = input("\n>>>   ")
            if loop_answer.lower()  == "y":
                global forest_loop
                forest_loop = True
                forest_scene()
            elif loop_answer.lower() == "n":
                typewriter("\nNevermind!  Better luck next time!")
                typewriter(style.RED + ''' 

                            You Lose
                        G A M E   O V E R
                        ''' + style.WHITE)
                sys.exit()
            else:
                continue_game()
    elif beach_bread == False:
            typewriter("\nWould you like to go back to the desert island to try and find more bread?\n  Y or N?")
            loop_answer = input("\n>>>   ")
            if loop_answer.lower()  == "y":
                global beach_loop
                beach_loop = True
                beach_scene()
            elif loop_answer.lower() == "n":
                typewriter("\nNevermind!  Better luck next time!")
                typewriter(style.RED + ''' 

                            You Lose
                        G A M E   O V E R
                        ''' + style.WHITE)
                sys.exit()
            else:
                continue_game()
    elif space_bread == False:
            typewriter("\nWould you like to go back to the alien planet to try and find more bread?\n  Y or N?")
            loop_answer = input("\n>>>   ")
            if loop_answer.lower()  == "y":
                global space_loop
                space_loop = True
                space_scene()
            elif loop_answer.lower() == "n":
                typewriter("\nNevermind!  Better luck next time!")
                typewriter(style.RED + ''' 

                            You Lose
                        G A M E   O V E R
                        ''' + style.WHITE)
                sys.exit()
            else:
                continue_game()
    elif temple_bread == False:
            typewriter("\nWould you like to go back to the mystical Monk to try and find more bread?\n  Y or N?")
            loop_answer = input("\n>>>   ")
            if loop_answer.lower()  == "y":
                global temple_loop
                temple_loop = True
                temple_scene()
            elif loop_answer.lower() == "n":
                typewriter("\nNevermind!  Better luck next time!")
                typewriter(style.RED + ''' 

                            You Lose
                        G A M E   O V E R
                        ''' + style.WHITE)
                sys.exit()
            else:
                continue_game()

def credits_scene():
    def typewriter2(message):
        for char in message:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.01)

    os.system("cls" if os.name == "nt" else "clear")    
    typewriter2(style.GREEN + '''
_____.___.               __      __            ._._._.
\__  |   | ____  __ __  /  \    /  \____   ____| | | |
 /   |   |/  _ \|  |  \ \   \/\/   /  _ \ /    \ | | |
 \____   (  <_> )  |  /  \        (  <_> )   |  \|\|\|
 / ______|\____/|____/    \__/\  / \____/|___|  /_____
 \/                            \/             \/\/\/\/


    ''')

    time.sleep(2)

    print('''
    o    .   _     .                  
            .     (_)         o      
    o                      _       o
                    o  (_)   .
                    O             _
    o              __      o   o    (_)
     . O            __          .  ,     o
        o8o     ___( o)>   ,o8oO8/( -TT
       o8o8O    \ <_. )  \Oo8OOoOo8OO||     O
    Oo(""o8"""""""""""""""8oo""""""")
    _   `\`'                  `'   /'   o
   (_)    \                       /    _   .
        O  \                     /    (_)
  o   .     `-. .-----------. .-'
     --------(_/-------------\_)--------
    
    
    
    '''  + style.WHITE)

    message = "Team 3 Productions.\nQuack The Code.\nWritten and coded by  - Scott Brown, Cara McPartland, Stephen Hough.\nNo animals were harmed in the making of this game.\nThanks to Codenation teacher Mike for his wit, knowledge and inspiration.\nMade in Liverpool & Chester, England.\n            2021\n\n\n\n\n"
    print("\n")
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.1)

    time.sleep(5)
    sys.exit()


os.system("cls" if os.name == "nt" else "clear")
typewriter("Quack The Code")
print(style.GREEN + '''
________                       __       __  .__             _________            .___      
\_____  \  __ _______    ____ |  | __ _/  |_|  |__   ____   \_   ___ \  ____   __| _/____  
 /  / \  \|  |  \__  \ _/ ___\|  |/ / \   __\  |  \_/ __ \  /    \  \/ /  _ \ / __ |/ __ \ 
/   \_/.  \  |  // __ \\\\  \___|    <   |  | |   Y  \  ___/  \     \___(  <_> ) /_/ \  ___/ 
\_____\ \_/____/(____  /\___  >__|_ \  |__| |___|  /\___  >  \______  /\____/\____ |\___  >
       \__>          \/     \/     \/            \/     \/          \/            \/    \/ 
''')
print("")
bread_counter = 0
def forest_scene():
    typewriter(style.WHITE + "One day Mike the duck was swimming in his pond, bored and looking for an adventure. He got out of the pond and followed the path into the forest. A feather blowing in the wind caught his eye and the feather ended up at the feet of a goblin...")
    print("")
    print(style.GREEN + '''
                             /  (.-./  (
                            /           \      .^.
                           |  -=- -=-    |    (_|_)
                            \   /       /      // 
                             \  .=.    /       \\\\
                        ___.__`..;._.-'---...  //
                  __.--"        `;'     __   `-.  
        -===-.--""      __.,              ""-.  ".
          '=_    __.---"   | `__    __'   / .'  .'
          `'-""""           \             .'  .'
                             |  __ __    /   |
                             |  __ __   //`'`'
                             |         ' | //
                             |    .      |//
                            .'`., , ,,,.`'.
                           .'`',.',`.` ,.'.`
                            ',',,,,.'...',,'
                            '..,',`'.`,`,.',
                           ,''.,'.,;',.'.`.'
                           '.`.',`,;',',;,.;
                            ',`'.`';',',`',.
    __                       |     |     |
___( o)>                     (     (     |
\ <_. )                      (     (     |
 `---'                     
                            
                             
    ''')
    typewriter(style.CYAN + '''
    "O M G What do I do? - Do I run away, talk to him or fight him???"
    ''')
    typewriter(style.WHITE + "\nA   " + style.CYAN +  "I am going to run and hide from him, I dont trust him.")
    typewriter(style.WHITE + "\nB   " + style.CYAN + "I am going to be brave and go and talk to him.")
    typewriter(style.WHITE + "\nC   " + style.CYAN + "Hey Goblin!!! (Fight!! Smack!! Bang!)")
    print("\n")
    typewriter(style.WHITE + "\nChoose - A, B, or C")

    def forest_decision():
        forest_choice = input("\n>>>   ").lower()
        if forest_choice == "a":
            print("\nYou've chosen to run away!")
            time.sleep(2)
            running_duck()
            #need to slow this bit down
            typewriter("you run further into the forest...")
            typewriter('''
            The further in to the forest you get, the more you begin to feel lost.
            The trees all start to look the same, and you've lost your sense of direction.
            Suddenly you catch a glimpse of the feather that led you here, so, scared and lost,
            you follow the feather, only to see it land right back at the feet of the Goblin that you ran away from!
            ''')
            typewriter(style.CYAN + '''
            "Back here again! What do I do??? - Do I run away again, talk to him or fight him???"
            ''')
            typewriter(style.WHITE + "\nA   " + style.CYAN +  "I am going to run away, even if I do keep getting lost.")
            typewriter(style.WHITE + "\nB   " + style.CYAN + "I am going to be brave and go and talk to him.")
            typewriter(style.WHITE + "\nC   " + style.CYAN + "Hey Goblin!!! (Fight!! Smack!! Bang!)")
            print("\n")
            typewriter(style.WHITE + "\nChoose - A, B, or C")

            #run function that loops back to start of forest
            #need more filler dialogue here
            forest_decision()
        elif forest_choice == "b":
            typewriter(style.CYAN + '''\n   Hello Mr Goblin!''')
            #continue to goblin question
        elif forest_choice == "c":
            print("\nHey Goblin (Fight!! Smack!! Bang!)")
            forest_fight()
            #set fight enemy to goblin
            #set fight scene to forest
            #run fight function
            #fight function should lead onwards to beach scene
        else:
            typewriter("Choose - A,B, or C")
            forest_decision()

    forest_decision()
    print("\n")
    typewriter(style.GREEN + '''
    "Hello little Duck!!!  You're a long way from your pond!"
    "This forest is a dark and strange place, but if you can answer my question I will guide you from here to somewhere much nicer."
    "Answer me this;"
    
    Which is the national tree of India?
    ''')
    typewriter(style.WHITE + "\n    A) " +style.GREEN + "Coconut Tree")
    typewriter(style.WHITE + "\n    B) " +style.GREEN + "Banyan Tree")
    typewriter(style.WHITE + "\n    C) " +style.GREEN + "Banana Tree")
    
    
    def forest_quiz_reply():
        typewriter(style.WHITE + "\n\n  Answer A,B, or C...")
        forest_answer = input("\n>>>   ")
        if forest_answer.lower() == "a":
            typewriter(style.GREEN + '''"That is the wrong answer!  If you got it right I would give you something useful, but oh well.."
            "I will still show you how to get to somewhere nicer though..."
            "Walk into that strange light over there!"
            ''') 
            time.sleep(2)
            #run duck animation
            running_duck() 
            #run beach scene function
            beach_scene()
        elif forest_answer.lower() == "b":
            typewriter(style.GREEN + '''
            "You are a wise duck!" 
            "Take this loaf of bread, you might need it later, so don't eat it all!"
            "Now, walk into that strange light over there, you will find yourself somewhere much nicer than here!"
            ''' + style.WHITE)
            global bread_counter
            bread_counter += 1
            global forest_bread
            forest_bread = True
            print(f"You have {bread_counter} pieces of bread.")
            time.sleep(2)
            ############## skip to temple here if forest_loop == True #############################
            if forest_loop == True and bread_counter == 3:
                print("\nYou feel a magical power within you now that you have 3 pieces of bread...")
                print("\nYou feel a surge of ambition and excitement,\n and the strange forest starts to blur at the edge of your vision.")
                print("\nThe world blurs around you, and as it comes back into focus \nyou find yourself back on top of the mountain at the mystical temple...")
                temple_scene()
            else:
                if beach_bread == True:
                    space_scene()
                else:
                    #run duck animation
                    running_duck() 
                    #run beach scene function
                    beach_scene()
        elif forest_answer.lower() == "c":
            typewriter(style.GREEN + '''"That is the wrong answer!  If you got it right I would give you something useful, but oh well.."
            "I will still show you how to get to somewhere nicer though..."
            "Walk into that strange light over there!"
            ''') 
            time.sleep(2)
            #run duck animation
            running_duck()
            #run beach scene function
            beach_scene()
        else: 
            forest_quiz_reply()
    
    forest_quiz_reply()


forest_scene()

