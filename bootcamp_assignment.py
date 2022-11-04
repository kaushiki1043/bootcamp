#Assignment 1
# #Write a program to find those numbers which are divisible by 15 and multiple of 5, between 10 and 150
print("-----------------------------------------------------------------------------------------------------------------")
print("Assignment 1")
print("Numbers which are divisible by 15 and are amultiple of 5 are as follows: ")
for num in range(10,150,1):
    if(num%15==0 and num%5==0):
        print(num,end=" ")

#Assignment 2
#Write a python program to print 100 prime numbers and you should print "Hey Bro done!"
print()
print("------------------------------------------------------------------------------------------------------------------")
print("Assignment 2")
print("First 100 prime numbers are: ")
for n in range(2,100):
    count=0
    for j in range(1,n+1):
        if(n%j==0):
            count=count+1
    if(count==2):
        print(n,end=" ")
print()
print("Hey bro, done!")
print("------------------------------------------------------------------------------------------------------------------")

