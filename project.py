# доделать функцию обновления пароля
# пароли храним в хеше (алгоритм )
# словарь с данными пользоветеля храним в файле
# ф-ии возвращают строки
from hashlib import md5
def to_md5(pw): #шифровщик
    return str(md5(pw.encode()).hexdigest())

def DB_init(): #открытие файла в формате словаря
    with open('database.txt', 'r', encoding='utf-8') as text_dict:
        text_dict = text_dict.readlines()
        global DB
        DB = {}
        for i in text_dict:
            i = i.split()
            k = i[0]
            v = i[1]
            v = v.strip()
            DB[k] = v

def DB_close(): #закрытие файла, формирует в файле новый список на основе обновленного словаря 
    with open('database.txt', 'w', encoding='utf-8') as text_dict:
            DB_list = DB.items()
            for i in DB_list:
              print(*i, file= text_dict)
        
def ReadAll(): #получение списка всех логинов 
    #DB_init()
    return print('Количество пользователей: ', len(DB), 'Список пользователей:', *DB), Back_to_Menu()

def GetUser(): #получить логин и пароль конкретного пользователя
    log = input('Для получения данных введите логин пользователя')
    pw = DB.get(log)
    if pw != None:
        print('Логин:', log, 'Пароль:', pw), Back_to_Menu()
    else:
        print('Пользователь не найден'), Back_to_Menu()

def DeleteUser(): #удалить контретного юзера по логину
    log = input('Для удаления данных введите логин пользователя: ')
    del DB[log]
    print('Данные пользователя удалены'), Back_to_Menu()
    
def UpdateUser(): #смена пароля
    login = input('Введите логин: ')
    password = to_md5(input('Введите пароль: '))
    if login in DB:
        if password == DB.get(login):
            new_password = to_md5(input('Введите новый пароль: '))
            DB[login] = new_password
            return print('Пароль изменен.'), Back_to_Menu()
        else:
            return print('Неверный пароль. Повторите попытку.'), UpdateUser()
    else:
        return print('Неверный логин. Повторите попытку.'), UpdateUser()

    # if login not in DB:
    #     print ('Такого пользователя не существует')
    #     return NewPassword()
    # password = input('Введите пароль: ')
    # if password != data_base[login]:
    #     while password != data_base[login]:
    #         password = input('Вве')

def NewUser(): #регистрация
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
         
def Menu(): #вывод меню
    print()
    print('Выберите действие:', 'Показать базу зарегистророванных пользователей - Введите цифру "1"', 'Зарегистрироваться - Введите цифру "2"', 'Сменить пароль - Введите цифру "3"', 'Получить данные определенного пользователя - Введите цифру "4"', 'Удалить данные определенного пользователя - Введите цифру "5"', 'Завершить работу - Введите цифру "6"', sep = '\n')
    return input()

def Back_to_Menu(): #предложение вернуться в меню  
    print('Чтобы вернуться обратно в меню - Введите слово "назад"')
    answ = input()
    if answ == 'назад':
        return Menu()
    else:
        return print('Команда не распознана.'), Back_to_Menu()

DB_init()
while True:
    res = Menu()
    if res == '1':
        ReadAll() #получение списка всех логинов
    if res == '2':
        NewUser() #регистрация
    if res == '3':
        UpdateUser() #смена пароля
    if res == '4':
        GetUser() #получить логин и пароль конкретного пользователя
    if res == '5':
        DeleteUser() #удалить контретного юзера по логину    
    if res == '6':     
        print('До свидания')
        DB_close()
        break