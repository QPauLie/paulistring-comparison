"""
Comparison of Pauli string manipulation libraries
"""
import subprocess
import cpuinfo
from pathlib import Path
from time import perf_counter
from random import choice
import matplotlib.pyplot as plt
import numpy as np
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
        'performance': []
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
        'performance': []
    })
    return paulistring_libs

def get_performance(n_qubits: int,lib: dict, paulistrings: list[str])->dict:
    """
    Performance calculation
    Args:
         n_qubits (int): Number of qubits
         lib (dict): Calling library functions
         paulistrings (list[str]): List of string representations of Pauli strings
    Returns:
          dict
          Call performance
    """
    performance = {'n_qubits': n_qubits}
    start_time = perf_counter()
    g = lib['build'](paulistrings)
    end_time = perf_counter()
    performance['build'] = end_time - start_time
    performance['n_build'] = len(g)
    start_time = perf_counter()
    n = lib['commutes_with'](g)
    end_time = perf_counter()
    performance['commutes_with'] = end_time - start_time
    performance['n_commutes_with'] = n
    start_time = perf_counter()
    n = lib['multiply'](g)
    end_time = perf_counter()
    performance['multiply'] = end_time - start_time
    performance['n_multiply'] = n
    return performance

def get_processor_info():
    """
       Get processor info
    """
    cpu_data = cpuinfo.get_cpu_info()
    return cpu_data['brand_raw']


def print_result(paulistring_libs: list[dict], list_n_qubits: list[int],
    list_length: list[int]) -> None:
    """
    Print the performance result on the screen.
    Args:
         paulistring_libs (list[dict]): List for calling library functions
         list_n_qubits (list[int]): List of qubit counts
         list_length (list[int]): List of Pauli string numbers
    """

    processor = get_processor_info()
    folder = f"./results/{processor}"
    Path(folder).mkdir(parents=True, exist_ok=True)

    def plot_result(paulistring_libs: list[dict], list_n_qubits: list[int],
        length: int, operation: str) -> None:
        """
        Print the performance result on the screen.
        Args:
            paulistring_libs (list[dict]): List for calling library functions
            list_n_qubits (list[int]): List of qubit counts
            length (int): Length of Pauli string numbers
            operation (str): Operation
        """
        def find_performance(length, paulistring_libs, name, operation):
            return np.array([performance[operation] for lib in paulistring_libs for performance in lib['performance']  
                if performance['n_build'] == length and lib['name'] == name])

        plt.figure(figsize=(10, 6))
        qubits = np.array(list_n_qubits)
        for lib in paulistring_libs:
            results = find_performance(length, paulistring_libs, lib['name'], operation)
            plt.plot(qubits, results, marker='x', linewidth=2, label=lib['name'])
        plt.title(f"Dependence of {operation} execution time on the number of qubits", fontsize=14, fontweight='bold', pad=15)
        plt.xlabel('Qubits', fontsize=12)
        plt.ylabel('Time (sec)', fontsize=12)
        plt.grid(True, linestyle="--", alpha=0.6) 
        plt.legend(fontsize=11, loc='upper left')
        filename = f"{folder}/{operation}_{length}.png"
        plt.savefig(filename, dpi=300, bbox_inches='tight')
        plt.close()
        return f"![Dependence of {operation} execution time on the number of qubits]({operation}_{length}.png)"

    def find_libs(length, n_qubits, paulistring_libs):
        return [{'name' : lib['name'],
                 'operations': performance['n_commutes_with'],
                 'performance': performance.copy()
                } for lib in paulistring_libs for performance in lib['performance']  
                if performance['n_build'] == length and performance['n_qubits'] == n_qubits]

    with open(f"{folder}/README.md", "w") as f:
        print(f"## Processor: {processor}", file=f)
        print("", file=f)
        for length in list_length:
            build_plot = plot_result(paulistring_libs, list_n_qubits, length, 'build')
            print(f"{build_plot}", file=f)
            commutes_with_plot = plot_result(paulistring_libs, list_n_qubits, length, 'commutes_with')
            print(f"{commutes_with_plot}", file=f)
            multiply_plot = plot_result(paulistring_libs, list_n_qubits, length, 'multiply')
            print(f"{multiply_plot}", file=f)
            print("", file=f)

            for n_qubits in list_n_qubits:
                libs = find_libs(length, n_qubits, paulistring_libs)
                if len(libs) == 0:
                    continue
                print(f"### Performance for {n_qubits} qubits (lenght of list is {length} and number of operations is {libs[0]['operations']})<br>", file=f)
                print('|library                  |build, sec|commutes_with, sec|multiply, sec|', file=f)
                print('|:----------------------- |:-----:   |:-----:           |:-----:      |', file=f)
                for lib in libs:
                    print(f"|{lib['name']}|{lib['performance']['build']: 0.4f}|{lib['performance']['commutes_with']: 0.4f}|{lib['performance']['multiply']: 0.4f}|", file=f)
                print("<br>", file=f)
                print("", file=f)

def main():
    """
    Comparison of Pauli string manipulation libraries
    """
    paulistring_libs = [
        {'name': 'stim',
         'build': get_stim_list,
         'commutes_with': check_stim_commutes_with,
         'multiply': check_stim_multiply,
         'performance': []
        },
        {'name': 'paulie',
         'build': get_paulie_list,
         'commutes_with': check_paulie_commutes_with,
         'multiply': check_paulie_multiply,
         'performance': []
        },
        {'name': 'pauliarray',
         'build': get_pauliarray_list,
         'commutes_with': check_pauliarray_commutes_with,
         'multiply': check_pauliarray_multiply,
         'performance': []
        },
    ]
    paulistring_libs = append_paulistring_jl(paulistring_libs)
    #paulistring_libs = append_python_paulistring_jl(paulistring_libs)

    list_n_qubits = [10, 100, 1000, 2000, 5000, 10000]
    list_n_qubits = [10, 100, 1000]
    list_length = [1000]

    for length in list_length:
        for n_qubits in list_n_qubits:
            paulistrings = get_random_list(n_qubits, length)
            for lib in paulistring_libs:
                try:
                    lib['performance'].append(get_performance(n_qubits, lib, paulistrings))
                except RuntimeError:
                    continue
    #print(f"{paulistring_libs}")
    print_result(paulistring_libs, list_n_qubits, list_length)


if __name__ == "__main__":
    main()
