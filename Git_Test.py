


import math


def solution(s):
    answer = s[math.ceil(len(s)/2)-1 : math.floor(len(s)/2)+1]
    return answer

print(solution('abde'))