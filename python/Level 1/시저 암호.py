def solution(s, n):
    answer = ''
        
    for word in s:
        if word == " ":
            answer += word
            continue
            
        res = ord(word) + n
        if word < 'a': # 대문자인 경우
            if res > ord('Z'):
                res -= 26 
        else: # 소문자인 경우
             if res > ord('z'):
                res -= 26
        
        answer += chr(res)

    return answer