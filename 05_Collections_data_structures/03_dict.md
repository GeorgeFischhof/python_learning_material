# Dictionaries

Python dictionary is an unordered collection of items (until 3.6).<br/>
From Python version 3.6 `dict` keeps its creation order.

While other compound data types have only value as an element,<br/>
a dictionary has a `key: value` pair.

Dictionaries are optimized to retrieve values when the key is known.

To create an empty dict you can use curly braces:<br/>
`empty_dict = {}`

But using the constructor makes the code more readable:<br/>
`empty_dict = dict()`

## example

```python
digit_names = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
}
print(digit_names[1])
```

## To iterate through all keys of a dictionary you can use a for cycle

```python
for key in digit_names:
    print(key)
```

## To get a key's value use the key like the index of a list

```python
print(digit_names[1])
# the 1 is NOT index, but the key
```

## If the key is a string, the string must be used

```python
print(digit_names["key_name"])
```

## Set a value or add a new key–value pair

```python
digit_names["key_name"] = "new_value"
# if the key exists the value will be overwritten
# if the key does not exist, it will be added with the value
```

## To check if an element is in the dictionary, use the in operator

```python
if 3 in digit_names:
    print("dictionary contains the key 3")
```

==> number_with_text.py
