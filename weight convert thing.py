## weight convert thing

weight = float(input("Input weight: "))
pound = input("(K)g or (L)bs?")

if pound == "L" or pound == "l":
    print("Your weight is: " + str(weight / 2.20462))

elif pound == "K" or pound == "k":
    print("Your weight is " + str(weight * 2.20462))


print("ok")