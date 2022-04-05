def solution(d, budget):
    answer = 0
    
    d.sort()
    
    for x in d:
        budget -= x
        if budget < 0:
            break
        answer += 1
    
    return answer