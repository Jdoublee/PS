def solution(n):
    i = n
    cnt = bin(n).count('1')
    
    while True:
        i += 1
        
        if bin(i).count('1') == cnt:
            return i