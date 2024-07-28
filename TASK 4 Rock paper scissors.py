print("Rock,Paper and Scissors game")
import random
def get_computer_choice():
    choices=['rock','paper','scissors']
    return random.choice(choices)

def determine_winner(user_choice,computer_choice):
    if(user_choice==computer_choice):
        return "tie"
    elif((user_choice=='rock'and computer_choice=='scissors') or (user_choice=='paper' and computer_choice=='rock') or 
         (user_choice=='scissors' and computer_choice=='paper')):
        return "user"
    else:
        return "computer wins"

user_score=0
computer_score=0
print("Welcome to the game")
while True:
    user_choice=input("Enter your choice(rock, paper, or scissors):").lower()
    if user_choice not in ['rock','paper','scissors']:
        print("Invalid input.Please enter among choices")
        continue
    get=get_computer_choice()
    print("Computer choice is:",get)
    winner=determine_winner(user_choice,get)
    if(winner=='tie'):
        print("It's a tie")
    elif(winner=='user'):
        print("You win")
        user_score+=1
    else:
        print("Computer wins!")
        computer_score+=1
    print("Computer-",computer_score,"You",user_score)
    play_again=input("Do you want play again?(yes/no)").lower()
    if(play_again!='yes'):
        break
print("BYE final score")
print("Your score",user_score)
print("Computer score",computer_score)