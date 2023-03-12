from hashlib import md5
with open('database.txt', 'a') as fileinp:
    for i in range(5):
        lg = input()
        pw = str(md5(input().encode()).hexdigest())
        print(lg, pw, file = fileinp)