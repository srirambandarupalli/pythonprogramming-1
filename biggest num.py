N=int(raw_input())
a=input().split()
a.sort()
S=0
s=len(a)
while(s>0):
    b=int(a[s-1])
    S=S*10+b
    s=s-1
print(S)
