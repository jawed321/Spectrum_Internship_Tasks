n=int(input("enter number\n"))
count=0
a=6
while(count<=n):
    while(a!=0 and count<=n):
        s=0
        for i in range(1,a):
            if(a%i==0):
                s=s+i
        if(a==s):
            count=count+1
            if(count<=n):
                print(a)
        a+=1

