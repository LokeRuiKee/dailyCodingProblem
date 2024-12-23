#Problem 1
#This problem was recently asked by Google.
#Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
#For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
#Bonus: Can you do this in one pass?

numList = []

getNumList = input("Please enter a list of numbers.\n")
print(getNumList)
numList = list(map(int, getNumList.split()))
getK = input("Please enter a number as k\n")
k = int(getK)

i=0
for i in range (len(numList)-1):
    if numList[i] + numList[i+1] == k:
        print("True")
        break
    else:
        print("False")