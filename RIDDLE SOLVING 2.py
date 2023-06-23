#riddle solving 2


import random

name=input("Enter your name: ")
print("Okay " + str(name) + ", let's solve a riddle! You only have 4 tries.")

riddle=random.choice(["What thing has keys but no locks, has space but no room and can enter but can't go inside?", "What did the zero said to the eight?", "What five-letter word becomes shorter when you add two letter to it?", "What can run but cannot walk?","What thing go all around the world but will never leave the corner?", "If you don't keep me, I'll break. What am I?", "What get wets as it dries?", "What will get bigger but will weigh less as it changes?", "If I have it, i don't share it. If I share it, I don't have it. What is it?", "What do elves learn at school?"])

if 'locks' in riddle:
    print(riddle)
    answer=(input("Your answer: ").lower())
    if 'keyboard' in answer:
        print("Wahhh you got it correct on the first try!")
    else:
        chance = 2
        while chance < 5:
            newanswer=(input("Opps, you got it wrong! Try again: "))
            if 'keyboard' in newanswer:
                print("Finally you got it correct in " + str(chance) + " tries!")
                break
            else:
                chance += 1
                if chance == 5:
                    print("Hhhh nice try... The answer is keyboard.")

if 'zero' in riddle:
    print(riddle)
    answer=(input("Your answer: ").lower())
    if 'belt' in answer:
        print("Wahhh you got it correct on the first try!")
    else:
        chance = 2
        while chance < 5:
            newanswer=(input("Opps, you got it wrong! Try again: "))
            if 'belt' in newanswer:
                print("Finally you got it correct in " + str(chance) + " tries!")
                break
            else:
                chance += 1
                if chance == 5:
                    print("Hhhh nice try... The answer is 'nice belt!'.")
        
if 'shorter' in riddle:
    print(riddle)
    answer=(input("Your answer: ").lower())
    if 'short' in answer:
        print("Wahhh you got it correct on the first try!")
    else:
        chance = 2
        while chance < 5:
            newanswer=(input("Opps, you got it wrong! Try again: "))
            if 'short' in newanswer:
                print("Finally you got it correct in " + str(chance) + " tries!")
                break
            else:
                chance += 1
                if chance == 5:
                    print("Hhhh nice try... The answer is 'short'.")

if 'walk' in riddle:
    print(riddle)
    answer=(input("Your answer: ").lower())
    if 'water' in answer:
        print("Wahhh you got it correct on the first try!")
    else:
        chance = 2
        while chance < 5:
            newanswer=(input("Opps, you got it wrong! Try again: "))
            if 'water' in newanswer:
                print("Finally you got it correct in " + str(chance) + " tries!")
                break
            else:
                chance += 1
                if chance == 5:
                    print("Hhhh nice try... The answer is water.")

if 'corner' in riddle:
    print(riddle)
    answer=(input("Your answer: ").lower())
    if 'stamp' in answer:
        print("Wahhh you got it correct on the first try!")
    else:
        chance = 2
        while chance < 5:
            newanswer=(input("Opps, you got it wrong! Try again: "))
            if 'stamp' in newanswer:
                print("Finally you got it correct in " + str(chance) + " tries!")
                break
            else:
                chance += 1
                if chance == 5:
                    print("Hhhh nice try... The answer is stamp.")

if 'break' in riddle:
    print(riddle)
    answer=(input("Your answer: ").lower())
    if 'promise' in answer:
        print("Wahhh you got it correct on the first try!")
    else:
        chance = 2
        while chance < 5:
            newanswer=(input("Opps, you got it wrong! Try again: "))
            if 'promise' in newanswer:
                print("Finally you got it correct in " + str(chance) + " tries!")
                break
            else:
                chance += 1
                if chance == 5:
                    print("Hhhh nice try... The answer is promise.")

if 'wet' in riddle:
    print(riddle)
    answer=(input("Your answer: ").lower())
    if 'towel' in answer:
        print("Wahhh you got it correct on the first try!")
    else:
        chance = 2
        while chance < 5:
            newanswer=(input("Opps, you got it wrong! Try again: "))
            if 'towel' in newanswer:
                print("Finally you got it correct in " + str(chance) + " tries!")
                break
            else:
                chance += 1
                if chance == 5:
                    print("Hhhh nice try... The answer is towel.")

if 'weigh' in riddle:
    print(riddle)
    answer=(input("Your answer: ").lower())
    if 'popcorn' in answer:
        print("Wahhh you got it correct on the first try!")
    else:
        chance = 2
        while chance < 5:
            newanswer=(input("Opps, you got it wrong! Try again: "))
            if 'popcorn' in newanswer:
                print("Finally you got it correct in " + str(chance) + " tries!")
                break
            else:
                chance += 1
                if chance == 5:
                    print("Hhhh nice try... The answer is popcorn.")
        
if 'share' in riddle:
    print(riddle)
    answer=(input("Your answer: ").lower())
    if 'secret' in answer:
        print("Wahhh you got it correct on the first try!")
    else:
        chance = 2
        while chance < 5:
            newanswer=(input("Opps, you got it wrong! Try again: "))
            if 'secret' in newanswer:
                print("Finally you got it correct in " + str(chance) + " tries!")
                break
            else:
                chance += 1
                if chance == 5:
                    print("Shhh...The answer is secret.")

if 'elves' in riddle:
    print(riddle)
    answer=(input("Your answer: ").lower())
    if 'abet' in answer:
        print("Wahhh you got it correct on the first try!")
    else:
        chance = 2
        while chance < 5:
            newanswer=(input("Opps, you got it wrong! Try again: "))
            if 'abet' in newanswer:
                print("Finally you got it correct in " + str(chance) + " tries!")
                break
            else:
                chance += 1
                if chance == 5:
                    print("Hhhh nice try... The answer is the Elf-abet.")

