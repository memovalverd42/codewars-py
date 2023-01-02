
from functools import reduce
import  numpy as np


def multi(n1, n2):
    return n1 * n2

B_list = [2, 3, 5, 8, 9, 4]

n = 2


# output1 = [B_list[i:i+n] for i in range(0, len(B_list), n)]
# print(output1)
# res = reduce(lambda x1, x2: x1*x2, B_list)
# print(res)


u = [1, 0, 1]
v = [2, 7]

a = [1, 1, 0]
b = [0, 2, 1]

c = [4, 5, 1]
d = [1, 0, 4]



print(np.convolve(u, v))





# output2 = [output1[i:i+n] for i in range(0, len(output1), n)]
# print(output2)

# output3 = [output2[i:i+n] for i in range(0, len(output2), n)]
# print(output3)

