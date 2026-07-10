menu = {}
restart = True
while restart is True:
    dish = input("Enter Dish Name : ")
    price = input("Enter Price : $")
    menu[dish] = price
    remain = input("Wanna Continue? (yas/no) ").upper()
    if remain == "NO":
        restart = False

for dish, price in menu.items():
    print(f"{dish} : ${price}")
