import random
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
            'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbol = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

alpha = input("How Many Letter Would You Like : ")
num = input("How Many Numbers Would You Like : ")
sym = input("How Many Symbols Would You Like : ")

# Way 1
password = []
for letter in range(int(alpha)):
    password.append(random.choice(alphabet))
for num in range(int(num)):
    password.append(random.choice(number))
for sym in range(int(sym)):
    password.append(random.choice(symbol))
random.shuffle(password)
print("".join(password))


# Way 2
password = ""
for char in range(0, alpha):
    password += random.choice(alphabet)
for n in range(0, num):
    password += random.choice(number)
for s in range(0, sym):
    password += random.choice(symbol)

print(password)






