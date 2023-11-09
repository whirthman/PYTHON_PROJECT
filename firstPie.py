# Tuple
west_africa = ("Ghana","Nigeria","Cote Divoier","Togo","Senegal")
east_africa = ("Kenya", "Ethopia", "Tanzania","Uganda","South Sudan")

# # Looping through a Tuple
for nation in west_africa:
    print(nation)

# # Looping through with the index
for i in range(len(west_africa)):
    print(west_africa[i])

# Looping through tuples with the While Loop
i = 0
while i< len(east_africa):
    print(east_africa[i])
    i+=1