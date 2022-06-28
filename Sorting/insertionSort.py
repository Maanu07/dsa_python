#Insertion sort
#Our array is divided into two parts one is sorted array and other is unsorted array 

def insertionSort(arr):
  for i in range(1,len(arr)):
    key=arr[i]
    j=i-1
    while(j>=0 and key < arr[j]):
        arr[j+1]=arr[j]
        j-=1
    arr[j+1]=key

  print(arr)

myList=[21,7,15,3,8,9,42,33]
insertionSort(myList)


#Time comp =>O(N*N)
#Space comp => O(1)