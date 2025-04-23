#file = open("example.txt", "r")

##writing a content in a file
file = open("hello.txt", "w")  # Open file in write mode
file.write("Hello, World!")  # Write content to file
file.close()  # Close the file


##Reading a file
#using read()
file = open("example.txt", "r")  # Open file in read mode
content = file.read()
#print(content)  # Output: Hello, World!
file.close()

#using readline ()
file = open("example.txt", "r")
line = file.readline()  # Reads first line only
#print(line)
file.close()

#using readlines ()
file = open("example.txt", "r")
lines = file.readlines()  # Returns a list of lines
#print(lines)
file.close()

##Add content without within the same file
file = open("hello.txt", "a")  # Open in append mode
file.write("\nHappy to help you!")  # Adds new content without deleting old data
file.close()

##With statement automatically close the file after excution
#with open("example.txt", "r") as file:
 #   content = file.read()
 #   print(content)  # File closes automatically after this block

##Checking ids the file exists or not 
from pathlib import Path
#file_path = Path("book.txt")
#if file_path.exists():
#    with file_path.open("r") as file:
 #       print(file.read())
#else:
 #   print("File does not exist.")

#Using tell() and seek()
#with open("example.txt", "r") as file:
#    print(file.tell())  # Output: 0 (Start of file)
 #   file.read(5)  # Read 5 characters
#    print(file.tell())  # Output: 5 (Cursor moved forward)



with open("example.txt", "r") as file:
    file.seek(5)  # Move cursor to the 5th byte
    print("Cursor moved to:", file.tell())  # Output: 5
    content = file.read(5)  # Read 5 characters from position 5
    print("Read content:", content) #output: lizab

with open("hello.txt", "rb") as file:
    file.read(5)  # Read first 5 characters
    print("Cursor at:", file.tell())  # Output: 5
    file.seek(3, 1)  # Move cursor 3 bytes forward from current position
    print("Cursor moved to:", file.tell())  # Output: 8

with open("example.txt", "rb") as file:  # Open in binary mode for `whence=2`
    file.seek(-5, 2)  # Move 5 bytes before the end
    print("Cursor moved to:", file.tell())  # Output: Position before last 5 bytes
    content = file.read()

    











































