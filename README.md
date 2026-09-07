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



