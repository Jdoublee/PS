def solution(n):
    answer = 0
    
    for x in range(2, n+1):
        flag = True
        for i in range(2,int(x**0.5)+1):
            if x % i == 0:
                flag = False
                break
        
        if flag:
            answer += 1
    
    return answer