def merge_sort_arr(arr1, arr2):
  sorted_arr = []
  i = 0
  j = 0

  while(i < len(arr1) or j < len(arr2)):
    if j == len(arr2) or (i< len(arr1) and arr1[i] < arr2[j]):
      sorted_arr.append(arr1[i])
      i += 1
    else:
      sorted_arr.append(arr2[j])
      j += 1

  return sorted_arr


arr1 = [0, 3, 4, 31]
arr2 = [5, 6, 30]
print(merge_sort_arr(arr1, arr2))