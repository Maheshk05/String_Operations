a = input(">")

count = 0

b = a.lower()
for i in b:
    if i == "a" or i == "e" or i == "i" or i == "o" or i == "u" :
        count += 1

if count == 0:
    print("Vowels not present")
else:
    print("Total vowels :" +str(count))
    
