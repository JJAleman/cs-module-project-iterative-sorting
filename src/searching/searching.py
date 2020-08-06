def linear_search(arr, target):
    
    for i in range(len(arr)): #traverses the length of the array

        if arr[i] == target: #if element is equal to the "target" it return the element
            return i

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:

        mid = (high + low) // 2

        if arr[mid] < target: #checks to see if target is present at mid
            low = mid + 1

        elif arr[mid] > target: #if target is greater, ignores LHS
            high = mid - 1

        else:  #if target is smaller, ignore RHS
            return mid


    return -1  # not found
