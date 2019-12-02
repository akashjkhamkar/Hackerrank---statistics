n=int(input())
nums=input()
nums=[int(i) for i in nums.split(" ")]
x=0
l=0
u=0
nums.sort()
lb=[]
hb=[]
def median(k , lsd):
        global x,u,lb,hb
        if lsd%2==0:
                x=(k[int((lsd/2)-1)]+k[int(lsd/2)])/2
                if k==nums:
                        lb=k[:int((lsd/2))]
                        hb=k[int((lsd/2)):]
        else:
                x=k[lsd//2]
                if k==nums:
                        lb=k[:int(lsd//2)]
                        hb=k[int((lsd//2)+1):]
median(nums , int(n))
median(lb , int(len(lb)))
print(int(x))
median(nums , n)
print(int(x))
median(hb , int(len(hb)))
print(int(x))
