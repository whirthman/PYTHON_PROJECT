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