"""
Paulistring.jl Performance Check
"""
from juliacall import Main as jl
from juliacall import AnyValue as JuliaObj
from itertools import combinations

jl.seval('using Pkg; Pkg.add("PauliStrings")')
jl.seval('using PauliStrings')


def get_paulistring_jl_list(paulistrings:list[str])->list[JuliaObj]:
    """
    Get list of Pauli strings.

    Args:
         paulistrings (list[str]): List of string representations of Pauli strings
    Returns:
         list[juliacall.JuliaObj]
         list of Pauli strings in the Paulistring.jl representation
    """
    return [jl.PauliString(paulistring) for paulistring in paulistrings]


def check_paulistring_jl_commutes_with(paulistrings: list[JuliaObj]) -> None:
    """
    Pairwise commutativity check
    Args:
         paulistrings (list[JuliaObj]): list of Pauli strings in the Paulistring.jl representation
    """
    for s1, s2 in combinations(paulistrings, r=2):
        comm_tuple = jl.commutator(s1, s2)
        is_commuting = (comm_tuple[1] == 0)


def check_paulistring_jl_multiply(paulistrings: list[JuliaObj]) -> None:
    """
    Pairwise multiplication check
    Args:
         paulistrings (list[JuliaObj]): list of Pauli strings in the Paulistring.jl representation
    """
    for s1, s2 in combinations(paulistrings, r=2):
        s_res = type(s1)(s1.v ^ s2.v, s1.w ^ s2.w)

