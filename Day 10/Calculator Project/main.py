from art import logo
print(logo)
def add(n1, n2):
    return n1 + n2
def sub(n1, n2):
    return n1 - n2
def mul(n1, n2):
    return n1 * n2
def div(n1, n2):
    return n1 / n2
operations = {"+": add,"-": sub,"*":mul,"/":div}
def calculate():
    first_num = float(input("What's the first number? "))
    is_countinue = True
    while is_countinue:
        pick_operation = input("+\n-\n*\n/\nPick operation to perform: ")
        second_num = float(input("What's the next number? "))
        output = operations[pick_operation](first_num, second_num)
        print(output)
        choice = input(f"Type 'y' to continue calculating with {output}, "
                       f"or type 'n' to start a new calculation: ").lower()
        if choice == "y":
            first_num = output
        elif choice == "n":
            print("\n" * 20)
            calculate()
calculate()










