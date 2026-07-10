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

image = [rock, paper, scissors]
print("0 - Rock")
print("1 - Paper")
print("2 - Scissors")
you = int(input("Enter your choice: "))

# For User
if you <0 or you>2:
    print("Invalid choice")
else:
    print(image[you])

# For Computer
computer = random.randint(0,2)
print("Computer Choice")
print(image[computer])


# To Check The Game
if you == computer:
    print("It's a tie!")
elif you == 0 and computer == 1 :
    print("You Lose!")
elif you == 0 and computer == 2 :
    print("You Win!")
elif you == 1 and computer == 0:
    print("You Win!")
elif you == 1 and computer == 2 :
    print("You Lose!")
elif you == 2 and computer == 0 :
    print("You Lose!")
elif you == 2 and computer == 1 :
    print("You Win!")
