str1 = input(">")

count = str()
b = str1.casefold()
for i in str1:
    if b == "a" or b == "e":
        pass

    else:
        count += i

if len(count) == 0:
    print("No vowel found in " + b)

else:
    print("After removing vowels :" + count)
