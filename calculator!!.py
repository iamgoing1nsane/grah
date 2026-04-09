operation = input("Which operation?(addition, subtraction, multiplication, or division) ")
first = (input("First number: "))
second =(input("Second number: "))
result = None

if operation == "addition":
 result = float(first) + float(second)

elif operation == "subtraction":
 result = float(first) - float(second)

elif operation == "multiplication" :
 result = float(first) * float(second)

elif operation == "division":
 result = float(first) / float(second)

else : print("Invalid operation")

if result is not None:
 print("Sum: " + str(result))
