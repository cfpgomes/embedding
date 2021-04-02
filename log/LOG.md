# Experiment results log.

## Planned order of scenarios

| Scenarios | Parameters     | Week                |
| --------- | -------------- | ------------------- |
| A1        | N              | March 23 - March 29 |
| A2        | B              | March 30 - April 5  |
| A3        | Datasets       | March 30 - April 5  |
| B1        | Chain Strength | April 6 - April 12  |
| B2        | Embedding      | April 13 - April 19 |
| B3        | Shots          | April 20 - April 26 |
| B4        | Annealing      | April 27 - May 3    |

## Actual order of scenarios

| Scenarios | Parameters     | Week                     |
| --------- | -------------- | ------------------------ |
| **A1**    | **N**          | **March 23 - March 29** |
| B1        | Chain Strength | March 30 - April 5       |
| A2        | B              | March 30 - April 5       |
| A3        | Datasets       | April 6 - April 12       |
| B2        | Embedding      | April 13 - April 19      |
| B3        | Shots          | April 20 - April 26      |
| B4        | Annealing      | April 27 - May 3         |

## Sidenotes to research about
- Scenario A1 epsilon values appear to follow a linear trend: y = (x-8) * 0.0142227624 + 1
- Find what is the maximum N value that is supported by dwave

## Scenario A1

We started by experimenting several values of N, in order to find the maximum possible value of N that could be solved in a reasonable time by the classical solver.

The N values are: 8, 16, 32, and 64. P was calculated as P = -q * min_sigma + max_mu

For this scenario, we used the "diversified" dataset and 1000 shots per execution. The q values are listed in the following table:

| N  | q values                                                     | Epsilon Indicator |
| -- | ------------------------------------------------------------ | ----------------- |
| 8  | 0, 11, 20, 54                                                | 1.0               |
| 16 | 0, 2, 6, 100, 500                                            | 1.114             |
| 32 | 0, 0.4, 0.9, 2, 3, 9, 100                                    | 1.340             |
| 64 | 0, 0.2, 0.4, 0.6, 1.1, 1.3, 1.5, 2, 5, 6, 7, 8, 10, 100, 500 | 1.755             |

![N8](C:\Users\Claubit\Documents\GitHub\embedding\log\A1\N8.png "N8")
![N16](C:\Users\Claubit\Documents\GitHub\embedding\log\A1\N16.png "N16")
![N32](C:\Users\Claubit\Documents\GitHub\embedding\log\A1\N32.png "N32")
![N64](C:\Users\Claubit\Documents\GitHub\embedding\log\A1\N64.png "N64")

### Key Takeaways:

As expected, the epsilon indicator increases with the N value. However, during those executions, dwave's problem inspector warned that the chains were too weak, and that, in the case of N=64, all samples had broken chains. Based on this warning, we decided to immediately execute scenario B1, changing the original order of scenarios.

## Scenario B1

Looking at the percent of chain breaks in scenario A1, we have the following boxplots:


We have three tables, one for the epsilon indicator, one for the percentages of valid solutions, and one for the percentages of chain breaks.

Starting with the percent of chain breaks:

| Chain strength | N8    | N16   | N32   | N64   |
| -------------- | ----- | ----- | ----- | ----- |
| default value  |       |       |       |       |
| 0.125 * maxAbs |       |       |       |       |
| 0.250 * maxAbs |       |       |       |       |
| 0.375 * maxAbs |       |       |       |       |
| 0.500 * maxAbs |       |       |       |       |
| 0.625 * maxAbs |       |       |       |       |
| 0.750 * maxAbs |       |       |       |       |
| 0.875 * maxAbs |       |       |       |       |
| 1.000 * maxAbs |       |       |       |       |
| 1.125 * maxAbs |       |       |       |       |
| 1.250 * maxAbs |       |       |       |       |
| 1.375 * maxAbs |       |       |       |       |
| 1.500 * maxAbs |       |       |       |       |


Then, we obtained the following epsilon indicators:

| Chain strength | N8    | N16   | N32   | N64   |
| -------------- | ----- | ----- | ----- | ----- |
| default value  | 1.000 | **1.114** | 1.340 | 1.755 |
| 0.125 * maxAbs | 1.368 | 6.672 | 1.426 | 1.640 |
| 0.250 * maxAbs | 1.000 | 1.167 | **1.245** | 1.504 |
| 0.375 * maxAbs | 1.000 | 1.176* | 1.275 | 1.429 |
| 0.500 * maxAbs | 1.000 | 1.177 | 1.284 | 1.524 |
| 0.625 * maxAbs | 1.000 | 1.208 | 1.325 | **1.388** |
| 0.750 * maxAbs | 1.000 | 1.164 | 1.364 | 1.423 |
| 0.875 * maxAbs | 1.000 | 1.208 | 1.372 | 1.358 |
| 1.000 * maxAbs | 1.000 | 1.140 | 1.567 | 1.520 |
| 1.125 * maxAbs | 1.000 | 1.182 | 1.350 | 1.421 |
| 1.250 * maxAbs | 1.000 | 1.218 | 1.457 | 1.518 |
| 1.375 * maxAbs | 1.000 | 1.130 | 1.462 | 1.488 |
| 1.500 * maxAbs | 1.000 | 1.182 | 1.445 | 1.583 |

* Interestingly, this iteration got 3 of the 5 optimal solutions.

Finally, we obtained the following percentages of valid solutions:

| Chain strength | N8    | N16   | N32   | N64   |
| -------------- | ----- | ----- | ----- | ----- |
| default value  | 0.877 | **0.688** | 0.121 | 0.094 |
| 0.125 * maxAbs | 0.001 | 0.002 | 0.076 | 0.205 |
| 0.250 * maxAbs | **0.934** | 0.622 | **0.395** | **0.243** |
| 0.375 * maxAbs | 0.848 | 0.543 | 0.325 | 0.220 |
| 0.500 * maxAbs | 0.781 | 0.485 | 0.299 | 0.186 |
| 0.625 * maxAbs | 0.703 | 0.444 | 0.261 | 0.172 |
| 0.750 * maxAbs | 0.665 | 0.388 | 0.252 | 0.170 |
| 0.875 * maxAbs | 0.630 | 0.406 | 0.242 | 0.163 |
| 1.000 * maxAbs | 0.598 | 0.366 | 0.235 | 0.151 |
| 1.125 * maxAbs | 0.594 | 0.370 | 0.219 | 0.148 |
| 1.250 * maxAbs | 0.556 | 0.342 | 0.223 | 0.129 |
| 1.375 * maxAbs | 0.540 | 0.330 | 0.212 | 0.136 |
| 1.500 * maxAbs | 0.512 | 0.310 | 0.198 | 0.138 |

### Key Takeaways:

