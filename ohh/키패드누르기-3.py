def GetKeyPadCoord():
    dic = {}
    
    k=1
    for i in range(0,3):
        for j in range(0,3):
            dic[k] = [i,j]
            k +=1
    dic['*'] = [3,0]
    dic[0] = [3,1]
    dic['#'] = [3,2]
    
    return dic


def solution(numbers, hand):    

    answer = ''
    lbefo = '*'
    rbefo = '#'

    dicKeyPadCoord = GetKeyPadCoord()

    for num in numbers:
        if num == 1 or num == 4 or num == 7:
            answer, lbefo = AppendValue(answer, 'L', num)
        elif num == 3 or num == 6 or num == 9:
            answer, rbefo = AppendValue(answer, 'R', num)
        else:
            ldis = GetDist(dicKeyPadCoord[num], dicKeyPadCoord[lbefo])
            rdis = GetDist(dicKeyPadCoord[num], dicKeyPadCoord[rbefo])
            if ldis < rdis or (ldis == rdis and hand == 'left'):
                answer, lbefo = AppendValue(answer, 'L', num)
            else:
                answer, rbefo = AppendValue(answer, 'R', num)
    return answer

def AppendValue(answer, ch, num):
    answer +=ch
    
    return answer, num

def GetDist(lsta, lstb):
    dis0 = abs(lsta[0] - lstb[0])
    dis1 = abs(lsta[1] - lstb[1])
    
    return dis0+dis1


print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"))