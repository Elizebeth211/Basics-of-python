import Math_operations

print(Math_operations.add(5, 3))  # Output: 8
print(Math_operations.subtract(10, 4))  # Output: 6
print(Math_operations.multiply(2, 2))  # Output: 4

#import only the function we want to use from the module
from Math_operations import add

print(add(5, 3)) # Output:8
