from hashlib import md5
import json

DATABASE = 'new_base.json' #json файл с данными

def benchmark(func): #decorator
    import time

    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print('[*] Время выполнения: {} секунд.'.format(end-start))
    return wrapper

    def wrapped(*args):
        start_time = time.perf_counter_ns()
        res = function(*args)
        print(time.perf_counter_ns() - start_time)
        return res
    return wrapped

def to_md5(pw): #шифровщик
    return str(md5(pw.encode()).hexdigest())

def LoadBase(): #подгрузка базы
    with open('new_base.json') as DB:
      data = json.load(DB) 
#LoadBase()

def DumpBase(db): #запись обновленного словаря в файл
  with open(DATABASE, 'w') as DB:
    json.dump(db, DB, indent=3)

def GetAllUsers():
    with open(DATABASE) as DB:
      data = json.load(DB)
      for i in data['users']:
        for k in i:
            print(k,':', i[k])
        print() 
#GetAllUsers()

def GetAllSortedUsers(): #добавлена сортировка
    with open(DATABASE) as DB:
      data = json.load(DB)
      for i in sorted(data['users'], key=lambda user: (user['age'], user['name'])): #сортировка по возрасту и имени
        for k in i:
            print(k,':', i[k])
        print() 
      return
#GetAllSortedUsers()

def GetUser(login):
    with open(DATABASE) as DB:
      data = json.load(DB)
    for i in data['users']:
        if i['login'] == login:
          for k in i:
              print(k,':', i[k])
          return ' '
    return 'Указанный пользователь не существует. Введите данные повторно'
#print(GetUser(input('Введите логин: ')))
        
def UpdateUser(login, password):
    with open(DATABASE) as DB:
      data = json.load(DB)
    for i in data['users']:
        if i['login'] == login:
            i['password'] = to_md5(password)
            DumpBase(data)
            return 'Данные успешно записаны'
    return 'Указанный пользователь не существует. Введите данные повторно'
#print(UpdateUser(input('Логин: '), input('Новый пароль: ')))      

def CreateUser(login, password, name, age):
    with open(DATABASE) as DB:
      data = json.load(DB) 
    for i in data['users']:
        if i['login'] == login:
            return 'Указанный пользователь уже существует. Введите данные повторно'
    du = {}
    l = data['users']
    du['login'] = login
    du['password'] = to_md5(password)
    du['name'] = name
    du['age'] = int(age)
    l.append(du)
    data['users'] = l
    DumpBase(data)
    return 'Данные успешно записаны'
#print(CreateUser(input('Логин: '), input('Пароль: '), input('Имя: '), input('Возраст: ')))

def DeleteUser(login):
    with open(DATABASE) as DB:
      data = json.load(DB)
    for i in range(len(data['users'])):
        if data['users'][i]['login'] == login:
            del data['users'][i]
            DumpBase(data)
            return 'Данные успешно записаны'
    return 'Указанный пользователь не существует. Введите данные повторно'
#print(DeleteUser(input('Логин: ')))

def Menu(): #вывод меню
    print('Выберите действие:', 'Показать базу зарегистророванных пользователей - Введите цифру "1"', 'Получить данные определенного пользователя - Введите цифру "2"', 'Создать пользователя - Введите цифру "3"', 'Получить данные определенного пользователя - Введите цифру "4"', 'Удалить данные определенного пользователя - Введите цифру "5"', 'Завершить работу - Введите цифру "6"', sep = '\n')
    return input()

while True:
    res = Menu()
    if res == '1':
        GetAllUsers()
    if res == '2':
        print(GetUser(input('Введите логин: ')))
    if res == '3':
        print(CreateUser(input('Логин: '), input('Пароль: '), input('Имя: '), input('Возраст: ')))
    if res == '4':
        print(UpdateUser(input('Логин: '), input('Новый пароль: '))) 
    if res == '5':
        print(DeleteUser(input('Логин: ')))    
    if res == '6':     
        print('До свидания')
        break