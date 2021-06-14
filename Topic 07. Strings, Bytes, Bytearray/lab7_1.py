text = input("Введіть текст який потрібно змінити: ")
print(' * так, щоб це число було менше ніж', len(text) / 2, "*")
swipe = int(input('Введіть на скільки символів потрібно обернути строку: '))

text = (
    text[swipe:] + text[:swipe]
    if swipe > 0
    else text[swipe:-1] + text[-1] + text[-len(text):swipe])

print(text)
