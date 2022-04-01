def solution(x):
    tot = 0
    val = x
    
    while val > 0:
        tot += val%10
        val //= 10
    
    if x % tot == 0: 
        return True
    
    return False