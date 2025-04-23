#s = "PYTHON, HTML, CSS"
#print (s.index("HTML"))#Output: 8
#print (s.find("JAVA"))#Output: -1

#def value_reverse(value):
#    reverse = value[::-1]
#    print(reverse)
#s = "PYTHON"
#result = value_reverse(s)#Output: NOHTYP

#L = [10, 20, 30, 40]
#L.append(50)
#print(L)#Output: [10, 20, 30, 40, 50]

#def value_reverse(value):
#    if type(value)== list or type(value)==str:
#        reverse = value[::-1]
#    else:
#            temp = str(value)
#            reverse = temp[::-1]
#    return reverse

#num = 10
#result = value_reverse(num)
#print(result) #Output: 01

#positional argument
def linear_search (l,key):
    for value in l:
        if key == value:
            return True
    else:
        return False
l = [100, 200, 300, 400, 500]
key = 400
result = linear_search(l, key)
print(result)

#default argument
def greet(name="Guest"):
    print(f"Hello, {name}!")

greet()  #Hello, Guest!
greet("Lisa")  #Hello, Lisa!



#keyword argument
def greet(name, age):
    print(f"Hello, {name}! You are {age} years old.")

greet(age=25, name="Alice")  #  Order does not matter


#3help(print)

#print(100, 200, sep = ",", end = " ")
#print("Hi")


#Variable length positional argument
def add_numbers(*args):
    return sum(args)

print(add_numbers(1, 2, 3))  # 3 arguments
print(add_numbers())  # No arguments (sum = 0)


#Variable length keyword argument
def display_info(**kwargs):
    """Prints all keyword arguments as key-value pairs."""
    for key, value in kwargs.items():
        print(f"{key}: {value}")

display_info(name="Alice", age=25, city="New York")













































    

