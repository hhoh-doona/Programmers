def solution(lottos, win_nums):
    rank = [6, 6, 5, 4, 3, 2, 1]

    zeros = lottos.count(0)
    ans = 0
    for i in win_nums:
        if i in lottos:
            ans += 1

    return rank[zeros + ans], rank[ans]


print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))
print(solution([0, 0, 0, 0, 0, 0], [38, 19, 20, 40, 15, 25]))
print(solution([45, 4, 35, 20, 3, 9],[20, 9, 3, 45, 4, 35]))