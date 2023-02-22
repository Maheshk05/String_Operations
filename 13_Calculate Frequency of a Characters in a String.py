str1 = input(">")

count = {}


for i in str1:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1


non_repeating = []


for i ,count in count.items():
    if count == 1:
        non_repeating.append(i)
print(non_repeating)
