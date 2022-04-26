from itertools import combinations
from collections import defaultdict

def solution(orders, course):
    answer = []
    dic = {}
    
    for cnt in course:
        dic[cnt] = defaultdict(int)      
    
    for str in orders:
        for cnt in course:
            if len(str) < cnt:
                break
            for com in list(combinations(str,cnt)):
                strcom = ''.join(sorted(list(com)))
                dic[cnt][strcom] +=1
                
    for cnt in course:
        if len(dic[cnt]) < 1:
            continue
        
        maxvalue =  max(dic[cnt].values())
        if maxvalue <= 1:
            continue
        
        for key in dic[cnt].keys():
            if dic[cnt][key] == maxvalue:
                answer.append(key)
    answer.sort()
    return answer


print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4]))