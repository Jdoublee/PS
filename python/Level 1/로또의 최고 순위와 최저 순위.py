def solution(lottos, win_nums):    
    cnt = sum([1 for l in lottos if l in win_nums])
    zeroCnt = lottos.count(0)
    
    rank = [6,6,5,4,3,2,1]
    
    return [rank[cnt+zeroCnt], rank[cnt]]