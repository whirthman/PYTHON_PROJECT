# Tuple
west_africa = ("Ghana","Nigeria","Cote Divoier","Togo","Senegal")
east_africa = ("Kenya", "Ethopia", "Tanzania","Uganda","South Sudan")

# Unpacking Tuples
(one,two,*three) = west_africa
print(one)
print(two)
print(three)
print(west_africa)

(first, *second, third) = east_africa
print(first)
print(second)
print(third)