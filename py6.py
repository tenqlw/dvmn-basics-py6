password = input('Введите пароль: ')
def score(password):
    score = 0
    if len(password) > 11:
        score += 2
    else:
        score = 0
    return score
def has_digit(password):
    score = 0
    if any(letter.isdigit() for letter in password):
        score += 2
    else:
        score = 0
    return score
def has_lower_letters(password):
    score = 0
    if any(has_lower_letters.islower() for has_lower_letters in password):
        score += 2
    else:
        score = 0
    return score
def has_upper_letters(password):
    score = 0
    if any(has_upper_letters.isupper() for has_upper_letters in password):
        score += 2
    else:
        score = 0
    return score
def has_symbols(password):
    score = 0
    if not has_digit(password) and has_lower_letters(password) and has_upper_letters(password) and score(password) in password:
        score += 2
    else:
        score = 0
    return score
check = [
    score(password),
    has_digit(password),
    has_lower_letters(password), 
    has_upper_letters(password),
    has_symbols(password)
    ]
sum_func = 0
for function in check:
    sum_func += function
print('Рейтинг пароля: ', sum_func)
if __name__ == '__main__':
    has_digit(password),
    has_lower_letters(password),
    has_upper_letters(password),
    has_symbols(password),
    score(password)