# Problem 6: 
# Given two strings ss and tt, determine if tt is an anagram of a substring of ss. In other 
# words, check if there exists a substring in ss that is an anagram of tt.


from collections import Counter

def funn(s,t):
    n,m = len(s),len(t)
    if m>n:
        return False
    t_count = Counter(t)
    wcnt = Counter(s[:m])



    if wcnt==t_count:
        return True

    for i in range(m, n):
        wcnt[s[i]] +=1
        wcnt[s[i-m]]-=1
        if wcnt[s[i-m]]==0:
            del wcnt[s[i-m]]
        if wcnt==t_count:
            return True
    return False


s="cbaebabacd"
t="abc"
print(funn(s,t)) 