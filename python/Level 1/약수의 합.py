def solution(n):    
    return sum([i for i in range(1, n+1) if n % i == 0])
    # 1부터 자기자신까지 
    # -> 더 효율적이게는 1부터 제곱근까지 계산 후 *2 (x**2 가 n인 경우는 한 번만 더해줌)
