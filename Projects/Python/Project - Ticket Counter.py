h = int(input("ENTER YOUR HEIGHT : "))

if h > 120 :
    print("YOU CAN RIDE")
    age = int(input("ENTER YOUR AGE : "))
    if age <= 12 :
        bill=5
        print("CHILD TICKETS : 5$")
    elif age <= 18 :
        bill=7
        print("TEEN TICKETS : 7$")
    else :
        bill=12
        print("ADULT TICKETS : 12$")

    photo = input("YOU WANT TO CLICK PHOTO (YES / NO ) : ")
    if photo == "YES"  :
        bill += 3
        print("TOTAL IS : ",bill)
    else :
        print("TOTAL IS : ",bill,"$")
else:
    print("YOU CANT RIDE")
