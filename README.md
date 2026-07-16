# paulistring-comparison
Performance comparison of Pauli string manipulation libraries

The following libraries are included in the comparison:

Stim: https://github.com/quantumlib/Stim
Paulie: https://github.com/QPauLie/PauLie
PauliArray: https://github.com/algolab-quantique/pauliarray
PauliString.jl: https://github.com/nicolasloizeau/PauliStrings.jl

### Installation
```
git clone https://github.com/QPauLie/paulistring-comparison.git
cd paulistring-comparison
uv sync
```
### Running
```
uv run python main
```

### PauliString Julia
To run tests for the PauliString.jl package, Julia must be installed on your computer. Additionally, Python must be installed from the official Python website; if installed via the Microsoft Windows Store, it will not work with the Julia package, as the Windows Store version of Python is subject to specific security restrictions that prevent it from invoking Julia.

