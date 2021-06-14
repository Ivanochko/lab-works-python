numbers = list(map(float, input("Введіть числа через пробіл: ").split(' ')))
number = float(input('Введіть число яке потрібно перевірити: '))

if number in numbers:
    print("Це число знаходиться в наборі чисел!")
else:
    print("Це число не знаходиться в наборі чисел!")
