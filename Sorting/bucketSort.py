#Bucket sort
#Bucket sort is used when the inputs are uniformly distributed


import math


def insertionSort(arr):
    for i in range(1,len(arr)):
      key=arr[i]
      j=i-1
      while(j>=0 and key < arr[j]):
        if arr[j] > key:
          arr[j+1]=arr[j]
          j-=1
      arr[j+1]=key
    return arr



def bucketSort(arr):
  no_of_buckets=round(math.sqrt(len(arr)))
  max_value=max(arr)
  b=[]

  for i in range(no_of_buckets):
    b.append([])

  for i in arr:
    b_index=math.ceil(i * no_of_buckets / max_value)
    b[b_index - 1].append(i)
  
  for i in range(no_of_buckets):
    b[i]=insertionSort(b[i])

  k=0
  for i in range(no_of_buckets):
    for j in range(len(b[i])):
        arr[k]=b[i][j]
        k+=1

  print(arr)
  

bucketSort([7,5,9,2,4,6,11,13])

#time comp => O(N*N)
#space comp => O(N)