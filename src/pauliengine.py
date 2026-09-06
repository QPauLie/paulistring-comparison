"""
pauliengine Performance Check
"""
from itertools import combinations
import pauliengine as pe

def get_pauliengine_list(paulistrings:list[str])->list[pe.PauliString]:
    """
    Get list of Pauli strings.

    Args:
         paulistrings (list[str]): List of string representations of Pauli strings
    Returns:
         list[pe.PauliString]:
         Array of Pauli strings in the pauliengine representation
    """
    pauli_strings_list = []

    for paulistring in paulistrings:
        string_dict = {i: op for i, op in enumerate(paulistring) if op != 'I'}
        ps = pe.PauliString(1.0, string_dict)
        pauli_strings_list.append(ps)
    return pauli_strings_list

def check_pauliengine_commutes_with(paulistrings: list[pe.PauliString]) -> int:
    """
    Pairwise commutativity check
    Args:
         paulistrings (list[pe.PauliString]): list of Pauli strings in the pauliengine representation
    Returns:
         int
         number of opertations
    """
    n = 0
    for s1, s2 in combinations(paulistrings, r=2):
        r = s1.commutator(s2)
        n += 1
    return n

def check_pauliengine_multiply(paulistrings: list[pe.PauliString]) -> int:
    """
    Pairwise multiplication check
    Args:
         paulistrings (list[pe.PauliString]: list of Pauli strings in the pauliengine representation
    Returns:
         int
         number of opertations
    """
    n = 0
    for s1, s2 in combinations(paulistrings, r=2):
        rs = s1 * s2
        r =  rs.naked()
        n += 1
    return n
