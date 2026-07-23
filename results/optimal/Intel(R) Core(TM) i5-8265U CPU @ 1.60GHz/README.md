## Processor: Intel(R) Core(TM) i5-8265U CPU @ 1.60GHz

![Dependence of build execution time on the number of qubits](build_1000.png)
![Dependence of commutes_with execution time on the number of qubits](commutes_with_1000.png)
![Dependence of multiply execution time on the number of qubits](multiply_1000.png)

### Performance for 10 qubits (lenght of list is 1000 and number of operations is 499500)<br>
|library                  |build, sec|commutes_with, sec|multiply, sec|
|:----------------------- |:-----:   |:-----:           |:-----:      |
|stim| 0.0015| 0.3480| 0.7925|
|paulie| 0.0012| 0.3182| 0.4634|
|pauliarray| 0.0187| 6.5504| 4.2826|
<br>

### Performance for 100 qubits (lenght of list is 1000 and number of operations is 499500)<br>
|library                  |build, sec|commutes_with, sec|multiply, sec|
|:----------------------- |:-----:   |:-----:           |:-----:      |
|stim| 0.0024| 0.3360| 0.7617|
|paulie| 0.0032| 0.3386| 0.4865|
|pauliarray| 0.0338| 6.5798| 4.3592|
<br>

### Performance for 1000 qubits (lenght of list is 1000 and number of operations is 499500)<br>
|library                  |build, sec|commutes_with, sec|multiply, sec|
|:----------------------- |:-----:   |:-----:           |:-----:      |
|stim| 0.0113| 0.3464| 0.7727|
|paulie| 0.0134| 0.3927| 0.5532|
|pauliarray| 0.2120| 8.5618| 4.9301|
<br>

### Performance for 2000 qubits (lenght of list is 1000 and number of operations is 499500)<br>
|library                  |build, sec|commutes_with, sec|multiply, sec|
|:----------------------- |:-----:   |:-----:           |:-----:      |
|stim| 0.0222| 0.3564| 0.8253|
|paulie| 0.0264| 0.4144| 0.5946|
|pauliarray| 0.4065| 10.1488| 5.2440|
<br>

### Performance for 5000 qubits (lenght of list is 1000 and number of operations is 499500)<br>
|library                  |build, sec|commutes_with, sec|multiply, sec|
|:----------------------- |:-----:   |:-----:           |:-----:      |
|stim| 0.0524| 0.3826| 0.8862|
|paulie| 0.0633| 0.4777| 0.6753|
|pauliarray| 1.0138| 13.7393| 5.6188|
<br>

### Performance for 10000 qubits (lenght of list is 1000 and number of operations is 499500)<br>
|library                  |build, sec|commutes_with, sec|multiply, sec|
|:----------------------- |:-----:   |:-----:           |:-----:      |
|stim| 0.1051| 0.4391| 0.9835|
|paulie| 0.1263| 0.5565| 0.7587|
|pauliarray| 2.0236| 19.9972| 6.9133|
<br>

