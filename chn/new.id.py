def solution(new_id):
    import re
    answer = ''
    new_id = new_id.lower()
    new_id = re.sub(r"[^a-z0-9-_.]","",new_id) 


    while new_id.replace("..",".") != new_id:
        new_id = new_id.replace("..",".") 

    while len(new_id) > 0 and new_id[0] == ".":
        new_id = new_id[1:]
    while len(new_id) > 0 and new_id[-1] == ".":  
        new_id = new_id[:-1]
    
    
    if new_id == "":
        new_id += "a"
   
    if len(new_id) >= 16:
        new_id = new_id[:15]
        while new_id[-1] == ".": 
            new_id = new_id[:-1]
    
    while len(new_id) < 3:
        new_id += new_id[-1]          
    return new_id



