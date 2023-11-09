# Dictionary
user = {
    "name" : "Jonah",
    "age" :   "23",
    "proffesion" : "Developer"
}

print(user)

# Accesing Items in list
print(user["name"])

# Length of Dictionary
print(len(user))


# Finding  Type of Dictionary Object
print(type(user))

# Creating Dictionary with Constructor
user2 = dict(name = "John", age = 23, profession = "Designer")
print(user2)

# Accesing Dict Items
print(user["proffesion"])

# Getting Keys from Dict Object
print(user.keys())

print(user2.keys())

print(user)

user["hometown"] = "Goaso"

print(user)

# Using the Get Values Method
print(user.values())

# Get Items Method return as tuples
print(user.items())

# Checking if Key Exist
if "hometown" in user:
    print("He is ",user["name"], "and he comes from ", user["hometown"] )