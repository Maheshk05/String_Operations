str1 = input("1:")
str2 = input("2:")

str1 = sorted(str1.casefold())
str2 = sorted(str2.casefold())

print("After sorting str1 :",str1)
print("After sorting str2 : ",str2)

if str1 == str2:
    print("It's an Anagram")
else:
    print("It's not")
