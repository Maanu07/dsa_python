#Selection Sort

def selectionSort(arr):
  for i in range(len(arr)):
    min_index=i
    for j in range(i+1,len(arr)):
      if arr[min_index] > arr[j]:
        min_index=j
    arr[i],arr[min_index]=arr[min_index],arr[i]

  print(arr)

#! descending order
def selectionSort(arr):
  for i in range(len(arr)):
    max_index=i
    for j in range(i+1,len(arr)):
      if arr[max_index] < arr[j]:
        max_index=j
    arr[i],arr[max_index]=arr[max_index],arr[i]

  print(arr)

myList=[10,7,9,1,45,21,14]
selectionSort(myList)


#Time comp =>O(N*N)
#Space comp => O(1)