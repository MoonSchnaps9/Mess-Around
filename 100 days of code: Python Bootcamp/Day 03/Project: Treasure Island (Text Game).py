# Treasure Island Project - Day 3 Final Project
# Goal: Build a "Choose Your Own Adventure" game
# Build a simple text-based game where the player's choices
# determine the outcome of the story

# FLOWCHART - Treasure Island
#
# START
#   -> "Left or right?"
#       -> Right (or anything else): "Fall into a hole. Game Over."
#       -> Left:
#           -> "Swim or wait?"
#               -> Swim (or anything else): "Attacked by trout. Game Over."
#               -> Wait:
#                   -> "Which door? Red, Yellow or Blue?"
#                       -> Red:    "Burned by fire. Game Over."
#                       -> Blue:   "Eaten by beasts. Game Over."
#                       -> Yellow: "You Win!"
#                       -> Anything else: "Game Over."

print('''
.    .    *  .   .  .   .  *     .  .        . .   .     .  *   .     .  .   .
   *  .    .    *  .     .         .    * .     .  *  .    .   .   *   . .    .
. *      .   .    .  .     .  *      .      .        .     .-o--.   .    *  .
 .  .        .     .     .      .    .     *      *   .   :O o O :      .     .
____   *   .    .      .   .           .  .   .      .    : O. Oo;    .   .
 `. ````.---...___      .      *    .      .       .   * . `-.O-'  .     * . .
   \_    ;   \`.-'```--..__.       .    .      * .     .       .     .        .
   ,'_,-' _,-'             ``--._    .   *   .   .  .       .   *   .     .  .
   -'  ,-'                       `-._ *     .       .   *  .           .    .
    ,-'            _,-._            ,`-. .    .   .     .      .     *    .   .
    '--.     _ _.._`-.  `-._        |   `_   .      *  .    .   .     .  .    .
        ;  ,' ' _  `._`._   `.      `,-''  `-.     .    .     .    .      .  .
     ,-'   \    `;.   `. ;`   `._  _/\___     `.       .    *     .    . *
     \      \ ,  `-'    )        `':_  ; \      `. . *     .        .    .    *
      \    _; `       ,;               __;        `. .           .   .     . .
       '-.;        __,  `   _,-'-.--  -:        `.   *   .    .  .   *   .
          `-..--'   `---''              \ `.        . .   .  .       . .  .
        .'                                 `. `.       `  .    *   .      .  .
       /                                     `. `.      ` *          .       .
      /                                        `. `.     '      .   .     *
     /                                           `. `.   _'.  .       .  .    .
    |                                              `._\-'  '     .        .  .
    |                                                 `.__, \  *     .   . *. .
    |                                                      \ \.    .         .
    |                                                       \ \ .     . . .. . 
''')

#Welcome Phrase"
print("Welcome to the NASA Artemis II mission!\nYour goal is to land safely on Earth!")

#First choice to ask
first_choice = input("We need first to do the deorbit burn. You have Theresia or Max to help you out\nWhich one do you choose? ").lower()

if first_choice == "max":
    print("Max has forgotten the correct order of the Python sequence, and prefer to eat a snack. Your spaceship eventually crashes into the ISS...\nGame over, sad :'( ")

elif first_choice == "theresia":
    print("Theresia put correctly the Python sequence! And in such a graceful way!\n(this is almost like she prefers to do this than asking HR at a party if she can grab some food for home)")
    
    #Second choice
    second_choice = input("Now, we need to ensure that the atmospheric entry goes well with the Ablative Shield! Ken and Rayna want to help :O\nWhich one? ").lower()
    
    if second_choice == "ken":
        print("Ken confuses the ablative shield activation blue button with the parachute activation red button (He was never good with colours..)\nNothing protects you from Earth and her summer party at 1000 C..\nGame over, so close :(")

    elif second_choice == "rayna":
        print("Rayna remembers that blue = Madarin language + shield, and she punches it like it was her mother when she was 6 as she forgot to book a hotel during their holidays\n(Don't smile, they had to sleep with a pigeon... wild.)")

        #third choice
        third_choice = input("You've made it, last step to do: Parachute deployment and SPLASHDOWN! (Yes, we prefer to splash into Water than into some trees.. we are cool with trees.. for now.)\nOMG, Guillaume, Will and Sonic want to help!!\nWhich one? ").lower()

        if third_choice == "guillaume":
            print("Guillaume has been trained by the head of the table, and as he always says: It's because I do it myself, that I am overwhelmed... deep\nCongrats! You have safely landed :D")

        elif third_choice == "will" or third_choice == "sonic":
            print("... I am sorry, I should have reminded you that will and sonic do not like each other, so they are debating about a principle like never take shorcut when they drive back home...\nConclusion, your spaceship does a fantastic Splashdown.. with your bones :/..\nGame over, I'm sorry :(")

        else:
            print("Let's be honest, with this typo.. What? I know you made one, I build that thing! >:(\nSo I was saying that your action is similar to a person who do all of the correct steps during an exam, and throw away the exam paper rather than the draft paper\nGame over :/)")
    
    else:
        print("This typo is a bit strange.. like it basically confuses the whole galaxy and now your ship doesn't want to go back to Earth\n In fact, it goes to Venus to have a life crisis with some Jalapenos\n Spicy Game over :/ (I don't like spicy food)")

else:
    print("Yes, you probably... I mean, most probably, like almost sure, like very much true that you made a typo. So, I can't understand you.. which means.. that the spaceship wants to go to Proxima Centaury.\nGame over, but at least you have 70 000 years to think about your career, dishses and.. snacks?")

#PS: I was thinking about if users writes "Guillaume" or "guillaume", how to handle it without going through variable == "Guillaume" or "guillaume"
#So, I asked claude in a way that I know how to do it with "Or", but to check if there could be another way that I haven't discovered yet in my course, and gave me the lower() function with upper() and capitalize. I take some advance haha



