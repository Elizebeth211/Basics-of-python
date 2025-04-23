import re


#recompile
pattern = re.compile(r"\d+")
fruit = "12 apples, 5 bananas"
matches = pattern.findall(fruit)
print(matches)  # Output: ['12', '5']

text = "Hello world! My number is 12345 and I love cats."

# . (Any one character except newline)
print(re.findall(r"c.t", "cat cut c8t cbt ctt"))  # Output: ['cat', 'cut', 'c8t', 'cbt', 'ctt']

# ^ (Matches start of the string)
print(re.search(r"^Hello", text).group())  # Output: 'Hello'

# $ (Matches end of the string)
print(re.search(r"world!$", text))  # Output: None (because there's more text after "world!")

# \d (Matches any digit)
print(re.findall(r"\d+", text))  # Output: ['12345']

# \w (Matches letters, numbers, underscore)
print(re.findall(r"\w+", "Hello_123 world!"))  # Output: ['Hello_123', 'world']

# \s (Matches any whitespace)
print(re.findall(r"\s+", "Hello   World"))  # Output: ['   '] (matches spaces)

# \b (Matches word boundary)
print(re.findall(r"\bcat\b", "The cat is here but caterpillar is not."))  # Output: ['cat']

# + (Matches one or more occurrences)
print(re.findall(r"a+", "apple banana aaa aardvark"))  # Output: ['a', 'a', 'aaa', 'a']

# * (Matches zero or more occurrences)
print(re.findall(r"ho*t", "ht hot hoot hooot"))  # Output: ['ht', 'hot', 'hoot', 'hooot']

# ? (Matches zero or one occurrence)
print(re.findall(r"colou?r", "color colour colouur"))  # Output: ['color', 'colour']

# {n} (Matches exactly n times)
print(re.findall(r"\d{3}", "123 12 1234 56789"))  # Output: ['123', '123', '567']

# {n,} (Matches at least n times)
print(re.findall(r"\d{2,}", "1 12 123 1234"))  # Output: ['12', '123', '1234']

# {n,m} (Matches between n and m times)
print(re.findall(r"\d{2,4}", "1 12 123 1234 12345"))  # Output: ['12', '123', '1234']


## dd-mm-yyyy
s = " Hi! today is 12-05-2018"
r = re.compile (r"([0-9]{2})-([0-9]{2})-([0-9]{4})")
l = re.findall(r,s) 
print(l) #output[('12', '05', '2018')]









