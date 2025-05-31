import random

# ASCII Art for rock, paper, scissors
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# List of actions and their corresponding numbers
actions = [rock, paper, scissors]

# User input
user = int(input("Press '0' for Rock, '1' for Paper, and '2' for Scissors:\n"))

# Check for valid input
if user < 0 or user > 2:
    print("Invalid Input! Please try again.")
else:
    # Display user's choice
    print("You chose:")
    print(actions[user])

    # Computer randomly chooses
    computer = random.randint(0, 2)
    print("Computer chose:")
    print(actions[computer])

    # Determine the result
    if user == computer:
        print("It's a Draw!")
    elif (user == 0 and computer == 2) or (user == 1 and computer == 0) or (user == 2 and computer == 1):
        print("You Win!")
    else:
        print("You Lose!")
