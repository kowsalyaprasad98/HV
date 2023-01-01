start=int(input())
end=int(input())
t=0
p=0
for i in range(start,end+1):
    if i%2==0:
        t+=i
    else:
        p+=1
print(t)

