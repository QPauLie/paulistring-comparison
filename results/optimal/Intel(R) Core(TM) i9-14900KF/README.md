## Processor: Intel(R) Core(TM) i9-14900KF

![Dependence of build execution time on the number of qubits](build_1000.png)
![Dependence of commutes_with execution time on the number of qubits](commutes_with_1000.png)
![Dependence of multiply execution time on the number of qubits](multiply_1000.png)

### Performance for 10 qubits (lenght of list is 1000 and number of operations is 499500)<br>
|library                  |build, sec|commutes_with, sec|multiply, sec|
|:----------------------- |:-----:   |:-----:           |:-----:      |
|stim| 0.0006| 0.1166| 0.2739|
|paulie| 0.0007| 0.1132| 0.2020|
|pauliarray| 0.0074| 3.0538| 1.7496|
<br>

### Performance for 100 qubits (lenght of list is 1000 and number of operations is 499500)<br>
|library                  |build, sec|commutes_with, sec|multiply, sec|
|:----------------------- |:-----:   |:-----:           |:-----:      |
|stim| 0.0013| 0.1168| 0.2761|
|paulie| 0.0013| 0.1155| 0.2081|
|pauliarray| 0.0150| 2.5904| 2.0159|
<br>

### Performance for 1000 qubits (lenght of list is 1000 and number of operations is 499500)<br>
|library                  |build, sec|commutes_with, sec|multiply, sec|
|:----------------------- |:-----:   |:-----:           |:-----:      |
|stim| 0.0098| 0.1191| 0.2820|
|paulie| 0.0087| 0.1836| 0.2441|
|pauliarray| 0.0941| 3.2868| 2.2828|
<br>

### Performance for 2000 qubits (lenght of list is 1000 and number of operations is 499500)<br>
|library                  |build, sec|commutes_with, sec|multiply, sec|
|:----------------------- |:-----:   |:-----:           |:-----:      |
|stim| 0.0190| 0.1204| 0.2847|
|paulie| 0.0168| 0.2309| 0.2556|
|pauliarray| 0.1819| 3.5961| 2.0377|
<br>

### Performance for 5000 qubits (lenght of list is 1000 and number of operations is 499500)<br>
|library                  |build, sec|commutes_with, sec|multiply, sec|
|:----------------------- |:-----:   |:-----:           |:-----:      |
|stim| 0.0469| 0.1321| 0.3122|
|paulie| 0.0413| 0.4092| 0.3242|
|pauliarray| 0.4451| 4.8056| 2.2360|
<br>

### Performance for 10000 qubits (lenght of list is 1000 and number of operations is 499500)<br>
|library                  |build, sec|commutes_with, sec|multiply, sec|
|:----------------------- |:-----:   |:-----:           |:-----:      |
|stim| 0.0936| 0.1407| 0.4136|
|paulie| 0.0820| 0.5774| 0.3549|
|pauliarray| 0.8858| 6.8689| 2.5959|
<br>

