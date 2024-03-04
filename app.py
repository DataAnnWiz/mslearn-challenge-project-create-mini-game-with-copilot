import random

score = 0
options = ['rock','paper','scissors']
rules = {'rock': 'scissors', 'paper': 'rock', 'scissors': 'paper'}

while(1) :
    comp_choice = options[random.randint(0,2)]
    player_choice = input("Choose either rock, paper or scissor: ").lower()
    print(comp_choice)
    if(player_choice not in options) :
        print("Invalid Input")
    elif(player_choice == comp_choice) :
        print("Tied with the opponent")
    elif(player_choice == rules[comp_choice]) :
        print("Opponent wins")
    else :
        print("You win!")
        score += 1
    if (input("Do you wanna play again? ").lower() == "no"):
        print(f"your total score is {score}" )
        break