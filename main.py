import psycopg2
from hashlib import md5


def to_md5(pw):  # шифровщик
    return str(md5(pw.encode()).hexdigest())


def Menu_Login():
    print('Выберите действие:',
          'Авторизоваться - Введите цифру "1"',
          'Зарегистрироваться - Введите цифру "2"',
          'Завершить работу - Введите цифру "3"', sep='\n')
    return str(input())


def Menu_Admin():
    print('Выберите действие:',
          'Показать базу зарегистророванных пользователей - Введите цифру "1"',
          'Получить данные определенного пользователя - Введите цифру "2"',
          'Изменить роль пользователя - Введите цифру "3"',
          'Изменить пароль - Введите цифру "4"',
          'Удалить данные определенного пользователя - Введите цифру "5"',
          'Выйти из аккаунта - Введите цифру "6"',
          'Завершить работу - Введите цифру "7"', sep='\n')
    return str(input())


def Menu_Moderator():
    print('Выберите действие:',
          'Показать базу зарегистророванных пользователей - Введите цифру "1"',
          'Получить данные определенного пользователя - Введите цифру "2"',
          'Изменить роль пользователя - Введите цифру "3"',
          'Изменить пароль - Введите цифру "4"',
          'Выйти из аккаунта - Введите цифру "5"',
          'Завершить работу - Введите цифру "6"', sep='\n')
    return str(input())


def Menu_User():
    print('Выберите действие:',
          'Получить данные своего аккаунта - Введите цифру "1"',
          'Изменить пароль - Введите цифру "2"',
          'Выйти из аккаунта - Введите цифру "3"',
          'Завершить работу - Введите цифру "4"', sep='\n')
    return str(input())


def Check_Role(log):
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM users WHERE login=(%s)", (log,))
        feedback = cur.fetchone()
        if feedback is not None:
            return feedback[6]
        else:
            return print('ОШИБКА РОЛИ')


def Check_Login(log):
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM users WHERE login=(%s)", (log,))
        feedback = cur.fetchone()
        if feedback is None:
            return 1
        else:
            return -1


def Auth(log, pw):
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM users WHERE login=(%s)", (log,))
        feedback = cur.fetchone()
        if feedback is not None:
            if feedback[2] == to_md5(pw):
                return feedback[6]
            else:
                return -2
        else:
            return -1


def CreateUser(log, pw, nam, surnam, ag):  # добавить проверку на логин и корректного ввода даты рождения
    pw = to_md5(pw)
    with conn.cursor() as cur:
        cur.execute("""INSERT INTO users(login, password, name, surname, age)
            VALUES (%(log)s, %(pw)s, %(nam)s, %(surnam)s, %(ag)s);
            """, {'log': log, 'pw': pw, 'nam': nam, 'surnam': surnam, 'ag': ag})
        conn.commit()
    return 'OK'


def Change_Role(log, role):
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM users WHERE login=(%s)", (log,))
        feedback = cur.fetchone()
        if feedback is not None:
            role = int(role)
            with conn.cursor() as cur:
                cur.execute("UPDATE users SET roles_id=(%s) WHERE login=(%s)", (role, log))
                conn.commit()
                return 'OK'
        else:
            return 'ОШИБКА ЛОГИНА'


def GetAllUsers():
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM users")
        return cur.fetchall()


def GetUser(log):
    with conn.cursor() as cur:
        cur.execute("""SELECT users.id, login, name, surname, age, role 
        FROM users inner join roles on users.roles_id = roles.id 
        WHERE login=(%s)""", (log,))
        feedback = cur.fetchone()
        if feedback is not None:
            return feedback
        else:
            return 'ОШИБКА'


def ChangePassword(log, pw):
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM users WHERE login=(%s)", (log,))
        feedback = cur.fetchone()
        if feedback is not None:
            pw = to_md5(pw)
            with conn.cursor() as cur:
                cur.execute("UPDATE users SET password=(%s) WHERE login=(%s)", (pw, log))
                conn.commit()
                return 'OK'
        else:
            return 'ОШИБКА'


def DeleteUser(log):
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM users WHERE login=(%s)", (log,))
        feedback = cur.fetchone()
        if feedback is not None:
            with conn.cursor() as cur:
                cur.execute("DELETE FROM users WHERE login=(%s)", (log,))
                conn.commit()
                return 'OK'
        else:
            return 'ОШИБКА'


try:
    conn = psycopg2.connect('postgresql://postgres:qwerty@localhost:5432/db')
except Exception as i:
    print(i)
else:
    status = 0
    flag = True
    while flag:
        while status == 0:  # log_out
            res = Menu_Login()
            if res == '1':
                # авторизация
                print('Выбрана авторизация')
                print('Введите логин: ')
                log = str(input())
                print('Введите пароль: ')
                pw = str(input())
                answ = Auth(log, pw)
                if answ == -1:
                    print('ОШИБКА ЛОГИНА')
                elif answ == -2:
                    print('ОШИБКА ПАРОЛЯ')
                elif 1 <= answ <= 3:
                    status = answ
            elif res == '2':
                # регистрация
                print('Выбрана регистрация')
                print('Введите логин')
                log = str(input())
                print('Введите пароль')
                pw = str(input())
                print('Введите имя')
                nam = str(input())
                print('Введите фамилию')
                surnam = str(input())
                print('Введите дату рождения в формате ХХХХ-ХХ-ХХ (ПРИМЕР: 2000-12-23)')
                ag = str(input())
                answ = Check_Login(log)
                if answ == 1:
                    print(CreateUser(log, pw, nam, surnam, ag))
                    status = Check_Role(log)
                else:
                    print('ОШИБКА ЛОГИНА')
            elif res == '3':
                status = 4

        while status == 1:  # admin
            res = Menu_Admin()
            if res == '1':
                print(GetAllUsers())
            elif res == '2':
                print('Введите логин пользователя')
                log_user = input()
                print(GetUser(log_user))
            elif res == '3':
                print('Введите логин пользователя')
                log_user = str(input())
                print('Выберите назначаемую роль:',
                      'Администратор - Введите цифру "1"',
                      'Модератор - Введите цифру "2"',
                      'Пользователь - Введите цифру "3"', sep='\n')
                role_user = str(input())
                if role_user in ['1', '2', '3']:
                    print(Change_Role(log_user, role_user))
                else:
                    print('ОШИБКА')
            elif res == '4':
                print('Введите новый пароль')
                new_pw = to_md5(input())
                print(ChangePassword(log, new_pw))
            elif res == '5':
                print('Введите логин пользователя')
                log_user = str(input())
                print(DeleteUser(log_user))
            elif res == '6':
                status = 0
            elif res == '7':
                status = 4

        while status == 2:  # moderator
            res = Menu_Moderator()
            if res == '1':
                print(GetAllUsers())
            elif res == '2':
                print('Введите логин пользователя')
                log_user = input()
                print(GetUser(log_user))
            elif res == '3':
                print('Введите логин пользователя')
                log_user = input()
                print('Выберите назначаемую роль:',
                      'Модератор - Введите цифру "2"',
                      'Пользователь - Введите цифру "3"', sep='\n')
                role_user = input()
                if role_user in ['2', '3']:
                    print(Change_Role(log_user, role_user))
                else:
                    print('ОШИБКА')
            elif res == '4':
                print('Введите новый пароль')
                new_pw = to_md5(input())
                print(ChangePassword(log, new_pw))
            elif res == '5':
                status = 0
            elif res == '6':
                status = 4

        while status == 3:  # user
            res = Menu_User()
            if res == '1':
                print(GetUser(log))
            elif res == '2':
                print('Введите новый пароль')
                new_pw = to_md5(input())
                print(ChangePassword(log, new_pw))
            elif res == '3':
                status = 0
            elif res == '4':
                status = 4

        while status == 4:  # finish
            flag = False
            break
