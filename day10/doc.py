#calculator

#add
def add(n1,n2):
    return n1+n2

#Subtract
def subtract(n1,n2):
    return n1-n2
#Multiply
def Multiply(n1,n2):
    return n1*n2
#Divide
def divide(n1,n2):
    return n1/n2

operations = {
    "+":add,
    "-":subtract,
    "*":Multiply,
    "/":divide
}
def calculator():
    num1 = float(input("what's the first number?: "))
    for symbol in operations:
        print(symbol)
    should_countinue = True
    while should_countinue:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("what's the second number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1,num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")
        continue_calculating = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation.: ").lower()

        if continue_calculating=="y":
            num1 = answer
        elif continue_calculating=="n":
            should_continue=False
            calculator()

calculator()

   
# def calculator():
#     print("aaaaaargh")
#     calculator()

# calculator()