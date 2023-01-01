"""Question 1 - 
Take five inputs from the user. Make sure those inputs are positive numbers (write the code for the same) and then add those numbers. Once the total is displayed in the console.
Optional - Try to save that number in the file as well (Using the file handling concept.)"""

a=int(input())
b=int(input())
c=int(input())
d=int(input())
e=int(input())
file=open("totalofproducts.txt","w")
if a<0 or b<0 or c<0 or d<0 or e<0:
    print("Negative number")
    file.write("enter positive")
else:
    t=a+b+c+d+e
    file.write("total: %d"%t)
    print(t)
file.close()
