s = input(">")

b = " "

for i in s:
    if (ord(i) >= 40 and ord(i) <= 41) or (ord(i) >= 91 and ord(i) <= 93) or(ord(i)>= 123 and ord(i) <= 125):
        
       pass
    else:
        b += i

print(b)
