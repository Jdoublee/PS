def solution(s):
    answer = ''
    i = 0
    
    for ch in s:
        if ch == ' ':
            answer += ch
            i = 0
            continue
        
        if i % 2 == 0:
            answer += ch.upper()
        else:
            answer += ch.lower()
        i += 1
    
    return answer