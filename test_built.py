import psycopg2
from hashlib import md5

def to_md5(pw):  # шифровщикаа
    return str(md5(pw.encode()).hexdigest())


def CreateUser(login, password, name, surname, age):  # добавить проверку на логин и корректного ввода даты рождения
    password = to_md5(password)
    with conn.cursor() as cur:
        cur.execute("""INSERT INTO users(user_login, user_password, user_name, user_surname, user_age)
            VALUES (%(log)s, %(pw)s, %(nam)s, %(surnam)s, %(ag)s);
            """, {'log': login, 'pw': password, 'nam': name, 'surnam': surname, 'ag': age})
        conn.commit()
        return "OK"

# print(CreateUser('kakuzo1', '12345', 'Kakuzo', 'Kunoichi', '2007-05-07'))


def GetAllUsers():
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM users")
        return cur.fetchall()

# print(GetAllUsers())


def GetAllSortedUsers():
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM users ORDER BY user_age")
        return cur.fetchall()


# print(GetAllSortedUsers())


def GetUser(login):
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM users WHERE user_login=(%s)", (login,))
        feedback = cur.fetchone()
        if feedback is not None:
            return feedback
        else:
            return 'ОШИБКА'


# print(GetUser('diablo2435'))


def UpdateUser(login, password):
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM users WHERE user_login=(%s)", (login,))
        feedback = cur.fetchone()
        if feedback is not None:
            password = to_md5(password)
            with conn.cursor() as cur:
                cur.execute("UPDATE users SET user_password=(%s) WHERE user_login=(%s)", (password, login))
                conn.commit()
                return 'OK'
        else:
            return 'ОШИБКА'


# print(UpdateUser('diablo2435', '12345qwerty'))


def DeleteUser(login):
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM users WHERE user_login=(%s)", (login,))
        feedback = cur.fetchone()
        if feedback is not None:
            with conn.cursor() as cur:
                cur.execute("DELETE FROM users WHERE user_login=(%s)", (login,))
                conn.commit()
                return 'OK'
        else:
            return 'ОШИБКА'


# print(DeleteUser('popopo'))


def Menu():  # вывод меню
    print('Выберите действие:', 'Показать базу зарегистророванных пользователей - Введите цифру "1"',
          'Получить данные определенного пользователя - Введите цифру "2"', 'Создать пользователя - Введите цифру "3"',
          'Получить данные определенного пользователя - Введите цифру "4"',
          'Удалить данные определенного пользователя - Введите цифру "5"', 'Завершить работу - Введите цифру "6"',
          sep='\n')
    return str(input())


try:
    conn = psycopg2.connect('postgresql://postgres:qwerty@localhost:5432/db')  # открытие соединения
except Exception as i:
    print(i)
else:
    while True:
        res = Menu()
        if res == '1':
            print(GetAllUsers())
        if res == '2':
            print('Введите логин: ')
            login = (input())
            print(GetUser(login))
        if res == '3':
            print('Введите логин')
            login = (input())
            print('Введите пароль')
            password = (input())
            print('Введите имя')
            name = (input())
            print('Введите фамилию')
            surname = (input())
            print('Введите дату рождения в формате ХХХХ-ХХ-ХХ (ПРИМЕР: 2000-12-23)')
            age = (input())
            print(CreateUser(login, password, name, surname, age))
        if res == '4':
            print('Введите логин')
            login = (input())
            print('Введите новый пароль')
            password = (input())
            print(UpdateUser(login, password))
        if res == '5':
            print('Введите логин')
            login = (input())
            print(DeleteUser(login))
        if res == '6':
            print('До свидания')
            break