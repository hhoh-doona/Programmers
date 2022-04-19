#문자열 압축
def solution(s):
    answer = len(s)
    
    for i in range(1,int(len(s)/2)+1):
        zipStrResult = zipStr(s,i)
        answer = min([answer, len(zipStrResult)])
        
    return answer

def zipStr(s, i):
    zipStrResult = ""
    
    befo = s[0:i]
    zipCnt = 1
    for j in range(i,len(s), i):
        curr = s[j:j+i]
        
        if befo == curr:
            zipCnt +=1
        else:
            if zipCnt == 1:
                zipStrResult += befo
            else:
                zipStrResult = zipStrResult + str(zipCnt) + befo
            befo = curr
            zipCnt = 1
    
    if zipCnt == 1:
        zipStrResult += befo
    else:
        zipStrResult = zipStrResult + str(zipCnt) + befo
        
    
    return zipStrResult


'''
def compress(text, tok_len):
    words = [text[i:i+tok_len] for i in range(0, len(text), tok_len)]
    res = []
    cur_word = words[0]
    cur_cnt = 1
    for a, b in zip(words, words[1:] + ['']):
        if a == b:
            cur_cnt += 1
        else:
            res.append([cur_word, cur_cnt])
            cur_word = b
            cur_cnt = 1
    return sum(len(word) + (len(str(cnt)) if cnt > 1 else 0) for word, cnt in res)

def solution(text):
    return min(compress(text, tok_len) for tok_len in list(range(1, int(len(text)/2) + 1)) + [len(text)])
'''
print(solution("xababcdcdababcdcd"))