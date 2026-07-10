def add(n1,n2) :
    return n1+n2
def sub(n1,n2) :
    return n1-n2
def mul(n1,n2) :
    return n1*n2
def div(n1,n2) :
    if n2==0 :
        print("Division by Zero is not possible")
    else :
        return n1/n2

def logo() :
    print("""
    ░█████╗░░█████╗░██╗░░░░░░█████╗░██╗░░░██╗██╗░░░░░░█████╗░████████╗░█████╗░██████╗░
    ██╔══██╗██╔══██╗██║░░░░░██╔══██╗██║░░░██║██║░░░░░██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗
    ██║░░╚═╝███████║██║░░░░░██║░░╚═╝██║░░░██║██║░░░░░███████║░░░██║░░░██║░░██║██████╔╝
    ██║░░██╗██╔══██║██║░░░░░██║░░██╗██║░░░██║██║░░░░░██╔══██║░░░██║░░░██║░░██║██╔══██╗
    ╚█████╔╝██║░░██║███████╗╚█████╔╝╚██████╔╝███████╗██║░░██║░░░██║░░░╚█████╔╝██║░░██║
    ░╚════╝░╚═╝░░╚═╝╚══════╝░╚════╝░░╚═════╝░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝
    """)

operation = {
                "+" : add , "-" : sub , "*" : mul , "/" : div,
             }
def cal() :
    remain = True
    first = True
    while remain  :
        if first :
            a = float(input("Enter a number 1 : "))
        else :
            a = pre
        op = input("Enter operation ( + , - , * , / ) : ")
        b = float(input("Enter a number 2 : "))

        if op in operation:
            result = operation[op](a,b)
            print(f"{a}  {op}  {b}  =  {result}")
        else :
            print("Invalid operation")
            continue


        want = input(f"Do you want to continue With {result} (Y/N) : ").upper()
        if want == "Y" :
            remain = True
            pre = result
            first = False
        elif want == "N" :
            # remain = False
            first = True
        else :
            print("Invalid Input")

logo()
cal()