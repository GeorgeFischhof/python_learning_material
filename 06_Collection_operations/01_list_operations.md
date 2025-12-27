# List operations

<https://docs.python.org/3.14/tutorial/datastructures.html>

<https://docs.python.org/3.14/library/stdtypes.html#typesseq-common>

# The most important functions:

# len(my_list)

Return the number of items in list `my_list`

## list.append(element)

Add one item to the end of the list.

## list.extend(iterable) | list += iterable

Extend the list by appending all the items in the given iterable
to the original list.

## list.insert(index, item)

Insert an item at a given position.<br/>
The first argument is the index of the element before which to insert,<br/>
so `a.insert(0, x)` inserts at the front of the list,<br/>
and `a.insert(len(a), x)` is equivalent to `a.append(x)`.

## list.remove(item)

Remove the first item from the list whose value is `item`.<br/>
It is an error if there is no such item.

## list.pop(index)

Remove the item at the given position in the list, and return it.<br/>
If no index is specified, `pop()` removes and returns the last item in the list.

## list.clear()

Remove all items from the list.<br/>
Equivalent to `del example_list[:]`.

## list.index(x) | list.index(x, start) | list.index(x, start, end)

Return the zero-based index in the list of the first item whose value is equal to `x`.<br/>
Raises a `ValueError` if there is no such item.<br/>
The optional arguments `start` and `end` are interpreted as in slice notation and are used to limit the search
to a particular subsequence of the list.<br/>
The returned index is computed relative to the beginning of the full sequence rather than the `start` argument.

## list.count(item)

Return the number of times `item` appears in the list.

## list.sort(key=None, reverse=False)

Sort the items of the list **in place** (no return value)<br/>
(the arguments can be used for sort customization,<br/>
see `sorted()` for their explanation).

## list.reverse()

Reverse the elements of the list **in place** (no return value).

## list.copy()

Return a shallow copy of the list.<br/>
Equivalent to `a[:]`.

# The del statement

There is a way to remove an item from a list given its index instead of its value:<br/>
the `del` statement.<br/>
It can also be used to remove slices from a list or clear the entire list.

```python
del list[0]
del list[2:4]
del list
```
