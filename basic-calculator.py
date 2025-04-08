equation = input("What's the type of equation you'd like to do? ").lower()
firstnumber = float(input("What's the first number? "))
secondnumber = float(input("What's the second number? "))

operations = {
    "multiply": firstnumber * secondnumber,
    "add": firstnumber + secondnumber,
    "subtract": firstnumber - secondnumber,
    "divide": firstnumber / secondnumber if secondnumber != 0 else "Cannot divide by zero",
}

#Ensure works for variation of words

if equation =="plus":
    equation = "add"
elif equation == "minus":
    equation = "subtract"

#Making the result presented a whole number if it is
if equation in operations:
    result = operations[equation]

if isinstance(result, float) and result.is_integer():
    print(f"{int(result)}") #If the result is an integer
else:
    print(f"{result:.2f}") #If result is float