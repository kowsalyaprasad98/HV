strs=list(input().split())
d={}
for i in strs:
    t=tuple(sorted(i))
    print("get:",d.get(t,[]))
    d[t]= d.get(t,[])+[i] 
    print("value:",d[t])
print("dici:",d)
print(list(d.values()))

"""cubic equation roots
l1=['c']
print(l1+['tac'])"""