def binary_search(arr, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return None

n = int(input())
store = list(map(int, input().split()))

m = int(input())
customer = list(map(int, input().split()))

store.sort()

for x in customer:
    if binary_search(store, x, 0, n-1) != None:
        print('yes', end=' ')
    else:
        print('no', end=' ')