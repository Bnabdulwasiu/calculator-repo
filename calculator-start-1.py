def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

def modulus(n1, n2):
    return n1 % n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    "%": modulus,
}

def calculator():
    num1 = int(input("What's the first number?: "))
    for operation in operations:
        print(operation) 
    # num2 = int(input("What's the second number?: "))
    # calculation_function = operations[operation_symbol]
    # first_answer = calculation_function(num1, num2)
    stop_calculation = False
    while stop_calculation == False:
        
        operation_symbol = input("Pick an operation: ")
        num2 = int(input("What's the next number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        loop_prompt = input(f"Type 'y' to continue calculating with {answer},\nor type 'n' to quit.: ").lower()
        
        if loop_prompt == 'y':
            num1 = answer
        
        elif loop_prompt == 'n':
            stop_calculation = True
            print("Good bye from the calculator")
            
        # elif loop_prompt == "l":
        #     stop_calculation = True
        #     calculator()
            
        else:
            print("Wrong input")

calculator()


# loop_prompt = input(f"Type 'y' to continue calculating with {first_answer}, or type 'l' to start a new calculation,\nor type 'n' to quit.: ").lower()