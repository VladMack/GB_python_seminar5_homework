def coding(text):
    counter = 1
    coded = ''
    i = 0
    while i < len(text):
        for j in range(i+1, len(text)):
            if text[j] == text[i]:
                counter += 1
        if counter == 1:
            coded += f'{text[i]}'
        else:
            coded += f'#{counter}{text[i]}'
        i += counter
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


string1 = 'аббббввввввг'
print(string1)
string2 = coding(string1)
print(string2)
string3 = decoding(string2)
print(string3)
string4 = 'а111бббб4'
print(string4)
string5 = coding(string4)
print(string5)
string6 = decoding(string5)
print(string6)
