

def solution(numbers, hand):
    
    answer = ''
    
    lbefo = -1
    rbefo = -1

    dic = {2:{1:1, 2:0, 3:1, 4:2, 5:1, 6:2, 7:3, 8:2, 9:3, 0:3, -1:4},
           5:{1:2, 2:1, 3:2, 4:1, 5:0, 6:1, 7:2, 8:1, 9:2, 0:2, -1:3},
           8:{1:3, 2:2, 3:3, 4:2, 5:1, 6:2, 7:1, 8:0, 9:1, 0:1, -1:2},
           0:{1:4, 2:3, 3:4, 4:3, 5:2, 6:3, 7:2, 8:1, 9:2, 0:0, -1:1}
           }    
    
    for num in numbers:
        if num == 1 or num == 4 or num == 7:
            answer += 'L'
            lbefo = num
        elif num == 3 or num == 6 or num == 9:
            answer += 'R'
            rbefo = num
        else:
            ldis = dic[num][lbefo]
            rdis = dic[num][rbefo]
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



print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"))