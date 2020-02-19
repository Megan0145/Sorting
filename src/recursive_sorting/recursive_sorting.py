# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = []
    # TO-DO
   
    # base case
    # if length of either array == 0 just return them
    if len(arrA) == 0 or len(arrB) == 0:
        return arrA or arrB

    i = 0
    j = 0

    # if length of merged array is equal to length of arrA + arrB, should just return merged array,
    # else :
    while len(merged_arr) < elements:
        # if element in arrA at index of current value of i is less than element in arrB at index of current value of j,
        # append it to merged array, increment i by 1 so that next time loop runs it only checks the next element in arrA
        if arrA[i] <= arrB[j]:
            merged_arr.append(arrA[i])
            i += 1
        # if element in arrB at index of current value of j is less than element in arrA at index of current value of i,
        # append it to merged array, increment j by 1 so that next time loop runs it only checks the next element in arrB  
        else:
            merged_arr.append(arrB[j])
            j += 1
        # if the value of i is equal to the length of arrA, or the value of j is equal to the length of arrB, it must be at the last element of array
        # -> extend merged array with element ( merge element into array )
        if i == len(arrA) or j == len(arrB):
            merged_arr.extend(arrA[i:] or arrB[j:])
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    # if length of array is less than two, it can't be split any further -> just return array
    if len(arr) < 2:
        return arr
    # else get index of middle element of array
    mid = len(arr)//2
    # set arrA equal to the value of recursively calling merge_sort on all elements up to element at index of mid
    # will continue to recur until length < 2
    arrA = merge_sort(arr[:mid])
     # set arrB equal to the value of recursively calling merge_sort on all elements after element at index of mid
     # will continue to recur until length < 2
    arrB = merge_sort(arr[mid:])
    # pass arrA and arrB into merge function to merge arrays
    return merge(arrA, arrB)

# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
