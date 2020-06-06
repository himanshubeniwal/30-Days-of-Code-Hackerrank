# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
n = int(input())

for i in range(n):
    val = 'Prime'
    number = int(input())
    if number==1:
        val = 'Not prime'
    else:
        sq = int(math.sqrt(number))
        for num in range(2,sq+1):
            if number%num==0:
                val = 'Not prime'
                break
    print(val)
        
        
