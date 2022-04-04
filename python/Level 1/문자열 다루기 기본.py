def solution(s):
    if (len(s) == 4 or len(s) == 6):
        return s.isdigit() # 내장함수 사용
# 예외처리문
#         try:
#             ans = int(s)
#             return True
#
#         except:
#             return False

    return False