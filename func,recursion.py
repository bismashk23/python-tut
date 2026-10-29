'''def calcSum(a,b): #parameters
    return a+b

sum=calcSum(3,5) #function call; arguments passed
print(sum)

for i in range(1,6): #loops practice 
    print("sum=",sum)'''

#-----------------------------------------------------------------------------------

#cal average
'''def Avg(a,b,c):
    return (a+b+c)/3

m,n,o=map(int,input('enter 3 numbers with space:').split())
print(Avg(m,n,o))'''

#-----------------------------------------------------------------------------------

#default parameters
#default values should be passed at the end and not mentioned at the start

'''def multi(b,a=4):
    return a*b

print(multi(7))''' #7 is value of b, as we're taking default value of a

#-----------------------------------------------------------------------------------

#function questions
# qs 1. cal length of lisy; list is the parameter

cities=['mumbai','delhi','banglore','chennai', 'ghuwati','pune']
food=['pav bhaji','noodles','chicken fried rice','biryani','chole bhature']

def length(list):
    print(len(list))

# length(cities)
# length(food)

#qs 2. to print list elements in a single line
'''def one(list):
    for i in list:
        print(i,end=" ")

one(food)'''

#-----------------------------------------------------------------------------------

#qs 3. print factorial of number n; parameter is n

''' def fact(n):
    sum=1    # Initialize variables inside the function scope
    for i in range(1,n+1):
        sum*=i
    return sum

m=int(input('enter a number:'))
print(fact(m)) '''

#-----------------------------------------------------------------------------------

#qs 4. convert usd to inr
''' def convert(u):   # 1 usd=95.21 inr
    result=u*95.21
    print(u,"USD is=", result,'INR')

usd=int(input('enter usd value to convert to inr:'))
convert(usd) '''

#-----------------------------------------------------------------------------------