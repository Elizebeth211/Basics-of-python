import itertools
l1 = [10, 20, 30, 40, 50]
l2 = [100, 200, 300, 400, 500]
i = itertools.chain(l1, l2)
print(i)
for value in i:
     print(value)


##Infinite counter
counter = itertools.count(start=10, step=2)  # Starts at 10, increments by 2

print(next(counter))  # Output: 10
print(next(counter))  # Output: 12
print(next(counter))  # Output: 14

##Infinite loop over a sequence
colors = itertools.cycle(["red", "blue", "green"])
print(next(colors))  # Output: red
print(next(colors))  # Output: blue
print(next(colors))  # Output: green
print(next(colors))  # Output: red (repeats)

##Repeating a value
repeater = itertools.repeat("Hello", 3)  # Repeat "Hello" 3 times
print(next(repeater))  # Output: Hello
print(next(repeater))  # Output: Hello
print(next(repeater))  # Output: Hello

##Generating all possible ordering
from itertools import permutations
perm = permutations([1, 2])  # Generate all orderings
print(list(perm))   ##Output[(1, 2), (2, 1)]

##Unique pair
from itertools import combinations
comb = combinations([1, 2, 3], 2)  # Choose 2 elements at a time
print(list(comb))##Output[(1, 2), (1, 3), (2, 3)]

##How to group an element
from itertools import groupby
data = [("Apple", "Fruit"), ("Carrot", "Vegetable"), ("Banana", "Fruit")]
# Sort first, since groupby only groups consecutive items
data.sort(key=lambda x: x[1])
grouped_data = groupby(data, key=lambda x: x[1])
for key, group in grouped_data:
    print(key, list(group))

##Cloning an iterator into multiple copies
from itertools import tee
numbers = iter([1, 2, 3, 4, 5])  # Create an iterator
# Create two copies of the iterator
copy1, copy2 = tee(numbers, 2)
print(list(copy1))  # Output: [1, 2, 3, 4, 5]
print(list(copy2))  # Output: [1, 2, 3, 4, 5] (independent of copy1)

###Slicing an operator
from itertools import islice
numbers = iter([10, 20, 30, 40, 50])
# Slice first 3 elements
sliced_numbers = islice(numbers, 3)
print(list(sliced_numbers))  # Output: [10, 20, 30]

##slicing an operator using range
numbers = iter(range(10, 101, 10))  # Iterator: [10, 20, ..., 100]
# islice(iterator, start, stop, step)
sliced = islice(numbers, 1, 7, 2)  # Equivalent to list[1:7:2]
print(list(sliced))  # Output: [20, 40, 60]





















