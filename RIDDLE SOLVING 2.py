def user_answer():
    print(riddle)
    answer=(input("Your answer: ").lower())
    if answer == realanswer:
        print("Congrats! You got in on the first try.")
    else:
        chance = 2
        while chance <5:
            newanswer=(input("Opps, you got it wrong! Try again: "))
            if newanswer == realanswer:
                print("Finally you got it correct in " + str(chance) + " tries!")
                break
                
            else:
                chance += 1
                if chance == 5:
                    print("Hhhh nice try... The answer is ", realanswer, ".")
                

import random

name=input("Enter your name: ")
print("Okay " + str(name) + ", let's solve a riddle! You only have 4 tries.")

riddle=random.choice(["What thing has keys but no locks, has space but no room and can enter but can't go inside?", "What did the zero said to the eight?", "What five-letter word becomes shorter when you add two letter to it?", "What can run but cannot walk?","What thing go all around the world but will never leave the corner?", "If you don't keep me, I'll break. What am I?", "What get wets as it dries?", "What will get bigger but will weigh less as it changes?", "If I have it, i don't share it. If I share it, I don't have it. What is it?", "What do elves learn at school?"])

if 'locks' in riddle:
    realanswer="keyboard" 
    user_answer()

elif 'zero' in riddle:
    realanswer="nice belt"
    user_answer()
        
elif 'shorter' in riddle:
    realanswer="short"
    user_answer()
        
elif 'walk' in riddle:
    realanswer="water"
    user_answer()

elif 'corner' in riddle:
    realanswer="stamp"
    user_answer()

elif 'break' in riddle:
    realanswer="promise"
    user_answer()

elif 'wet' in riddle:
    realanswer="towel"
    user_answer()

elif 'weigh' in riddle:
    realanswer="popcorn"
    user_answer()
        
elif 'share' in riddle:
    realanswer="secret"
    user_answer()

elif 'elves' in riddle:
    realanswer="elfabet"
    user_answer()
