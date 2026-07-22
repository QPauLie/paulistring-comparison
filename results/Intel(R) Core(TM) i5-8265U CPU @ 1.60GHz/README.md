## Processor: Intel(R) Core(TM) i5-8265U CPU @ 1.60GHz
### Performance for 10 qubits (lenght of list is 1000 and number of operations is 499500)<br>
|library                  |build, sec|commutes_with, sec|multiply, sec|
|:----------------------- |:-----:   |:-----:           |:-----:      |
|stim| 0.0023| 0.2690| 0.6572|
|paulie| 0.0075| 0.3391| 0.4702|
|pauliarray| 0.0205| 10.7189| 4.8528|
|julia paulistring| 2.7511| 5.4661| 6.6893|
<br>
### Performance for 100 qubits (lenght of list is 1000 and number of operations is 499500)<br>
|library                  |build, sec|commutes_with, sec|multiply, sec|
|:----------------------- |:-----:   |:-----:           |:-----:      |
|stim| 0.0078| 0.4661| 1.1320|
|paulie| 0.0446| 0.4791| 0.5737|
|pauliarray| 0.0406| 6.2294| 4.1782|
|julia paulistring| 0.1086| 5.7707| 15.3951|
<br>
### Performance for 1000 qubits (lenght of list is 1000 and number of operations is 499500)<br>
|library                  |build, sec|commutes_with, sec|multiply, sec|
|:----------------------- |:-----:   |:-----:           |:-----:      |
|stim| 0.1162| 0.2681| 0.7193|
|paulie| 0.3616| 0.4060| 0.5459|
|pauliarray| 0.4175| 8.3371| 5.3474|
|julia paulistring| 5.2451| 84.1380| 117.8570|
<br>
