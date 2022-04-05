def solution(n):
    answer = 0
    val = ''
    
    while n >= 3:
        val += str(n%3)
        n //= 3
    val += str(n)
    
    i = 0
    for v in val[::-1]:
        answer += int(v) * 3**i
        i += 1
    
    return answer