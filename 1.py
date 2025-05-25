# Problem 1: 
# Given an array of strings, group anagrams together.



def grp_ana(listt):
    list1=[0]*len(listt)
    anss={}
    for i in range(len(listt)):
        list1[i]="".join(sorted(listt[i]))

    for i in range(len(list1)):
        if list1[i] in anss:
            anss[list1[i]].append(listt[i])
        else:
            anss[list1[i]]=[listt[i]]
    return list(anss.values())



strs = ['bat','tab','act','cat']
print(grp_ana(strs))
    
