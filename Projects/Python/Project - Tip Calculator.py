print("WELCOME TO THE TIP CALCULATOR")
bill=float(input("ENTER TOTAL BILL : "))
tip=float(input("HOW MUCH TIP WOULD U LIKE TO GIVE (10% , 12% , 15%) : "))
person = int(input("HOW MANY PEOPLE TO SPLIT THE BILL : "))
total= tip/100*bill+bill
each = total/person
final=round(each,2)
print(f"EACH PERSON SHOULD PAY : {final}")
