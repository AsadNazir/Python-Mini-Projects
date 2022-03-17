import os
from string import whitespace
import random

#The game function over here

def Game(rounds):

    RPS=('R','S','P')
    computerPoints=0
    userPoints=0

    while(rounds>0):
       #Inputs for Both Computer and user are taken over here

       userInput=input("Enter a character.\nR or r for Rock\nP or p for paper\nS or S for scissors\n")
       ComputerInput=random.randint(0,2)
        
       #Input Validation over here
       if(len(userInput)>1):
           print("Please enter correct values.\n")
           userInput=input("Enter a character.\nR or r for Rock\nP or p for paper\nS or S for scissors\n")

       #Correct Character Validation 
       while(userInput.capitalize() != 'R' and userInput.capitalize() != 'P' and userInput.capitalize() != 'S'):
           print("\nPlease enter from given Choices \n")
           userInput=input("Enter a character.\nR or r for Rock\nP or p for paper\nS or S for scissors\n\n")

       if(userInput.capitalize()==RPS[ComputerInput]):
            print("Draw....\n")
            print("Computer :",RPS[ComputerInput],"\nYou entered : ",userInput )
            computerPoints+=1
            userPoints+=1

       elif(userInput.capitalize()=="R"and RPS[ComputerInput]=='P'):
            print("Computer Won...\n")
            print("Computer :",RPS[ComputerInput],"\nYou entered : ",userInput )
            computerPoints+=1
        
       elif(userInput.capitalize()=="P"and RPS[ComputerInput]=='R'):
            print("You Won...\n")
            print("Computer :",RPS[ComputerInput],"\nYou entered : ",userInput )
            userPoints+=1
        
       elif(userInput.capitalize()=="S"and RPS[ComputerInput]=='R'):
            print("Computer Won...\n")
            print("Computer :",RPS[ComputerInput],"\nYou entered : ",userInput )
            computerPoints+=1

       elif(userInput.capitalize()=="R"and RPS[ComputerInput]=='S'):
            print("You Won...\n")
            print("Computer :",RPS[ComputerInput],"\nYou entered : ",userInput )
            userPoints+=1
        
       elif(userInput.capitalize()=="S"and RPS[ComputerInput]=='P'):
            print("You Won...\n")
            print("Computer :",RPS[ComputerInput],"\nYou entered : ",userInput )
            userPoints+=1

       elif(userInput.capitalize()=="P"and RPS[ComputerInput]=='S'):
            print("You Won...\n")
            print("Computer :",RPS[ComputerInput],"\nYou entered : ",userInput )
            comoputerPoints+=1

       rounds-=1
    
    print("Computer Score : ",computerPoints,"\nYour Score : ",userPoints)

    if(computerPoints>userPoints):
        print("Computer Won the game...\n")
    else:
        print("You won the game...\n")

    


    return None

Game(4)