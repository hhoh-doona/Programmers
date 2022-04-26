def solution(N, stages):
    dic = {}
    
    for i in range(1,N+1):
        total = 0
        fail_cnt = 0
        for j in stages:
            if j<i:continue #오르지도 못한사람은 제외
            
            total +=1 #도전자횟수
            if j==i: fail_cnt +=1 #실패횟수
            
        if total == 0:
            dic[i] = 0
        else:
            dic[i] = fail_cnt/total #실패율 dic에
            
    sorted_dic = sorted(dic.items(), reverse=True, key=lambda item:item[1]) #Value 기준으로 정렬
    
    return [i[0] for i in sorted_dic] #Key값만 리스트로 만들어 리턴

print(solution(4,[2, 1, 2, 6, 2, 4, 3, 3]))