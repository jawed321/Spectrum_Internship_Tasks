# Python Program to enter an integer ‘n’ find all prime numbers from 1 to n.

#to check if prime no.
def checkPrime(n):
    if n <= 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True

#print prime no.
def printPrime(n):
    print("Prime numbers between 1 and ", n, " are:- ")
    for i in range(2, n + 1):

        if checkPrime(i):
            print(i, end=" ")



num = int(input("Enter The Number upto which You Want To Print The Prime Numbers: \n"))
printPrime(num)