n = int(input())
plans = list(input().split())

x = 1
y = 1

for plan in plans:
    if plan == 'L':
        y = max(y-1, 1)
    elif plan == 'R':
        y = min(y+1, n)
    elif plan == 'U':
        x = max(x-1, 1)
    else:
        x = min(x+1, n)
        
print(x, y)
    
    
