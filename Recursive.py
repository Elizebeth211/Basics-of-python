#Recursive function

def factorial(num):
    if num == 1:  # Base case
        return 1
    else:
        return num* factorial(num - 1)  # Recursive case
print(factorial(5))  # Output: 120 (5*4*3*2*1)




#binary_Search
def binary_search_recursive(arr, left, right, target):
    if left > right:  # Base case: Target not found
        return -1
    mid = (left + right) // 2  # Find middle index

    if arr[mid] == target:  # Base case: Target found
        return mid
    elif arr[mid] > target:  # Search in left half
        return binary_search_recursive(arr, left, mid - 1, target)
    else:  # Search in right half
        return binary_search_recursive(arr, mid + 1, right, target)


arr = [10, 20, 30, 40, 50, 60, 70]  # Sorted list
target = 40
result = binary_search_recursive(arr, 0, len(arr) - 1, target)

print("Element found at index:", result)  # Output: Element found at index: 3
