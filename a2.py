def get_length(dna):
    """ (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """
    return len(dna)

def is_longer(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """
    if dna1 > dna2:
        return True
    elif dna1 == dna2:
        return False
    else:
        return False

def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """
    number = 0
    for num in dna:
        if num == nucleotide:
           number += 1
    return number

def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False
    """
    if dna2 in dna1:
        return True
    else:
        return False

def is_valid_sequence(dna):
    ''' (str) -> bool

    Return True if only DNA sequence is valid.

    >>> is_valid_sequence('ATCGGTCA')
    True
    >>> is_valid_sequence('LTPROCKS')
    False
    '''
    for n in dna:
        if n not in('ATCG'):
            return False
        else:
            return True

def insert_sequence(dna1, dna2, number):
    '''(str, str, int) -> str

    Return the DNA sequence obtained by inserting
    the second DNA sequence into the first DNA sequence.

    >>> insert_sequence ('CCGG', 'AT', 2)
    'CCATGG'
    >>> insert_sequence ('CAGT', 'CGC',3)
    'CACGCGT'
    '''
    return dna1[:number] + dna2 + dna1[number:]

def get_complement(nucleot):
    ''' (str) -> str

    Return the complement of a nucleotide.

    >>> get_complement('T')
    'A'
    >>> get_complement('C')
    'G'
    '''
    if nucleot == 'T':
        return 'A'
    elif nucleot == 'A':
        return 'T'
    
    if nucleot == 'G':
        return 'C'
    elif nucleot == 'C':
        return 'G'

def get_complementary_sequence(dna):
    '''(str) -> str

    Return the complement of a given DNA sequence.

    >>> get_complementary_sequence('ATCGGACT')
    TAGCCTGA
    >>> get_complementary_sequence('GCACTCC')
    CGTGAGG
    '''
    complementary_seq = ''

    for nucleot in dna:
        complementary_seq += get_complement(nucleot)
    return complementary_seq


