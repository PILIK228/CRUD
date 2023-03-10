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
    return(input())

flag = True
while flag == True:
    res = Menu()
    if res == 1:
        ShowDB()
    if res == 2:
        NewUser()
    if res == 3:
        print('До свидания')
        flag = False
        print(123)
        break