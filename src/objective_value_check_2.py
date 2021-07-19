import numpy as np

mu = np.array([0.8, 0.4, 0.3, 0.4, 0.5, 0.6, 0.1, 0.2, 0.7, 0.1,
      0.8, 0.4, 0.2, 0.9, 0.1, 0.4, 0.5, 0.9, 0.6, 0.4])

sigma = np.array([[2, 0, 8, 1, 0, 6, 3, 2, 2, 0, 9, 0, 3, 5, 7, 7, 4, 3, 8, 3],
         [0, 6, 7, 0, 7, 4, 4, 0, 8, 7, 3, 4, 2, 5, 0, 0, 7, 8, 2, 2],
         [8, 7, 3, 9, 3, 2, 6, 3, 0, 0, 7, 5, 4, 8, 1, 0, 5, 0, 7, 6],
         [1, 0, 9, 9, 9, 9, 6, 3, 8, 7, 2, 8, 1, 0, 2, 6, 6, 6, 6, 9],
         [0, 7, 3, 9, 7, 4, 6, 6, 2, 7, 5, 4, 5, 2, 9, 8, 8, 0, 5, 0],
         [6, 4, 2, 9, 4, 0, 7, 3, 2, 7, 8, 1, 0, 4, 3, 3, 1, 5, 3, 6],
         [3, 4, 6, 6, 6, 7, 3, 7, 5, 3, 2, 9, 3, 6, 2, 2, 7, 5, 8, 8],
         [2, 0, 3, 3, 6, 3, 7, 3, 4, 8, 3, 9, 8, 0, 1, 5, 7, 3, 2, 1],
         [2, 8, 0, 8, 2, 2, 5, 4, 9, 0, 9, 6, 9, 7, 1, 4, 9, 6, 2, 9],
         [0, 7, 0, 7, 7, 7, 3, 8, 0, 0, 7, 2, 1, 3, 6, 6, 5, 9, 3, 0],
         [9, 3, 7, 2, 5, 8, 2, 3, 9, 7, 4, 2, 4, 9, 1, 4, 4, 2, 6, 0],
         [0, 4, 5, 8, 4, 1, 9, 9, 6, 2, 2, 4, 4, 1, 6, 4, 7, 6, 0, 6],
         [3, 2, 4, 1, 5, 0, 3, 8, 9, 1, 4, 4, 3, 2, 3, 7, 9, 4, 7, 0],
         [5, 5, 8, 0, 2, 4, 6, 0, 7, 3, 9, 1, 2, 1, 9, 2, 7, 4, 4, 9],
         [7, 0, 1, 2, 9, 3, 2, 1, 1, 6, 1, 6, 3, 9, 4, 4, 4, 3, 1, 1],
         [7, 0, 0, 6, 8, 3, 2, 5, 4, 6, 4, 4, 7, 2, 4, 6, 9, 0, 4, 9],
         [4, 7, 5, 6, 8, 1, 7, 7, 9, 5, 4, 7, 9, 7, 4, 9, 0, 9, 8, 9],
         [3, 8, 0, 6, 0, 5, 5, 3, 6, 9, 2, 6, 4, 4, 3, 0, 9, 6, 0, 9],
         [8, 2, 7, 6, 5, 3, 8, 2, 2, 3, 6, 0, 7, 4, 1, 4, 8, 0, 3, 9],
         [3, 2, 6, 9, 0, 6, 8, 1, 9, 0, 0, 6, 0, 9, 1, 9, 9, 9, 9, 3]])

q = 1
B = 10
P = 100

solution = np.array([0,1,1,0,0,1,0,1,0,0,0,1,0,1,1,1,0,1,1,0])

print("Volatilidade correta:")
print(q*np.transpose(solution).dot(sigma).dot(solution))

print("Retorno correto:")
print(-np.transpose(mu).dot(solution))

print("Penalização correta:")
print(P * np.square(np.ones((1,20)).dot(solution) - B))

print("Valor objetivo correto:")
print(q*np.transpose(solution).dot(sigma).dot(solution) - np.transpose(mu).dot(solution) + P * np.square(np.ones((1,20)).dot(solution) - B))

N = 20

# There are three terms in the objective function: Covariance, Return, and Budget

Q = np.zeros((20,20))

# Covariance term
for i in range(N):
      Q[i][i] = float(q * sigma[i][i])
      for j in range(i+1, N):
            Q[i][j] = float(2 * q * sigma[i][j])

# Covariance term
for i in range(N):
      for j in range(i, N):
            Q[i][j] = float(q * sigma[i][j])

# Return term
for i in range(N):
      Q[i][i] += float(-mu[i])

# Budget term is decomposed into four terms, per the formula ((sum^{n-1}_{i=0} x_i) - B)^2
for i in range(N):
      Q[i][i] += float(P)

for i in range(N):
      for j in range(i + 1, N):
            Q[i][j] += float(2*P)

for i in range(N):
      Q[i][i] += float(-2 * B * P)


print("QUBO:")
print(np.transpose(solution).dot(Q).dot(solution))

print("QUBO + constante:")
print(np.transpose(solution).dot(Q).dot(solution) + (P * B * B))
