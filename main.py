import random, time, datetime

print("Welcome to Wordle But Python!")
print()
print("This is a simple Wordle-inspired game but where it is written in native Python code and the temrinal is used to play!")
print()

def playGuide():
    print("""
-----
HOW IT WORKS:


    """)



while True:
    try:
        playChoice = input("Would you like to play (1), read the play guide (2)? (Type a number) ")
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
        pass
    elif playChoice == 2:
        playGuide()
        print()
        print()
        continue