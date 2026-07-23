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

Results for various processors are located in the `results` folder.
The `paulie` library performs best on multiplication operations. It slightly trails the `stim` library in the commutativity check and shows lackluster results when instantiating `PauliString` objects. This poor instantiation performance stems from the conversion of strings to a binary format within the `bitarray` library, as the process relies on a Python callback. To improve performance, a function needs to be added to `bitarray` that handles the conversion from string to bit representation internally; a commutativity check function should also be added to `bitarray`.


build: Time to create an array of length 1000 with n_qubits = 1000<br>
commutes_with: Pairwise commutativity check<br>
multiply: Pairwise multiplication<br>

#### Computer: Intel Core i5-8265U 1.60 GHz/8Gb

Performance for 1000 qubits (lenght of list is 1000)<br>
|library           |build, sec|commutes_with, sec|multiply, sec|
|:---------------- |:-----:   |:-----:           |:-----:      |
|stim              |0.0149    |0.3723            |0.8251       |
|paulie            |0.4304    |0.3945            |0.5620       |
|pauliarray        |0.2201    |9.2504            |5.8017       |
|julia paulistring |4.2598    |4.9675            |8.8966       |
<br>

Performance for 10 qubits (lenght of list is 1000)<br>
|library                  |build, sec|commutes_with, sec|multiply, sec|
|:----------------------- |:-----:   |:-----:           |:-----:      |
|stim                     |0.0038    |0.2350            |0.5794       |
|paulie                   |0.0077    |0.2978            |0.4490       |
|pauliarray               |0.0419    |5.8926            |3.9369       |
|julia paulistring        |2.2405    |5.3270            |6.9090       |
|python julia paulistring |0.0005    |8.6245            |9.4381       |
<br>

#### Computer: Intel Core i9-14900KF 6.0GHz (24 cores)/64GB

Performance for 1000 qubits (lenght of list is 1000)<br>
|library           |build, sec|commutes_with, sec|multiply, sec|
|:---------------- |:-----:   |:-----:           |:-----:      |
|stim              |0.0100    |0.1180            |0.2801       |
|paulie            |0.1464    |0.1769            |0.2461       |
|pauliarray        |0.0948    |3.3331            |1.9737       |
|julia paulistring |2.5861    |2.3711            |4.0043       |
<br>


Performance for 10 qubits (lenght of list is 1000)<br>
|library                  |build, sec|commutes_with, sec|multiply, sec|
|:----------------------- |:-----:   |:-----:           |:-----:      |
|stim                     |0.0008    |0.1136            |0.2555       |
|paulie                   |0.0023    |0.1173            |0.2077       |
|pauliarray               |0.0085    |2.5827            |1.7516       |
|julia paulistring        |1.4010    |2.3578            |1.6733       |
|python julia paulistring |0.0000    |6.8815            |4.7550       |
<br>

