str1 = input(">")

str2 = ""

for i in str1:
    if i.isupper():
        i = i.lower()
        str2 = str2 + i

    else:
        i = i.upper()
        str2 = str2 + i

print(str1 + " after changing " + str2)


#OR

str = "MahesH"
print(str.swapcase())
