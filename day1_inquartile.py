n=int(input())
arr=[int(i) for i in input().split(" ") ]
f=[int(i) for i in input().split(" ") ]

final=[]
lb=[]
hb=[]
for i in range(n):
    for j in range(f[i]):
        final.append(arr[i])

x=0

final.sort()

def median(k , lsd):
        global x,lb,hb
        if lsd%2==0:
                if k==final:
                        lb=k[:int((lsd/2))]
                        hb=k[int((lsd/2)):]
                return (k[int((lsd/2)-1)]+k[int(lsd/2)])/2
        else:
                if k==final:
                        lb=k[:int(lsd//2)]
                        hb=k[int((lsd//2)+1):]
                return k[lsd//2]
median(final , len(final))

a1=median(lb , int(len(lb)))
a2=median(hb , int(len(hb)))
print(float(a2-a1))
