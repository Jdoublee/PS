def solution(n):
    arr = [1 if i == 1 else 0 for i in range(n+1)]
    
    for i in range(2,n+1):
        arr[i] = arr[i-2] + arr[i-1]
    
    return arr[n] % 1234567

    # 예전 풀이
    # a = 0
    # b = 1
    
    # for _ in range(2, n+1):
    #     a, b = b, a+b
        
    # return b % 1234567