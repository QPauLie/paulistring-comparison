"""
Python version of PauliStrings.jl Performance Check
"""
from itertools import combinations
import paulistrings as ps


def get_python_paulistring_jl_list(paulistrings:list[str])->list[str]:
    """
    Get list of Pauli strings.

    Args:
         paulistrings (list[str]): List of string representations of Pauli strings
    Returns:
         list[juliacall.JuliaObj]
         list of Pauli strings in the Paulistrings representation
    """
    return paulistrings.copy()


def check_python_paulistring_jl_commutes_with(paulistrings: list[str]) -> None:
    """
    Pairwise commutativity check
    Args:
         paulistrings (list[str]): list of Pauli strings in the Paulistrings representation
    """
    for s1, s2 in combinations(paulistrings, r=2):
        num_qubits = len(s1)
        op1 = ps.Operator(num_qubits)
        op1 += s1
    
        op2 = ps.Operator(num_qubits)
        op2 += s2
    
        comm = ps.commutator(op1, op2)
        is_commuting = len(comm) == 0


def check_python_paulistring_jl_multiply(paulistrings: list[str]) -> None:
    """
    Pairwise multiplication check
    Args:
         paulistrings (list[str]): list of Pauli strings in the Paulistrings representation
    """
    for s1, s2 in combinations(paulistrings, r=2):
        num_qubits = len(s1)
        op1 = ps.Operator(num_qubits)
        op1 += s1
    
        op2 = ps.Operator(num_qubits)
        op2 += s2
        r = op1 * op2
