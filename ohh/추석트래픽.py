from datetime import datetime, timedelta

def GetDateTime(tempArr):
    tx = tempArr[0]+' '+tempArr[1]
    endDT = datetime.strptime(tx, "%Y-%m-%d %H:%M:%S.%f")    
    
    return endDT
    
def solution(lines):
    answer = 0
    startlist = []
    
    for i in range(len(lines)-1, -1,-1):
        tempArr = lines[i].split(' ')
        endDT = GetDateTime(tempArr)
              
        startDT = endDT - timedelta(seconds=float(tempArr[2][:-1])-0.001)      
        
        startlist.append(startDT)
        answer = max(answer, len(startlist))
        
        if i == 0: break
        
        befoendDT = GetDateTime(lines[i-1].split(' '))
        startlist = [j for j in startlist if j - timedelta(seconds=1) < befoendDT]
            
    return answer

print(solution([
"2016-09-15 01:00:04.002 2.0s",
"2016-09-15 01:00:07.000 2s"
]))