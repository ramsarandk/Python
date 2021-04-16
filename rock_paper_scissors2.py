computer_choice = 'R'
user_choice = input("What do you choose?'R', 'P' or 'S'\n")
if user_choice == computer_choice:
    print("Tie")
elif user_choice == 'R' and computer_choice == 'S':
    print("You Win")
elif user_choice == 'P' and computer_choice == 'R':
    print("You Win")
elif user_choice == 'S' and computer_choice == 'P':
    print("You Win")
else:
    print("Computer Wins")
    

