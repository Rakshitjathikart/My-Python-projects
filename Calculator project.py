from msilib import add_stream

import art


def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mul(n1, n2):
    return  n1 * n2

def div(n1, n2):
    return  n1 / n2

operations = {
    "+":add,
    "-":sub,
    "*":mul,
    "/":div,
}

def calculator():
    from art import logo
    print(art.logo)
    should_accumulate = True
    num1 = int(input("What's the first number?"))

    while should_accumulate:
        for symbol in operations:
            print(symbol)

        op_symbol = input("Pick an operation:")
        num2 = int(input("What's the next number?"))
        answer = operations[op_symbol](num1, num2)
        print(f"{num1} {op_symbol} {num2} = {answer}")
        choice = input(f"Type 'y' to continue with {answer}, or type 'n' to start a new calculation:")
        if choice == 'y':
            num1 = answer

        else:
            should_accumulate = False
            print("\n"*30)
            calculator()

calculator()


