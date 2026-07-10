print("WELCOME TO PIZZA CLUB ")
size = str(input("ENTER THE SIZE OF PIZZA YOU WANT S M OR L : ")).upper()
pap = str(input("DO YOU WANT PAPERONI Y / N : ")).upper()
cheeze = str(input("DO YOU EXTRA WANT CHEEZE Y / N : ")).upper()
sp=15
mp = 20
lp = 25
bill = 0

if size == "S" : # FOR SMALL PIZZA
    bill=sp
    if pap == "Y" :
        bill+=2
    else :
        bill=sp
    if cheeze == "Y" :
            bill+=1
            print("TOTAL IS : ",bill,"$")
    else:
            print("TOTAL IS : ",bill,"$")
elif size == "M" : # FOR MEDIUM PIZZA
    bill=mp
    if pap == "Y" :
        bill+=3
    else :
        bill=mp
    if cheeze == "Y" :
            bill+=1
            print("TOTAL IS : ",bill,"$")
    else:
            print("TOTAL IS : ",bill,"$")
elif size == "L" : # FOR LARGE PIZZA
    bill=lp
    if pap == "Y" :
        bill+=3
    else :
        bill=lp
    if cheeze == "Y" :
            bill+=1
            print("TOTAL IS : ",bill,"$")
    else:
            print("TOTAL IS : ",bill,"$")
else : # FOR VALID COMMAND
    print("ENTER VALID COMMAND ")



#  ALTER WAY
# TO CHECK PIZZA SIZE AND PAP
# if size == "S" : # FOR SMALL PIZZA
#     bill=sp
#     if pap == "Y" :
#         bill+=2
#     else :
#         bill=sp
# elif size == "M" : # FOR MEDIUM PIZZA
#     bill=mp
#     if pap == "Y" :
#         bill+=3
#     else :
#         bill=mp
# elif size == "L" : # FOR LARGE PIZZA
#     bill=lp
#     if pap == "Y" :
#         bill+=3
#     else :
#         bill=lp
# else : # FOR VALID COMMAND
#     print("ENTER VALID COMMAND ")
#     exit()
#
# FOR CHEEZE
# if cheeze == "Y" :
#     bill+=1
#
# FINAL OUTPUT
# print("TOTAL IS : ",bill,"$")

# WAY 2
# FOR SIZE
# if size == "S":
#     bill += 15
# elif size == "M":
#     bill += 20
# elif size == "L":
#     bill += 25
# else :
#     print("OOPS : YOU TYPED WRONG ")
#     exit()
#
# # FOR PAP
# if pap == "Y":
#     if size == "S" :
#         bill += 2
#     else :
#         bill += 3
#
#
# # FOR CHEEZE
# if cheeze == "Y":
#     bill += 1
#
# # FINAL OUTPUT
# print(f"TOTAL IS : {bill}$")