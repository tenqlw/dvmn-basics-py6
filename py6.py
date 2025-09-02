password = input('Введите пароль: ')

def sumlength(password):
    return any(len(password) > 11 in password)

def has_digit(password):
    return any(letter.isdigit() for letter in password)

def has_lower_letters(password):
    return any(has_lower_letters.islower() for has_lower_letters in password)

def has_upper_letters(password):
    return any(has_upper_letters.isupper() for has_upper_letters in password)

def number(password):
    return any(not sumlength(password) and has_digit(password) and has_lower_letters(password) and has_upper_letters(password) for number in password)

def total(password):
    sum_func = 0
    check = [
        sumlength(password),
        has_digit(password),
        has_lower_letters(password), 
        has_upper_letters(password),
        number(password)
        ]
    for function in check:
        if function == True:
            sum_func += 2
    return sum_func
    print('Рейтинг пароля: ', sum_func)

def main():
    if __name__ == '__main__':
        total(password),
        main()