t = int(input())

for i in range(t):
    n = input()
    tmp=1
    for j in range(1,len(n)):
        if n[j-1] != n[j]:
            print(tmp,end ='')
            print(n[j-1],end ='')
            tmp=1
        else:
            tmp+=1
    print(tmp,end ='')
    print(n[len(n)-1])