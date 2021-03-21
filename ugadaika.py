from random import *

print('''Добро пожаловать в числовую угадайку!
За сколько попыток вы сможете отгадать число от 1 до 100?
Я загадываю число...''')


def convert():
    chislo = randint(1, 100)

    def is_valid(s):
        return s.isdigit() and 1 <= int(s) <= 100

    popytki = 0

    while True:
        s = input('Введите число от 1 до 100: ')
        if is_valid(s) == True:
            s = int(s)
            popytki += 1
        else:
            print('А может быть все-таки введем целое число от 1 до 100?')
            continue
        if s < chislo:
            print('Ваше число меньше загаданного, попробуйте еще разок')
        elif s > chislo:
            print('Ваше число больше загаданного, попробуйте еще разок')
        else:
            print('Вы угадали, поздравляем!')
            print('Количество попыток:', popytki)
            break


convert()
while True:
    vopros = input('Хотите сыграть еще разок? ')
    if vopros.lower() == 'да':
        convert()
    elif vopros.lower() == 'нет':
        print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
        break
    else:
        print('Я понимаю только да/нет, извините...')
        continue
