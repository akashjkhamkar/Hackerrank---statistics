# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
n=int(input())
x=[float(i) for i in input().split(" ")]
w=[float(i) for i in input().split(" ")]
s=0.0
for i in range(n):
    s+=x[i]*w[i]
print(round(s/float(sum(w)) , 1))
