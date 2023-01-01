import math
import os
import random
import re
import sys

#
# Complete the 'handshake' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def handshake(n):
    c=0
    for i in range(n+1):
        if i>1:
            c+=(i-1)
        else:
            c+=0
    print(c)
    
    # Write your code here

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = handshake(n)

        #fptr.write(str(result) + '\n')

    #fptr.close()
 