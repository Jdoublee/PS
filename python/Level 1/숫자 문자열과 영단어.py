def solution(s):
    answer = ''
    
    eng = ['zero','one','two','three','four','five','six','seven','eight','nine']
    num = '0123456789'
    
    tmp = ''
    
    for n in s:
        if n in num:
            if tmp != '':
                answer += str(eng.index(tmp))
                tmp = ''
            answer += n 
        elif tmp in eng:
            answer += str(eng.index(tmp))
            tmp = n
        else:
            tmp += n

    if tmp != '':
        answer += str(eng.index(tmp))
    
    return int(answer)
    # replace 사용 가능