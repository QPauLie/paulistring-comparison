# paulistring-comparison
Performance comparison of Pauli string manipulation libraries
<br>
The following libraries are included in the comparison:
<br>
Stim: https://github.com/quantumlib/Stim<br>
Paulie: https://github.com/QPauLie/PauLie<br>
PauliArray: https://github.com/algolab-quantique/pauliarray<br>
PauliString.jl (juliacall): https://github.com/nicolasloizeau/PauliStrings.jl<br>
PauliStrings (Python version of PauliStrings.jl): https://github.com/nicolasloizeau/PauliStrings.py
Pauliengine: https://github.com/tequilahub/pauliengine

### Installation
```
git clone https://github.com/QPauLie/paulistring-comparison.git
cd paulistring-comparison
uv sync --link-mode=copy
```
### Running
```
uv run python main.py
```

### PauliString Julia
#### Via juliacall
To run tests for the PauliString.jl package, Julia must be installed on your computer. Additionally, Python must be installed from the official Python website; if installed via the Microsoft Windows Store, it will not work with the Julia package, as the Windows Store version of Python is subject to specific security restrictions that prevent it from invoking Julia.

#### Via PauliString python library
To build the library on Windows, you need to use WSL, as the PauliStrings library does not compile.<br>

To compile, the necessary libraries must be installed. If they are not, install them.<br>
```
sudo apt update && sudo apt install -y build-essential python3-dev
```
PauliStrings does not work with long Pauli strings; it throws an error for 1000 qubits.<br>
OverflowError: Python int too large to convert to C long<br>

### Results

PauliString.jl (juliacall)
PauliStrings (Python version of PauliStrings.jl)
Comparison results have been excluded, as they are an order of magnitude slower than the other packages when using Python.

The tests were run on two processors. The results are available at the link.
<br>
####Intel(R) Core(TM) i5-8265U
<p align="center">
  <img src="results/statistic/Intel(R)%20Core(TM)%20i5-8265U%20CPU%20%40%201.60GHz/2026-09-06_18-39-26/build_1000.png" alt="Dependence of build execution time on the number of qubits" width="32%">
  <img src="results/statistic/Intel(R)%20Core(TM)%20i5-8265U%20CPU%20%40%201.60GHz/2026-09-06_18-39-26/commutes_with_1000.png" alt="Dependence of commutes_with execution time on the number of qubits" width="32%">
  <img src="results/statistic/Intel(R)%20Core(TM)%20i5-8265U%20CPU%20%40%201.60GHz/2026-09-06_18-39-26/multiply_1000.png" alt="Dependence of multiply execution time on the number of qubits" width="32%">
</p>
<br>
https://github.com/QPauLie/paulistring-comparison/tree/main/results/statistic/Intel(R)%20Core(TM)%20i5-8265U%20CPU%20%40%201.60GHz/2026-09-06_18-39-26
<br>
####Intel(R) Core(TM) i9-14900KF
<p align="center">
  <img src="results/statistic/Intel(R)%20Core(TM)%20i9-14900KF/2026-09-06_21-07-52/build_1000.png" alt="Dependence of build execution time on the number of qubits" width="32%">
  <img src="results/statistic/Intel(R)%20Core(TM)%20i9-14900KF/2026-09-06_21-07-52/commutes_with_1000.png" alt="Dependence of commutes_with execution time on the number of qubits" width="32%">
  <img src="results/statistic/Intel(R)%20Core(TM)%20i9-14900KF/2026-09-06_21-07-52/multiply_1000.png" alt="Dependence of multiply execution time on the number of qubits" width="32%">
</p>
<br>

https://github.com/QPauLie/paulistring-comparison/tree/main/results/statistic/Intel(R)%20Core(TM)%20i9-14900KF/2026-09-06_21-07-52


