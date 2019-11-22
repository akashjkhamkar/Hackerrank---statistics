import statistics as st
n=int(input())
nums=[int(i) for i in input().split(" ")]
mean=st.mean(nums)

sums=0
for i in nums:
        sums+=(i-mean)**2
print((sums/n)**(0.5))
