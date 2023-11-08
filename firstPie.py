# List
west_africa = ["Ghana","Nigeria","Ivory Coast","Togo","Senegal","Burkina Faso","Liberia"]
east_africa = ["Kenya", "Ethopia", "Uganda", "Tanzania"]

# Sort List
west_africa.sort()
print(west_africa)

# Sorting in Descending Order Using Reverse
west_africa.sort(reverse=True)
print(west_africa)

# Sorting using keys with function
def myFun(n):
    return abs(n-50)

myInt = [100, 80, 200, 60, 50, 30, 70, 115]
myInt.sort(key=myFun)
print(myInt)

# Overcoming case insensitve unexpexted behaviours using key func
fruits = ["banana", "Orange", "Kiwi", "cherry"]

fruits.sort(key=str.lower)
print(fruits)

# Reversing the Order
fruits.reverse()
print(fruits)