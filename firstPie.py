# Formating Strings
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for ${}"

print(myorder.format(quantity, itemno, price))

text = "My name is {0}, Ive been in {1} for the past {2} years"
name = input('What is your name')
city = input('Which city are you living currently')
years = input('How many years have reside in your current city')
print(text.format(name,city,years))