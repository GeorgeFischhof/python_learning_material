# Readable functions

**Cognitive complexity**

The number of objects an average human can
hold in working memory is **7 ± 2**.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - *Miller's Law*

Write short functions, extract the parts into other functions.

## Avoid too many nested levels

Bad:

```python
def update_post(...):
    post = get_post(...)
    if action == "update-title":
        if title == "":
            ...
        else:
            ...
    elif action == "add-tag":
        ...
```

Good:

```python
def update_post(...):
    post = get_post(...)
    if action == "update-title":
        update_post_title(...)
    elif action == "add-tag":
        update_post_add_tag(...)
```

## Use linters to check the code

- [complexipy](https://pypi.org/project/complexipy/)
