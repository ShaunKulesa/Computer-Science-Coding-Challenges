import random

guess_number_reveal = ['', '', '', '']

number = str(random.randint(1000,9999))

tries = 0

loop = True
easy = False
hard = False
while loop == True:
    print("""Options:
    1: Easy
    2: Hard""")

    mode = input("Choose Mode:")

    if mode == "1":
        easy = True

    while hard == True:
        print("coming soon")
        loop = True

    while easy == True:
        print(guess_number_reveal)
        guess = str(input("Guess the four digit number"))
        
        if len(guess) == 4:
            tries = tries + 1
            easy = True
            if guess[0] == number[0]:
                guess_number_reveal[0] = number[0]
                n1_correct = False
                easy = True
            if guess[0] != number[0]:
                easy = True
            if guess[1] == number[1]:  
                guess_number_reveal[1] = number[1]
                n2_correct = False
                easy = True         
            if guess[1] != number[1]:  
                easy = True  
            if guess[2] == number[2]:  
                guess_number_reveal[2] = number[2]
                n3_correct = False
                easy = True
            if guess[2] != number[2]:
                easy = True
            if guess[3] == number[3]:
                guess_number_reveal[3] = number[3]
                n4_correct = False
                easy = True
            if guess[3] != number[3]:
                easy = True
        else:
            print("number has to be 4 digits")
        
        if guess[0] == number[0] and guess[1] == number[1] and guess[2] == number[2] and guess[3] == number[3]:
            print("you guessed the number")
            print("It took " + str(tries) + " times to guess the number") 
            number = str(random.randint(1000,9999))
            tries = 0
            easy = False
            loop = True
            print(easy)
            guess_number_reveal = []
            
        
