import json
import pandas as pd
import numpy as np
import os
import networkx as nx

# To formulate QUBO
from collections import defaultdict

# To run QUBO
from dwave.system import DWaveSampler, FixedEmbeddingComposite
import dwave.inspector

from embera.composites.layout_aware import LayoutAwareEmbeddingComposite

from dimod.reference.composites.structure import StructureComposite
from dimod.reference.samplers.simulated_annealing import SimulatedAnnealingSampler

# To print variables:


def print_var(variable_name, variable):
    print(f'{variable_name}:\n{variable}')

# Five steps:
# 1. Get parameters N, q, B, P, tickers, sigma, and mu from data
# 2. Formulate QUBO
# 3. Solve it.


# Get sampler
sampler = DWaveSampler()

Sg = nx.complete_graph(64)

# Layout of the problem graph
layout = {v: v for v in Sg}

Tg = sampler.to_networkx_graph()

# Setup Composite
candidates_parameters = {'vicinity': 0,
                         'd_lim': 0.125,
                         'delta_t': 0.4,
                         'enable_migration': True}
embedding_parameters = {'tries': 20}

# Use any sampler and make structured (i.e. Simulated Annealing, Exact) or use structured sampler if available (i.e. D-Wave machine)
structsampler = StructureComposite(sampler, Tg.nodes, Tg.edges)
sampler = LayoutAwareEmbeddingComposite(structsampler, layout=layout,
                                        candidates_parameters=candidates_parameters,
                                        embedding_parameters=embedding_parameters)

for factor1 in ['try1', 'try2', 'try3', 'try4', 'try5']:
    # Results are stored on a specific folder
    folder_name = f'scenarioB2_N64_Pformulated_Cformulated1.000_Allocated_layout_aware_annealer_{factor1}'
    # Check if folder exists and creates if not
    if not os.path.exists('results/' + folder_name):
        os.makedirs('results/' + folder_name)

    # Step 1: Get parameters N, q, B, P, tickers, sigma, and mu from data
    f = open('data/out_diversified_N32_p1mo_i1d.json')
    data = json.load(f)

    N = data['N']               # Universe size
    tickers = data['tickers']   # Tickers
    mu = pd.Series(data['mu'])
    sigma = pd.DataFrame.from_dict(data['sigma'], orient='index')

    print_var('mu', mu)
    print_var('sigma', sigma)

    B = int(N * 0.5)
    print_var('B', B)

    q_values = None

    # diversified
    if N == 8:
        q_values = [0, 11, 20, 54]
    elif N == 16:
        q_values = [0, 2, 6, 100, 500]
    elif N == 32:
        q_values = [0, 0.4, 0.9, 2, 3, 9, 100]
    elif N == 64:
        q_values = [0, 0.2, 0.4, 0.6, 1.1, 1.3,
                    1.5, 2, 5, 6, 7, 8, 10, 100, 500]

    # strongly_correlated
    # if N == 32:
    #     q_values = [0, 1, 6, 10, 70, 90]
    # elif N == 64:
    #     q_values = [0, 0.1, 0.2, 0.3, 0.6, 1, 2, 3, 4, 6, 10, 20, 80]

    # if factor2 == 'lessDmoreS':
    #     q_values = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 1000]
    # elif factor2 == 'mediumDmediumS':
    #     q_values = [0, 0.2, 0.4, 0.6, 0.8, 1, 2, 3, 4, 5, 7.5, 10, 50, 100, 1000]
    # elif factor2 == 'moreDlessS':
    #     q_values = [0, 0.1, 1, 10, 100, 1000]
    print_var('q_values', q_values)

    shots_allocation = 15000

    shots = int(shots_allocation/len(q_values))

    print_var('shots per q_value', shots)

    min_sigma = 0
    for i in range(N):
        for j in range(i+1, N):
            if sigma[tickers[i]][tickers[j]] < 0:
                min_sigma += sigma[tickers[i]][tickers[j]]

    max_mu = 0
    for i in range(N):
        if mu[tickers[i]] > 0:
            max_mu += mu[tickers[i]]

    for q in q_values:
        # Step 2: Formulate QUBO
        Q = defaultdict(float)

        P = -q * min_sigma + max_mu

        # There are three terms in the objective function: Covariance, Return, and Budget

        # Covariance term
        for i in range(N):
            for j in range(i, N):
                Q[(i, j)] = float(q * sigma[tickers[i]][tickers[j]])

        # Return term
        for i in range(N):
            Q[(i, i)] += float(-mu[tickers[i]])

        # Budget term is decomposed into four terms, per the formula ((sum^{n-1}_{i=0} x_i) - B)^2
        for i in range(N):
            Q[(i, i)] += float(P)

        for i in range(N):
            for j in range(i + 1, N):
                Q[(i, j)] += float(2*P)

        for i in range(N):
            Q[(i, i)] += float(-2 * B * P)

        # Chain_strength is a guessed value. Good rule of thumb is to have the same order of magnitude as max abs value of Q.
        Q_key_max = max(Q.keys(), key=(lambda k: abs(Q[k])))
        chain_strength = abs(Q[Q_key_max]) * 1.000

        print_var('Q', Q)

        # Step 3: Solve QUBO
        sampleset = sampler.sample_qubo(
            Q, num_reads=shots, chain_strength=chain_strength)

        chain_strength = sampleset.info['embedding_context']['chain_strength']
        # dwave.inspector.show(sampleset)

        print('Solved')
        print(sampleset)
        sampleset.to_pandas_dataframe().sort_values(
            by=['energy']).to_csv(f'results/{folder_name}/out_layout_awareN{N}q{q:.2f}B{B}P{P:.3f}C{chain_strength}.csv', index=False)
