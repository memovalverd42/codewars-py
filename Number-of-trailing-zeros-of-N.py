import numpy as np

def zeros(n):
    factorial = np.math.factorial(n)
    number_zeros = 0
    for i in str(factorial)[::-1]:
        if i != '0': break
        number_zeros += 1
    return number_zeros

print(zeros(1000))