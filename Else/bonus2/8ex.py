letter = input("Введіть букву: ")
if len(letter) > 1:
    print("Введено більше ніж 1 буква!")
    exit()
if letter.isupper():
    print("Введена буква велика!")
else:
    print("Введена буква не є велика!")
