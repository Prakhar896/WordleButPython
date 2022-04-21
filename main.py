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


    """)


def playGame():
    newWord = random.choice(database)
    newWordAsList = list(newWord)
    gottenCorrect = False
    guesses = []
    triesLeft = 6
    print()
    
    ## DEBUG ONLY
    print(newWord)
    print()

    ## Main Guesses Loop
    while (not gottenCorrect) and triesLeft > 0:
        print("LETS START THE GAME!")
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
            print("CONGRATULATIONS! YOU GOT IT! It was:", newWord)
            print("You beat the game with {} tries left!".format(triesLeft))
            print()
            gottenCorrect = True
            break

        ## Loop through letters and form dict
        guessDict = {}
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
            guessDict[char] = currentEmoji

        print("Guess Dict:", guessDict)
        print()
        keysAsCaps = []
        for key in guessDict.keys():
            keysAsCaps.append(key.upper())
        
        print(' '.join(keysAsCaps))
        print(' '.join(guessDict.values()))

        triesLeft -= 1
        continue



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