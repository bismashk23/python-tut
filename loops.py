#WHILE LOOP

#qs1
# num=1

# while num<=100:
#     print(num)
#     num += 1

#qs2
# num=100

# while num>=1:
#     print(num)
#     num -= 1

#qs3
# n * till i = i*n
# num = int(input("enter a number:"))
# i=1

# while i <= 10:
#     print(num,"*", i,"=", num*i)
#     i+=1

#qs4 print a list using loops
# nums=[1,33,3,16,87,41,81,23]  #nums[idx] will give the value of the list at index idx
# heroes=["ironman","superman","spiderman","batman","hulk"]

# idx=0
# while idx < len(heroes): #traversal
#     print(heroes[idx])
#     idx+=1

#qs5
# tup=(1,4,9,16,25,36,49,64,81,100)

# n=int(input("enter a number to check if it is present in the tuple:"))
# i=0
# while i<len(tup):
#     if n==tup[i]: #tup[i] means if number at index i is matching.
#         print(n," found at index ",i)
#     i+=1

#break and continue
# i=1
# while i<=5:
#     print(i)
#     if i==3:
#         break   
#     i+=1

# print("end of loop")

# i=1
# while i<=10:
#     if (i%2==0):
#         i+=1
#         continue #even numbers do not get printed because of continue statement. It skips the current iteration and goes to next iteration.
#     print(i)
#     i+=1


#FOR LOOP : for sequential traversal of a list, tuple, string, dictionary, set etc.
# for element in listName:

# veggies=["tomato","onion","potato","carrot","cabbage"]

# for val in veggies:
#     if(val=="carrot"):
#         break
#     print(val)

# print("end of loop")

#qs2
# nums=[1,33,3,16,87,41,81,23]
# x=81
# idx=0
# for val in nums:
#     if(val==x):
#         print("number found at idx",idx)
#         break
#     idx +=1


#range() function returns a sequence of numbers,starting from 0: range(start?,stop,step?) [in stop, ending number is excluded];  ? means mentioning it is optional, hence stop is mandatory

# seq=range(1,101) #qs1 1-100
# seq=range(100,0,-1) #qs2, negative step size, 100-1
# for i in seq:
#     print(i)

# n=int(input("enter a number:")) #qs3 multplication table

# for i in range(1,11):
#     print(i*n)

# pass is used as placeholder for future code. null statement in loop that does nothing.

#loops questions
# 1. wap to find sum of first n natural numbers (using while)

# num=int(input("enter a number:"))
# i=1
# sum=0
# while (i<=num):
#     sum=sum+i
#     i+=1

# print(sum)
# #for loop 
# sum1=0
# for i in range(1,num+1):
#     sum1+=i

# print(sum1)

# 2. find factorial of n numbers using for loop
n=6 #1*2*....*n
fact=1
for i in range(1,n+1):
    fact*=i

print(fact)