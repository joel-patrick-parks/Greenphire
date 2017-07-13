#Powerball Project for Greenphire
#Works for 2 people wishing to play powerball
#Gets each player's input and then generates a final powerball winning number based on their selected numbers
#Joel Parks, 7/12/2017

from random import randint

#class used to hold the name of a player and the number they selected
class PowerballPlayer:
    def __init__(self,name):
        self.name = name
        self.numbers = []

    def addNumbers(self,number):
        self.numbers.append(number)

#gets the names and numbers of the players playing the game
powerBallers = []
addPlayer = True;
currentPlayer = 0
counter = 0
while addPlayer:
    print "Enter your first name:"
    firstName = raw_input();
    print firstName
    print "Enter your last name:"
    lastName = raw_input();
    print lastName
    fullName = firstName + " " + lastName
    powerBallers.append(PowerballPlayer(fullName))

    #checks the numbers the users enter to make sure that there are no duplicates
    while counter < 6:
        if counter == 0:
            print "Enter 1st # (1 thru 69):"
            num = input()
            if (num < 1) or (num > 69):
                print "Invalid entry"
            else:
                print num
                powerBallers[currentPlayer].addNumbers(num)
                counter += 1
        if counter == 1:
            print "Enter 2nd # (1 thru 69 excluding",powerBallers[currentPlayer].numbers[0],"):"
            num = input()
            if (num < 1) or (num > 69) or (num == powerBallers[currentPlayer].numbers[0]):
                print "Invalid entry"
            else:
                print num
                powerBallers[currentPlayer].addNumbers(num)
                counter += 1
        if counter == 2:
            print "Enter 3rd # (1 thru 69 excluding",powerBallers[currentPlayer].numbers[0],"and",powerBallers[currentPlayer].numbers[1],"):"
            num = input()
            if (num < 1) or (num > 69) or (num == powerBallers[currentPlayer].numbers[0]) or (num == powerBallers[currentPlayer].numbers[1]):
                print "Invalid entry"
            else:
                print num
                powerBallers[currentPlayer].addNumbers(num)
                counter += 1
        if counter == 3:
            print "Enter 4th # (1 thru 69 excluding",powerBallers[currentPlayer].numbers[0],",",powerBallers[currentPlayer].numbers[1],"and",powerBallers[currentPlayer].numbers[2],"):"
            num = input()
            if (num < 1) or (num > 69) or (num == powerBallers[currentPlayer].numbers[0]) or (num == powerBallers[currentPlayer].numbers[1]) or (num == powerBallers[currentPlayer].numbers[2]):
                print "Invalid entry"
            else:
                print num
                powerBallers[currentPlayer].addNumbers(num)
                counter += 1
        if counter == 4:
            print "Enter 5th # (1 thru 69 excluding",powerBallers[currentPlayer].numbers[0],",",powerBallers[currentPlayer].numbers[1],",",powerBallers[currentPlayer].numbers[2],"and",powerBallers[currentPlayer].numbers[3],"):"
            num = input()
            if (num < 1) or (num > 69) or (num == powerBallers[currentPlayer].numbers[0]) or (num == powerBallers[currentPlayer].numbers[1]) or (num == powerBallers[currentPlayer].numbers[2]) or (num == powerBallers[currentPlayer].numbers[3]):
                print "Invalid entry"
            else:
                print num
                powerBallers[currentPlayer].addNumbers(num)
                counter += 1
        if counter == 5:
            print "Enter powerball # (1 thru 26):"
            num = input()
            if (num < 1) or (num > 26):
                print "Invalid entry"
            else:
                print num
                powerBallers[currentPlayer].addNumbers(num)
                counter += 1

    #asks if there is another person who would like to play
    print "Would another like to play (Y or N)?"
    userAnswer = raw_input()
    if userAnswer == "Y":
        currentPlayer += 1
        counter = 0
    else:
        addPlayer = False

#prints out the selected power ball numbers of the users
numPowerBallers = 0
while numPowerBallers < len(powerBallers):
    print powerBallers[numPowerBallers].name + "",powerBallers[numPowerBallers].numbers[0],"",powerBallers[numPowerBallers].numbers[1],"",powerBallers[numPowerBallers].numbers[2],"",powerBallers[numPowerBallers].numbers[3],"",powerBallers[numPowerBallers].numbers[4],"Powerball:",powerBallers[numPowerBallers].numbers[5]
    numPowerBallers += 1

powerBallLength = 0
powerBallCount = 0
powerBallExists = False
finalPowerBall = []

while powerBallLength < 6:
    #checks if the two numbers are equal
    #if they are, add the number to the final powerball number
    #if not, move on to generating a random number
    if powerBallers[0].numbers[powerBallLength] == powerBallers[1].numbers[powerBallLength]:
        finalPowerBall.append(powerBallers[0].numbers[powerBallLength])
        powerBallLength += 1
    else:
        #generates a random number between 1 and 69
        #if the number is already apart of the final powerball sequence, doesn't move on
        #if it is, moves on to the next number
        randomPowerNumber = randint(1,69)
        if powerBallLength != 0:
            while powerBallCount < powerBallLength:
                if randomPowerNumber == finalPowerBall[powerBallCount]:
                    powerBallExists = True
                powerBallCount += 1
        if not powerBallExists:
            finalPowerBall.append(randomPowerNumber)
            powerBallLength += 1

#prints out the winning powerball number
print "Winning Powerball Number:",finalPowerBall[0],"",finalPowerBall[1],"",finalPowerBall[2],"",finalPowerBall[3],"",finalPowerBall[4],"Powerball:",finalPowerBall[5]