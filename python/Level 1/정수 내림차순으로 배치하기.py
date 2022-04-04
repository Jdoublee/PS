def solution(n):    
    ans = list(str(int(n))) # 런타임에러때문에 int로 감싸줌
    
    ans.sort(reverse=True)
        
    return int(''.join(ans))