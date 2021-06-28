# Python find the number of trailing zeros in the factorial of the number
num = int(input(" Enter The Number Of factorial to find :\n"))
num1=num
count=0
if (num < 0):
    print("enter a positive number")
else:
    while(num>=5):
        num//=5;
        count+=num

print("Number Of trailing 0's in the Factorial of ", num1, " is : ", count)