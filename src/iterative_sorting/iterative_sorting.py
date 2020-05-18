# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    # O(n)*O(n) = O(n * n) = O(n²)
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here
        for j in range(smallest_index, len(arr)):
            if arr[j] < arr[smallest_index]:
                arr[i], arr[j] = arr[j], arr[i]
        # TO-DO: swap
        # Your code here
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Your code here
    # O(n)*O(n) = O(n * n) = O(n²)
    end = len(arr)
    for i in range(end):
        for j in range(end - 1 - i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):
    # Your code here

    return arr
