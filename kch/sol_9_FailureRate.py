def solution(N, stages):
    player = len(stages)
    failList = []
    answer = []

    for i in range(1, N+1): # N + 1 하지 않으면 1 ~ 4까지 나옴
        cnt = stages.count(i) # 클리어 못한 플레이어

        if (player == 0): # 실패율 계산 0일 경우 실패한 플레이어 X
            fail = 0
        else: 
            fail = cnt / player
        
        player -= cnt # 다음 스테이지에 도달한 플레이어 수

        failList.append((i, fail)) # 리스트를 딕셔너리처럼 쓸수 있음

    failList = sorted(failList, key=lambda x: x[1], reverse=True) # 정렬

    for i in failList:
        answer.append(i[0])

    return answer


print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4, [4, 4, 4, 4, 4]))