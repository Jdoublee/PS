def solution(n, arr1, arr2):
    answer = []
    a1 = []
    a2 = []
    
    for a, b in zip(arr1, arr2):
        res = ''
        while a > 0:
            res += str(a % 2)
            a = a//2
        
        while len(res) < n:
            res += '0'
        a1.append(''.join(reversed(res)))
        
        res = ''
        while b > 0:
            res += str(b % 2)
            b = b//2
        
        while len(res) < n:
            res += '0'
        a2.append(''.join(reversed(res)))
        
    for a, b in zip(a1,a2):
        answer.append(''.join('#' if x == '1' or y == '1' else ' ' for x, y in zip(a,b)))
        
    return answer