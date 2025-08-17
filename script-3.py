def run_model(tipo='perceptron'):
    if tipo == 'perceptron':
        print("Rodando Perceptron...")
        # Chamar função Perceptron aqui (ou o código já dado)

    elif tipo == 'adaline':
        print("Rodando Adaline...")
        # Chamar função Adaline aqui

    elif tipo == 'mlp':
        print("Rodando MLP...")
        # Chamar MLP (Keras)

    else:
        print("Modelo inválido.")

# Exemplo de uso:
run_model('perceptron')
run_model('adaline')
run_model('mlp')
