#range function 
# for i in range(1,101,2):
#   print(i)

# find greatest number in a array  
#! method 1 
def findGreatestNumber(array):
    biggestNumber=array[0]              #=>O(1)
    for i in range(1,len(array),1):     #=>O(n)
      if(array[i]>biggestNumber):       #=>O(1)
        biggestNumber=array[i]          #=>O(1)

    print(biggestNumber)                #=>O(1)

findGreatestNumber([23,45,89,65,23,48,56,36,99])

#! method 2 (using recursion)
def greatestNumber(array,n):
  if (n<=0):
    return array[0]

  return (max(array[n-1],greatestNumber(array,n-1)))

print(greatestNumber([23,45,89,65,23,48,56,36,99],9))