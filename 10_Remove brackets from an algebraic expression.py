str1 = input(">")

sum = 0


for i in str1:
    if (i >= "a" and i <= "z") or (i >= "A" and i <= "Z"):
        pass
    else:
        sum += int(i)
print("sum of numbers in a string :",sum)
