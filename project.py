# доделать функцию обновления пароля
# пароли храним в хеше (алгоритм md5)
# словарь с данными пользоветеля храним в файле
# ф-ии возвращают строки
# +20 задач

data_base = {'dimka39':'1234fs',
        'lana_rhoades':'fwsfwefg',
        'jojo':'qwerty',
        'vodka_pivo':'fjasdasd'}

def ShowDB():
    return print('Количество пользователей: ', len(data_base), 'Список пользователей:', *data_base, sep='\n'), Menu()
    
def NewUser():
    print('Если хотите вернуться обратно в меню - напишите в терминале слово "назад"')
    login = input('Введите логин: ')
    if login == 'назад':
        return Menu()
    password = input('Введите пароль: ')
    if password == 'назад':
        return Menu()
    if login not in data_base:
        data_base[login] = password
        return print('Ваши данные зарегистрированы. Возвращение в меню.'), Menu()
    else:
        return print('Указанный логин занят. Пожалуйста, повторите попытку.'), NewUser()
         
def Menu():
    print()
    print('Выберите действие:', 'Показать базу зарегистророванных пользователей - Введите цифру "1"', 'Зарегистрироваться - Введите цифру "2"', 'Завершить работу - Введите цифру "3"', sep = '\n')
    return input()

def NewPassword():
    login = input('Введите логин: ')

    # использовать get
    if login not in data_base:
        print ('Такого пользователя не существует')
        return NewPassword()
    password = input('Введите пароль: ')
    if password != data_base[login]:
        while password != data_base[login]:
            password = input('Вве')


flag = True
while flag == True:
    res = Menu()
    if res == 1:
        ShowDB()
        flag = False
    if res == 2:
        NewUser()
        flag = False
    if res == 3:
        print('До свидания')
        print()
        flag = False
        break