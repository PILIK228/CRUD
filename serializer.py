with open('new_base.json') as DB:
    m = DB.read().split('\n')
global_dict = dict()
d = dict()
empty_dict = dict()

i = 0

def CreateDict(index):
    d = dict()
    global i
    for _ in range(index+1, len(m)):
        s = str(m[i].strip())
        if s == "{" or s == "}":
            i += 1
            continue
        ind = s.find('"', 1)
        key = s[1:ind]
        if s.endswith(":"): 
            d[key]= CreateDict(i)
            i += 1
            continue
        if s.endswith(","):     
            value = s[ind+4: -2]
            d[key] = value
            i += 1
        else:
            i += 1
            value = s[ind+4: -1]
            d[key] = value
            return d


print(CreateDict(0))



# for i in range(len(m)):
#     i = i.strip()
#     if i[0] == "{":
#         # if d != empty_dict:
#             # global_dict = d
#         d = dict()
#         continue
#     if i[0] == '"':
#         ind = i.find('"', 1)
#         if i[-1] == "[":
#             global key
#             key = i[1:ind]
#             d[key] = list()
#         elif i[-1] == ",":
#             key1 = i[1:ind]
#             value1 = i[ind+4: -2]
#             d[key1] = value1
#         else:
#             key1 = i[1:ind]
#             value1 = i[ind+4: -1]
#             d[key1] = value1    
#             t = type(global_dict[key])
#             if t == list:
#                 a = global_dict.get(key)
#                 a.append(d)
                
