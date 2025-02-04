from random import sample

digits: str = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
il = 'il1Lo0O'
chars = ''

counts = int(input('Количество паролей для генерации: '))
length = int(input('Длина одного пароля: '))
flag_numbers = True if input('Включать ли цифры? y/n\n').lower() == 'y' else False
flag_upper = True if input('Включать ли прописные буквы? y/n\n').lower() == 'y' else False
flag_lower = True if input('Включать ли строчные буквы? y/n\n').lower() == 'y' else False
flag_symbols = True if input('Включить ли символы? y/n\n').lower() == 'y' else False
flag_il = True if input('Включать ли неоднозначные символы? y/n\n').lower() == 'y' else False

chars += digits if flag_numbers else ''
chars += lowercase_letters if flag_lower else ''
chars += uppercase_letters if flag_upper else ''
chars += punctuation if flag_symbols else ''
chars += il if flag_il else ''

def generate_password(length, chars):
    for i in range(counts):
        print(*sample(chars, length), sep='')

generate_password(length, chars)