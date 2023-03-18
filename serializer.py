with open('new_base.json') as DB:
    m = DB.read().split('\n')
m = ''.join(map(lambda x: x.strip(), m))
m = m[1:-1]
s = {}
k = True

# for i in range(len(m)):
#     if m[i] == '"' and k == True:
#         sk = m[i+1]
#         ek = m.find('"', i+1, len(m))+1
#         k = False
#         key = m[sk:ek]
#     elif m[i] == '"' and k == False:
#         k = True 



print(m)