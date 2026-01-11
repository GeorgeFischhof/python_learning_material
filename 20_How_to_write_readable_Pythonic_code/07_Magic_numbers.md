# Magic numbers and magic strings

```python
list_1 = [1, 2, 3, 4, 5]
list_2 = [2, 3, 4, 5, 6]
list_3 = [3, 4, 5, 6, 7]

matrix = [list_1, list_2, list_3]

for row in range(3):
    for cell in range(5):
        print(matrix[row][cell])
```

Right now we can see or we can think we know
why the `range(3)` and `range(5)` are there. <br/>
But what if the lists and the matrix come from different places? <br/>
... <br/>
and we want to process them on a third different place?

There is no way to know where the **3** and the **5** come from... <br/>
These are the **magic numbers**. <br/>
(The similar can happen with strings or with any other data types.)

### What can we do with them to make the code understandable? <br/> Let's see.

1.  Give a name to the numbers (assign to a variable). <br/>
    With the names it is much more understandable:

    ```python
    number_of_rows = 3
    number_of_cells = 5

    for row in range(number_of_rows):
        for cell in range(number_of_cells):
            print(matrix[row][cell])
    ```

2.  If we need the index indeed <br/>
    (quite rare case, and normally solved with `enumerate`), <br/>
    then let's acquire it from the collection itself using `len()`:

    ```python
    number_of_rows = len(matrix)
    number_of_cells = len(list_1)

    for row in range(number_of_rows):
        for cell in range(number_of_cells):
            print(matrix[row][cell])
    ```

3.  The Pythonic way is to use the `for` cycle to iterate through the list <br/>
    because the list is iterable, <br/>
    and this way there is no need to use index nor `range`:

```python
for row in matrix:
    for cell in row:
        print(cell)
```

As you can see there is no magic number appearing from nothing. <br/>
And as there are no burned‑in numbers, if the length of the list changes, <br/>
the program will work well without any change.
