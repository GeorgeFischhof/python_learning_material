# Preamble

So far we did not use the following phrase:

```python
if __name__ == "__main__":
    main_or_whatever_the_main_functions_is_called()
```

But from now on it will be mandatory :-)

# Modules

<https://www.programiz.com/python-programming/modules>  
<http://docs.python-guide.org/en/latest/writing/structure/#modules>

TODO search for some better, newer article

Python modules are one of the main abstraction layers available and
probably the most natural one. Abstraction layers allow separating
code into parts holding related data and functionality.

For example, a layer of a project can handle interfacing with user
actions, while another would handle low-level manipulation of data.
The most natural way to separate these two layers is to regroup all
interfacing functionality in one file, and all low-level operations
in another file. In this case, the interface file needs to import
the low-level file.  
This is done with the `import` and `from ... import` statements.

As soon as you use import statements you use modules. These can be
either built-in modules such as `os` and `sys`, third-party modules you
have installed in your environment, or your project’s internal modules.

-- o --

# Very bad

```python
from my_module import *

x = sqrt(4)  # Is sqrt part of my_module? A builtin? Defined above?
```

# Better

```python
from my_module import sqrt

x = sqrt(4)  # sqrt may be part of my_module, if not redefined in between
```

# Best

```python
import my_module

x = my_module.sqrt(4)  # sqrt is visibly part of my_module's namespace
```

# Search path

Python uses (among some other methods) the <br/>
`PYTHONPATH` environment variable to search for modules to be imported. <br/>
(At least this is the one we can use the easiest way...)

# Search order

<https://docs.python.org/3/tutorial/modules.html>

> When a module named `spam` is imported, the interpreter first searches 
> for a built-in module with that name. These module names are listed 
> in `sys.builtin_module_names`. If not found, it then searches for a file
> named `spam.py` in a list of directories given by the variable `sys.path`. 
> `sys.path` is initialized from these locations:
>
> - The directory containing the input script  
>   (or the current directory when no file is specified).  
> - `PYTHONPATH` (a list of directory names, with the same  
>   syntax as the shell variable `PATH`).  
> - The installation-dependent default 
>   (by convention including a `site-packages` directory, handled by the `site` module).
> 
> **Note:**  
> On file systems which support symlinks, the directory containing
> the input script is calculated after the symlink is followed.
> In other words the directory containing the symlink is **not** added
> to the module search path.
> 
> After initialization, Python programs can modify `sys.path`
> (equal to the `PYTHONPATH` environment variable,
> just from inside the script).  
> The directory containing the script being run is placed at the
> beginning of the search path, ahead of the standard library path.
> This means that scripts in that directory will be loaded instead of
> modules of the same name in the library directory. This is an error
> unless the replacement is intended. 

# Order of modules to be imported for readability

1. **standard library** — alphabetical
2. **third party** — alphabetical
3. **project's own modules** — alphabetical

with a **blank line** between the groups
