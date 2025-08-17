import numpy as np

# Dados da função AND
X = np.array([[1, 1], [1, -1], [-1, 1], [-1, -1]])
d = np.array([1, -1, -1, -1])  # Saídas desejadas

# Inicialização
w = np.array([0.3, -0.25])  # Pesos iniciais
b = -0.2  # Bias
eta = 0.1  # Taxa de aprendizagem
limiar = 0.5

# Função de ativação (degrau binário)
def step(net):
    return 1 if net >= limiar else -1

# Treinamento
for epoch in range(2):  # 2 ciclos
    print(f'Epoch {epoch + 1}')
    for i in range(len(X)):
        net = np.dot(X[i], w) + b
        y = step(net)
        erro = d[i] - y
        w += eta * erro * X[i]
        b += eta * erro
        print(f'Entrada: {X[i]}, Saída: {y}, Erro: {erro}, Pesos: {w}, Bias: {b}')
