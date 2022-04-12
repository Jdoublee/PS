from itertools import combinations

def solution(nums):
    ans = 0
    sumList = list(map(sum,list(combinations(nums,3))))
    
    for n in sumList:
        flg = True
        for i in range(2,n):
            if n % i == 0:
                flg = False
                break
        
        if flg:
            ans += 1
    
    return ans