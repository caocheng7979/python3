"""This module contains a code example related to

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

License: http://creativecommons.org/licenses/by/4.0/
"""

from __future__ import print_function, division

"""
This module provides one function, structshape(), which takes
an object of any type and returns a string that summarizes the
"shape" of the data structure; that is, the type, size and
composition.
"""

def structshape(ds):
    """Returns a string that describes the shape of a data structure.

    ds: any Python object

    Returns: string
    """
    typename = type(ds).__name__

    # handle sequences
    sequence = (list, tuple, set, type(iter('')))
    if isinstance(ds, sequence):
        t = []
        for i, x in enumerate(ds):
            t.append(structshape(x))
        rep = '%s of %s' % (typename, listrep(t))
        return rep

    # handle dictionaries
    elif isinstance(ds, dict):
        keys = set()
        vals = set()
        for k, v in ds.items():
            keys.add(structshape(k))
            vals.add(structshape(v))
        rep = '%s of %d %s->%s' % (typename, len(ds), 
                         