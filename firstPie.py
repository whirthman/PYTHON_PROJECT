# List
west_africa = ["Ghana","Nigeria","Ivory Coast","Togo","Senegal","Burkina Faso","Liberia"]
east_africa = ["Kenya", "Ethopia", "Uganda", "Tanzania"]

# Using the For Loop

for country in west_africa:
    print(country)

for i in range(len(west_africa)):
    print(west_africa[i])


#  Using the While Loop
i = 0
while i < len(east_africa):
    print(east_africa[i])
    i += 1

print(range(len(east_africa)))

# Looping using Comprehension
[print(x) for x in east_africa]