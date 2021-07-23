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

for factor1 in ['try1','try2','try3']:
    for factor2 in [16, 32, 64]:
        for factor3 in [1.500]:
            for factor4 in ['1000per']:
                for factor5 in ['minimal']:
                    for factor6 in [0.5]:
                        for factor7 in ['normal']:
                            for factor8 in ['standard']:
                                for factor9 in ['industry_diversified']:
                                    for factor10 in ['pegasus']:
                                        # Results are stored on a specific folder
                                        folder_name = f'S2m_{factor2}_{factor3}_{factor4}_{factor5}_{factor6}_{factor7}_{factor8}_{factor9}_{factor10}_{factor1}'
                                        # Check if folder exists and creates if not
                                        if not os.path.exists('results/' + folder_name):
                                            os.makedirs('results/' + folder_name)

                                        # Step 1: Get parameters N, q, B, P, tickers, sigma, and mu from data
                                        f = open(f'data/out_{factor9}_N{factor2}_p1mo_i1d.json')
                                        data = json.load(f)

                                        N = data['N']               # Universe size
                                        tickers = data['tickers']   # Tickers
                                        mu = pd.Series(data['mu'])
                                        sigma = pd.DataFrame.from_dict(data['sigma'], orient='index')

                                        print_var('mu', mu)
                                        print_var('sigma', sigma)

                                        B = int(N * factor6)
                                        print_var('B', B)

                                        q_values = None

                                        # minimal set of industry_correlated
                                        # if N == 32:
                                        #     q_values = [0, 1, 6, 10, 70, 90]
                                        # elif N == 64:
                                        #     q_values = [0, 0.1, 0.2, 0.3, 0.6, 1, 2, 3, 4, 6, 10, 20, 80]


                                        # minimal set of industry_diversified
                                        if factor5 == 'minimal':
                                            if N == 8:
                                                q_values = [0, 11, 20, 54]
                                            elif N == 16:
                                                q_values = [0, 2, 6, 100, 500]
                                            elif N == 32:
                                                q_values = [0, 0.4, 0.9, 2, 3, 9, 100]
                                            elif N == 64:
                                                q_values = [0, 0.2, 0.4, 0.6, 1.1, 1.3, 1.5, 2, 5, 6, 7, 8, 10, 100, 500]
                                        elif factor5 == 'moreDlessS':
                                            q_values = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 1000]
                                        elif factor5 == 'mediumDmediumS':
                                            q_values = [0, 0.2, 0.4, 0.6, 0.8, 1, 2, 3, 4, 5, 7.5, 10, 50, 100, 1000]
                                        elif factor5 == 'lessDmoreS':
                                            q_values = [0, 0.1, 1, 10, 100, 1000]
                                        
                                        
                                        print_var('q_values', q_values)

                                        shots_allocation = 15000

                                        shots = int(shots_allocation/len(q_values))

                                        if factor4 == '1000per':
                                            shots = 1000

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
                                        # embedding_type = 'normal'
                                        # embedding_type = 'layout'
                                        embedding_type = factor7

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
                                                Q[(i, i)] = float(q * sigma[tickers[i]][tickers[i]])
                                                for j in range(i+1, N):
                                                    Q[(i, j)] = float(2 * q * sigma[tickers[i]][tickers[j]])

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
                                            chain_strength = None
                                            if factor3 != 'default':
                                                chain_strength = abs(Q[Q_key_max]) * factor3

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
                                            anneal_schedule = None
                                            if factor8 == 'standard':
                                                anneal_schedule = [[0.0, 0.0], [20.0, 1.0]]
                                            elif factor8 == 'long':
                                                anneal_schedule = [[0.0, 0.0], [100.0, 1.0]]
                                            elif factor8 == 'pause':
                                                anneal_schedule = [[0.0, 0.0], [10.0, 0.5], [110.0, 0.5], [120, 1.0]]
                                            elif factor8 == 'quench':
                                                anneal_schedule = [[0.0, 0.0], [10.0, 0.5], [12.0, 1.0]]

                                            sampleset = None
                                            # Step 3: Solve QUBO
                                            if factor3 == 'default' and factor8 == 'standard':
                                                sampleset = composite.sample_qubo(
                                                    Q, num_reads=shots)
                                            elif factor3 == 'default' and factor8 != 'standard':
                                                sampleset = composite.sample_qubo(
                                                    Q, num_reads=shots, anneal_schedule=anneal_schedule)
                                            elif factor3 != 'default' and factor8 != 'standard':
                                                sampleset = composite.sample_qubo(
                                                    Q, num_reads=shots, chain_strength=chain_strength, anneal_schedule=anneal_schedule)
                                            else:
                                                sampleset = composite.sample_qubo(
                                                    Q, num_reads=shots, chain_strength=chain_strength)

                                            chain_strength = sampleset.info['embedding_context']['chain_strength']
                                            #dwave.inspector.show(sampleset)

                                            print('Solved')
                                            # print(sampleset)
                                            sampleset.to_pandas_dataframe().sort_values(
                                                by=['energy']).to_csv(f'results/{folder_name}/out_{embedding_type}N{N}q{q:.2f}B{B}P{P:.3f}C{chain_strength}.csv', index=False)
