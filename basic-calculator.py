#Aliases
operation_aliases = {
    "plus": "add",
    "addition": "add",
    "sum": "add",
    "minus": "subtract",
    "subtraction": "subtract",
    "subtract": "subtract",
    "multiply": "multiply",
    "times": "multiply",
    "divide": "divide",
    "division": "divide",
}

#Expressions for operations aliases dictionary

operations = {
    "multiply": lambda first_number, second_number: first_number * second_number,
    "add": lambda first_number, second_number: first_number + second_number,
    "subtract": lambda first_number, second_number: first_number - second_number,
    "divide": lambda first_number, second_number: first_number / second_number if second_number != 0 else "Cannot divide by zero",
}

while True:
    equation = input("What's the type of equation you'd like to do? Or type 'exit' to quit. ").lower()
    if equation == "exit":
        break
    try:
        firstnumber = float(input("What's the first number? "))
        secondnumber = float(input("What's the second number? "))
    except ValueError:
        print("Please enter valid numbers.")
        exit()

    if equation in operation_aliases:
        equation = operation_aliases[equation]

#Making the result presented a whole number if it is
    if equation in operations:
        result = operations[equation](firstnumber, secondnumber) #Calling lambda

    if isinstance(result, float) and result.is_integer():
        print(f"{int(result)}") #If the result is an integer
    else:
        print(f"{result:.2f}") #If result is float
