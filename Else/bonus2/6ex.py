string = input("Введіть рядок чисел через пробіл: ")
n = int(input("Введіть число n ( кількість копій ): "))
if n < 1:
    print("Неправильно введено n")
    print("Введена буква велика!")
    exit()

array = list(map(int, string.split(' ')))

if len(array) < 2:
    array *= (n + 1)
else:
    array[0:0] = array[0:2] * n

print(array)
