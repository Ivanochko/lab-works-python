numbers = []
numbers.append(float(input("Введіть перше число: ")))
numbers.append(float(input("Введіть перше число: ")))
numbers.append(float(input("Введіть перше число: ")))

summ_of_elem = sum(numbers)
if summ_of_elem.is_integer():
    print("Result is integer: ", summ_of_elem, summ_of_elem, summ_of_elem)
else:
    print("Result is not integer: ", summ_of_elem)
