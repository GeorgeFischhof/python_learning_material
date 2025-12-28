# File operations

To store and retrieve data from files. 
Basically there are two types of files 
- text files 
- binary files

To make a file usable we must open it, using the `open` function.<br/>
After using the file it must be closed with the `file.close()` method.<br/>
Using `close` manually is not recommended. Instead use the `with` statement 

The `with` statement (the recommended way) closes the file after the with block,
and if the program terminates unexpectedly. So using the `with` statement
we can be sure that the file will be closed.

open documentation (and file modes):  
<https://docs.python.org/3.14/library/functions.html#open>

# Reading files - one line at a time

## Iterate over the lines of the file – `for` cycle (the most comfortable way)

```python
with open("some_file.txt", encoding="utf-8") as my_text_file:
    for line in my_text_file:
        # variable "line" will contain the end of line character (\n)
        # process the single line ...
```

## Using readline()

```python
line = None
with open("some_file.txt", encoding="utf-8") as my_text_file:
    while line != "":
        line = my_text_file.readline()
        # variable "line" will contain the end of line character (\n)
        # process the single line ...
```

# Reading files – all of the file content at a time

## readlines() or list(opened_file)

```python
with open("some_file.txt", encoding="utf-8") as my_text_file:
    lines = my_text_file.readlines()
    # variable "lines" is a list of lines 
    # every single line will contain the end of line character (\n)
    # process the content ...
```

## Read the entire file as a single string

```python
with open("some_file.txt", "rt", encoding="utf-8") as my_text_file:
    data = my_text_file.read()
    # data will contain every characters in one big string, contains \n too 
    # process file content ...
```

# Writing files – all of the file content at a time

## Write chunks of text to file - `write()`

```python
with open("some_file.txt", "w", encoding="utf-8") as my_text_file:
    my_text_file.write("new text line" + "\n")
    my_text_file.write("Last line without new line")
    # write command writes the exact string,
    # it does not add end of line character (\n)
    # you must add it if you want
```

## Write several lines into file at a time - `writelines()`

```python
lines = list()
lines.append("Line 01 \n")
lines.append("Line 02 \n")
lines.append("Line 03 \n")
# writelines does not add line ending

with open("some_file.txt", "w", encoding="utf-8") as my_text_file:
    my_text_file.writelines(lines)
```

## `print` into file

There is a possibility to use the `print` command to print into an open file.
It can be useful when you want to write several small pieces of info into
one line and want to add separator and line ending strings:

```python
with open("some_file.txt", "w", encoding="utf-8") as my_text_file:
    print(1, 2, 3, 4, sep=" < ", end=" increasing numbers", file=my_text_file)
    # 1 < 2 < 3 < 4 increasing numbers
```

# Append to text file

Nothing special, just need to open for append, and write into it:

```python
with open("some_file.txt", "a", encoding="utf-8") as my_text_file:
    my_text_file.write("new text line" + "\n")
    my_text_file.write("Last line without new line")
```
