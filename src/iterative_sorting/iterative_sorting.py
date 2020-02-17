# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 

        # loop over all elements to the right hand side 
        for j in range(i + 1, len(arr)):
            # if element is less than value of element at current smallest index, 
            # set the smallest index to index of that element
            # keep doing this til end of array
            if arr[j] < arr[smallest_index]:
                smallest_index = j

        # TO-DO: swap
        # swap element at current index to element at smallest index,
        # keep doing this til end of array
        arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]
   
    # return the sorted array
    return arr

# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    # loop over entire array from 0 to length of array minus 1
    for i in range(0, len(arr) - 1):
        # the last item in the list is already going to be sorted (largest number 'bubbles' to end of list after every pass)
        # -> there's no need to check last item 
        # -> j = length of array minus 1 minus i
        for j in range (0, len(arr) - 1 - i): 
            # compare the item with the item to the RHS
            # if item > item to RHS, swap
            # else break and continue looping through array til all items sorted (ie. i == len(arr) - 1)
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr