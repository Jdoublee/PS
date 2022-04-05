def solution(arr, d):
    answer = [i for i in arr if i % d == 0]
    
    if len(answer) == 0:
        answer.append(-1)
    
    return sorted(answer)