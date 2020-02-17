arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,14, 15, 16, 17, 18, 19]

# STRETCH: implement Linear Search				
def linear_search(arr, target):
  
  # TO-DO: add missing code
  # loop over array
  for i in range(0, len(arr)):
    # if element at index i == target, return index
    if arr[i] == target:
      return i
  # if at the end of the loop the element still hasn't been found - return -1    
  return -1   # not found


# STRETCH: write an iterative implementation of Binary Search 
def binary_search(arr, target):

  if len(arr) == 0:
    return -1 # array empty
    
  low = 0
  high = len(arr)-1

  # TO-DO: add missing code
  # high must be more than low, otherwise must have searched entire array and not found the target 
  while high >= low:
    # get middle element index, make sure it's not a float
    middle = (low + high) // 2
    # if element at middle index is equal to target -> return index
    if arr[middle] == target:
      return middle
    # if element at middle index is MORE than target, target MUST be on LHS of array -> eliminate RHS of array 
    elif arr[middle] > target:
      # set value of high equal to value of middle index - 1 so that 
      # when the loop runs again (so long as high >= low),
      # RHS of array is eliminated; 
      # considers middle of array to be element in between the index of low and the index of current middle of array - 1
      high = middle - 1
    # if element at middle index is LESS than target, target MUST be on RHS of array -> eliminate LHS of array
    elif arr[middle] < target:
      # set value of low equal to value of middle index + 1 so that 
      # when the loop runs again (so long as high >= low),
      # LHS of array is eliminated; 
      # considers middle of array to be element in between the index of middle element + 1 and the last element of array
      low = middle + 1
  return -1 # not found


# STRETCH: write a recursive implementation of Binary Search 
def binary_search_recursive(arr, target, low, high):
  
  middle = (low+high)//2

  if len(arr) == 0:
    return -1 # array empty
  # TO-DO: add missing if/else statements, recursive calls
  
  # if element at middle index is equal to target -> return index
  if arr[middle] == target:
    return middle
    
  # if element at middle index is MORE than target, target MUST be on LHS of array -> eliminate RHS of array 
  elif arr[middle] > target:
    # -> recur passing in middle - 1 as value of high to eliminate RHS of array
    return binary_search_recursive(arr, target, low, middle - 1)  
    
  # if element at middle index is LESS than target, target MUST be on RHS of array -> eliminate LHS of array
  elif arr[middle] < target:
    # -> recur passing in middle + 1 as value of low to eliminate LHS of array
    return binary_search_recursive(arr, target, middle + 1, high) 

  return - 1