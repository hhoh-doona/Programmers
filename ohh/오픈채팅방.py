from collections import defaultdict

def solution(record):
    
    answer = []
    
    dicidname = {}
    dicidchange = defaultdict(list)
    
    for msg in record:
        spltmsg = msg.split(' ')
        if spltmsg[0] == 'Enter':
            dicidname[spltmsg[1]] = spltmsg[2]            
            dicidchange[spltmsg[1]].append(len(answer))
            answer.append("{}님이 들어왔습니다.".format(spltmsg[1]))
            
        elif spltmsg[0] == 'Leave':
            dicidchange[spltmsg[1]].append(len(answer))
            answer.append("{}님이 나갔습니다.".format(spltmsg[1]))
            
        elif spltmsg[0] == 'Change':
            dicidname[spltmsg[1]] = spltmsg[2]

    for key, value in dicidname.items():
        for i in dicidchange[key]:
            answer[i] = answer[i].replace(key,value)
    
    return answer

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))