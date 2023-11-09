# Tuple
west_africa = ("Ghana","Nigeria","Cote Divoier","Togo","Senegal")
print(west_africa)

# Tuple Length
print(len(west_africa))

# Cheking the Type
print(type(west_africa))

# Creating Tuple form Constructor
east_africa = tuple(("Kenya","Uganda","Ethopia","Tanzania"))
print(east_africa)

# Changing Tuples
mod_east_afica = list(east_africa)
mod_east_afica[3] = "South Sudan"
east_africa = tuple(mod_east_afica)
print(east_africa)

# Adding Items to Tuples
cov_east_africa = list(east_africa)
cov_east_africa.append("Tanzania")
east_africa = tuple(cov_east_africa)
print(east_africa)

# Removing Items
rev_east_africa = list(east_africa)
rev_east_africa.remove("South Sudan")
east_africa = tuple(rev_east_africa)
print(east_africa)