<<<<<<< HEAD
import pandas as pd
n=list(map(int,input().split()))
s=pd.Series(n)
print("Series:\n",s)
"""print(s*s)"""
for i in s:
    print(i*i,end=" ")


=======
import pandas as pd
n=list(map(int,input().split()))
s=pd.Series(n)
print("Series:\n",s)
print(s*s)
for i in s:
    print(i*i,end=" ")


>>>>>>> 29702f06d99eaa23a7ecf5c8af44c01e8192d0fb
