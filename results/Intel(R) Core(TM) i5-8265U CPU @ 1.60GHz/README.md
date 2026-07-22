## Processor: Intel(R) Core(TM) i5-8265U CPU @ 1.60GHz
### Performance for 10 qubits (lenght of list is 1000 and number of operations is 499500)<br>
|library                  |build, sec|commutes_with, sec|multiply, sec|
|:----------------------- |:-----:   |:-----:           |:-----:      |
|stim| 0.0049| 0.2553| 0.5696|
|paulie| 0.0202| 0.3027| 0.4692|
|pauliarray| 0.0223| 11.7410| 4.9024|
|julia paulistring| 2.4812| 6.6090| 5.9600|
<br>

### Performance for 100 qubits (lenght of list is 1000 and number of operations is 499500)<br>
|library                  |build, sec|commutes_with, sec|multiply, sec|
|:----------------------- |:-----:   |:-----:           |:-----:      |
|stim| 0.0099| 0.2754| 0.6197|
|paulie| 0.0333| 0.3271| 0.5070|
|pauliarray| 0.0383| 6.2206| 4.2859|
|julia paulistring| 0.1828| 17.0697| 7.2811|
<br>

### Performance for 1000 qubits (lenght of list is 1000 and number of operations is 499500)<br>
|library                  |build, sec|commutes_with, sec|multiply, sec|
|:----------------------- |:-----:   |:-----:           |:-----:      |
|stim| 0.1367| 0.2995| 0.6763|
|paulie| 0.3949| 0.4491| 0.6022|
|pauliarray| 0.4619| 8.8747| 5.5975|
|julia paulistring| 5.8880| 67.8186| 134.9384|
<br>

