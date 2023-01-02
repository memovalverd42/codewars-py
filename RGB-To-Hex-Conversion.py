r = -20
g = 275
b = 125

def is_OoR(n):
    if n > 255: n = 255
    elif n < 0: n = 0
    return n


hexa = str(hex(is_OoR(r)))[2:].zfill(2).upper() + str(hex(is_OoR(g)))[2:].zfill(2).upper() + str(hex(is_OoR(b)))[2:].zfill(2).upper()

# print(hexa)


# Forma pro

round = lambda x: min(255, max(x, 0))
hexa = ("{:02X}" * 3).format(round(r), round(g), round(b))

print(hexa)






