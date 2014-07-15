import sys
import types
from collections import defaultdict


def list_functions():
    '''Lists all functions in the module except for list_functions.'''
    functions = []
    current_module = sys.modules[__name__]
    for a in dir(current_module):
            if isinstance(current_module.__dict__.get(a), types.FunctionType):
                functions.append(current_module.__dict__.get(a).__name__)

    functions.remove('list_functions')
    return functions


def count_nucleotides(str):
    '''Counts the number of occurences of 'A', 'C', 'G' or 'T' in str. Returns
    a list containing four integers representing the frequencies of the former.

    Solves Rosalind Problem #1
    http://rosalind.info/problems/dna/
    '''
    frequencies = defaultdict(int)
    for nucleotide in str:
        frequencies[nucleotide] += 1

    return '%(A)s %(C)s %(G)s %(T)s' % frequencies
