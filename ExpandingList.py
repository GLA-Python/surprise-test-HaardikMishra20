def expanding(n):
    c=[]
    x=0
    for i in range(0,len(n)-1):
        a=abs(n[i]-n[i+1])
        c.append(a)
    f=c[0]
    for j in range(1,len(c)):
        if c[j]<=f:
            x+=1
        f=c[j]
    if x>0:
        return False
    else:
        return True
    
n1=list(map(int,input().split()))
ans=expanding(n1)
print(ans)
