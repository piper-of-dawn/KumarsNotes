from typing import Iterable
def flatten_iterable (iterable: Iterable):
    for i in iterable:
        if hasattr(i, '__iter__'):
            yield from flatten_iterable(i)
        else:
            yield i