from functools import reduce

n = 4
cont = 0
while len(str(n))>1:
    n = reduce(lambda a, b: int(a)*int(b), list(str(n)))
    cont += 1

#print(cont)


# Forma pro

