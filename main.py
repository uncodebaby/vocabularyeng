import random
import sqlite3
from colorama import init
from colorama import Fore, Style
from time import sleep
import os


init()
con = sqlite3.connect("vocabulary.db")
cursor = con.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS vocabulary
                (id INTEGER PRIMARY KEY AUTOINCREMENT,  
                eng_word TEXT, 
                ru_word TEXT)
            """)


# vocabulary = {
#     'to classify': 'классифицировать',
#     'structure': 'структура, сооружение, конструкция, здание, строение',
#     'bearing structure': 'несущая конструкция',
#     'structural': 'структурный, строительный, конструктивный',
#     'natural': 'естественный',
#     'artificial': 'искусственный',
#     'stone': 'камень',
#     'clay': 'глина',
#     'sand': 'песок',
#     'lime': 'известь',
#     'timber wood': 'дерево, лесоматериалы',
#     'brick': 'кирпич',
#     'concrete': 'бетон',
#     'cement': 'цемент',
#     'steel': 'сталь',
#     'plastics': 'пластмассы',
#     'binding': 'вяжущие',
#     'secondary': 'второстепенные'
# }

#main program
def main(vocabulary, answer) -> None:
    rand_pair = random.choice(list(vocabulary.items()))
    lst = [el for el in rand_pair]
    translate = str(input(f'\nВведите перевод слова {lst[1]}: '))

    try:
        if translate == lst[0]:
            correct(vocabulary, lst, answer)
        else:
            incorrect(vocabulary, lst, answer)

    except IndexError:
        ask = input('Начать заново? Y/N: ')
        if ask == str('Y'):
            start(answer)
        else:
            print('Всего доброго!')
            sleep(5)

#works when user answers correctly after asking the translation
def correct(vocabulary: dict, lst: list, answer: str) -> None:
    print(Fore.GREEN + 'Перевод введён верно.' + Style.RESET_ALL)
    if answer == 'Y':
        print(f'Произношение, транскрипция: https://wooordhunt.ru/word/{lst[0]}\n')
    key = str(lst[0])
    del vocabulary[key]
    main(vocabulary, answer)

#works when user answers incorrectly after asking the translation
def incorrect(vocabulary: dict, lst: list, answer: str) -> None:
    print(Fore.RED + 'Перевод введён неверно.' + Style.RESET_ALL)
    print(f'Правильный перевод: {lst[0]}')
    if answer == 'Y':
        print(f'Произношение, транскрипция: https://wooordhunt.ru/word/{lst[0]}\n')
    main(vocabulary, answer)

#works when user choose first branch
def start(answer):
    vocabulary = dict()
    cursor.execute("SELECT * FROM vocabulary")
    for pair_words in cursor.fetchall():
        vocabulary = {**vocabulary, pair_words[1]: pair_words[2]}
    main(vocabulary, answer)

def add_pair_in_vocabulary():
    eng_word = str(input('Введите английское слово/пару слов: '))
    ru_word = str(input('Введите русское слово/пару слов: '))
    cursor.execute(f"INSERT INTO vocabulary (eng_word, ru_word) VALUES ('{eng_word}', '{ru_word}')")
    con.commit()
    print('Успешно!')
    ask_to_continue = int(input('Введите 1, если хотите продолжить\nВведите 2, чтобы вернуться в меню: '))
    if ask_to_continue == 1:
        add_pair_in_vocabulary()
    elif ask_to_continue == 2:
        change_vocabulary()
    else:
        print('Ошибка 5.12')
        sleep(2)
        change_vocabulary()

def detele_data_from_table():
    cursor.execute("""DELETE FROM vocabulary
    """)
    con.commit()
    change_vocabulary()

#works when user choose second branch
def change_vocabulary():
    user_answer = int(input('Введите 1, чтобы просмотреть весь словарь\nВведите 2, чтобы изменить содержимое словаря\nВведите 3, чтобы вернуться в меню: '))
    if user_answer == 1:
        os.system('cls||clear')
        cursor.execute("SELECT * FROM vocabulary")
        for pair_words in cursor.fetchall():
            print(f"{pair_words[0]} - {pair_words[1]} - {pair_words[2]}")
        input('\nНажмите enter чтобы продолжить..')
        os.system('cls||clear')
        change_vocabulary()
    elif user_answer == 2:
        os.system('cls||clear')
        ask_user = int(input('Введите 1, чтобы удалить весь словарь\nВведите 2, чтобы добавить новую пару слов\nВведите 3, чтобы выйти из режима редактирования: '))
        if ask_user == 1:
            detele_data_from_table()
        elif ask_user == 2:
            add_pair_in_vocabulary()
        elif ask_user == 3:
            change_vocabulary()
        else:
            print('Ошибка 5.12')
            sleep(2)
            change_vocabulary()
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
        start(answer)
    elif branch == 2:
        os.system('cls||clear')
        change_vocabulary()
    else:
        print('Введено неверное число.')
        ask_branch()

if __name__ == '__main__':
    ask_branch()
        