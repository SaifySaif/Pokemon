import random, time, sys, pygame

pygame.mixer.init() #initalise
#stats for pokemon
pdfn , patk ,pspeed = [random.randrange(0,5) , random.randrange(0,5) , random.randrange(0,10)]  #generates player's defense attack and speed
print("your pokemon's defense:- ",pdfn ,"\n your pokemon's attack:- ",patk, "\n your pokemon's speed:- ", pspeed)
oppdfn , oppatk, oppspeed= [random.randrange(0,5), random.randrange(0, 10) , random.randrange(0,10)] # generates opponent's defense attack and speed

phealth = random.randrange(60,80) #generates player pokemon's health
restorephealth = phealth #will use this variable to set diminished health of player in battle back to original health
opphealth = random.randrange(60,80) #generates opponent pokemon's health
restoreopphealth = opphealth #will use this variable to set diminished health of opponent in battle back to original health
print("max hp is:",phealth)

def print_animation(text, *delay, ascii_txt=False): #function for print animation
    delay = list(delay)
    if delay == []:
        delay.append(0.04)
        delay.append(0.7)
        if not ascii_txt:
            for char in text:
                print(char, end="", flush=True)
                if char not in ["!", ".", ":"]:
                    time.sleep(delay[0])
                else:
                    time.sleep(delay[1])
        else:
            for char in text:
                print(char[0], flush=True)
                time.sleep(delay[0])
        print()

    elif delay == [delay[0]]:
        delay.append(0.7)
        if not ascii_txt:
            for char in text:
                print(char, end="", flush=True)
                if char not in ["!", ".", ":"]:
                    time.sleep(delay[0])
                else:
                    time.sleep(delay[1])
        else:
            for char in text:
                print(char[0], flush=True)
                time.sleep(delay[0])
        print()
    else:
        if not ascii_txt:
            for char in text:
                print(char, end="", flush=True)
                if char not in ["!", ".", ":"]:
                    time.sleep(delay[0])
                else:
                    time.sleep(delay[1])
        else:
            for char in text:
                print(char[0], flush=True)
                time.sleep(delay[0])
        print()
#intro
while True:
    try: #tries the code under the indent, if there is an error, it will execute whatever is indented under 'except' keyword
        temp = input("type 1 to start playing: ")
        if temp == "1":
            break 
        else:
            print("No type 1 if you want to play")
        continue 
    except:
        print("No type 1 if you want to play")
        continue 
while True:
    try:
        temp = input("type 1 to skip the intro: ")
        if temp == "1":
            pygame.mixer.music.load("GiveLifebacktomusic.mp3") 
            pygame.mixer.music.play(loops=-1) #plays givelifebacktomusic with loop = infinite
            break
        pygame.mixer.music.load("GiveLifebacktomusic.mp3") 
        pygame.mixer.music.play(loops=-1) #plays givelifebacktomusic with loop = infinite
        print_animation("Great Let's start")
        time.sleep(4.1)
        print(r"""
                                                  ,'\
    _.----.        ____         ,'  _\   ___    ___     ____
_,-'       `.     |    |  /`.   \,-'    |   \  /   |   |    \  |`.
\      __    \    '-.  | /   `.  ___    |    \/    |   '-.   \ |  |
 \.    \ \   |  __  |  |/    ,','_  `.  |          | __  |    \|  |
   \    \/   /,' _`.|      ,' / / / /   |          ,' _`.|     |  |
    \     ,-'/  /   \    ,'   | \/ / ,`.|         /  /   \  |     |
     \    \ |   \_/  |   `-.  \    `'  /|  |    ||   \_/  | |\    |
      \    \ \      /       `-.`.___,-' |  |\  /| \      /  | |   |
       \    \ `.__,'|  |`-._    `|      |__| \/ |  `.__,'|  | |   |
        \_.-'       |__|    `-._ |              '-.|     '-.| |   |
                                `'                            '-._|


            """)
        time.sleep(2) 
        print("brought to you by",end =" ",flush=True)
        time.sleep(2) 
        print("bintendo")
        time.sleep(2) 
        print("sponsored by siddu sir")
        time.sleep(2) 
        print(":)")
        time.sleep(2)
        print("have fun")
        time.sleep(2)
        break
    except:
        print("exception in pokemon intro")
        break
#battle
while True:
    #choosing pokemon for battle
    while True:
        try:
            print("choose",end = " ",flush=True)
            time.sleep(2.3)
            pokemon = input("your pokemon: \n (1)Charman (2)pikawhoosh (3)bulbabaur ") # choose your pokemon
            if pokemon not in ["1","2","3"]:
                raise Exception("did not type 1,2 or 3")
            opppokemon = input("choose which pokemon you want to battle: \n (1)Charman (2)pikawhoosh (3)bulbabaur, type anything else if you want to choose your pokemon again ") #choose opponent's pokemon
            if opppokemon not in ["1","2","3"]:
                raise Exception("did not type type 1,2 or 3")
            break
        except:
            print("you did not type 1,2 or 3")
            continue

    pygame.mixer.music.stop() #stops Givelifebacktomusic.mp3
    battle_music_ch = random.choice(["Cynthia_Pokemon.mp3", "Team_Galactic_Boss.mp3"])
    pygame.mixer.music.load(battle_music_ch)
    pygame.mixer.music.play(loops=-1) #plays randomly selected song

    #if pokemon and opppokemon are charman
    if pokemon == "1" and opppokemon == "1":
        #resets status effects from previous fight
        phealth = restorephealth
        opphealth = restoreopphealth
        isoppscaryfaced = False
        ispscared = False 
        ispburned = False
        isoppburned = False
        paccreduc = 0 
        oppaccreduc = 0 
        smokescreenusecount = 0 
        pburn = 0 
        oppburn = 0
        pdmgaddon = patk - oppdfn
        oppdmgaddon = oppatk - pdfn
        #char
        def pburned(): #player burned effect
            global pburn, ispburned, phealth
            if pburn <= 0:
                print_animation("player is no longer burned")
                ispburned == False
            else:
                print_animation(f"player has been burned for {pburn} damage")
                phealth = phealth - pburn
                pburn = pburn-1
        def oppburned(): #opponent burned effect
            global oppburn, isoppburned, opphealth
            if oppburn <= 0:
                print_animation("opponent is no longer burned")
                isoppburned == False
            else:
                print_animation(f"opponent has been burned for {oppburn} damage")
                opphealth = opphealth - oppburn
                oppburn = oppburn - 1

        def char(attack): #moves of charmander pokemon
            global  opphealth, oppspeed, oppaccreduc, isoppscaryfaced, oppburn, isoppburned
            global  phealth, pspeed, paccreduc, ispscared, pburn, isoppscaryfaced, ispburned
            global smokescreenusecount

            scratch = [random.randrange(10,13),random.randrange(1,101)]                     #[damage=[5,8),paccuracy=95%,oppaccuracy=100%]
            ember = [random.randrange(17,23),random.randrange(1,101),random.randrange(1,101)] #[damage=[13,17) ,paccuracy=70%,oppaccuracy=80%,pburnchance=20%]
            smokescreen = [random.randrange(4,12),random.randrange(1,101)]                #[accuracy reduction=[4,12) ,paccuracy=70%,oppaccuracy=]
            scaryface = [0, random.randrange(1,101)]                              #[speed reduced to = 0 ,accuracy = 50%]
            
            if move == "playerturn":
                if attack == "1": #checking if player selected scratch
                    print_animation("You used Scratch")
                    time.sleep(4)
                    if scratch [1] <= (95-paccreduc): #paccuracy = 95%, paccreduc reduces accuracy
                        opphealth = opphealth - scratch[0] - pdmgaddon #damage
                        print_animation(f"opponent's health is now {opphealth}")
                        time.sleep(4)
                    else:
                        print_animation("Scratch missed")

                elif attack == "2": #checking if player selected ember
                    print_animation("You used Ember")
                    time.sleep(4)
                    if ember [1] <= (70-paccreduc): #70 % = accuracy of player, paccreduc reduces accuracy
                        opphealth = opphealth - ember[0] - pdmgaddon #damage
                        print_animation(f"opponent's health is now {opphealth}")

                        if ember [2] <= 200: #pburnchance=20%                
                            oppburn = oppburn + 5
                            isoppburned = True
                            print_animation(f"Opponent has been burned, burn damage on opponent is currently = {oppburn}",)
                    else:
                        print_animation("Ember missed")

                elif attack == "3": #checking if player selected smokescreen
                    print_animation(f"You used smokescreen")
                    time.sleep(4)
                    if smokescreenusecount >= 3:
                        print_animation("The Battlefield is filled with too much smoke. Your smokescreen has no effect")
                        time.sleep(4)
                    elif smokescreen[1] <= (70-paccreduc): # 70% = accuracy of player, paccreduc reduces accuracy
                        smokescreenusecount = smokescreenusecount + 1
                        oppaccreduc = oppaccreduc + smokescreen[0] #increases oppaccreduc to decrease accuracy of opponent
                        print_animation(f"opponent's accuracy has been reduced by {smokescreen[0]}")
                    else:
                        print_animation("smokescreen missed")

                elif attack == "4": #checking if player selected scaryface
                    print_animation("You used scaryface")
                    time.sleep(4)
                    if isoppscaryfaced == True:
                        print_animation("Opponent is already scared")
                    elif scaryface[1] <= (50 -paccreduc): # 50% = accuracy of player, paccreduc reduces accuracy
                        isoppscaryfaced = True
                        oppspeed = scaryface[0] #sets speed to scaryface[0] = 0
                        print_animation(f"opponent's speed has been set to {oppspeed}")
                    else:
                        print_animation("Opponent found your face funny, No effect.")
                if ispburned == True:
                    pburned()


            elif move == "oppturn": 
                if attack == "1":  #checking if opponent selected scratch 
                    print_animation("Opponent used scratch")
                    time.sleep(2)
                    if scratch [1] <= (100-oppaccreduc): #accuracy = 100%, oppaccreduc reduces accuracy
                        phealth = phealth - scratch[0] - oppdmgaddon
                        print_animation(f"Your health is now {phealth}")
                    else:
                        print_animation("scratch missed")

                elif attack == "2":  #checking if opponent selected ember
                    print_animation("Opponent used ember")
                    time.sleep(4)
                    if ember [1] <= (80-oppaccreduc): #accuracy = 80% , oppaccreduc reduces accuracy
                        phealth = phealth - ember[0] - oppdmgaddon
                        print_animation(f"Your health is now {phealth}")
                        if ember[2] <= 200:
                            pburn = pburn + 5
                            print_animation(f"You have been burned, burn damage is currently {pburn}",)
                            ispburned = True
                    else:
                        print_animation("Ember missed")

                elif attack == "3": #checking if opponent selected smokescreen
                    print_animation("Opponent used smokescreen")
                    time.sleep(4)
                    if smokescreenusecount >= 3:
                        print_animation("The Battlefield is filled with too much smoke. Opponent's smokescreen has no effect")
                        time.sleep(4)
                    elif smokescreen[1] <= (70-oppaccreduc):#accuracy = 70%, oppaccreduc reduces accuracy
                        smokescreenusecount = smokescreenusecount + 1
                        paccreduc = paccreduc + smokescreen[0]
                        print_animation(f"your accuracy has been reduced by {smokescreen[0]}")
                    else:
                        print_animation("smokescreen missed")

                elif attack == "4": #checking if player selected scaryface
                    print_animation("Opponent used scaryface")
                    time.sleep(4)
                    if ispscared == True:
                        print_animation("Player is already scared, no effect.")
                    elif scaryface[1] <= (50 -oppaccreduc): #accuracy = 50%, oppaccreduc reduces accuracy
                        pspeed = scaryface[0]
                        ispscared = True
                        print_animation(f"Your speed has been set to {pspeed}")
                    else:
                        print_animation("You found your opponent's face funny, No effect.")
                if isoppburned == True:
                    oppburned()

        while True:
            try:
                if pspeed >= oppspeed: #if player's speed is greater than opponent he starts first
                    move = "playerturn" #assigns move in char() to players turn
                    time.sleep(3)
                    #prints charman
                    print(r'''
              _.--""`-..
            ,'          `.
          ,'          __  `.
         /|          " __   \
        , |           / |.   .
        |,'          !_.'|   |
      ,'             '   |   |
     /              |`--'|   |
    |                `---'   |
     .   ,                   |                       ,".
      ._     '           _'  |                    , ' \ `
  `.. `.`-...___,...---""    |       __,.        ,`"   L,|
  |, `- .`._        _,-,.'   .  __.-'-. /        .   ,    \
-:..     `. `-..--_.,.<       `"      / `.        `-/ |   .
  `,         """"'     `.              ,'         |   |  ',,
    `.      '            '            /          '    |'. |/
      `.   |              \       _,-'           |       ''
        `._'               \   '"\                .      |
           |                '     \                `._  ,'
           |                 '     \                 .'|
           |                 .      \                | |
           |                 |       L              ,' |
           `                 |       |             /   '
            \                |       |           ,'   /
          ,' \               |  _.._ ,-..___,..-'    ,'
         /     .             .      `!             ,j'
        /       `.          /        .           .'/
       .          `.       /         |        _.'.'
        `.          7`'---'          |------"'_.'
       _,.`,_     _'                ,''-----"'
   _,-_    '       `.     .'      ,\\
   -" /`.         _,'     | _  _  _.|
    ""--'---"""""'        `' '! |! /
''')
                    char(input("\n Enter your attack:- 1(scratch) 2(ember) 3(smokescreen) 4(scaryface)"))
                    if opphealth <= 0:
                        print("\n you win")
                        pygame.mixer.music.stop()
                        break

                    move = "oppturn" #assigns move in char() to opponent's turn
                    print("")
                    time.sleep(3)
                    char(str(random.randrange(1,5)))
                    if phealth <= 0:
                        print("\n you lose")
                        pygame.mixer.music.stop()
                        break
                    print("\n")

                else:
                    move = "oppturn" #assigns move in char() to opponent's turn
                    print("")
                    time.sleep(3)
                    char(str(random.randrange(1,5)))
                    if phealth <= 0:
                        print("\n you lose")
                        pygame.mixer.music.stop()
                        break

                    move = "playerturn" #assigns move in char() to opponent's turn
                    time.sleep(3)
                    #prints charman
                    print(r'''
              _.--""`-..
            ,'          `.
          ,'          __  `.
         /|          " __   \
        , |           / |.   .
        |,'          !_.'|   |
      ,'             '   |   |
     /              |`--'|   |
    |                `---'   |
     .   ,                   |                       ,".
      ._     '           _'  |                    , ' \ `
  `.. `.`-...___,...---""    |       __,.        ,`"   L,|
  |, `- .`._        _,-,.'   .  __.-'-. /        .   ,    \
-:..     `. `-..--_.,.<       `"      / `.        `-/ |   .
  `,         """"'     `.              ,'         |   |  ',,
    `.      '            '            /          '    |'. |/
      `.   |              \       _,-'           |       ''
        `._'               \   '"\                .      |
           |                '     \                `._  ,'
           |                 '     \                 .'|
           |                 .      \                | |
           |                 |       L              ,' |
           `                 |       |             /   '
            \                |       |           ,'   /
          ,' \               |  _.._ ,-..___,..-'    ,'
         /     .             .      `!             ,j'
        /       `.          /        .           .'/
       .          `.       /         |        _.'.'
        `.          7`'---'          |------"'_.'
       _,.`,_     _'                ,''-----"'
   _,-_    '       `.     .'      ,\\
   -" /`.         _,'     | _  _  _.|
    ""--'---"""""'        `' '! |! /
''' ) 
                    char(input("\n Enter your attack:- 1(scratch) 2(ember) 3(smokescreen) 4(scaryface)"))
                    if opphealth <= 0:
                        print("you win")
                        pygame.mixer.music.stop()
                        break
                    print("\n")
                    continue


            except:
                print("you did not input 1,2,3,4. Input 1 to execute 1.move1, input 2 to execute 2.move2, input 3 to execute 3.move3, inpute 4 to execute 4.move4 ")
                continue
        continue
    
    
    elif pokemon == "1" and opppokemon == "2":
        phealth = restorephealth
        opphealth = restoreopphealth
        isoppscaryfaced = False
        ispscared = False 
        paccreduc = 0 
        oppaccreduc = 0 
        smokescreenusecount = 0 
        pburn = 0 
        oppburn = 0
























































