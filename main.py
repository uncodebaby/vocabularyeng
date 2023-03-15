import random
from colorama import init
from colorama import Fore, Style
from time import sleep
import os
init()

vocabulary = {
    'to classify': 'классифицировать',
    'structure': 'структура, сооружение, конструкция, здание, строение',
    'bearing structure': 'несущая конструкция',
    'structural': 'структурный, строительный, конструктивный',
    'natural': 'естественный',
    'artificial': 'искусственный',
    'stone': 'камень',
    'clay': 'глина',
    'sand': 'песок',
    'lime': 'известь',
    'timber wood': 'дерево, лесоматериалы',
    'brick': 'кирпич',
    'concrete': 'бетон',
    'cement': 'цемент',
    'steel': 'сталь',
    'plastics': 'пластмассы',
    'binding': 'вяжущие',
    'secondary': 'второстепенные'
}

#main program
def main(vocabulary: dict, answer: str, mistakes: int, length_vocabulary: int) -> None:
    rand_pair = random.choice(list(vocabulary.items()))
    lst = [el for el in rand_pair]
    translate = str(input(f'\nВведите перевод слова {lst[1]}: '))

    try:
        if translate == lst[0]:
            correct(vocabulary, lst, answer, mistakes, length_vocabulary)
        else:
            incorrect(vocabulary, lst, answer, mistakes, length_vocabulary)

    except IndexError:
        ask = input(f'Правильных ответов: {length_vocabulary-mistakes} из {length_vocabulary}\nНачать заново? Y/N: ')
        if ask == str('Y'):
            start(answer)
        else:
            print('Всего доброго!')
            sleep(5)

#works when user answers correctly after asking the translation
def correct(vocabulary: dict, lst: list, answer: str, mistakes: int, length_vocabulary: int) -> None:
    print(Fore.GREEN + 'Перевод введён верно.' + Style.RESET_ALL)
    if answer == 'Y':
        print(f'Произношение, транскрипция: https://wooordhunt.ru/word/{lst[0]}\n')
    key = str(lst[0])
    del vocabulary[key]
    main(vocabulary, answer, mistakes, length_vocabulary)

#works when user answers incorrectly after asking the translation
def incorrect(vocabulary: dict, lst: list, answer: str, mistakes: int, length_vocabulary: int) -> None:
    mistakes += 1
    print(Fore.RED + 'Перевод введён неверно.' + Style.RESET_ALL)
    print(f'Правильный перевод: {lst[0]}')
    if answer == 'Y':
        print(f'Произношение, транскрипция: https://wooordhunt.ru/word/{lst[0]}\n')
    main(vocabulary, answer, mistakes, length_vocabulary)

#works when user choose first branch
def start(answer, mistakes):
    length_vocabulary = len(vocabulary.keys())
    main(vocabulary, answer, mistakes, length_vocabulary)
            
#works when user choose second branch
def change_vocabulary():
    user_answer = int(input('Введите 1, чтобы просмотреть весь словарь\nВведите 2, чтобы изменить содержимое словаря\nВведите 3, чтобы вернуться в меню: '))
    if user_answer == 1:
        os.system('cls||clear')
        for key, value in vocabulary.items():
            print(key + ' - ' + value)
        input('\nНажмите enter чтобы продолжить..')
        os.system('cls||clear')
        change_vocabulary()
    elif user_answer == 2:
        os.system('cls||clear')
        pass
    elif user_answer == 3:
        os.system('cls||clear')
        ask_branch()

#asking the user what branch he prefer to use now
def ask_branch():
    branch = int(input('Выберите 1, если хотите войти в режим практики\nВыберите 2, если хотите войти в режим изменения словаря: '))
    os.system('cls||clear')
    if branch == 1:
        os.system('cls||clear')
        answer = input('\nПоказывать ли транскрипцию? Y/N: ')
        start(answer, mistakes=int())
    elif branch == 2:
        os.system('cls||clear')
        change_vocabulary()
    else:
        print('Введено неверное число.')
        ask_branch()

if __name__ == '__main__':
    ask_branch()
        