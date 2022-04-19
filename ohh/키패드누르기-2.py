

def solution(numbers, hand):    

    answer = ''
    lbefo = '*'
    rbefo = '#'

    dic ={}
    k=1
    for i in range(0,3):
        for j in range(0,3):
            dic[k] = [i,j]
            k +=1
    dic['*'] = [3,0]
    dic[0] = [3,1]
    dic['#'] = [3,2]

    for num in numbers:
        if num == 1 or num == 4 or num == 7:
            answer += 'L'
            lbefo = num
        elif num == 3 or num == 6 or num == 9:
            answer += 'R'
            rbefo = num
        else:
            ldis = GetDist(dic[num], dic[lbefo])
            rdis = GetDist(dic[num], dic[rbefo])
            if ldis < rdis:
                answer +='L'
                lbefo = num
            elif rdis < ldis:
                answer +='R'
                rbefo = num
            else:
                if hand == 'left':
                    answer +='L'
                    lbefo = num
                else:
                    answer +='R'
                    rbefo = num
                    
    return answer

def GetDist(lsta, lstb):
    dis0 = abs(lsta[0] - lstb[0])
    dis1 = abs(lsta[1] - lstb[1])
    
    return dis0+dis1


print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"))