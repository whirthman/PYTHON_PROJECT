#  Arthmetric Operators Program

x = int(input("Enter the first value (x)"))
y = int(input("Enter the second value (y)"))
z = input("Input your operator")

# Additon
if(z == "+"):
    print("Additon: " + str(x)+"+"+str(y) + "=", x+y)

# Substraction
elif(z == "-"):
    print("Substraction: " + str(x)+"-"+str(y) + "=", x-y)

# Multiplication
elif(z == "*"):
    print("Multiplication: " + str(x)+"*"+ str(y) + "=", x*y)

# Division
elif(z == "/"):
    print("Division: " + str(x) + "/" + str(y) + "=", x/y )

# Modulus
elif(z == "%"):
    print("Modulus :" + str(x) + "%" + str(y) + "=", x%y)

# Exponentiation
elif(z == "**"):
    print("Exponentiation :" + str(x) + "**" + str(y) + "=", x**y)

# Floor Division
elif(z == "//"):
    print("Floor Division: " + str(x) + "//" + str(y) + "=", x//y )