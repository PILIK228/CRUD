# from hashlib import md5
# with open('database.txt', 'a') as fileinp:
#     for i in range(5):
#         lg = input()
#         pw = str(md5(input().encode()).hexdigest())
#         print(lg, pw, file = fileinp)
def DB_read():
    with open('database.txt', 'r', encoding='utf-8') as text_dict:
        text_dict = text_dict.readlines()
        global user
        user = []
        for i in text_dict:
            user.append(i.split())
        print(user)
        pass

def DB_init():
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
        print(DB)
def DB_c():
  with open('database.txt', 'w', encoding='utf-8') as text_dict:
            DB_list = DB.items()
            for i in DB_list:
              print(*i, file= text_dict)

DB_init()
DB['koka']= 'kkkkk'
DB_c()
DB_init()