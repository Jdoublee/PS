def solution(nums):
    spc = list(set(nums))
    
    if len(spc) > len(nums)//2:
        return len(nums)//2
    else:
        return len(spc)