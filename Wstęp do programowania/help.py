def solution(s):
    if len(s) == 0: return []
    ret = []
    
    str = ''
    for char in s:
        if len(str) < 2:
            str += char
        else:
            ret.append(str)
            str = char
        
    ret.append(str)

            
    if len(ret[-1]) == 1:
        ret[-1] += '_' 
            
    return ret
            

print(solution("asdfadsf"))
print(solution("asdfads"))
print(solution("x"))