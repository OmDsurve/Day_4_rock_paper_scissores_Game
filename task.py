import random
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
game_images = [rock, paper, scissors]
user_choice = int(input("what is your choice 0 for rock, 1 for paper and 2 for scissors "))
computer_choice = random.choice([0,1,2])
print("Computer Chose ")
print(game_images[computer_choice])
print("You chose")
print(game_images[computer_choice])

if user_choice == 0 and computer_choice == 2:
    print("You Win!")
elif user_choice == 0 and computer_choice == 1:
    print("You Lose!")
elif user_choice == 0 and computer_choice == 0:
    print("Its a Draw!")
elif user_choice == 1 and computer_choice == 0:
    print("You lose!")
elif user_choice == 1 and computer_choice == 2:
    print("You Win!")
elif user_choice == 1 and computer_choice == 1:
    print("Its a Draw!")
elif user_choice == 2 and computer_choice == 0:
    print("You lose!")
elif user_choice == 2 and computer_choice == 1:
    print("You Win!")
elif user_choice == 2 and computer_choice == 2:
    print("Its a Draw!")
else:
    print("You did invalid move!")


