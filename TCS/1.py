# 0 0 2 1 4 2 6 3 8 4 10 5 .......
""" n=int(input("Enter which number you want in the series : "))
a=0
b=0
for i in range(1,n+1):
    if i % 2 !=0:
        if i > 1:
            a=a+2
    else:
        b=a//2
    
if i % 2==0:
    print(b)
else:
    print(a) """


# Queue and mints question 
""" firsMintValue=int(input("First mint value "))
n=int(input("queue length "))
prevSum=0
totalSum=firsMintValue
for i in range(1,n):
    prevSum=totalSum - 1
    totalSum+=prevSum
print(totalSum) """


#Check whether a number is strong or not
#A number is strong if sum of factorial of its digit is equal to the number
""" num=input()
sum=0

def fact(n):
  if n==1 or n==0:
    return 1
  return n * fact(n-1)

for i in num:
  sum+=fact(int(i))
if sum == int(num):
  print(True)
else:
  print(False) """



#calcuate total cost of painting a property
""" niwalls=int(input())
newalls=int(input())
totalInteriorArea=0
totalExteriorArea=0

if niwalls < 0 or newalls < 0:
  print('Invalid input ')
else:
  for i in range(0,niwalls):
    area=float(input())
    totalInteriorArea+=area

  for j in range(0,newalls):
    area=float(input())
    totalExteriorArea+=area

  print("Total Cost :"+ str(float(totalInteriorArea * 18 + totalExteriorArea * 12) ) + " INR") """