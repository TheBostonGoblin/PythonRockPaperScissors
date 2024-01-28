
#Application by Daniel Joseph Jr.
import random

#intial variables
opponetMove = ["rock","paper","scissors"];
won = False;
randomInt = random.randint(0,2);

#While the user has not won keep playing
while won == False:
    
    #Ask the user for input   
    userInput = input("Enter your move(rock,paper,scissors):");
    print("Your Input:"+userInput);
    randomInt = random.randint(0,2);
    
    print("Opponent Input:"+opponetMove[randomInt]);
    
    #sanitize user input
    userInput = userInput.lower();

    #By checking for a tie first we can reduce the amount of conditional statements we need to go through
    if userInput == opponetMove[randomInt]:
        print("Tie Try Again");
    
    elif userInput == "rock":
        
        if opponetMove[randomInt] == "paper":
            print("Your opponet covered your rock with paper [YOU LOSE] try again");
        else:
            print("You crushed the scissors with your rock");
            won = True;
    
    elif userInput == "paper":
        
        if opponetMove[randomInt] == "scissors":
            print("Your opponet cut your paper with scissors [YOU LOSE] try again");
        else:
            print("You covered your opponets rock with your paper")
            won = True;
    
            
    elif userInput == "scissors":
        
        if opponetMove[randomInt] == "rock":
            print("Your opponet crushed your sciossors with a rock [YOU LOSE] try again");
        else: 
            print("You cut your opponets paper with your scissors");
            won = True;
    
    
    #Checking for invalid inputs  
    else:
        print("invalid input try again");

print("You Won!!! :D")