def looknsay(num):
    lst=[]
    i = 0
    while i < len(num):
        count = 1
        while i+1 < len(num) and num[i]==num[i+1]:
            i += 1 
            count += 1 
        lst.append(str(count)+num[i])
        i += 1 
    return ''.join(lst)

n=int(input())
x=1
for i in range(n):
    print(x)
    x=looknsay(str(x))
