# lambda - The Anonymous Functions

These functions are called anonymous because they are not
declared in the standard manner by using the `def` keyword.
You can use the `lambda` keyword to create small anonymous functions.

Lambda forms can take any number of arguments but return
just one value in the form of an expression. They cannot
contain commands or multiple expressions.

An anonymous function cannot be a direct call to `print`
because lambda requires an expression.

Lambda functions have their own local namespace and cannot
access variables other than those in their parameter list
and those in the global namespace.

## Syntax

```
lambda [arg1 [,arg2,.....argn]]: expression
```

## Examples

```python
# Function definition is here
sum = lambda arg1, arg2: arg1 + arg2
print("Value of total : ", sum(10, 20))
```

```python
g = lambda x: x*2
g(3)
# 6
```

```python
(lambda x: x*2)(3)
# 6
```

## Usage

Can be used for example  
- when selecting a key in sorting,  
- for short and obvious calculations  

## Example sorting usage

```python
students = [
    ("john", "A", 15),
    ("jane", "B", 12),
    ("dave", "B", 10),
]
sorted(students, key=lambda student: student[2])   # sort by age
# ==> [("dave", "B", 10), ("jane", "B", 12), ("john", "A", 15)]
```

Note: as it has no name, it can **reduce readability**, <br/>
because the reader must evaluate the expression<br/>
during reading **instead of reading a meaningful name**.
