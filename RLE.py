def coding(text):
    counter = 1
    coded = ''
    for i in range(1, len(text)):
        if text[i] == text[i-1]:
            counter += 1
        else:
            if counter == 1:
                coded += f'{text[i-1]}'
            else:
                coded += f'#{counter}{text[i-1]}'
                counter = 1
    return coded


def decoding(text):
    decoded = ''
    i = 0
    while i < len(text):
        if text[i] == '#':
            decoded += text[i+2] * int(text[i+1])
            i += 3
        else:
            decoded += text[i]
            i += 1
    return decoded


string1 = 'аббббвввввг'
print(string1)
string2 = coding(string1)
print(string2)
string3 = decoding(string2)
print(string3)
