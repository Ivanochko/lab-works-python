string = input("Введіть рядок: ")
if string.startswith("ls"):
    print(string)
else:
    print("ls" + string)
