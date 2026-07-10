import random
art = """
██╗░░██╗░█████╗░███╗░░██╗░██████╗░███╗░░░███╗░█████╗░███╗░░░███╗
██║░░██║██╔══██╗████╗░██║██╔════╝░████╗░████║██╔══██╗████╗░████║
███████║███████║██╔██╗██║██║░░██╗░██╔████╔██║███████║██╔████╔██║
██╔══██║██╔══██║██║╚████║██║░░╚██╗██║╚██╔╝██║██╔══██║██║╚██╔╝██║
██║░░██║██║░░██║██║░╚███║╚██████╔╝██║░╚═╝░██║██║░░██║██║░╚═╝░██║
╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝░╚═════╝░╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░░░░╚═╝
"""
print(art)


print("WELCOME TO HANGMAN. YOU HAVE TO GUESS A WORD BY CHOOSING A LETTER")
print("YOU HAVE TOTAL 6 LIVES OTHERWISE U WILL BE HANGED OVER")
stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
word = ["APPLE" , "BANANA" , "STAR" , "ROSE" , "SKY"]
lives = 6
rword = random.choice(word)
length = len(rword)
placeholder = ""
for position in range(length):
    placeholder += "_"
print(placeholder)

game_over = False
correct = []
while not game_over:
    user = input("\nENTER A LETTER TO GUESS : ").upper()

    if user in correct :
        print(f"YOU HAVE AlREADY GUESSED {user}")

    display = ""
    for letter in rword :
        if letter == user:
            display += letter
            correct.append(letter)
        elif letter in correct:
            display += letter
        else :
            display += "_"
    print("Word To Guess : " ,display)

    if user not in correct:
        lives -= 1
        print(f"YOU GUESSED {user} .THAT IS NOT IN A WORD ")
        print(f"NOW U HAVE {lives} LIVES")
        if lives == 0:
            game_over = True

            print(f"IT WAS {rword} . YOU LOSE")

    if "_" not in display:
        game_over = True
        print("You Won")

    print(stages[lives])

