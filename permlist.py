def isPalindrome(s):
    print(s)
    ini = 0
    end = len(s)-1
    while(ini < end):
        if(s[ini] != s[end]):
            return False
        else:
            ini+=1
            end-=1
    return True

def generate(pos, b, subs , curr):
    print(subs)
    if(len(subs)==len(b)):
        curr.append(subs)
        return
    for i in range(pos, len(b)):
        generate(pos+1, b, subs + b[i], curr)
a='abcd'
c = []
generate(0, a, '' , c)
#print(c)



'''
subsets
def isPalindrome(s):
    print(s)
    ini = 0
    end = len(s)-1
    while(ini < end):
        if(s[ini] != s[end]):
            return False
        else:
            ini+=1
            end-=1
    return True

def generate(pos, b, subs , curr):
    print(subs)
    if(len(subs)==len(b)):
        curr.append(subs)
        return
    for i in range(pos, len(b)):
        generate(i+1, b, subs + b[i], curr)


a='abcd'
c = []
generate(0, a, '' , c)
#print(c)
'''