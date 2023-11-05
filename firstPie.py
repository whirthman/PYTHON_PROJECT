# List
west_africa = ["Ghana","Nigeria","Ivory Coast","Togo","Senegal","Burkina Faso","Liberia"]
east_africa = ["Kenya", "Ethopia", "Uganda", "Tanzania"]
west_africa.insert(6,"Seira Leone")
print(west_africa)

# Extend
west_africa.extend(east_africa)
print(west_africa)

# Add any iterable using extend method
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

# Remove Method
thislist.remove("kiwi")
print(thislist)

# Pop Method
thislist.pop()
print(thislist)

thislist.pop(1)
print(thislist)

# Clear Method
thislist.clear()
print(thislist)