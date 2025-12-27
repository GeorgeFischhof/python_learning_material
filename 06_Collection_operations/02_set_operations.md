# Set operations

<https://docs.python.org/3.14/library/stdtypes.html#set-types-set-frozenset>

# The most important functions:

## len(s)

Return the number of elements in set `s` (cardinality of `s`).

## set.add(item)

Add `item` to the set.

## set.remove(item)

Remove `item` from the set.<br/>
Raises `KeyError` if `item` is not contained in the set.

## set.discard(item)

Remove `item` from the set if it is present.<br/>
(No error is raised.)

## set.pop()

Remove and return an arbitrary element from the set.<br/>
Raises `KeyError` if the set is empty.

## set.clear()

Remove all elements from the set.

## set.copy()

Return a shallow copy of the set.
