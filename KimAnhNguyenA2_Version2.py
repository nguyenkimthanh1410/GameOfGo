"""
Date: 17/05/2015.
Student: Kim Anh Nguyen
Student ID: 13138914
Basic description: Golf Game
    User see menu of 4 options: Instructions, View scores, Play round, Quit
    Program always returns to menu, only if quit is chosen
    When the game starts:
            Each swing, user selects one of 4 clubs,
            Program generates random distance for each shot
            The game continues until the ball is in the hole.
    View scores: Display names and scores in assending order        
"""
"""
Pseudocode:


# Declare GLOBAL CONSTANTS

Minimum character of name
Maximum character of name
Minimum number of rounds to play
Maximum number of rounds to play
Filename will be used to record the scores

Dictionary to store list of clubs and its properties
the club's information will be kept with key-value pair
in format as follow:
one (key: value pair) = "symbol character":(name club, length of club)

Minimum distance of Putter can hit
Origin distance of the ball
Par value
Low limit rate of average distance
High limit rate of average distance


1.Define main function
    Display a welcom message with programer's name
    Get valid name
    Display choice menu
    Get choice
        while choice not equal to Quit
              if choice is I
                 display Instructions
                 display list of clubs to choose
               else if choice is V
                  display all scores, names kept in scores.txt in assending order
               else if choice is P
                  player will play round
               else
                  display invalid menu choice
               Display choice menu
               Get choice again
        Display thanks for playing.

2. Define getValidName, check name's length, with 2 parameters (prompt, error message)
    User keys in name with prompt
    while length of name doesn't fall into range of min, max number of characters
        display error message
        ask user to key in other name
    return name


3. Define function to display club selection
    for each abbreviation in dictionary keys
        display fullname and length of each club

4. Define function to view score
"""

"""
Python codes
"""

# Declare GLOBAL CONSTANTS
MIN_NAME_CHAR = 1 # Minimum character of name
MAX_NAME_CHAR = 27 # Maximum character of name

MIN_ROUND = 1 # Minimum number of round to play
MAX_ROUND = 9 # Maximum number of round to play

FILE_NAME = 'scores.txt' # File to read or write scores

# key &(name, value) of clubs stored in a dictionary
DICT_CLUBS = {'7':('7 Iron',30),
             'D':('Driver',100),
             'P':('Putter',10),
             '3':('3 Iron',60)} 

MIN_LEN_P = 1 # Minimum distance of Putter can hit: 1m
TARGET = 230 # The origin distance: 230m
PAR_NUM = 5 # par=5
LOW_RATE = 0.8 # Lower limit rate of average distance:80%
HIGH_RATE = 1.2 # High limit rate of average distance: 120%
    
def main():

    # Display a welcome message with name in it
    print("""Let's play golf, CP1200 style!
Written by Kim Anh Nguyen, May 2015
"""
,end='')

         
    # Get valid name
    name = getValidName('Please enter your name: ',\
                        'Your name can not be blank and must be <= 27 characters')


    # Get choice and execute codes associated with choice
    viewMenuChoice()
    choice = input('>>> ')
    choice = choice.upper()
    while choice != 'Q':
       if choice == 'I':
           print("""Instructions: It's a golf on your console. Each shot will vary in distance around
its average.
"""
,end='')
           viewClubSelection()
       elif choice == 'V':
           viewScores()
       elif choice == 'P':
           playRound(name)
       else:
           print('Invalid menu choice.')
       viewMenuChoice()
       choice = input('>>> ')
       choice = choice.upper()
    print('Thanks for playing.')  
    
# Function getValidName error-checking name to satisfy name's length
def getValidName (prompt,errorMessage):
    name = input(prompt)
    while len(name) not in list(range(MIN_NAME_CHAR, MAX_NAME_CHAR)):
        print(errorMessage)
        name = input(prompt)
    return name

# Function to display options of menu choice
def viewMenuChoice():
    print("""
Golf!
(I)structions
(V)iew scores
(P)lay round
(Q)uit
"""
,end='')

# Function to display club selection
def viewClubSelection():
    print('Club selection:')
    for key in DICT_CLUBS.keys():
        nameClub,lenClub = DICT_CLUBS.get(key)
        print(key, ' for ', nameClub, ' (',lenClub,')',sep='')
        
# Function to view players' scores
# Read scores from the file, store values into a list, sort list
# Display results in ascending order
def viewScores():
    scores = []
    fileIn = open(FILE_NAME, 'r')
    for line in fileIn:
        line = line.strip().split(', ')
        record = (int(line[0]),line[1])
        scores.append(record)
    scores.sort()
    for score, name in scores:
        print(name,' '*(27-len(name)), format(score,'2,d'))
    fileIn.close()

# Function to error-checking valid number of rounds to play
# Check number of round  is digits, alpha
def getValidRound(prompt,errorMessage):
    isRoundInvalid = True
    numRound = input(prompt+ ' ('+ str(MIN_ROUND)+ '-'+ str(MAX_ROUND)+ ') ')
    while isRoundInvalid:
        if numRound.isdigit():
            if int(numRound) not in range(MIN_ROUND,MAX_ROUND+1):
                print(errorMessage)
            else:
                isRoundInvalid = False
        elif numRound.isalpha():
            print(errorMessage)
        else:
            print(errorMessage)
        if isRoundInvalid == True:
            numRound = input(prompt+ ' ('+ str(MIN_ROUND)+ '-'+ str(MAX_ROUND)+ ') ')
    return int(numRound)

# Function to calculate result of each shot
def calculateShotResult(distanceToTarget,countShot,club):

    # Import random function to calculate result of shot
    import random
    
    lenClub = DICT_CLUBS.get(club)[1]
    distanceShot = random.randint(int(lenClub*LOW_RATE),int(lenClub*HIGH_RATE))
    distanceToTarget = abs(distanceToTarget - distanceShot) # get the absolute value
    countShot +=1
    return distanceShot, distanceToTarget, countShot

# Function to save score by appending a new score to the existing file
def saveScoreIntoFile(countShot,name):
    fileOut = open(FILE_NAME, 'a')
    fileOut.write(str(countShot)+ ', '+ name+ '\n')
    fileOut.close()

# Function to error-checking save score
def getValidOptionSave(name):
    saveScore = input('Would you like to save your score, '\
                      + name.strip().split()[0]+ '? (Y/N) ')
    saveScore=saveScore.upper()

    while saveScore not in('Y','N'):
        print('Please enter Y or N')
        saveScore = input('Would you like to save your score, '\
                          + name.strip().split()[0]+ '? (Y/N) ')
        saveScore=saveScore.upper()
    return saveScore

# Play round with a given player

def playRound(name):

    numRound = getValidRound('How many rounds would you like to play? ',\
                             'Invalid number of rounds')

    import random

    # For each round, player plays by choosing clubs
    # The each round only finishs when the ball is in the hole
    for round in list(range(1,numRound+1)):
        print()

        # Display general information
        print('Round', round, sep = ' ')
        print('This hole is a ', TARGET, 'm par ',PAR_NUM,sep='')
        
        viewClubSelection()
        print('You are ', TARGET, 'm from the hole, after 0 shot/s',sep='')

        # Declare varibales: countShot to trace number of shots
        # distanceToTarget to trace the distance to Target after each shot
        countShot = 0
        distanceToTarget = TARGET # The postion at the beginning

        # Declare a boolen variable isInHole as a flag when the ball is in the hole
        isInHole = False

        while not isInHole:

            # Pick a club to start playing
            chooseClub = input('Choose club: ')
            chooseClub = chooseClub.upper()

            # Calulate result for each shot
            if chooseClub == 'D': # Driver is chosen
                distanceShot, distanceToTarget, countShot = calculateShotResult(distanceToTarget,countShot,chooseClub)
                                
            elif chooseClub == '7': # 7 Iron is chosen
                distanceShot, distanceToTarget, countShot = calculateShotResult(distanceToTarget,countShot,chooseClub)
                                
            elif chooseClub == '3':  # 3 Iron is chosen
                distanceShot, distanceToTarget, countShot = calculateShotResult(distanceToTarget,countShot,chooseClub)
                
            # club P is chosen & ball within lenP
            # Length of club P: lenP = dictClubs.get('P')[1] 
            
            elif (chooseClub == 'P' and distanceToTarget < DICT_CLUBS.get('P')[1]): 

                # min distance Putter can hit the ball
                if distanceToTarget == MIN_LEN_P: 
                    distanceShot = MIN_LEN_P
                    distanceToTarget = 0
                    countShot += 1

                # Calculate distance of shot, distance to target, count shot    
                else:
                    distanceShot = random.randint(int(distanceToTarget*LOW_RATE),\
                                                  int(distanceToTarget*HIGH_RATE))
                    distanceToTarget = abs(distanceToTarget - distanceShot)
                    countShot += 1

            # club P is chosen, distance >= min len of P 
            elif chooseClub == 'P': 
                distanceShot, distanceToTarget, countShot = calculateShotResult(distanceToTarget,countShot,chooseClub)

            # User picked an invalid club, ball does not move
            # still count number of shots
            else: 
                distanceShot = 0
                countShot += 1
                print("Invalid club selection = air swing :(")
                viewClubSelection()

            # Display the result of each shot
            print('Your shot went ',distanceShot,'m',sep='')

            # Ball is still outside the hole
            if distanceToTarget != 0: 
                print('Your are ',distanceToTarget,\
                  'm from the hole, after ',countShot,' shot/s',sep='')

            # When the ball is in the hole, the distanceToTarget == 0
            else: 
                isInHole = True # the flag shows up
                print('Cluck... After ',countShot,' hits, the ball is in the hole!',sep='')

        # Display complements depending on total shots taken and PAR_NUM
        if countShot > PAR_NUM:
            print('Disappointing. You are ',countShot-PAR_NUM,' over par.',sep='')
        elif countShot < PAR_NUM:
            print('Congratulations. You are ',PAR_NUM-countShot,' under par.','\n',sep='')
        else:
            print("And that's par.","\n")

        saveScore = getValidOptionSave(name)

        # User chose to save score
        if saveScore == 'Y': 
            saveScoreIntoFile(countShot,name)
            print('Score saved. New high scores:')
            viewScores()
                          
# Call main function to excute the code                          
main()
                        
                        
                
                
            
                
                
    





















