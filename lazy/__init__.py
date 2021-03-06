from itertools import count


class lazy(object):
    _offset = 0

    def __init__(self, it):
        self._L = []
        self._it = it
        self._i = iter(it)
        self.realized = False

    def _realize(self, index):
        # XXX index may be a slice object or negative
        L = self._L
        i = self._i

        # Special case--we may have skipped some elements using 'rest' that
        # we never need to actually store
        offset = self._offset
        if not L and offset:
            try:
                # Skip unnecessary elements
                while offset:
                    next(i)
                    offset -= 1
            except StopIteration:
                # Skipped past end of sequence.  This sequence will be empty.
                self.realized = True
                raise
            self._offset = offset

        # Attempt to realize enough of the sequence to be able to find the
        # indexed element
        index += self._offset
        try:
            while len(L) < index + 1:
                L.append(next(i))
        except StopIteration:
            self.realized = True
            raise

        return L[index]

    def __getitem__(self, index):
        if not self.realized:
            try:
                return self._realize(index)
            except StopIteration:
                raise IndexError(index)
        return self._L[index]

    def __repr__(self):
        return u'lazy(%r)' % self._it

    def first(self):
        """
        Returns the first element of the lazy sequence.
        """
        return self[0]

    def rest(self):
        """
        Returns a new lazy sequence which starts at the second element of the
        current lazy sequence.
        """
        cls = type(self)
        seq = cls.__new__(cls)
        seq._it = self._it
        seq._i = self._i
        seq.realized = self.realized
        seq._offset = self._offset + 1
        seq._L = self._L
        return seq

    def __iter__(self):
        """
        Iterate over elements, realizing sequence as we go.
        """
        if self.realized:
            return iter(self._L)
        return (self._realize(i) for i in count())
