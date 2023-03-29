from hashlib import md5
def to_md5(pw): #шифровщик
    return str(md5(pw.encode()).hexdigest())

def GetAllUsers():
    with open('database.txt', 'r', encoding='utf-8') as DataBase:
        DataBase = DataBase.readlines()
        AllUsers = []
        for i in DataBase:
            AllUsers.append(i.split())
    return AllUsers
#print(GetAllUsers()

def GetUser():
    with open('database.txt', 'r', encoding='utf-8') as DataBase:
        DataBase = DataBase.readlines()
        AllUsers = []
        for i in DataBase:
            AllUsers.append(i.split())
    login = input('Для получения данных введите логин пользователя: ')
    flag = False
    for i in AllUsers:
        if i[0] == login:
            flag = True
            return print('Логин: {0}, Пароль: {1}'.format(i[0],i[1]))
            break
    if flag == False:
        return print('Указанный пользователь не существует. Введите данные повторно'), GetUser()
#GetUser()
        
def UpdateUser():
    with open('database.txt', 'r', encoding='utf-8') as DataBase:
        DataBase = DataBase.readlines()
        AllUsers = []
        for i in DataBase:
            AllUsers.append(i.split())
    login = input('Для изменения данных введите логин пользователя: ')
    flag = False
    for i in AllUsers:
        if i[0] == login:
            pw = to_md5(input('Введите новый пароль: '))
            flag = True
            AllUsers.remove(i)
            AllUsers.append([login, pw])
            break
    if flag == False:
        return print('Указанный пользователь не существует. Введите данные повторно'), UpdateUser()
    with open('database.txt', 'w', encoding='utf-8') as DataBase:
        for i in AllUsers:
            print(*i, file= DataBase)
    return print('Данные успешно записаны')
#UpdateUser()        

def CreateUser():
    with open('database.txt', 'r', encoding='utf-8') as DataBase:
        DataBase = DataBase.readlines()
        AllUsers = []
        for i in DataBase:
            AllUsers.append(i.split())
    login = input('Введите логин: ')
    flag = False
    for i in AllUsers:
        if i[0] == login:
            flag = True
            return print('Указанный логин уже существует. Введите данные повторно'), CreateUser()
            break
    if flag == False:
        pw = to_md5(input('Введите пароль: '))
        AllUsers.append([login, pw])
    with open('database.txt', 'w', encoding='utf-8') as DataBase:
        for i in AllUsers:
            print(*i, file= DataBase)
    return print('Данные успешно записаны')
#CreateUser()

def DeleteUser():
    with open('database.txt', 'r', encoding='utf-8') as DataBase:
        DataBase = DataBase.readlines()
        AllUsers = []
        for i in DataBase:
            AllUsers.append(i.split())
    login = input('Для удаления данных введите логин пользователя: ')
    flag = False
    for i in AllUsers:
        if i[0] == login:
            flag = True
            AllUsers.remove(i)
            break
    if flag == False:
        return print('Указанный пользователь не существует. Введите данные повторно'), UpdateUser()
    with open('database.txt', 'w', encoding='utf-8') as DataBase:
        for i in AllUsers:
            print(*i, file= DataBase)
    return print('Данные успешно удалены')

