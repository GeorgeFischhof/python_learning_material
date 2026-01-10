
list_markers_1 = (1, 2, 3, 4)
list_markers_a = ("a", "b", "c", "d")
list_markers_i = ("i", "ii", "iii", "iv")

list_markers_by_level = zip(list_markers_1, list_markers_a, list_markers_i)

print(list(list_markers_by_level))
# ==> [(1, "a", "i"), (2, "b", "ii"), (3, "c", "iii"), (4, "d", "iv")]

print(list(zip("ABCD", "xy")))  # ==> [("A", "x"), ("B", "y")]
# zip works until the shortest iterable is finished


# zip() should only be used with unequal length inputs
# when you don’t care about trailing, unmatched values
# from the longer iterables.
# If those values are important, use itertools.zip_longest() instead.
