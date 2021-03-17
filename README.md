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

#

Encontrar formula para P

Definir 3 datasets  reais.

Como seleccionar ponto de cada execução (que tem vários shots)



1º Fixar todos menos datasets q. (usar implementação default)

2º Fixar Tudo menos N B (escolher melhores P q e fixar dataset real normal)

3º depois o mesmo para parametros de implementação