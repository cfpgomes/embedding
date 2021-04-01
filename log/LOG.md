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

![N8](\A1\N8.png "N8")
![N16](\A1\N16.png "N16")
![N32](\A1\N32.png "N32")
![N64](\A1\N64.png "N64")

As expected, the epsilon indicator increases with the N value.

However, during those executions, dwave's problem inspector warned that the chains were too weak, and that, in the case of N=64, all samples had broken chains. Based on this warning, we decided to execute scenario B1, changing the original order of scenarios.

## Scenario B1

Looking at the percent of chain breaks in scenario A1, we have the following boxplots:

Fazer