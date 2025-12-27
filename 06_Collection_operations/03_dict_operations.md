# Dict operations

<https://docs.python.org/3.14/library/stdtypes.html#mapping-types-dict>

# The most important functions:

## len(my_dict)

Return the number of items in the dictionary `my_dict`.

## dict.clear()

Remove all items from the dictionary.

## dict.copy()

Return a shallow copy of the dictionary.

## fromkeys(iterable[, value])

Create a new dictionary with keys from `iterable` and values set to `value`.<br/>
`fromkeys()` is a class method that returns a new dictionary.<br/>
`value` defaults to `None`.

example:

```python
cities = ["New York", "London", "Budapest"]
cities_with_zip = dict.fromkeys(cities)
# Add zip numbers here...
```

## dict.get(key[, default])

Return the value for `key` if `key` is in the dictionary,<br/>
else `default`. If `default` is not given, it defaults to `None`,<br/>
so this method never raises a `KeyError`.

## dict.items()

Return a list (exactly a view) of the dictionary’s items as<br/>
`(key, value)` pairs (the list contains tuples).

## dict.keys()

Return a list (exactly a view) of the dictionary’s keys.

## dict.values()

Return a list (exactly a view) of the dictionary’s values.

**About the dict views** <br/>
<https://docs.python.org/3.14/library/stdtypes.html#dict-views>


## dict.pop(key[, default])

If `key` is in the dictionary,<br/>
remove it and return its value,<br/>
else return `default`.

If `default` is not given and `key` is not in the dictionary,<br/>
a `KeyError` is raised.

## dict.popitem()

Remove and return a `(key, value)` pair from the dictionary.<br/>
Pairs are returned in LIFO order.

`popitem()` is useful to destructively iterate over a dictionary,<br/>
as often used in set algorithms.<br/>
If the dictionary is empty, calling `popitem()` raises a `KeyError`.

Changed in version 3.7: LIFO order is now guaranteed.<br/>
In prior versions, `popitem()` would return an arbitrary key/value pair.

## dict.update([other])

Update the dictionary with the key/value pairs from `other`,<br/>
overwriting existing keys. Return `None`.

`update()` accepts either another dictionary object or an
iterable of key/value pairs (as tuples or other iterables of length two).<br/>
If keyword arguments are specified, the dictionary is then updated
with those key/value pairs: `d.update(red=1, blue=2)`.
