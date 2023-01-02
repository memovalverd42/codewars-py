
############# Palabras pares ################
s = 'testing'

# print(len(s))
# print(len(s)/2)
# print(s[(int(len(s)/2))-1:(int(len(s)/2))+1])

# s2 = 'middle'

# print(len(s2))
# print(len(s2)/2)
# print(s2[(int(len(s2)/2))-1:(int(len(s2)/2))+1])

# print('\n##########################################')

# s3 = 'testing'

# print(len(s3))
# print(int(len(s3)/2))
# print(s3[int(len(s3)/2)])
# print('\n #############')

# s4 = 'oso'

# print(len(s4))
# print(int(len(s4)/2))
# print(s4[int(len(s4)/2)])

# s5 = 'A'
# print(len(s5))
# print(int(len(s5)/2))
# print(s5[int(len(s5)/2)])

print(s[(int(len(s)/2))-1:(int(len(s)/2))+1] if len(s)%2 == 0 else s[int(len(s)/2)])

print(s[int((len(s)-1)/2):int(len(s)/2)+1])