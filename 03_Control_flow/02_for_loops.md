# For loops

Programs sometimes need to repeat actions.  
To repeat actions we can use a `for` loop.

The `for` loop iterates over an iterable.  
Several things can be an *iterable*:

- strings  
- collections (list, tuple, dictionary, set)  
- text files  
- results of special functions that create an iterable  

If we want to execute a code part for a given number of cycles,  
we can use the `range()` function  
(this is a built‑in special function mentioned above).

## range()

```python
range(stop)
range(start, stop)
range(start, stop, step)
```

- the parameters are integers  
- `start` defaults to 0  
- `stop`: numbers will be generated until `stop`, excluding the value of `stop`  
- `step` defaults to 1  

## example_1

```python
for number in range(4):
    print(number)
```

**result_1:**

```
0
1
2
3
```

## example_2

```python
for even_number in range(2, 11, 2):
    print(even_number)
```

**result_2:**

```
2
4
6
8
10
```

## example_3

```
fruits = ("apple", "banana", "lemon")  # tuple, iterable
for fruit in fruits:
    print(fruit)
```

**result_3:**

```
apple
banana
lemon
```
