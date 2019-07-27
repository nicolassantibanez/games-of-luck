import random, time

def coinFlip():
    winCount = 0
    totalCount = 0
    coin = ['heads', 'tails']
    while True:
        print("")
        userPick = input("Try to guess the outcome of the coin flip by typing 'heads' or 'tails': ")
        while userPick.lower() not in coin:
            userPick = input("Please type 'heads' or 'tails': ")
        
        print("FLIPPING THE COIN!")
        for i in range(3):
            print('.')
            time.sleep(1)
        flipResult = random.choice(coin)

        print("Coin flip result:", flipResult)
        if flipResult == userPick.lower():
            print("You guessed correctly!")
            winCount += 1
        else:
            print("You didn't guess correctly :c")
        
        time.sleep(2)
        totalCount += 1
        print("Total count:", totalCount,
        "\nCorrect count:", winCount)
        
        newRound = input("Do you want to try again? (Y\\N): ")
        while newRound.lower() != 'y' and newRound.lower() != 'n':
            newRound = input('Do you want to try again? (Y\\N): ')
        if newRound.lower() == 'y':
            continue
        else:
            break

def diceRoll():
    winCount = 0
    totalCount = 0
    diceList = ['1', '2', '3', '4', '5', '6']
    while True:
        print("")
        userNum = input("Type a number from 1-6 to guess the dice outcome: ")
        while userNum not in diceList:
            userNum = input("Please type a number from 1 to 6: ")
        
        print('ROLLING THE DICE!')
        for i in range(3):
            print('.')
            time.sleep(1)
        diceResult = random.choice(diceList)


        print("Dice roll result:", diceResult)
        if userNum == diceResult:
            print("You guessed correctly!")
            winCount +=1
        else:
            print("You didn't guess correctly :c")

        time.sleep(2)
        totalCount += 1
        print("Total count:", totalCount,
        "\nCorrect count:", winCount)

        newRound = input("Do you want to try again? (Y\\N): ")
        while newRound.lower() != 'y' and newRound.lower() != 'n':
            newRound = input('Do you want to try again? (Y\\N): ')
        if newRound.lower() == 'y':
            continue
        else:
            break

#Game Introduction 
print("Welcome to 'The Games of Luck'!",
"\nWhich game would you like to play:",
"\n (1) Coin flip guess",
"\n (2) 6-sided dice roll guess")

gameSelected = input("Type '1' or '2' to choose: ")

while gameSelected not in ['1', '2']:
    gameSelected = input("Please type '1' or '2': ")
    
if gameSelected == '1':
    coinFlip()
else:
    diceRoll()