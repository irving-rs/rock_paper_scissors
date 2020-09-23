#rock_paper_scissors.py
#Date: 23/September/2020
#by irving-rs

#Description:
#The classical Game: Rock-Paper-Scissors

#Preparatives:
from random import randrange #To perform an aleatory selection.

#Functions:
def result(x, y):
    global victory, draw, losses
    if x == y: #If they chose the same weapon.
        print("\nDraw!")
        draw += 1
    else:
        if x==1: #User chose Rock.
            if y==2: #User chose Rock and machine chose Paper.
                print("\nYou lost -> Paper covers rock!")
                losses += 1
            else: #User chose Rock and machine chose Scissors.
                print("\nYou won -> Rock crushes scissors!")
                victory += 1
        if x==2: #User chose Paper.
            if y==1: #User chose Paper and machine chose Rock.
                print("\nYou won -> Paper covers rock!")
                victory += 1
            else: #User chose Paper and machine chose Scissors.
                print("\nYou lost -> Scissors cuts paper!")
                losses += 1
        if x==3: #User chose Scissors.
            if y==1: #User chose Scissors and machine chose Rock.
                print("\nYou lost -> Rock crushes scissors!")
                losses += 1
            else: #User chose Scissors and machine chose Paper.
                print("\nYou won -> Scissors cuts paper!")
                victory += 1

#Variables:
victory = 0 #Counts the number of victories.
draw = 0 #Counts the number of draws.
losses = 0 #Counts the number of defeats.
matches = 0 #Counts the number of matches.
dict_comp = {1:"rock", 2:"paper", 3:"scissors"}

#Presentation of the game:
print("\nROCK - PAPER - SCISSORS")

#Rules:
print("\nRules:")
print("i. Rock crushes scissors.")
print("ii. Paper covers rock.")
print("iii. Scissors cuts paper.")
print("iv. Same selection (e.g, rock vs rock) = draw.")

while True:
    matches += 1
    print("\n-----------------------------------------------------")
    print("Match number", matches)

    #User and computer selection:
    print("\nChoose your weapon:")
    print("1) Rock     2) Paper     3) Scissors     4) Exit")
    sel_user = int(input("\nSelection: ")) #User selection.
    sel_machine = randrange(1,4) #Aleatory computer selection.

    #Exit option:
    if sel_user == 4:
        print("\nSee you later.")
        break
    
    #Displays selections:
    print("User has selected:", dict_comp[sel_user])
    print("Computer has selected:", dict_comp[sel_machine])

    result(sel_user, sel_machine) #Decides the result.

    #Statistics:
    print("\nStatistics:")
    print("Victories:", victory, "     Draws:", draw, "     Losses:", losses) #Results
