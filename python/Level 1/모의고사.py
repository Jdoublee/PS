def solution(answers):
    arr = [0 for _ in range(3)]
    
    firstw = '12345' # 5
    secondw = '21232425' # 8
    thirdw = '3311224455' # 10
    
    for i, ans in enumerate(answers):
        if int(firstw[i%5]) == ans:
            arr[0] += 1
        if int(secondw[i%8]) == ans:
            arr[1] += 1
        if int(thirdw[i%10]) == ans:
            arr[2] += 1
    
    return [i+1 for i in range(3) if arr[i] == max(arr)]