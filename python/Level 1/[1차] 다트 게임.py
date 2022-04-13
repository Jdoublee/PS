def solution(dartResult):
    answer = [0,0,0]
    scr = ''
    bns = ''
    score = {0:[], 1:[], 2:[]}
    i = 0
    
    for res in dartResult:
        if res in '1234567890':
            if bns:
                score[i].append(scr)
                score[i].append(bns)
                i += 1
                scr = ''
                bns = ''
            scr += res
        else:
            bns += res
    score[i].append(scr)
    score[i].append(bns)
    
    for k,v in score.items():
        val = int(v[0])
        if v[1][0] == 'S':
            cnt = val
        elif v[1][0] == 'D':
            cnt = val**2
        else:
            cnt = val**3
        
        if len(v[1]) > 1:
            if v[1][1] == '*':
                if k > 0:
                    answer[k-1] *= 2
                cnt *= 2
            else:
                cnt *= -1
        answer[k] = cnt
    
    return sum(answer)