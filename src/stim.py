"""
Stim Performance Check
"""
from itertools import combinations
import stim

def get_stim_list(paulistrings:list[str])->list[stim.PauliString]:
    """
    Get list of Pauli strings.

    Args:
         paulistrings (list[str]): List of string representations of Pauli strings
    Returns:
         list[stim.PauliString]
         Array of Pauli strings in the stim.PauliString representation
    """
    return [stim.PauliString(paulistring) for paulistring in paulistrings]

def check_stim_commutes_with(paulistrings: list[stim.PauliString]) -> int:
    """
    Pairwise commutativity check
    Args:
         paulistrings (list[stim.PauliString]): list of Pauli strings in the stim representation
    Returns:
         int
         number of opertations
    """
    n = 0
    for s1, s2 in combinations(paulistrings, r=2):
        r = s1.commutes(s2)
        n += 1
    return n

def check_stim_multiply(paulistrings: list[stim.PauliString]) -> int:
    """
    Pairwise multiplication check
    Args:
         paulistrings (list[stim.PauliString]): list of Pauli strings in the stim representation
    Returns:
         int
         number of opertations
    """
    n = 0
    for s1, s2 in combinations(paulistrings, r=2):
        r = s1 * s2
        n += 1
    return n
