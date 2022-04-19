def solution(n):
    wm = ''
    for i in range(n) :
        if i % 2 == 0: 
            wm = wm + '수'
        elif i % 2 == 1: 
            wm = wm + '박'
    return wm

print(solution(3))