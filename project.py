# доделать функцию обновления пароля
# пароли храним в хеше (алгоритм )
# словарь с данными пользоветеля храним в файле
# ф-ии возвращают строки
from hashlib import md5
def to_md5(pw):
    return str(md5(pw.encode()).hexdigest())

def DB_init():
    with open('database.txt', 'r', encoding='utf-8') as text_dict:
        text_dict = text_dict.readlines()
        global DB
        DB = {}
        for i in text_dict:
            i = i.split(':')
            k = i[0]
            v = i[1]
            v = v.strip()
            DB[k] = v

def DB_close():
    with open('database.txt', 'w', encoding='utf-8') as text_dict:
        print(DB, file= text_dict)
        
def ShowDB():
    #DB_init()
    return print('Количество пользователей: ', len(DB), 'Список пользователей:', *DB), Back_to_Menu()

def Back_to_Menu():   
    print('Чтобы вернуться обратно в меню - Введите слово "назад"')
    answ = input()
    if answ == 'назад':
        return Menu()
    else:
        return print('Команда не распознана.'), Back_to_Menu()
    
def NewUser():
    #print('Если хотите вернуться обратно в меню - напишите в терминале слово "назад"')
    login = input('Введите логин: ')
    # if login == 'назад':
    #     return Menu()
    password = input('Введите пароль: ')
    # if password == 'назад':
    #    return Menu()
    if login not in DB:
        DB[login] = to_md5(password)
        return print('Ваши данные зарегистрированы.'), Back_to_Menu()
    else:
        return print('Указанный логин занят. Пожалуйста, повторите попытку.'), NewUser()
         
def Menu():
    print()
    print('Выберите действие:', 'Показать базу зарегистророванных пользователей - Введите цифру "1"', 'Зарегистрироваться - Введите цифру "2"', 'Сменить пароль - Введите цифру "3"', 'Завершить работу - Введите цифру "4"', sep = '\n')
    return input()

def NewPassword():
    login = input('Введите логин: ')
    password = to_md5(input('Введите пароль: '))
    if login in DB:
        if password == DB.get(login):
            new_password = to_md5(input('Введите новый пароль: '))
            DB[login] = new_password
            return print('Пароль изменен.'), Back_to_Menu()
        else:
            return print('Неверный пароль. Повторите попытку.'), NewPassword()
    else:
        return print('Неверный логин. Повторите попытку.'), NewPassword()

    # if login not in DB:
    #     print ('Такого пользователя не существует')
    #     return NewPassword()
    # password = input('Введите пароль: ')
    # if password != data_base[login]:
    #     while password != data_base[login]:
    #         password = input('Вве')

DB_init()
while True:
    res = Menu()
    if res == '1':
        ShowDB() #поправить вывод
    if res == '2':
        NewUser()
    if res == '3':
        NewPassword()
    if res == '4':
        print('До свидания')
        DB_close()
        break