#로또의 최고 순위와 최저순위
def solution(lottos, win_nums):
    answer = []
    
    countZero = lottos.count(0)
    
    #0제거
    lottos = [i for i in lottos if i != 0] 
    
    setUnion = set(lottos + win_nums)
    countSame = len(lottos) + len(win_nums) - len(setUnion)
    
    min = 7-countSame
    if countSame <= 1: min=6

    max = 7-(countSame + countZero)
    if (countSame + countZero) <= 1: max=6
           
    return [max, min]



print(solution([44, 1, 0, 0, 31, 25], 	[31, 10, 45, 1, 6, 19]))