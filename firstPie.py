# Tuple
west_africa = ("Ghana","Nigeria","Cote Divoier","Togo","Senegal")
east_africa = ("Kenya", "Ethopia", "Tanzania","Uganda","South Sudan")

# Joining Tuples
africa = west_africa + east_africa
print(africa)

# Multiply Tuples
nations = africa * 10
sort_tup = list(nations)
sort_tup.sort()
nations = tuple(sort_tup)
print(nations)