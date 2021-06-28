# Python Program to find the greatest common divisor(GCD) of a the given set of numbers.


# Function

def getgcd(x, y):
    while (y):
        x, y = y, x % y

    return x

lst = []

n = int(input("Enter number of elements in the array : "))


for i in range(0, n):
    element = int(input())

    lst.append(element)

num1 = lst[0]
num2 = lst[1]
gcd = getgcd(num1, num2)

for i in range(2, len(lst)):
    gcd = getgcd(gcd, lst[i])

print("The Greatest Common Divisor of",lst,"is : ", gcd)