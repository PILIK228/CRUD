import psycopg2


conn = psycopg2.connect('postgresql://postgres:qwerty@localhost:5432/db') #открытие соединения

cur = conn.cursor()

cur.execute("""INSERT INTO users (user_login, user_password, user_name, user_surname, user_age)
            VALUES (%(login)s, %(password)s, %(name)s, %(surname)s, %(age)s);
            """, {'login': '<логин>', 'password': '<password>', 'name': '<name>', 'surname': '<surname>', 'age': '<age>'})
conn.commit()

full_fetch



# try:
#     conn = psycopg2.connect('postgresql://postgres:qwerty@localhost:5432/db')
#
#     with conn.cursor() as cursor:
#         cursor.execute(
#             '''INSERT INTO public.users (new_id, user_login, user_password, user_name, user_surname, user_age) VALUES (DEFAULT, 'popopo'::varchar(30), 'wr23e1y23812us12us10us901u9u9u21'::varchar(60), 'Popp'::varchar(30), 'Kjkjkd'::varchar(30), '1999-03-18'::date)'''
#         )
#         conn.commit()
#         print('[INFO] Data was successfully inserted')
#
#
# except:
#     print('Can`t establish connection to database')
