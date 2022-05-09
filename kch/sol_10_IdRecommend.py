def solution(new_id):
    answer = []

    new_id = new_id.lower() # 소문자 변환

    for i in new_id:
        if (i.isalnum() or i in ['-', '_', '.']): # 숫자와 알파벳인지 확인
            if (answer):
                if (i == '.' and answer[-1] == '.'):
                    continue
            answer.append(i)
    
    if (answer):
        if (answer[0] == '.'): # 첫번째
            answer.pop(0)

    if (answer):
        if (answer[-1] == '.'): # 마지막
            answer.pop() # 숫자 지정 안하면 마지막 값 pop

    if (len(answer) == 0):
        answer = 'a'

    if (len(answer) >= 16):
        answer = answer[:15]
        if (answer[-1] == '.'):
            answer.pop(-1)

    if (len(answer) <= 2):
        while len(answer) < 3:
            answer += answer[-1]

    return ''.join(answer)

print(solution("...!@BaT#*..y.abcdefghijklm"))
print(solution("=.="))
print(solution("abcdefghijklmn.p"))