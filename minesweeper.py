import random

r, c = 8, 8  # Amount of rows and columns
num = ""
count = 0

bomb = [["0" for column in range(c)] for row in range(r)]  # Sets "0" for all the coordinates in the solution map
cover = [["-" for column in range(c)] for row in range(r)]  # Sets "-" for all the coordinates in the cover map
length = len(bomb)


def endGame():  # Gets called if the player loses
    print("Thank you for playing!")
    print("Solution")
    for row in bomb:  # Prints the solution
        print(*row)
    exit()


def isValid(x):  # Checks to see if the user input is valid
    return 0 <= x < length


def inRange(row, col):  # Checks to see if the current position is in range of the map
    return 0 <= row < length and 0 <= col < length


def isBomb(x, y):  # Checks to see if the current position is a bomb
    return bomb[x][y] == "*"


def makeField():  # Places bombs around the field randomly
    rand = len(bomb)
    maxBomb = int((rand * rand) / 5)
    bombCount = 0

    for i in range(maxBomb):
        for j in range(maxBomb):
            x = random.randrange(rand)  # Chooses a random x coordinate
            y = random.randrange(rand)  # Chooses a random y coordinate
            if bomb[x][y] != "*" and bombCount < maxBomb:
                bomb[x][y] = "*"
                bombCount += 1


makeField()  # Calls makeField


# This goes through the map and counts how many bombs are around each coordinate
for x in range(r):
    for y in range(c):
        count = 0
        if isBomb(x, y):
            pass

        else:
            # Checks north of the coordinate
            if inRange(x - 1, y):
                if isBomb(x - 1, y):
                    count += 1
                    num = str(count)
                    bomb[x][y] = num

            # Checks south of the coordinate
            if inRange(x+1, y):
                if isBomb(x+1, y):
                    count += 1
                    num = str(count)
                    bomb[x][y] = num

            # Checks east of the coordinate
            if inRange(x, y + 1):
                if isBomb(x, y + 1):
                    count += 1
                    num = str(count)
                    bomb[x][y] = num

            # Checks west of the coordinate
            if inRange(x, y - 1):
                if isBomb(x, y - 1):
                    count += 1
                    num = str(count)
                    bomb[x][y] = num

            # Checks north east of the coordinate
            if inRange(x - 1, y + 1):
                if isBomb(x - 1, y + 1):
                    count += 1
                    num = str(count)
                    bomb[x][y] = num

            # Checks north west of the coordinate
            if inRange(x - 1, y - 1):
                if isBomb(x - 1, y - 1):
                    count += 1
                    num = str(count)
                    bomb[x][y] = num

            # Checks south east of the coordinate
            if inRange(x + 1, y + 1):
                if isBomb(x + 1, y + 1):
                    count += 1
                    num = str(count)
                    bomb[x][y] = num

            # Checks south west of the coordinate
            if inRange(x + 1, y - 1):
                if isBomb(x + 1, y - 1):
                    count += 1
                    num = str(count)
                    bomb[x][y] = num

# Prints solution
def solution():
    for row in bomb:
        print(*row)


def printField():  # Prints the map for the player
    solution()
    print('\n')
    for row in cover:
        print(*row)
    blanks()


def blanks():  # Checks to see how many spots are revealed
    blank = 0
    arrLength = len(cover)
    bombAmount = int((arrLength * arrLength) / 5)
    win = (arrLength * arrLength) - bombAmount

    for row in range(arrLength):  # Increases blank count when player reveals a spot
        for col in range(arrLength):
            if cover[row][col] != "-" and cover[row][col] != "F":
                blank += 1

            if blank == win:  # If all the spots that are not bombs are revealed, then player wins
                print("\n\nCongrats You Win!")
                endGame()


def recursion(x, y):  # Reveals all areas around coordinates with no bombs around it
    if not inRange(x, y):
        return

    if bomb[x][y] != cover[x][y] and bomb[x][y] == "0":  # Checks to see if a coordinate is still unrevealed and is 0
        cover[x][y] = bomb[x][y]  # Reveals the coordinate
        recursion(x+1, y)  # Checks south of the coordinate
        recursion(x-1, y)  # Checks north of the coordinate
        recursion(x, y+1)  # Checks east of the coordinate
        recursion(x, y-1)  # Checks west of the coordinate
        recursion(x+1, y+1)  # Checks south east of the coordinate
        recursion(x+1, y-1)  # Checks south west of the coordinate
        recursion(x-1, y-1)  # Checks north west of the coordinate
        recursion(x-1, y+1)  # Checks north east of the coordinate

    else:
        cover[x][y] = bomb[x][y]
        return


def updateCover(x, y):  # Updates the map for the player when they reveal or flag a coordinate
    if bomb[x][y] != "0":
        cover[x][y] = bomb[x][y]
        printField()

    else:
        recursion(x, y)
        printField()


def placeFlag():  # Allows the player to place flags down on coordinates they think are bombs
    print("Please enter a number between 0 and 7 for both row and column")
    xInput = input("Row: ")
    row = int(xInput)
    while not isValid(row):  # Keeps looping until the player enters a valid x coordinate
        xInput = input("Please enter a valid number: ")
        row = int(xInput)

    yInput = input("Column: ")
    col = int(yInput)
    while not isValid(col):  # Keeps looping until the player enters a valid y coordinate
        yInput = input("Please enter a valid number: ")
        col = int(yInput)

    if cover[row][col] == "-":
        cover[row][col] = "F"
        printField()
        userInput()

    else:
        print("You have revealed that area already please choose another spot\n")
        placeFlag()


def userInput():  # Reads the input from the player
    print("Type the number next to the option")
    print("1. Place Flag \n2. Reveal")
    choice = input("Option: ")
    option = False
    if choice == "1" or choice == "2":
        option = True

    while not option:  # Keeps looping until player inputs 1 or 2
        choice = input("Please enter a valid number: ")
        if choice == "1" or choice == "2":
            option = True

    if choice == "1":  # If the choice is 1 then placeFlag is called
        placeFlag()
        return 1

    elif choice == "2":  # If the choice is 2 then ask for x and y coordinates
        print("Please enter a number between 0 and 7 for both row and column")
        xInput = input("Row: ")
        row = int(xInput)
        while not isValid(row):  # Keeps looping until the player enters a valid x coordinate
            xInput = input("Please enter a valid number: ")
            row = int(xInput)

        yInput = input("Column: ")
        col = int(yInput)
        while not isValid(col):  # Keeps looping until the player enters a valid y coordinate
            yInput = input("Please enter a valid number: ")
            col = int(yInput)

        if cover[row][col] == "F":  # Makes sure player wants to reveal a spot they flagged earlier
            replace = False
            print("You have marked this spot with a Flag are you sure you want to reveal this spot?")
            while not replace:  # Loops until player inputs "yes" or "no"
                c = input("Enter Yes or No: ")
                l = c.lower()
                if l == "no" or l == "yes":
                    replace = True

            if l == "yes":  # If the player says yes then check if the coordinate is a bomb or not
                while not isBomb(row, col):  # If the coordinate is not a bomb reveal the position
                    updateCover(row, col)
                    userInput()

                else:  # If the coordinate is a bomb the game ends
                    endGame()

            else:  # If the player says no, then ask the player to flag or reveal a coordinate
                printField()
                userInput()

        else:  # If the coordinate is not flagged check to see if the coordinate is a bomb or not
            while not isBomb(row, col):
                updateCover(row, col)
                userInput()
            else:
                print("\n\nYou Lost!")
                endGame()


printField()  # Calls printField
userInput()  # Calls userInput

