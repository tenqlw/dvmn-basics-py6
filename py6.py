password = input('Введите пароль: ')

def sumlength(password):
    if len(password) > 11:
        return True
    return False

def has_digit(password):
    return any(letter.isdigit() for letter in password)

def has_lower_letters(password):
    return any(has_lower_letters.islower() for has_lower_letters in password)

def has_upper_letters(password):
    return any(has_upper_letters.isupper() for has_upper_letters in password)

def has_symbols(password):
    return any(has_symbols.isalnum() for has_symbols in password)

def main(password):
    sum_func = 0
    check = [
        sumlength(password),
        has_digit(password),
        has_lower_letters(password), 
        has_upper_letters(password),
        has_symbols(password)
        ]
    for function in check:
        if function == True:
            sum_func += 2
    print('Рейтинг пароля', sum_func)
if __name__ == '__main__':
    main(password)
