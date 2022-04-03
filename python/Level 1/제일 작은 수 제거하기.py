def solution(arr):
    num = min(arr)
    
    arr.remove(num) # O(N)
    
    if len(arr) == 0:
        arr.append(-1)
        
    return arr