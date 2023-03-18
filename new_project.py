from hashlib import md5
import json
import time

DATABASE = 'new_base.json' #json файл с данными

def benchmark(func): #decorator
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print('[*] Время выполнения: {} секунд.'.format(end-start))
    return wrapper

def to_md5(pw): #шифровщик
    return str(md5(pw.encode()).hexdigest())

def LoadBase(): #подгрузка базы
    with open(DATABASE) as DB:
      return json.load(DB) 

def DumpBase(db): #запись обновленного словаря в файл
    with open(DATABASE, 'w') as DB:
        json.dump(db, DB, indent=3)
    return "OK"

def GetAllUsers():
      data = LoadBase()
      return data['users']
#GetAllUsers()

def GetAllSortedUsers(): #добавлена сортировка
      data = LoadBase()
      return sorted(data['users'], key=lambda user: (user['age'], user['name']))
#GetAllSortedUsers()

def GetUser(login):
      data = LoadBase()
      for i in data['users']:
        if i['login'] == login:
          return i
      return 'ОШИБКА'
#print(GetUser(input('Введите логин: ')))
        
def UpdateUser(login, password):
      data = LoadBase()
      for i in data['users']:
        if i['login'] == login:
            i['password'] = to_md5(password)
            DumpBase(data)
            return 'ОК'
      return 'ОШИБКА'
#print(UpdateUser(input('Логин: '), input('Новый пароль: ')))      

def CreateUser(login, password, name, age):
    data = LoadBase() 
    for i in data['users']:
        if i['login'] == login:
            return 'ОШИБКА'
    du = {}
    l = data['users']
    du['login'] = login
    du['password'] = to_md5(password)
    du['name'] = name
    du['age'] = int(age)
    l.append(du)
    data['users'] = l
    DumpBase(data)
    return 'ОК'
#print(CreateUser(input('Логин: '), input('Пароль: '), input('Имя: '), input('Возраст: ')))

def DeleteUser(login):
    data = LoadBase()
    for i in range(len(data['users'])):
        if data['users'][i]['login'] == login:
            del data['users'][i]
            DumpBase(data)
            return 'ОК'
    return 'ОШИБКА'
#print(DeleteUser(input('Логин: ')))

def Menu(): #вывод меню
    print('Выберите действие:', 'Показать базу зарегистророванных пользователей - Введите цифру "1"', 'Получить данные определенного пользователя - Введите цифру "2"', 'Создать пользователя - Введите цифру "3"', 'Получить данные определенного пользователя - Введите цифру "4"', 'Удалить данные определенного пользователя - Введите цифру "5"', 'Завершить работу - Введите цифру "6"', sep = '\n')
    return input()

while True:
    res = Menu()
    if res == '1':
        print(GetAllUsers())
    if res == '2':
        print('Введите логин: ')
        login = input()
        print(GetUser(login))
    if res == '3':
        print('Введите логин')
        login = input()
        print('Введите пароль')
        password = input()
        print('Введите имя')
        name = input()
        print('Введите возраст')
        age = input()
        print(CreateUser(login, password, name, age))
    if res == '4':
        print('Введите логин')
        login = input()
        print('Введите новый пароль')
        password = input()
        print(UpdateUser(login, password)) 
    if res == '5':
        print('Введите логин')
        login = input()
        print(DeleteUser(login))    
    if res == '6':     
        print('До свидания')
        break