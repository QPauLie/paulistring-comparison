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
uv run python main.py
```

### PauliString Julia
To run tests for the PauliString.jl package, Julia must be installed on your computer. Additionally, Python must be installed from the official Python website; if installed via the Microsoft Windows Store, it will not work with the Julia package, as the Windows Store version of Python is subject to specific security restrictions that prevent it from invoking Julia.

### Results

build: Time to create an array of length 1000 with n_qubits = 1000<br>
commutes_with: Pairwise commutativity check<br>
multiply: Pairwise multiplication<br>

#### Computer: Intel Core i5-8265U 1.60 GHz/8Gb

Performance for 1000 qubits (lenght of list is 1000)<br>
library: stim | build:  0.0149 sec | commutes_with:  0.3723 sec | multiply:  0.8251 sec<br>
library: paulie | build:  0.4304 sec | commutes_with:  0.3945 sec | multiply:  0.5620 sec<br>
library: pauliarray | build:  0.2201 sec | commutes_with:  9.2504 sec | multiply:  5.8017 sec<br>
library: julia paulistring | build:  4.2598 sec | commutes_with:  4.9675 sec | multiply:  8.8966 sec<br>

#### Computer: Intel Core i9-14900KF 6.0GHz (24 cores)/64GB<br>

Performance for 1000 qubits (lenght of list is 1000)<br>
library: stim | build:  0.0100 sec | commutes_with:  0.1180 sec | multiply:  0.2801 sec<br>
library: paulie | build:  0.1464 sec | commutes_with:  0.1769 sec | multiply:  0.2461 sec<br>
library: pauliarray | build:  0.0948 sec | commutes_with:  3.3331 sec | multiply:  1.9737 sec<br>
library: julia paulistring | build:  2.5861 sec | commutes_with:  2.3711 sec | multiply:  4.0043 sec<br>
