# Joining List
list1 = [1,2,3,4,5,6,7]
list2 = ["a","b","c"]

list3 = list1 + list2
print(list3)

west_africa = ["Nigeria", "Burkina Faso", "Ghana","Togo","Senegal","Mali","Cote Divoire","Liberai"]
east_africa = ["Tanzania","Kenya","South Sudan","Ethiopia","Uganda","Somalia"]

africa = []
africa.extend(east_africa)
print(africa)

for x in west_africa:
    africa.append(x)

print(africa)