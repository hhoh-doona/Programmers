
#거리두기 확인하기
import itertools


def solution(places):
    answer = []
    for aPlace in places:        
        answer.append(CheckPlace(aPlace))
    return answer

def CheckPlace(aPlace):
    for i,j in itertools.product(range(0,5),repeat=2):
        if aPlace[i][j] == 'P':
            if CheckDistance(aPlace, i, j) == False:
                return 0
    return 1
                
    
def CheckDistance(aPlace, i, j):
    d = i + 1
    if d < 5:
        if aPlace[d][j] == 'P':
            return False
        elif d+1 < 5 and aPlace[d][j] == 'O' and aPlace[d+1][j] == 'P':
            return False
    
    r = j + 1
    if r < 5:
        if aPlace[i][r] == 'P':
            return False
        elif r+1 <5 and aPlace[i][r] == 'O' and aPlace[i][r+1] == 'P':
            return False
    
    if (d<5 and r<5) and aPlace[d][r] == 'P' and (aPlace[d][j] != 'X' or aPlace[i][r] != 'X'):
        return False
    
    l = j -1
    
    if (d<5 and l>-1) and aPlace[d][l] == 'P' and (aPlace[d][j] != 'X' or aPlace[i][l] != 'X'):
        return False
    
    return True

print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]));