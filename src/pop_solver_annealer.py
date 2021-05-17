import json
import pandas as pd
import numpy as np
import os

# To formulate QUBO
from collections import defaultdict

# To run QUBO
from dwave.system import DWaveSampler, FixedEmbeddingComposite
import dwave.inspector

# To print variables:


def print_var(variable_name, variable):
    print(f'{variable_name}:\n{variable}')

# Five steps:
# 1. Get parameters N, q, B, P, tickers, sigma, and mu from data
# 2. Formulate QUBO
# 3. Solve it.

for factor1 in [64]:
    for factor2 in ['try1', 'try2', 'try3', 'try4', 'try5', 'try6', 'try7', 'try8', 'try9', 'try10']:
        for factor3 in  ['industry_diversified']:
            for factor4 in ['']:
                for factor5 in [0.5]:
                    # Results are stored on a specific folder
                    folder_name = f'scenarioB5_N{factor1}_Pformulated_Cformulated1.000_Allocated_Pegasus_{factor3}_annealer_{factor2}'
                    # Check if folder exists and creates if not
                    if not os.path.exists('results/' + folder_name):
                        os.makedirs('results/' + folder_name)

                    # Step 1: Get parameters N, q, B, P, tickers, sigma, and mu from data
                    f = open(f'data/out_{factor3}_N{factor1}_p1mo_i1d.json')
                    data = json.load(f)

                    N = data['N']               # Universe size
                    tickers = data['tickers']   # Tickers
                    mu = pd.Series(data['mu'])
                    sigma = pd.DataFrame.from_dict(data['sigma'], orient='index')

                    print_var('mu', mu)
                    print_var('sigma', sigma)

                    B = int(N * factor5)
                    print_var('B', B)

                    q_values = None

                    # industry_diversified
                    if N == 8:
                        q_values = [0, 11, 20, 54]
                    elif N == 16:
                        q_values = [0, 2, 6, 100, 500]
                    elif N == 32:
                        q_values = [0, 0.4, 0.9, 2, 3, 9, 100]
                    elif N == 64:
                        q_values = [0, 0.2, 0.4, 0.6, 1.1, 1.3, 1.5, 2, 5, 6, 7, 8, 10, 100, 500]

                    # industry_correlated
                    # if N == 32:
                    #     q_values = [0, 1, 6, 10, 70, 90]
                    # elif N == 64:
                    #     q_values = [0, 0.1, 0.2, 0.3, 0.6, 1, 2, 3, 4, 6, 10, 20, 80]

                    # if factor4 == 'moreDlessS':
                    #     q_values = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 1000]
                    # elif factor4 == 'mediumDmediumS':
                    #     q_values = [0, 0.2, 0.4, 0.6, 0.8, 1, 2, 3, 4, 5, 7.5, 10, 50, 100, 1000]
                    # elif factor4 == 'lessDmoreS':
                    #     q_values = [0, 0.1, 1, 10, 100, 1000]
                    
                    # scenarioA3
                    # q_values = [0, 0.2, 0.4, 0.6, 0.8, 1, 2, 3, 4, 5, 7.5, 10, 50, 100, 1000]
                    print_var('q_values', q_values)

                    shots_allocation = 15000

                    shots = int(shots_allocation/len(q_values))
                    # shots = 1000
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

                    # Get sampler
                    sampler = DWaveSampler()
                    embedding_type = 'normal'
                    # embedding_type = 'layout'
                    # embedding_type = factor4

                    # Get embedding
                    f = open(f'data/embedding_{embedding_type}N{N}.json')
                    embedding = json.load(f)
                    embedding = {int(k):[int(i) for i in v] for k,v in embedding.items()}
                    print_var('embedding', embedding)


                    composite = FixedEmbeddingComposite(sampler, embedding=embedding)

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

                        # To check graph connectivity
                        # import matplotlib.pyplot as plt
                        # import networkx as nx
                        # Qg = nx.Graph()
                        
                        # for i in range(N):
                        #     for j in range(i, N):
                        #         Qg.add_edge(i, j, weight=Q[(i,j)])

                        # deg_list = [len(Qg.adj[v])/len(Qg) for v in Qg] # Where deg=1.0 means that node is fully connected
                        # plt.hist(deg_list, bins=100)
                        # plt.show()
                        # anneal_schedule = None
                        # if factor4 == 'default':
                        #     anneal_schedule = [[0.0, 0.0], [20.0, 1.0]]
                        # elif factor4 == 'long':
                        #     anneal_schedule = [[0.0, 0.0], [100.0, 1.0]]
                        # elif factor4 == 'pause':
                        #     anneal_schedule = [[0.0, 0.0], [10.0, 0.5], [110.0, 0.5], [120, 1.0]]
                        # elif factor4 == 'quench':
                        #     anneal_schedule = [[0.0, 0.0], [10.0, 0.5], [12.0, 1.0]]

                        # Step 3: Solve QUBO
                        sampleset = composite.sample_qubo(
                            Q, num_reads=shots, chain_strength=chain_strength)

                        chain_strength = sampleset.info['embedding_context']['chain_strength']
                        #dwave.inspector.show(sampleset)

                        print('Solved')
                        # print(sampleset)
                        sampleset.to_pandas_dataframe().sort_values(
                            by=['energy']).to_csv(f'results/{folder_name}/out_{embedding_type}N{N}q{q:.2f}B{B}P{P:.3f}C{chain_strength}.csv', index=False)
