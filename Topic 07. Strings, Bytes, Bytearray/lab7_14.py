def isValid(mail):
    mail = mail.strip().lower()
    symbols = 'abcdefghijklmnopqrstuvwxyz.-_@0123456789'
    if '@' in mail\
       and mail.count('@') == 1\
       and mail.index('@') < 30\
       and mail.index('@') > 5:
        for i in mail:
            if i not in symbols:
                break
        else:
            if mail.rindex('.') < len(mail) - 2\
               and mail.index('.', mail.index('@')) - mail.index('@') > 1:
                return True
    return False


if __name__ == '__main__':

    mail = input('Введіть потрібну пошту: ')
    if isValid(mail):
        print('Пошта задовільняє всі стандарти електронної пошти!')
    else:
        print('Пошта не задовільняє стандарти електронної пошти!')
