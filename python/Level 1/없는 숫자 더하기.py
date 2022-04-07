def solution(numbers):    
    cmp = [i for i in range(10) if i not in numbers]
    
    return sum(cmp) # 45 - sum(numbers)