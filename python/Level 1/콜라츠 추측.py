def solution(num):
    count = 0
    
    while count < 500:
        if num == 1: # 13번 케이스. 비교 순서 명확히
            return count
        
        count += 1

        if num % 2 == 0:
            num /= 2
        else:
            num = num*3 + 1
    
    return -1