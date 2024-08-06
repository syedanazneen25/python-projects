logo = r'''
_____________________
|  _________________  |
| | JO           0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|
'''



def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mul(n1, n2):
    return n1 * n2

def div(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div
}
def calculator():
    print(logo)
    end_operations = False
    first_number = float(input("Enter the first number:\n"))

    while not end_operations:
        for symbol in operations:
            print(symbol)
        user_choice = input("What operation you want to do ?")
        second_number = float(input("Enter the second number:\n"))
        result = operations[user_choice](first_number, second_number)
        print(f"{first_number} {user_choice} {second_number} = {result}")
        reset = input(f"If you want to continue operation with {result}. y or n?\n")
        if reset == "y":
            first_number = result
        else:
            end_operations = True
            print("\n" * 20)
            calculator()

calculator()
            


