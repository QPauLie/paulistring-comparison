## Processor: Intel(R) Core(TM) i5-8265U CPU @ 1.60GHz

![Dependence of build execution time on the number of qubits](build_1000.png)
![Dependence of commutes_with execution time on the number of qubits](commutes_with_1000.png)
![Dependence of multiply execution time on the number of qubits](multiply_1000.png)

### Performance for 10 qubits (lenght of list is 1000 and number of operations is 499500)<br>
|library                  |build, sec|commutes_with, sec|multiply, sec|
|:----------------------- |:-----:   |:-----:           |:-----:      |
|stim| 0.0018| 0.2880| 0.6878|
|paulie| 0.0061| 0.3215| 0.4856|
|pauliarray| 0.0223| 5.7890| 3.8077|
<br>

### Performance for 100 qubits (lenght of list is 1000 and number of operations is 499500)<br>
|library                  |build, sec|commutes_with, sec|multiply, sec|
|:----------------------- |:-----:   |:-----:           |:-----:      |
|stim| 0.0021| 0.2408| 0.5940|
|paulie| 0.0267| 0.3288| 0.4860|
|pauliarray| 0.0346| 5.7752| 4.6209|
<br>

### Performance for 1000 qubits (lenght of list is 1000 and number of operations is 499500)<br>
|library                  |build, sec|commutes_with, sec|multiply, sec|
|:----------------------- |:-----:   |:-----:           |:-----:      |
|stim| 0.0144| 0.2708| 0.6053|
|paulie| 0.3376| 0.3936| 0.5581|
|pauliarray| 0.2530| 7.7185| 4.4682|
<br>

### Performance for 2000 qubits (lenght of list is 1000 and number of operations is 499500)<br>
|library                  |build, sec|commutes_with, sec|multiply, sec|
|:----------------------- |:-----:   |:-----:           |:-----:      |
|stim| 0.0267| 0.2590| 0.6001|
|paulie| 0.6193| 0.4425| 0.5325|
|pauliarray| 0.4076| 8.3049| 4.6201|
<br>

### Performance for 5000 qubits (lenght of list is 1000 and number of operations is 499500)<br>
|library                  |build, sec|commutes_with, sec|multiply, sec|
|:----------------------- |:-----:   |:-----:           |:-----:      |
|stim| 0.0636| 0.2683| 0.6459|
|paulie| 1.5683| 0.5573| 0.5730|
|pauliarray| 0.9928| 11.1902| 5.0880|
<br>

### Performance for 10000 qubits (lenght of list is 1000 and number of operations is 499500)<br>
|library                  |build, sec|commutes_with, sec|multiply, sec|
|:----------------------- |:-----:   |:-----:           |:-----:      |
|stim| 0.1246| 0.2949| 0.8261|
|paulie| 3.1632| 1.0319| 0.8784|
|pauliarray| 2.1628| 15.2195| 5.7928|
<br>

