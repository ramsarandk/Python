import random
computer_choice = random.choice(['rock', 'scissors','paper']) 
user_choice = input("Do you choose rock, paper or scissors?\n")
if user_choice == computer_choice:
    print("Tie! The computer had " + computer_choice)
elif user_choice == 'paper' and computer_choice == 'rock':
    print("You win! The computer had " + computer_choice)
elif user_choice == 'scissors' and computer_choice == 'rock':
    print("Computer Wins! The computer had " + computer_choice)
elif user_choice == 'rock' and computer_choice == 'paper':
    print("You win! The computer had " + computer_choice)
else:
    print("Computer Wins! The computer had " + computer_choice)


