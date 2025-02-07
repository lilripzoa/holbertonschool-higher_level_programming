#!/usr/bin/env python3


class SwimMixin:
    """
    A mixin class with a swim method.
    """
    
    def swim(self):
        """
        Prints a message indicating that the creature is swimming.
        """
        print("The creature swims!")
    
class FlyMixin:
    """
    A mixin class with a fly method.
    """
    
    def fly(self):
        """
        Prints a message indicating that the creature is flying.
        """
        print("The creature flies!")

class Dragon(SwimMixin, FlyMixin):
    """
    A class representing a dragon, inheriting from both SwimMixin and FlyMixin.
    """
    
    def roar(self):
        """
        Prints a message indicating that the dragon is roaring.
        """
        print("The dragon roars!")
