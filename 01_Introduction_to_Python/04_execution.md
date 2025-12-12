# Execution

**Trying something**
You can try something in the interactive python interpreter: start python by typing `python` on the
command line
`>>>` cursor appears, you can write to it.  
You can do the same a little bit easier in the PyCharm IDE using the Python Console window.

**Script execution**
Instructions are executed from top to down, left to right in a script file.  
If a script file contains only function definitions, nothing will be happened. ... The interpreter
parses the functions, put them into the memory, and that is all. A function must be called in order
to execute it.

**example:**

```python
def some_function():
    print('apple')

some_function()
```


Above a function is defined with name `some_function`, and called after the definition.


The Python script has no explicit entry point. <br/>
The top-level code is executed (the most outdented) <br/>
Therefore you can define functions in any order even if they call each-other,
because they just must be defined before calling

```python
def function_one():
    function_two()

def function_two():
    pass

function_one()
```

The above code will be executed in the following order:
- creating function named functions_one
- creating function named functions_two
- executing the function call for function_one
- executing function_one which calls functions_two
- executing function_two which does nothing



Execution of the script file is invoked with a command like this:
`c:\> python path\to\my_script.py`
