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
    # originally had this set to just be count = [0] * 10 -> count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    # was just going to get count of occurences in arr from 0 - 9 (could only pass in array of nums from 0 - 9)
    # but test was failing
    # refactored to initialise count to be array countaining 200 zeros -> now you can pass in array containing nums between 0 -200
    count = [0] * 200
    # append number * num of occurences in array to output array and return 
    output = []
    # count number of occurences of each number in array
    for i in range(0, len(arr)):
        # edge case - if value at index i is a negative number,
        # break and return error message
        if arr[i] <0:
            return "Error, negative numbers not allowed in Count Sort"
            break
        # else set the value of element in count array at the index of the value of element at index i in original array = its current value + 1
        # ie. original array = [1, 4, 1]
        #     count array will eventually be equal to [0, 2, 0, 1.....]  
        #     (count index = 0, 0 occurences of 0 in original array, count[0] == 0)
        #     (count index = 1, 2 occurences of 1 in original array, count[1] == 2)
        else: 
            count[arr[i]] +=1
            
    # loop over count array
    for j in range(0, len(count)):
        # if value of element at index j is more than 0, extend the output array with j * value of element at index j
        # eg. original array = [1, 3, 1]
        #     count array will eventually be equal to [0, 2, 0, 1.....]  
        #     where j = 0, count[j] = 0 -> do nothing
        #     where j = 1, count[j] = 2 
        #           -> [j] * count[j] = [1, 1]
        #           -> extend output array with [1, 1]
        #           -> output array = [1, 1]
        #     where j = 2, count[j] = 0 -> do nothing 
        #     where j = 3, count[j] = 1 
        #           -> [j] * count[j] = [3]
        #           -> extend output array with [3]
        #           -> output array = [1, 1, 3]
       
        if count[j] > 0:
            output.extend([j] * count[j])
    return output

print(count_sort([1, 4, 2, 7, 5, 2, 9, 0, 0]))