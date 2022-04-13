def solution(N, stages):
    answer = [[i,0] for i in range(1,N+1)]
    
    for i in range(1,N+1):
        if max(stages) < i:
            answer[i-1][1] = 0
            continue
            
        answer[i-1][1] = sum([1 for x in stages if x == i]) / sum([1 for x in stages if x >= i])
        
    answer.sort(key=lambda x:(-x[1],x[0]))
    
    return [x for x,_ in answer]