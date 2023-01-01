
#"""n=int(input("no of cars:"))
#m=int(input("no of bikes:"))
#print(n*40+m*20)"""

#"""By using map representation

#n,m=map(int,input().split())
#print(n*40+m*20)"""

#"""Cheking whether input is positive or negative and print total amount

#a=int(input("Quantity of first product:"))
#b=int(input("Quantity Of Second Product:"))
#c=int(input("Price Of First Product:"))
#d=int(input("Price of Second Product:"))
#if(a<=0 or b<=0 or c<=0 or d<=0):
#    print("Zero or Negative Value")
#else:
#    print(a*c+b*d)#total amount"""

#Another Representation by list

l=list(input().split())
a=int(input())#price of a car
b=int(input())#price of abike
c=0 #car count
d=0 #bike count
for i in l:
    if i=="bike":
        d+=1
    else:
        c+=1
#printing total amount
print(c*a+d*b)





