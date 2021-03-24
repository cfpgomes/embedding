# Embedding Repository

## Definitions to remember
- **Attribute** - A characteristic of an object (person, thing, etc.).
- **Variable** - A logical set of attributes. May be dependent or independent.
- **Dependent Variable** - Their values are studied under the supposition or hypothesis that they depend, by some law or rule (e.g., by a mathematical function), on the values of other variables.
- **Independent Variable** - Not seen as depending on any other variable in the scope of the experiment in question. Some common independent variables are time, space, density, mass, fluid flow rate, and previous values of some observed value of interest (e.g. human population size) to predict future values (the dependent variable).
- **Parameters** - Changes relationships between variables in a model of a system. For example, in calculating income based on wage and hours worked (income equals wage multiplied by hours worked), it is typically assumed that the number of hours worked is easily changed, but the wage is more static. This makes wage a parameter, hours worked an independent variable, and income a dependent variable.

## Goal
Perform an empirical study on how variables affect the results in a D-Wave system, in a POP context.

## Parameters and Independent Variables
### POP formulation parameters
- **P** - Penalty factor
- **q** - Risk appetite

### POP formulation independent variables
- **N** - Universe size (number of assets to choose from) - 
- **B** - Budget (number of assets to choose)
- **mu** - Expected return
- **sigma** - Covariance matrix

### D-Wave system parameters
- **Chain Strength** - Non-negative float numbers between system limits.
- **Embedding** - Normal or Clique, experimentar third-party e custom
- **Shots** - Positive integers below system limit.
- **Annealing** - Standard, Pause, Quench, or Reverse Annealing
- **Annealing time** - Sets the duration (in microseconds) of quantum annealing time, per read.

- Ising só pra eventualmente comparar

## Calendar

Weeks start on Tuesday and end on Monday.

- **March 23 - March 29** - Experiencia Preliminar, P formulation and datasets, Scenario 1 - N
- **March 30 - April 5** - Scenario 2 and 3 - B e depois datasets
- **April 6 - April 12** - Scenario 4 - Chain Strength
- **April 13 - April 19** - Scenario 5 - Ver de novo embedding and Embedding
- **April 20 - April 26** - Scenario 6 - Shots and Annealing
- **April 27 - May 3** - Scenario 7 - Annealing and Annealing Time

- **May 4 - May 10** - Scenario 8 - ???

- **May 11 - May 17** - Writing
- **May 18 - May 24** - Writing
- **May 25 - May 31** - Writing
- **June 1 - June 7** - Writing
- **June 8 - June 14** - Writing
- **June 15 - June 21** - Writing
- **June 22 - June 28** - Writing

## Anything else

Encontrar formula para P - done

Definir 3 datasets  reais. 

Como seleccionar ponto de cada execução (que tem vários shots) - done



1º Fixar todos menos datasets. (usar implementação default)

2º Fixar Tudo menos N B (escolher melhores P q e fixar dataset real normal)

3º depois o mesmo para parametros de implementação



