# Set
countries = {"Malta", "Ghana", "Italy", "United Kingdom"}
print(countries)

# Accesing a Sets by Looping
for country in countries:
    print(country)

# Adding items to Sets
countries.add("United States")
print(countries)

# Adding an Iterable to a Set
eu_count = ["Spain", "Portugal", "France"]
countries.update(eu_count)
print(countries)

# Removing Items from Sets
countries.remove("Italy")
print(countries)

# Using the Discard Method
countries.discard("France")
print(countries)

# Looping throug a Sets
for country in countries:
    print(country)

africa = {"Nigeria", "Kenya","Uganda","Senegal","Ghana"}
nations = africa.union(countries)
print(nations)

# Using the Update Method
middle_east = {"Turkey", "Israel", "Saudi Arabia", "UAE"}
nations.update(middle_east)
print(nations)

# Keeping only the Duplicate / Intersectio of Sets
fruits = {"apple", "mango", "banana"}
tech = {"microsoft", "google", "apple"}
intersect = fruits.intersection(tech)
print(intersect)

# Keeping both but not duplicate / using symetric_diffrecne method
sym_diff = fruits.symmetric_difference(tech)
print(sym_diff)

# Findig only Sets Members with diffrence
# Fruit Only
diff_fruits = fruits.difference(tech)
print(diff_fruits)

# Tech Only
diff_tech = tech.difference(fruits)
print(diff_tech)
