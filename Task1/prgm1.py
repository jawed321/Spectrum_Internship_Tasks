def swapcase(str):
    l = len(str)

    for i in range(l):

        # Checking lowercase character and coverting

        if str[i] >= 'a' and str[i] <= 'z':

            str[i] = chr(ord(str[i]) - 32)

        # Checking Uppercase character and converting

        elif str[i] >= 'A' and str[i] <= 'Z':

            str[i] = chr(ord(str[i]) + 32)



str = input("Enter The String : \n")
str = list(str)

swapcase(str)
str = ''.join(str)
print("String After Swapping : " + str)
