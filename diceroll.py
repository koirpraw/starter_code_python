from multiprocessing import Event
import random

#range of the values of a dice
min_val = 1
max_val = 8
delay1 = 1

#to loop the rolling through user input
roll_again = "yes"
restart = "yes"

#loop
while roll_again == "yes" or roll_again == "y": 
    print("Rolling The Dices...")
    Event().wait(delay1)
    print("Rolling The Dices...")
    Event().wait(delay1)
    print("The Values are :")
    Event().wait(delay1)

    dice1_roll = random.randint(min_val,max_val)
    dice2_roll = random.randint(min_val,max_val)
    
    #generating and printing 1st random integer from 1 to 6
    # print(random.randint(min_val, max_val))
    print(dice1_roll)
    print(dice2_roll)
    
    #generating and printing 2nd random integer from 1 to 6
    # print(random.randint(min_val, max_val))
    
    #asking user to roll the dice again. Any input other than yes or y will terminate the loop
    roll_again = input("Do you wanna play again?") 
else:
    print("The game is over")
    Event().wait(delay1)
    print(". . .")
    Event().wait(delay1)
    restart=input("Do you want to Re-start?")

    

while restart == "yes" or restart =="y":
    print("Game re-started !")
    Event().wait(delay1)
    print("Rolling Dices")
    Event().wait(delay1)
    print(". . .")
    Event().wait(delay1)
    print("And the numbers are...")
    
    
    print(dice1_roll)
    print(dice2_roll)

    roll_again = input("Do you wanna play again?") 




    



    