
"""
Date: 23/04/2015.
Student: Kim Anh Nguyen
Student ID: 13138914
Basic description: Golf Game
    User can see menu with 3 options: instruction, play the game, and quit
    Program always returns to menu, only if quit is chosen
    When the game starts: Each swing, user selects one of 3 clubs,
    Program generates distance for each shot
    The game continues until the ball is in the hole.
"""

"""
Pseudocode

def main()
    Display a welcome message with name in it

    # Display menu
    display Golf
    display Instruction
    display Playround
    display Quit

    # Select option in menu
    get selectOption

    while selectOption!="Q" and selectOption!="q" # when Quit isn't chosen

        if selectOption=="I" or selectOption=="i" # when Instruction is chosen
            display Instruction
            
        else if selectOption=="P" and selectOption=="p" # when Playround is chosen
            call function playRound()

        # when none of the menu options is chosen                            
        else    
            display Invalid menu choice

        # Display menu and get user choose option
        display menu
        get selectOption
            
    # User quits the game    
    display thanks message


def playRound()

    # Import random library to generate random integer numbers
    import random function

    # Declare CONSTANTs
    TARGET=230 # The origin distance: 230m
    PAR_NUM=5 # par=5
    AVG_DISTANCE_D=100 # The average distance of Driver: 100m
    AVG_DISTANCE_I=30  # The average distance of Iron: 30m
    AVG_DISTANCE_P=10 # The average distance of Putter: 10m
    LOW_RATE=0.8 # Lower limit rate of average distance:80%
    HIGH_RATE=1.2 # High limit rate of average distance: 120%
    MIN_DISTANCE_SHOT_P=1 # Minimum distance of Putter can hit: 1m
    
    # Display general information
    display This hole is a TARGET m par PAR_NUM
    display Club selection: press D for driver, I for Iron, P for Putter
    display You are TARGET from the hole, after 0 shot/s
       
    # Declare variables to trace number of shots, distance to Target after each shot
    # Note: Use word "Target" in distanceToTarget to refer to the current distance to the hole updated
    # And word "Hole" to distanceToHoleI to refer the location of ball relative to the hole when Iron selected, for example.

    countShot=0
    distanceToTarget=TARGET

    # Declare a Boolen variable to check whether ball is in the hole
    isInHole=False

    while not isInHole

        # Get a club to start playing
        ask chooseClub
    
        # Driver is chosen for the shot
        if chooseClub=="D" or chooseClub=="d"

            # Generate the exact distance of the shot of Driver
            distanceShot=random.randint(AVG_DISTANCE_D*LOW_RATE,AVG_DISTANCE_D*HIGH_RATE) 

            # Calculate the distance to the Hole
            distanceToTarget=abs(distanceToTarget-distanceShot)

            # Update the value for number of shots when using Driver
            countShot+=1

            # Display result of this shot
            display Your shot went distanceShot m
            if distanceToTarget!=0
               display You are distanceToTarget m from the hole after countShot shot/s
                       
        # Iron is chosen for the shot
        else if chooseClub=="I" or chooseClub=="i"

            # Genrate the exact distance of the shot of Iron
            distanceShot=random.randint(AVG_DISTANCE_I*LOW_RATE,AVG_DISTANCE_I*HIGH_RATE)

            # Calculate the distance to the Hole
            distanceToTarget=abs(distanceToTarget-distanceShot)

            # Update the value for number of shots when using Iron
            countShot+=1

            # Display result of this shot
            display Your shot went distanceShot m
            if distanceToTarget!=0
                display You are distanceToTarget m from the hole after countShot shot/s
                   
        # Putter is chosen and ball is inside AVG_DISTANCE_P at the same time
        else if (chooseClub=="P" and distanceToTarget<AVG_DISTANCE_P)or (chooseClub=="p" and distanceToTarget<AVG_DISTANCE_P)

            # When distanceToTarget=MIN_DISTANCE_SHOT_P
             if distanceToTarget==MIN_DISTANCE_SHOT_P
                countShot+=1
                display Your shot went distanceToTarget m
                update the value for distanceToTarget=0

            # When current distanceToTarget <AVG_DISTANCE_P
             else    

                # Generate the exact distance of the shot of Putter
                distanceShot=randan.randint(int(distanceToTarget*LOW_RATE),int(distanceToTarget*HIGH_RATE))

                # Calculate the distance to the hole
                distanceToTarget=abs(distanceToTarget-distanceShotInsideP)

                # Update the value for number of shots when satisfying Putter and inside AVG_DISTANCE_P
                countShot+=1

                # Display result of this shot
                display Your shot went distanceShot m

                # if distanceToTarget!=0
                     display You are distanceToTarget m from the hole after countShot shot/s

               
        # Putter is chosen and the distanceToTarget >=AVG_DISTANCE_P
        else if chooseClub=="P" or chooseClub=="p"

            # Generate the exact distance of the shot of Putter
            distanceShot=random.randint(AVG_DISTANCE_P*LOW_RATE,AVG_DISTANCE_P*HIGH_RATE)

            # Calculate the distance to the hole
            distanceToTarget=abs(distanceToTarget-distanceShot)

            # Update the value for number of shots
            countShot+=1
            
            # Display the result of this shot
            display Your shot went distanceShot m
            if distanceToTarget!=0
                display You are distanceToTarget m from the hole after countShot shot/s

            
        # user chose an invalid club, the ball doesn't move, still count number of shots
        else
            distanceShot=0
            countShot+=1

            # Display the result of this shot
            display Invalid club selecion=air swing :(
            display Your shot went distanceShot m
            display You are distanceToTarget m from the hole after countShot shot/s

           
        # When the ball's in the hole   
        if distanceToTarget==0

            # The boolen variable changes from False to True, escape from the while loop 
            isInHole=True

            # Display total of shots taken to get the ball into the hole
            display Cluck...After countShot hits, the ball is in the hole!

            # Display complements depending on total of shots taken and PAR_NUM
            if countShot>PAR_NUM
                display Disappointing. You are over (countShot-PAR_NUM) over par
            else if countShot<PAR_NUM
                display Congratulations. Your are (PAR_NUM-countShot) under par
            else
                 display And that's par
           
# Call main() function to execute the codes
main()
"""            

"""
Python codes
"""

def main():
    # Display a welcome message with name in it
    print("Let's play golf, CP1200 style!")
    print("Written by Kim Anh Nguyen, April 2015","\n")

    # Display menu
    print("Golf!")
    print("(I)nstructions")
    print("(P)lay round")
    print("(Q)uit")
            
    # Select option in menu
    selectOption=input(">>> ")
    
    while selectOption!="Q" and selectOption!="q": # when Quit isn't chosen

        # When Instruction is chosen
        if selectOption=="I" or selectOption=="i":
            print("Instructions: It's golf on your console.")
            print("For each shot, you may use a driver, iron, or a putter - each shot will vary in distance.")
            print("The average distance each club can hit is: Driver = 100m, Iron = 30m, Putter = 10m","\n")
            
        # When Playround is chosen 
        elif selectOption=="P" or selectOption=="p":
            playRound()
                                    
        # When none of the menu options is chosen
        else:
            print("Invalid menu choice.","\n")

        # Display menu and get user choose option
        print("Golf!")
        print("(I)nstructions")
        print("(P)lay round")
        print("(Q)uit")

        # Select other option
        selectOption=input(">>> ")

    # user quits the game, say thanks        
    print("Thanks for playing.")   
    
def playRound():

    # Import random library to generate random integer numbers
    import random

    # Declare CONSTANTs
    TARGET=230 # The origin distance: 230m
    PAR_NUM=5 # par=5
    AVG_DISTANCE_D=100 # The average distance of Driver: 100m
    AVG_DISTANCE_I=30  # The average distance of Iron: 30m
    AVG_DISTANCE_P=10 # The average distance of Putter: 10m
    LOW_RATE=0.8 # lower limit rate of average distance:80%
    HIGH_RATE=1.2 # high limit rate of average distance: 120%
    MIN_DISTANCE_SHOT_P=1 # Minimum distance of Putter can hit: 1m
    
    # Display general information
    print("This hole is a ",TARGET,"m par ",PAR_NUM,sep="")
    print("Club selection: press D for driver, I for Iron, P for Putter.")
    print("You are ",TARGET,"m from the hole, after 0 shot/s",sep="")
       
    # Declare variables to trace number of shots, distance to Target after each shot
    # Note: Use word "Target" in distanceToTarget to refer to the current distance to the hole updated
    # And word "HoleD" to distanceToHoleD to refer the location of ball relative to the hole when Driver selected, for example.
    countShot=0
    distanceToTarget=TARGET

    # Declare a Boolen variable to check whether ball is in the hole
    isInHole=False
      
    while not isInHole:

        # Get a club to start playing
        chooseClub=input("Choose club: ")

        # Driver is chosen for the shot
        if chooseClub=="D" or chooseClub=="d":

            # Generate the exact distance of the shot of Driver
            distanceShot=random.randint(AVG_DISTANCE_D*LOW_RATE,AVG_DISTANCE_D*HIGH_RATE) 

            # Calculate the distance to the Hole
            distanceToTarget=abs(distanceToTarget-distanceShot)

            # Update the value for number of shots when using Driver
            countShot+=1

            # Display result of this shot
            print("Your shot went ",distanceShot,"m",sep="")
            if distanceToTarget!=0:
                print("You are ",distanceToTarget,"m from the hole, after ",countShot," shot/s",sep="")

            
        # Iron is chosen for the shot   
        elif chooseClub=="I" or chooseClub=="i":

            # Generate the exact distance of the shot of Iron
            distanceShot=random.randint(AVG_DISTANCE_I*LOW_RATE,AVG_DISTANCE_I*HIGH_RATE)

            # Calculate the distance to the Hole
            distanceToTarget=abs(distanceToTarget-distanceShot)

            # Update the value for number of shots when using Iron
            countShot+=1

            # Display result of this shot
            print("Your shot went ",distanceShot,"m",sep="")
            if distanceToTarget!=0:
                print("You are ",distanceToTarget,"m from the hole, after ",countShot," shot/s",sep="")

            
        # Putter is chosen and ball is inside AVG_DISTANCE_P at the same time
        elif (chooseClub=="P" and distanceToTarget<AVG_DISTANCE_P)or(chooseClub=="p" and distanceToTarget<AVG_DISTANCE_P):

            # when the current distance to target is equal (MIN_DISTANCE_SHOT_P)
            if distanceToTarget==MIN_DISTANCE_SHOT_P:
                countShot+=1
                print("Your shot went ",distanceToTarget,"m",sep="")

                # Update the value for distance to target = 0, the ball's in the hole
                distanceToTarget=0

            # when distanceToTarget< AVG_DISTANCE_P 
            else:
                
                # Generate the exact distance of the shot of Putter
                distanceShot=random.randint(int(distanceToTarget*LOW_RATE),int(distanceToTarget*HIGH_RATE))

                # Caluclate for distance to the hole
                distanceToTarget=abs(distanceToTarget-distanceShot)

                # Update the value for number of shots
                countShot+=1

                # Display result of this shot
                print("Your shot went ",distanceShot,"m",sep="")

                if distanceToTarget !=0:
                    print("You are ",distanceToTarget,"m from the hole, after ",countShot," shot/s",sep="")

                
        # Putter is chosen and the current distance between ball and the hole >= AVG_DISTANCE_P
        elif chooseClub=="P" or chooseClub=="p":

            # Generate the exact distance of the shot of Putter
            distanceShot=random.randint(AVG_DISTANCE_P*LOW_RATE,AVG_DISTANCE_P*HIGH_RATE)

            # Calculate the distance to the hole
            distanceToTarget=abs(distanceToTarget-distanceShot)

            # Update value for number of shots
            countShot+=1

            # Display the result of this shot
            print("Your shot went ",distanceShot,"m",sep="")
            if distanceToTarget !=0:
                print("You are ",distanceToTarget,"m from the hole, after ",countShot," shot/s",sep="")

        # user selects an invalid club, the ball doesn't move, still counting number of shots
        else:            
            distanceShot=0
            countShot+=1

            # Display the result of this shot
            print("Invalid club selection = air swing :(")
            print("Your shot went ",distanceShot,"m",sep="")
            print("You are ",distanceToTarget,"m from the hole, after ",countShot," shot/s",sep="")

            
        # When the ball's in the hole
        if distanceToTarget==0:

            # Boolen variable change from False to True, escape from while loop
            isInHole=True   

            # Display total of shots taken to get the ball into the hole
            print("Cluck... After ",countShot," hits, the ball is in the hole!",sep="")

            # Display complements depending on total of shots taken and PAR_NUM
            if countShot>PAR_NUM:
                print("Disappointing. You are ",(countShot-PAR_NUM)," over par.",sep="")
            elif countShot<PAR_NUM:
                print("Congratulations. Your are ",(PAR_NUM-countShot)," under par.","\n",sep="")
            else:
                print("And that's par.","\n")

# Call main() function to execute the codes
main()

        

























            
































    
