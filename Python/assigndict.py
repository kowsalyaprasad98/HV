"""Create a dictionary in Python, with the name “Car”, which has keys and values. Fetch the “brand name”
as the key and “color” as the value from the user. Display the complete dictionary in the console and 
try to save the output in the file also (Using the file handling concept)"""

a=int(input())# number of the features
Car={}
for i in range(a):
    b,c=input().split()# b=key and c=value
    Car[b]=c
print(Car)
with open("brandandcolor.txt","w") as f:
    f.write("Car Brands and Colors\n")
    for i,j in Car.items():
        f.write("%s:%s\n"%(i,j))
f.close()
