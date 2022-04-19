#로또의 최고 순위와 최저순위
def solution(lottos, win_nums):
        
    countZero = lottos.count(0)    
    lottos = [i for i in lottos if i != 0]     
    #0제거 # 리스트 컴프리헨션(list comprehension)
    
    setUnion = set(lottos + win_nums)
    countWin = len(lottos) + len(win_nums) - len(setUnion)
    
    min = GetRank(countWin)
    max = GetRank(countWin + countZero)
    
    return [max, min]

def GetRank(countSame):
    if countSame <= 1:
        return 6
    return 7- countSame

print(solution([44, 1, 0, 0, 31, 25], 	[31, 10, 45, 1, 6, 19]))