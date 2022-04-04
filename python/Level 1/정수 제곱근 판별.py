def solution(n):
    val = n ** 0.5
    
    if val == int(val):
        return (val+1) ** 2
    else:
        return -1