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
from datetime import datetime


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

def get_performance(n_qubits: int, lib: dict, paulistrings: list[str])->dict:
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
    performance = {}
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

def get_folder(processor: str):
    """
    Get folder for results
    """
    now = datetime.now()

    folder_time = now.strftime("%Y-%m-%d_%H-%M-%S")

    folder = f"./results/statistic/{processor}/{folder_time}"
    Path(folder).mkdir(parents=True, exist_ok=True)
    return folder

def output_result(paulistring_libs: list[dict], list_n_qubits: list[int],
    performances: list[dict], n_attemptions:int, length: int) -> None:
    """
    Output the performance result on readme.md.
    Args:
         paulistring_libs (list[dict]): List for calling library functions
         list_n_qubits (list[int]): List of qubit counts
         performances (list[dict]): List of results
    """
    processor = get_processor_info()
    folder = get_folder(processor)

    def get_seria(operation: str, performances: list[dict], library: str, n_qubits: int) -> list[float]:
        """
        """
        return [p["performance"].get(operation) 
            for p in performances if p["library"] == library and p["n_qubits"] == n_qubits
        ]

    def get_statistic(list_data: list[float]) -> dict:
        average = sum(list_data)/len(list_data)
        variance = sum((x - average) ** 2 for x in list_data) / len(list_data)
        std_dev = variance ** 0.5
        return {
            "average": average,
            "std_dev": std_dev
        }


    def get_performance_by_filter(operation: str, performances: list[dict], libraries: str, n_qubits: int):
        return {library: get_seria(operation, performances, library, n_qubits) for library in libraries}
            


#         return [{
#           item["library"]: item["performance"][operation]
#           for item in data
#             if item["n_qubits"] == n_qubits and operation in item["performance"]
#    }]


    def plot_result(paulistring_libs: list[dict], performances: list[dict], list_n_qubits: list[int],
        length: int, operation: str) -> None:
        """
        Print the performance result on the screen.
        Args:
            paulistring_libs (list[dict]): List for calling library functions
            list_n_qubits (list[int]): List of qubit counts
            length (int): Length of Pauli string numbers
            operation (str): Operation
        """


        plt.figure(figsize=(10, 6))
        qubits = np.array(list_n_qubits)
        for lib in paulistring_libs:
            results = [get_statistic(get_seria(operation, performances, lib["name"], n_qubits)) 
                 for n_qubits in list_n_qubits 
            ] 
            y = np.array([r.get("average") for r in results])
            y_err = np.array([r.get("std_dev") for r in results])

            plt.errorbar(qubits, y, yerr=y_err, fmt='-o', capsize=4, linewidth=2, label=lib['name']) #marker='x',

            #results = find_performance(length, paulistring_libs, lib['name'], operation)
            #plt.plot(qubits, results, marker='x', linewidth=2, label=lib['name'])

        plt.yscale('log')
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

    libraries = [lib.get("name") for lib in paulistring_libs]
    with open(f"{folder}/README.md", "w") as f:
        print(f"## Processor: {processor}", file=f)
        print("", file=f)
        build_plot = plot_result(paulistring_libs, performances, list_n_qubits, length, 'build')
        print(f"{build_plot}", file=f)
        commutes_with_plot = plot_result(paulistring_libs, performances, list_n_qubits, length, 'commutes_with')
        print(f"{commutes_with_plot}", file=f)
        multiply_plot = plot_result(paulistring_libs, performances, list_n_qubits, length, 'multiply')
        print(f"{multiply_plot}", file=f)
        print("", file=f)


        headers = "| # | " + " | ".join(libraries) + " |"
        separators = "| :---: | " + " | ".join([":------:"] * len(libraries)) + " |"

        
        list_operations = ["build", "commutes_with", "multiply"]
        for n_qubits in list_n_qubits:
            for operation in list_operations:
                table_rows = [headers, separators]    
                results = get_performance_by_filter(operation, performances, libraries, n_qubits)
                #results = get_performance_by_filter(performances, operation, n_qubits)
                #seria = get_seria(operation, performances, "stim", n_qubits)
                #print(f"seria = {seria}")
                first_library = libraries[0]

                for idx,_ in enumerate(results.get(first_library)):
                    row_cells = [str(idx + 1)]

                    for lib in libraries:
                        value = results.get(lib)[idx]
                        if value is not None:
                            row_cells.append(f"{value:.6f}")
                        else:
                            row_cells.append("-")
                    table_rows.append("| " + " | ".join(row_cells) + " |")

                row_cells_avarage = ["avg"]
                row_cells_std_dev = ["dev"]
                for lib in libraries:
                      list_data = get_seria(operation, performances, lib, n_qubits)
                      stat = get_statistic(list_data) 
                      row_cells_avarage.append(f"{stat.get('average'):.6f}")
                      row_cells_std_dev.append(f"{stat.get('std_dev'):.6f}")
                table_rows.append("| " + " | ".join(row_cells_avarage) + " |")
                table_rows.append("| " + " | ".join(row_cells_std_dev) + " |")
                markdown_table = "\n".join(table_rows)
                print(f"### Performance for {operation} ({n_qubits} qubits and lenght of list is {length}'))<br>", file=f)
                print(markdown_table, file=f)
    with open(f"{folder}/result.csv", "w") as f:
        print(f"#;qubits;operation;library;performance", file=f)
        for operation in list_operations:
            for library in libraries:
                for n_qubits in list_n_qubits:
                    seria = get_seria(operation, performances, library, n_qubits)
                    for idx, item in enumerate(seria):
                        print(f"{idx + 1};{n_qubits};{operation};{library};{item}", file=f)
def main():
    """
    Comparison of Pauli string manipulation libraries
    """
    print(f"start")
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
    #paulistring_libs = append_paulistring_jl(paulistring_libs)
    #paulistring_libs = append_python_paulistring_jl(paulistring_libs)

    list_n_qubits = [10, 100, 1000, 3000, 6000, 8000, 10000, 12000]
    #list_n_qubits = [10, 100, 500, 1000, 2000, 5000]
    length = 10
    n_attemptions = 5
    performances = []
    for attemption in range(0, n_attemptions):
        for n_qubits in list_n_qubits:
            paulistrings = get_random_list(n_qubits, length)
            for lib in paulistring_libs:
                try:
                    performances.append(
                         {
                           "library": lib.get("name"),
                           "n_qubits": n_qubits,
                           "performance": get_performance(n_qubits, lib, paulistrings),
                         }
                    )
                except RuntimeError:
                    continue
    #print(f"{paulistring_libs}")
    output_result(paulistring_libs, list_n_qubits, performances, n_attemptions, length)


if __name__ == "__main__":
    main()
