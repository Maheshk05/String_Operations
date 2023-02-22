def first_last(string):
    words = string.split()

    for i in range(len(words)):
        first_word = words[i][0]
        last_word = words[i][-1]


    words[i] = first_word.upper() + words[i][1:-1] + last_word.upper()

    cap_string = "".join(words)
    return cap_string

string = "hello"

cap_string = first_last(string)

print(cap_string)
