L = [100, 200, 300]
L2 = []
for value in L:
    L2.append(value*value)
print(L2) #[10000, 40000, 90000]


L = [100, 200, 300]
L3 = [value*value for value in L]
print(L3)#Output: 10000, 40000, 90000]


#Pure function
def square(x):
    return x * x  # No side effects

print(square(4))  # Output: 16
print(square(4))  # Output: 16 (Always the same)

#immutability
L = [1, 2, 3]
L2 = [x * 2 for x in L]  # Creates a new list

print(L)   # Output: [1, 2, 3] (Original list remains unchanged)
print(L2)  # Output: [2, 4, 6] (New modified list)


l = ['ABC', 'CDEFG', 'SUPER']
l2 = [len(value)for value in l]
print(l2) #Output [3, 5, 5]


##First class function
def greet(name):
    return f"Hello, {name}!"

greeting = greet  # Assign function to a variable
print(greeting("Merry"))  # Output: Hello, Merry!


##Higher-order function
def apply_function(func, value):
    return func(value)

def square(x):
    return x * x

print(apply_function(square, 5))  # Output: 25

##Recursion
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)  # Recursive call

print(factorial(5))  # Output: 120

#Map()
numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x * x, numbers))
print(squared)  # Output: [1, 4, 9, 16] 

##Filter ()
numbers = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # Output: [2, 4, 6]

##Reduce
from functools import reduce

numbers = [1, 2, 3, 4, 5]
sum_all = reduce(lambda x, y: x + y, numbers)
print(sum_all)  # Output: 15


#l2 = [(value1, value2) for value1 in range (1,5) for value2 in range(100, 103)]
#print(l2)

##using normal for loop
l = [[1, 2, 3], [4, 5, 6]]
l2 = []
for value in l:
    for val2 in value:
        print(val2)
        l2.append(val2)
print(l2)
##List comprehension

numbers = [1, 2, 3, 4]
squared = [x * x for x in numbers]
print(squared)  # Output: [1, 4, 9, 16]

##Using if 
numbers = [1, 2, 3, 4, 5, 6]
evens = [x for x in numbers if x % 2 == 0]
print(evens)  # Output: [2, 4, 6]

numbers = [1, 2, 3, 4, 5, 6]
modified = [x if x % 2 == 0 else "Odd" for x in numbers]
print(modified)  # Output: ['Odd', 2, 'Odd', 4, 'Odd', 6]

###Instead of using a for loop we can use a list comprehension
l = [[1, 2, 3], [4, 5, 6]]
flattened = [val2 for value in l for val2 in value]  # Flattening the list
print(flattened)  # Output: [1, 2, 3, 4, 5, 6]

##Dictionary comprehension
d = {x:x**2 for x in range(1,5)}
print(d) #Ouput: {1: 1, 2: 4, 3: 9, 4: 16}

d = {chr(x):x for x in range(65,90)}
print(d) ##Output: {'A': 65, 'B': 66, 'C': 67, 'D': 68, 'E': 69, 'F': 70, 'G': 71, 'H': 72, 'I': 73, 'J': 74, 'K': 75, 'L': 76, 'M': 77, 'N': 78, 'O': 79, 'P': 80, 'Q': 81, 'R': 82, 'S': 83, 'T': 84, 'U': 85, 'V': 86, 'W': 87, 'X': 88, 'Y': 89}


##Swapping keys and values in a dictionary

original_dict = {'a': 1, 'b': 2}

swapped_dict = {v: k for k, v in original_dict.items()}
print(swapped_dict) ##Output: {1: 'a', 2: 'b'}

##basic of generator function
def printval(l):
    for value in l:
        yield value
l = [10, 20, 30, 40, 50, 60]
g = printval(l)
print(next(g)) ##Output: 10
print(next(g)) ##Output: 20
  

#Fibonaci using generator code
def fibo():
    first_num = 0
    second_num = 1
    while(True):
        next_val = first_num + second_num
        yield next_val
        first_num,second_num = second_num,next_val
g = fibo()
print(next(g)) ##Output: 1
print(next(g)) ##Output: 2

##Iterator and itertools
l = [10, 20, 30, 40, 50, 60]
i = iter(l)
print(next(i)) ##Output: 10
print(next(i)) ##Output: 10
for value in i:
     print(value)
#Output
10
20
30
40
50
60








       

