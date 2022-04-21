import random, time, datetime, sys

## Load words from file that are 5 letters long
database = []
with open('words_alpha.txt', 'r') as f:
    for word in f.readlines():
        if len(word.strip()) == 5:
            database.append((word.strip()).lower())


print("Welcome to Wordle But Python!")
print()
print("This is a simple Wordle-inspired game but where it is written in native Python code and the temrinal is used to play!")
print()

def playGuide():
    print("""
-----
HOW IT WORKS:

| INTRO |

This game is inspired by the Wordle game currently run by NY Times as of writing.

This game is very small and simple and is written in Python, a programming language, in a singular main.py file.

| GAME RULES |

You get 6 tries to guess a five-lettered word in the English Dictionary. The word can be any valid word.

Letters in your guess that are (a) in the actual word and (b) in the right position within the word,
are signified by a green box (🟩) below the letter.

Letters in your guess that are (a) in the actual word but (b) not in the right position within the word,
are signified by a blue box (🟦) below the letter.

Letters in your guess that are not within the word at all are signified by a red box (🟥) below the letter.

| CONCLUSION |

That's it! This game written made by Prakhar Trivedi in 2022. You can check it out at the GitHub Repository:

            https://github.com/Prakhar896/WordleButPython

Thank you for downloading this game, and good luck, because you will need it. ;)

-----
    """)


def playGame():
    newWord = random.choice(database)
    newWordAsList = list(newWord)
    gottenCorrect = False
    guesses = []
    triesLeft = 6
    print()

    ## Main Guesses Loop
    print("LETS START THE GAME!")
    while (not gottenCorrect) and triesLeft > 0:
        while True:
            ## Input Validation Loop
            guess = input(("Guess a 5 letter word now ({} Tries Left): ".format(triesLeft)))
            if guess == "0":
                print("Exiting...")
                sys.exit(0)

            if len(guess) != 5:
                print("Please guess a five-lettered word only.")
                print()
                continue

            if not guess.isalpha():
                print("Please only guess an alphabetical 5-lettered word.")
                print()
                continue
            
            guess = guess.lower()
            
            if guess not in database:
                print("No such word exists. Please try again.")
                print()
                continue
            
            break
        
        print()
        if guess == newWord:
            print("🎉🎉🎉 CONGRATULATIONS! YOU GOT IT! It was:", newWord)
            print("You beat the game with {} tries left!".format(triesLeft))
            print()
            gottenCorrect = True
            break

        ## Loop through letters and form dict
        lettersList = [x.upper() for x in guess]
        emojisList = []
        currentEmoji = ''
        charPosition = 0
        for char in guess:
            if char in newWordAsList:
                for i in range(len(newWordAsList)):
                    if newWordAsList[i] == char:
                        if charPosition == i:
                            currentEmoji = '🟩'
                        else:
                            currentEmoji = '🟦'
            else:
                currentEmoji = '🟥'
            emojisList.append(currentEmoji)
            charPosition += 1
        
        print(f"""

{lettersList[0]}\t{lettersList[1]}\t{lettersList[2]}\t{lettersList[3]}\t{lettersList[4]}
{emojisList[0]}\t{emojisList[1]}\t{emojisList[2]}\t{emojisList[3]}\t{emojisList[4]}

        """)

        triesLeft -= 1
        print()
        continue
    
    if gottenCorrect:
        return
    elif triesLeft == 0 and (not gottenCorrect):
        print()
        print("You ran out of tries! The word was:", newWord)
        return




while True:
    try:
        playChoice = int(input("Would you like to play (1), read the play guide (2)? (Type a number) "))
        if playChoice == 0:
            print("Exiting....")
            break
        if playChoice not in [1, 2]:
            raise Exception
    except Exception as e:
        print("Invalid choice provided. Please try again.")
        print()
        continue
    
    if playChoice == 1:
        playGame()
        print()
        print()
        continue
    elif playChoice == 2:
        playGuide()
        print()
        print()
        continue