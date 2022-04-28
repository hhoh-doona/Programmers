def solution(numbers, hand):
    answer = ''
    dic = {1 : [0, 0], 2 : [0, 1], 3 : [0, 2], 
           4 : [1, 0], 5 : [1, 1], 6 : [1, 2], 
           7 : [2, 0], 8 : [2, 1], 9 : [2, 2], 
           '*' : [3, 0], 0 : [3, 1], '#' : [3, 2]}
    
    left_n = dic['*']
    right_n = dic['#']

    for i in numbers:
        now = dic[i]
        if (i == 1 or i == 4 or i == 7) :
            answer += 'L'
            left_n = now 
        elif (i == 3 or i == 6 or i == 9) :
            answer += 'R'
            right_n = now
        else :
            left_d = 0
            right_d = 0

            for a, b, c in zip(left_n, right_n, now):
                left_d += abs(a - c) # 절대값 = abs
                right_d += abs(b - c)
            
            if (left_d < right_d):
                answer += 'L'
                left_n = now
            elif (right_d < left_d):
                answer += 'R'
                right_n += now
            else :
                if (hand == 'left'):
                    answer += 'L'
                    left_n = now    
                else :
                    answer += 'R'
                    right_n = now
    
    return answer


print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], 'right'))
print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], 'left'))
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], 'right'))

# LRLLRRLLLRR
# LRLLLRLLLRR