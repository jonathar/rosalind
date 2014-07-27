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


def count_nucleotides(dna_str):
    '''Counts the number of occurences of 'A', 'C', 'G' or 'T' in str. Returns
    a list containing four integers representing the frequencies of the former.

    Solves Rosalind Problem #1
    http://rosalind.info/problems/dna/
    '''
    frequencies = defaultdict(int)
    for nucleotide in dna_str:
        frequencies[nucleotide] += 1

    return '%(A)s %(C)s %(G)s %(T)s' % frequencies

def transcribe_dna_to_rna(dna_str):
    '''An RNA string is a string formed from the alphabet containing 'A', 'C',
    'G', and 'U'.

    Given a DNA string t corresponding to a coding strand, its transcribed RNA
    string u is formed by replacing all occurrences of 'T' in t with 'U' in u.

    Given: A DNA string t having length at most 1000 nt.

    Return: The transcribed RNA string of t.
    '''
    return dna_str.replace('T', 'U')


def reverse_compliment(dna_str):
    '''In DNA strings, symbols 'A' and 'T' are complements of each other, as
    are 'C' and 'G'.

    The reverse complement of a DNA string s is the string sc formed by
    reversing the symbols of s, then taking the complement of each symbol
    (e.g., the reverse complement of "GTCA" is "TGAC").

    Given: A DNA string s of length at most 1000 bp.

    Return: The reverse complement sc of s.
    '''
    compliments = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return ''.join([compliments[c] for c in dna_str[::-1] if c in compliments])


def fib_with_k(input_str):
    """
    Given: Positive integers n<=40 and k<=5.

    Return: The total number of rabbit pairs that will be present after n
    months if we begin with 1 pair and in each generation, every pair of
    reproduction-age rabbits produces a litter of k rabbit pairs (instead of
    only 1 pair).

    Base case with n=1, k=3
    >>> fib_with_k('1 3')
    1

    Secondary Base case with n=2, k=3
    >>> fib_with_k('2 3')
    1

    First result without hitting base case
    >>> fib_with_k('3 3')
    4

    Test n < 0 returns 0
    >>> fib_with_k('-1 3')
    0

    Test k < 0 returns 0
    >>> fib_with_k('3 -2')
    0

    Test with real input
    >>> fib_with_k('4 3')
    7

    Test wtih real input
    >>> fib_with_k('5 3')
    19

    Test with large real input
    >>> fib_with_k('30 3')
    20444528200
    """
    inputs = input_str.split(' ')
    n = int(inputs[0])
    k = int(inputs[1])

    def fib(n, k):
        if n < 0 or k < 0 or n == 0:
            return 0
        elif n ==1:
            return 1
        else:
            return fib(n=n-1, k=k) + (fib(n=n - 2, k=k) * k)

    return fib(n=n, k=k)
