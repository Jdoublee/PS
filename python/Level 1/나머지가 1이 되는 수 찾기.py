def solution(n):
    x = 2
    
    while x < n:
        if n % x == 1:
            break
        x += 1
    
    return x