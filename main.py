"""
Comparison of Pauli string manipulation libraries
"""
import subprocess
from time import perf_counter
from random import choice
from src.paulie import *
from src.stim import *
from src.pauliarray import *

def is_julia_installed()->bool:
    """ 
    Checking if Julia is installed
    Returns:
         bool
         True if Julia is installed

    """
    try:
        result = subprocess.run(["julia", "--version"], capture_output=True, text=True, check=True)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False

def is_python_julia_installed()->bool:
    """ 
    Checking if Python Paulistrings Julia is installed
    Returns:
         bool
         True if Python Paulistrings Julia is installed

    """
    try:
        import paulistrings as ps
        H = ps.Operator(1)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False


def get_random(n_qubits: int) -> str:
    """ 
    Get random Pauli String for n_qubits
    Args:
         n_qubits (int): Number of qubits
    Returns:
         str
         Random Pauli string

    """
    return''.join([choice("IXYZ") for _ in range(n_qubits)])

def get_random_list(n_qubits:int, length: int) -> list[str]:
    """ 
    Get random list of Pauli strings of length `length` for `n_qubits`
    Args:
         n_qubits (int): Number of qubits
         length (int): List size
    Returns:
         list[str]
         A list of random Pauli string

    """
    return [get_random(n_qubits) for _ in range(length)]

def append_paulistring_jl(paulistring_libs: list[dict])->list[dict]:
    """
    Adding the PauliString library in Julia, if it is installed.
    Args:
        paulistring_libs (list[dict]): List for calling library functions
    Returns:
        list[dict]
        List for calling library functions
    """
    if not is_julia_installed:
        return paulistring_libs

    from src.paulistring_jl import (get_paulistring_jl_list,
        check_paulistring_jl_commutes_with,
        check_paulistring_jl_multiply)
    paulistring_libs.append({
        'name': 'julia paulistring',
        'build': get_paulistring_jl_list,
        'commutes_with': check_paulistring_jl_commutes_with,
        'multiply': check_paulistring_jl_multiply,
    })
    return paulistring_libs

def append_python_paulistring_jl(paulistring_libs: list[dict])->list[dict]:
    """
    Adding the Python PauliString library in Julia, if it is installed.
    Args:
        paulistring_libs (list[dict]): List for calling library functions
    Returns:
        list[dict]
        List for calling library functions
    """
    if not is_python_julia_installed():
        return paulistring_libs

    from src.paulistrings import (get_python_paulistring_jl_list,
        check_python_paulistring_jl_commutes_with,
        check_python_paulistring_jl_multiply)
    paulistring_libs.append({
        'name': 'python julia paulistring',
        'build': get_python_paulistring_jl_list,
        'commutes_with': check_python_paulistring_jl_commutes_with,
        'multiply': check_python_paulistring_jl_multiply,
    })
    return paulistring_libs

def get_performance(lib: dict, paulistrings: list[str])->dict:
    """
    Performance calculation
    Args:
         lib (dict): Calling library functions
         paulistrings (list[str]): List of string representations of Pauli strings
    Returns:
          dict
          Call performance
    """
    performance = {}
    start_time = perf_counter()
    g = lib['build'](paulistrings)
    end_time = perf_counter()
    performance['build'] = end_time - start_time
    start_time = perf_counter()
    lib['commutes_with'](g)
    end_time = perf_counter()
    performance['commutes_with'] = end_time - start_time
    start_time = perf_counter()
    lib['multiply'](g)
    end_time = perf_counter()
    performance['multiply'] = end_time - start_time
    return performance

def print_result(n_qubits:int, length: int, paulistring_libs: list[dict]) -> None:
    """
    Print the performance result on the screen.
    Args:
         n_qubits (int): Number of qubits
         length (int): List size
         paulistring_libs (list[dict]): List for calling library functions
    """
    print(f"Performance for {n_qubits} qubits (lenght of list is {length})")
    for lib in paulistring_libs:
        print(f"library: {lib['name']} | build: {lib['performance']['build']: 0.4f} sec | commutes_with: {lib['performance']['commutes_with']: 0.4f} sec | multiply: {lib['performance']['multiply']: 0.4f} sec")

def main():
    """
    Comparison of Pauli string manipulation libraries
    """
    paulistring_libs = [
        {'name': 'stim',
         'build': get_stim_list,
         'commutes_with': check_stim_commutes_with,
         'multiply': check_stim_multiply,
        },
        {'name': 'paulie',
         'build': get_paulie_list,
         'commutes_with': check_paulie_commutes_with,
         'multiply': check_paulie_multiply,
        },
        {'name': 'pauliarray',
         'build': get_pauliarray_list,
         'commutes_with': check_pauliarray_commutes_with,
         'multiply': check_pauliarray_multiply,
        },
    ]
    paulistring_libs = append_paulistring_jl(paulistring_libs)
    #paulistring_libs = append_python_paulistring_jl(paulistring_libs)
    n_qubits = 1000
    length = 1000
    paulistrings = get_random_list(n_qubits, length)
    for lib in paulistring_libs:
        lib['performance'] = get_performance(lib, paulistrings)

    print_result(n_qubits, length, paulistring_libs)


if __name__ == "__main__":
    main()
