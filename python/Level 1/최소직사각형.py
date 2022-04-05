def solution(sizes):    
    w = 0
    h = 0
    
    for x, y in sizes:
        if x > y:
            x, y = y, x
        w = max(w, x) # 둘 중 긴 것 중에 최대값
        h = max(h, y) # 둘 중 짧은 것 중에 최대값
    
    return w * h