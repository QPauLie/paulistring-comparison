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

build: Time to create an array of length 1000 with n_qubits = 1000<br>
commutes_with: Pairwise commutativity check<br>
multiply: Pairwise multiplication<br>

#### Computer: Intel Core i5-8265U 1.60 GHz/8Gb

Performance for 1000 qubits (lenght of list is 1000)<br>
library: stim | build:  0.0149 sec | commutes_with:  0.3723 sec | multiply:  0.8251 sec<br>
library: paulie | build:  0.4304 sec | commutes_with:  0.3945 sec | multiply:  0.5620 sec<br>
library: pauliarray | build:  0.2201 sec | commutes_with:  9.2504 sec | multiply:  5.8017 sec<br>
library: julia paulistring | build:  4.2598 sec | commutes_with:  4.9675 sec | multiply:  8.8966 sec<br>

Performance for 10 qubits (lenght of list is 1000)<br>
library: stim | build:  0.0038 sec | commutes_with:  0.2350 sec | multiply:  0.5794 sec<br>
library: paulie | build:  0.0077 sec | commutes_with:  0.2978 sec | multiply:  0.4490 sec<br>
library: pauliarray | build:  0.0419 sec | commutes_with:  5.8926 sec | multiply:  3.9369 sec<br>
library: julia paulistring | build:  2.2405 sec | commutes_with:  5.3270 sec | multiply:  6.9090 sec<br>
library: python julia paulistring | build:  0.0005 sec | commutes_with:  8.6245 sec | multiply:  9.4381 sec<br>

#### Computer: Intel Core i9-14900KF 6.0GHz (24 cores)/64GB<br>

Performance for 1000 qubits (lenght of list is 1000)<br>
library: stim | build:  0.0100 sec | commutes_with:  0.1180 sec | multiply:  0.2801 sec<br>
library: paulie | build:  0.1464 sec | commutes_with:  0.1769 sec | multiply:  0.2461 sec<br>
library: pauliarray | build:  0.0948 sec | commutes_with:  3.3331 sec | multiply:  1.9737 sec<br>
library: julia paulistring | build:  2.5861 sec | commutes_with:  2.3711 sec | multiply:  4.0043 sec<br>


