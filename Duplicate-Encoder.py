mi_string = "(( @"
lower_string = mi_string.lower()
encode = ""        

for i in lower_string:
    if lower_string.count(i) > 1: 
        encode += ')'
    else:
        encode += '('

print(encode)   
   

