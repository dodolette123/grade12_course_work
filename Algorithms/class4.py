
# define bubble_sort():
def bubble_sort(arr):
  for el in arr:

    for i in range(len(arr)-1):
      
      if arr[i] > arr[i+1]:
        swap(arr,i,i+1) 

##### test statements

print("Pre-Sort: {0}".format(nums))      
bubble_sort(nums)
print("Post-Sort: {0}".format(nums))


#MERGE SORT