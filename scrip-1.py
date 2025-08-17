import numpy as np

X = np.array([[1, 1], [1, -1], [-1, 1], [-1, -1]])
d = np.array([1, -1, -1, -1])

w = np.array([0.3, -0.25])
b = -0.2
eta = 0.1

for epoch in range(2):
    print(f'Epoch {epoch + 1}')
    for i in range(len(X)):
        net = np.dot(X[i], w) + b
        y = net  # Saída linear
        erro = d[i] - y
        w += eta * erro * X[i]
        b += eta * erro
        print(f'Entrada: {X[i]}, Saída: {y:.2f}, Erro: {erro:.2f}, Pesos: {w}, Bias: {b}')
