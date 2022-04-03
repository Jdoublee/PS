def solution(n, m):
    answer = []
    
    # a > b
    a = max(n, m)
    b = min(n, m)
    
    # 유클리드 호제법 - 최대공약수 구하기
    while b > 0:
        mod = a % b
        a = b
        b = mod
    
    answer.append(a)
    answer.append(n*m/a) # 두 수의 곱 = 최대공약수와 최소공배수의 곱
    
    return answer