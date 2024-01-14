class Sort():
  def __init__(self, arr):
    self.array = arr

  def quick_sort(self, arr):
    if len(arr) <= 1:
      return arr
    else:
      pivote = arr[len(arr)-1]
      left_arr = []
      right_arr = []
      for i in range(len(arr)-1):
        if arr[i] <= pivote:
          left_arr.append(arr[i])
        elif arr[i] > pivote:
          right_arr.append(arr[i])
    return self.quick_sort(left_arr) + [pivote] + self.quick_sort(right_arr)


input = [1,4,6,5,9,2,10,3,8,7]
sort = Sort(input)
print(input)
print(sort.quick_sort(input))