def solution(numbers, hand):
    answer = ''
    
    thumbL = 10
    thumbR = 12
    
    h = 'L' if hand == 'left' else 'R'
    
    for number in numbers:
        if number == 0:
            number = 11
            
        if number in [1, 4, 7]:
            answer += 'L'
            thumbL = number
        elif number in [3, 6, 9]:
            answer += 'R'
            thumbR = number
        else:
            distL = 0
            distR = 0
            backL = thumbL
            backR = thumbR
            
            if thumbL in [1,4,7,10]:
                distL += 1
                thumbL += 1
            distL += abs(number - thumbL)//3
            
            if thumbR in [3,6,9,12]:
                distR += 1
                thumbR -= 1
            distR += abs(number - thumbR)//3
            
            if distL == distR:
                answer += h
                if h == 'L':
                    thumbL = number
                    thumbR = backR
                else:
                    thumbR = number
                    thumbL = backL
            elif distL < distR:
                answer += 'L'
                thumbL = number
                thumbR = backR
            else:
                answer += 'R'
                thumbR = number
                thumbL = backL
    
    return answer