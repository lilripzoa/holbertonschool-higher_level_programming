#!/usr/bin/env python3
""" Pickle module
"""
import pickle


class CustomPickle:
    """ CustomPickle class
    """

    @staticmethod
    def dump(obj, file):
        """ dump method
        """
        with open(file, 'wb', encoding='utf-8') as fic:
            pickle.dump(obj, fic)

    @staticmethod
    def load(file):
        """ load method
        """
        with open(file, 'rb', encoding='utf-8') as fic:
            return pickle.load(fic)
