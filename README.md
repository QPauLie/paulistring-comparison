# paulistring-comparison
Performance comparison of Pauli string manipulation libraries
<br>
The following libraries are included in the comparison:
<br>
Stim: https://github.com/quantumlib/Stim<br>
Paulie: https://github.com/QPauLie/PauLie<br>
PauliArray: https://github.com/algolab-quantique/pauliarray<br>
PauliString.jl: https://github.com/nicolasloizeau/PauliStrings.jl<br>

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

