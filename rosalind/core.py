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
