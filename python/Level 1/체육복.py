def solution(n, lost, reserve):    
    students = [1 for _ in range(n)]
    
    for i in lost:
        students[i-1] -= 1
    
    for j in reserve:
        students[j-1] += 1
        
    for i, s in enumerate(students):
        if s > 1:
            if i > 0 and students[i-1] == 0:
                students[i-1] += 1
                students[i] -= 1
            elif i < n-1 and students[i+1] == 0:
                students[i+1] += 1
                students[i] -= 1
    
    return  n - students.count(0)