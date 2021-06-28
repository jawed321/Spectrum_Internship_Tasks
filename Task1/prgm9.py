n = int(input("Enter number of elements : \n"))
lst=[]
print("enter",n ,"elements")
for i in range(0, n):
    element = int(input())
    lst.append(element)
idx=int(input("enter the value of n to get nth smallest no.\n"))
lst.sort()
print("your nth smallest no. is: ",lst[idx-1])