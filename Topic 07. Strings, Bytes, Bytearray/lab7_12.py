inp = input('Введіть речення: ')
for i in range(len(inp)):
    if i == len(inp) - 1:
        if inp[i] == ' ':
            inp = inp[:i]
        break
    if inp[i] == ' ' and inp[i + 1] == ' ':
        inp = inp[:i] + inp[i + 1:]
        i -= 1

print(inp)
