#!/usr/bin/env python3

from task_05_dragon import Dragon

"""Design two mixin classes, SwimMixin
and FlyMixin, each equipped with methods
swim and fly respectively. Next, construct
a class Dragon that inherits from both these
mixins. Your aim is to show that a Dragon instance
can both swim and fly."""


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
