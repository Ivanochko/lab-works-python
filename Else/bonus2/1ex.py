def find_difference(number) -> float:
    if number > 17:
        return (number - 17) * 2
    return number - 17


number = float(input('Введіть число: '))
print("Result: ", find_difference(number))
