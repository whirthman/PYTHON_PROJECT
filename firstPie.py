# Format  Method
# Returns the index of a string if its finds and returns -1 if doesnt exist

txt = "For only {price:.2f} dollars!"
x = txt.format(price = 200)
print(x)

txt2 = "My name is {name} i am {age} old"
print(txt2.format(name="Jonah", age="25"))