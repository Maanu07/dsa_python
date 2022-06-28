#Bubble Sort
#Nested loop is used 
#For each loop the greatest element moves to the rightmost place

def bubbleSort(arr):
  for i in range(len(arr) -1):
    for j in range(len(arr) - 1 - i):
      if arr[j] > arr[j+1]:
        arr[j],arr[j+1]=arr[j+1],arr[j]
  print(arr)

myList=[11,9,7,5,3,2,1]
bubbleSort(myList)


#Time comp => O(N*N)
#SPace comp => O(1)