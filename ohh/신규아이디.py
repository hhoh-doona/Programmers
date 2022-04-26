
import re

def solution(new_id):
    new_id = new_id.lower()
    new_id = re.sub('[^0-9a-z-_.]','',new_id) #정규표현식
    
    while(new_id.find('..') != -1):
        new_id = new_id.replace('..','.') #보기 좋을듯 반복문
    
    new_id = new_id.strip('.')
        
    if len(new_id) == 0:
        new_id = 'a'
    
    if len(new_id) >= 16:
        new_id = new_id[0:15]
    
    new_id = new_id.strip('.') #strip 한번더
    
    while(len(new_id) <= 2):
        new_id += new_id[-1]
    
    return new_id

print(solution("...!@BaT#*..y.abcdefghijklm"))
print(solution("z-+.^."))
print(solution("=.="))
print(solution("123_.def"))
print(solution("abcdefghijklmn.p"))