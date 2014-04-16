
class lazy(object):

    def __init__(self, i):
        self._L = []
        self._i = iter(i)
        self.realized = False

    def __getitem__(self, index):
        L = self._L
        if not self.realized:
            try:
                while len(L) < index + 2:  # Look ahead one to find end
                    L.append(next(self._i))
            except StopIteration:
                self.realized = True
        return L[index]

    """
__add__
__class__
__contains__
__delattr__
__delitem__
__delslice__
__doc__
__eq__
__format__
__ge__
__getattribute__
__getslice__
__gt__
__hash__
__iadd__
__imul__
__init__
__iter__
__le__
__len__
__lt__
__mul__
__ne__
__new__
__reduce__
__reduce_ex__
__repr__
__reversed__
__rmul__
__setattr__
__setitem__
__setslice__
__sizeof__
__str__
__subclasshook__
append
count
extend
index
insert
pop
remove
reverse
sort
"""
