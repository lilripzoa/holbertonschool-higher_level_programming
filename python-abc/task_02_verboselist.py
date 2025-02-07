#!/usr/bin/env python3

"""Verboselist module"""


def verboselist(list):
    """Verboselist function"""
    class Verboselist(list):
        """Verboselist class"""
        def append(self, value):
            """Append method"""
            print("APPEND {}".format(value))
            super().append(value)

        def extend(self, values):
            """Extend method"""
            print("Extended the list with {} items.".format(values))
            super().extend(values)

        def remove(self, value):
            """Remove method"""
            print("removed {} from the list.".format(value))
            super().remove(value)

        def pop(self, index=None):
            """Pop method"""
            if index is None:
                print("Popped {} from the list.".format(self[-1]))
            else:
                print("Popped {} from the list.".format(index))
            return super().pop(index)

    return Verboselist(list)
