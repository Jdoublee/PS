def solution(arr):
    return [x for i, x in enumerate(arr) if i == 0 or arr[i-1] != arr[i]]