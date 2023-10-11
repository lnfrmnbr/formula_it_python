users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']

d = {"Общее количество": 0, "Уникальные посещения": 0}

d["Общее количество"] = len(users)

def unique_request(ls):
    l = []
    k = 0
    for el in ls:
        if not (el in l):
            k+=1
            l.append(el)
    return k

d["Уникальные посещения"] = unique_request(users)
print(d)
