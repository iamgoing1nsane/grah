
print ("sleepheads calculator ver 1.2")

while True:
    operation = input("Select operation: (A)ddition, (S)ubtraction, (M)ultiplication, (D)ivision, or Q to quit.").strip().lower()
    if operation == "Q" or operation =="q":
        print("ending now.")
        break
    result = None

    first = input("First number: ")
    second = input("Second number: ")

    if operation.upper() == "A":
        result = float(first) + float(second)
    elif operation.upper() == "S":
        result = float(first) - float(second)
    elif operation.upper() == "M": 
        result = float(first) * float(second)
    elif operation.upper() == "D":
        if float(second) != 0:
           result = float(first) / float(second)
        else:
            print("cant do that.")
            continue
    else:
      print("huh?")
      continue

    print("Result:", result)

    