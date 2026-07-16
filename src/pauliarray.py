"""
PauliArray Performance Check
"""
from itertools import combinations
from pauliarray import PauliArray

def get_pauliarray_list(paulistrings:list[str])->list[PauliArray]:
    """
    Get list of Pauli strings.

    Args:
         paulistrings (list[str]): List of string representations of Pauli strings
    Returns:
         list[PauliArray]
         List of Pauli strings in the PauliArray representation
    """
    return [PauliArray.from_labels(paulistring) for paulistring in paulistrings]

def check_pauliarray_commutes_with(paulistrings: list[PauliArray]) -> None:
    """
    Pairwise commutativity check
    Args:
         paulistrings (list[PauliArray]): list of Pauli strings in the PauliArray representation
    """
    for s1, s2 in combinations(paulistrings, r=2):
        r = s1.commute_with(s2)

def check_pauliarray_multiply(paulistrings: list[PauliArray]) -> None:
    """
    Pairwise multiplication check
    Args:
         paulistrings (list[PauliArray]): list of Pauli strings in the PauliArray representation
    """
    for s1, s2 in combinations(paulistrings, r=2):
        r = s1.tensor_pauli_array(s2)
