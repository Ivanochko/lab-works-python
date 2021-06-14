arr = [(i, len(i)) for i in input('Введіть речення на сорт.: ').split(' ')]
arr = sorted(arr, key=lambda x: x[1], reverse=True)
print()
for x, i in arr:
    print(x, end=' ')
print()
