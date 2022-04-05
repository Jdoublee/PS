def solution(price, money, count):    
    answer = (price*count*(count+1)//2) - money
    
    return max(0,answer)
    
    # if answer > 0:
    #     return answer
    # else:
    #     return 0