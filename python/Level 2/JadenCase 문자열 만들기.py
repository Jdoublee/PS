def solution(s):    
    s = s[0].upper() + s[1:].lower()
    
    s = ''.join(list(s[0])+( [x.upper() if s[i] == ' ' else x for i, x in enumerate(s[1:])]))
    
    return s