# data = [[18, 20], [45, 2], [61, 12], [37, 6], [21, 21], [78, 9]]

data = [(54, 7), (47, 20), (10, 20), (85, 6), (55, 21), (83, 25), (79, 7)]

output = []

for i in data:
    output.append("Senior" if i[0]>=55 and (-2<=i[1]<=26) and i[1]>=7 else "Open")

print(output)

# Forma mas chida
# ["Senior" if age >= 55 and handicap >= 8 else "Open" for (age, handicap) in data]