def solution(id_list, report, k):    
    dic = {}
    rep = {}
    
    for user in id_list:
        dic[user] = 0
        rep[user] = []
    
    for r in report:
        key, val = r.split()
        rep[val].append(key)
    
    for key, val in rep.items():
        if len(set(val)) >= k:
            for v in set(val):
                dic[v] += 1
    
    return list(dic.values())