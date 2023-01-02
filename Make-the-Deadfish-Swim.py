'''
i => increments the value (initially 0)
d => decrements the value
s => squares the value
o => outputs the value into the return array
'''

test1 = "iiisdoso"      # ==>  [8, 64]
test2 = "ioioio"        # ==>  [1, 2, 3]
test3 = "isoisoiso"     # ==>  [1, 4, 25]

def parse(data):
    valor_actual = 0
    result = []
    for elemento in data:
        if elemento == 'i':
            valor_actual += 1
        elif elemento == 'd':
            valor_actual -= 1
        elif elemento == 's':
            valor_actual = valor_actual**2
        elif elemento == 'o':
            result.append(valor_actual)

    return result


print(parse(test2)) 