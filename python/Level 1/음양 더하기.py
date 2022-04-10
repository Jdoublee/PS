def solution(absolutes, signs):
    return sum([ab if sn else -1*ab for ab, sn in zip(absolutes, signs)])