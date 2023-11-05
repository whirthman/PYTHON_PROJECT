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