"""
Paulie Performance Check
"""
from itertools import combinations
from paulie.common.pauli_string_bitarray import PauliString

def get_paulie_list(paulistrings:list[str])->list[PauliString]:
    """
    Get list of Pauli strings.

    Args:
         paulistrings (list[str]): List of string representations of Pauli strings
    Returns:
         list[PauliString]
         Array of Pauli strings in the Paulie representation
    """
    return [PauliString(pauli_str=paulistring) for paulistring in paulistrings]

def check_paulie_commutes_with(paulistrings: list[PauliString]) -> int:
    """
    Pairwise commutativity check
    Args:
         paulistrings (list[PauliString]): list of Pauli strings in the Paulie representation
    Returns:
         int
         number of opertations
    """
    n = 0
    for s1, s2 in combinations(paulistrings, r=2):
        r = s1.commutes_with(s2)
        n += 1
    return n

def check_paulie_multiply(paulistrings: list[PauliString]) -> int:
    """
    Pairwise multiplication check
    Args:
         paulistrings (list[PauliString]): list of Pauli strings in the Paulie representation
    Returns:
         int
         number of opertations
    """
    n = 0
    for s1, s2 in combinations(paulistrings, r=2):
        r = s1.multiply(s2)
        n += 1
    return n
