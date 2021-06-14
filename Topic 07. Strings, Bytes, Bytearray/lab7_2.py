def toLetters(text):
    symbols = ' .,!?/\\"\':;<>(){}[]-'
    for x in symbols:
        text = text.replace(x, '')
    return text


def isPalindrome(text):
    return text[:int(len(text) / 2)] == text[-1:-int(len(text) / 2) - 1:-1]


text = input("Введіть текст який потрібно перевірити: ")
text = toLetters(text).lower()
print(isPalindrome(text))
