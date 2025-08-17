from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import numpy as np

# XOR problem (não linearmente separável)
X = np.array([[0,0],[0,1],[1,0],[1,1]])
y = np.array([[0],[1],[1],[0]])

model = Sequential()
model.add(Dense(4, input_dim=2, activation='relu'))  # Camada oculta
model.add(Dense(1, activation='sigmoid'))            # Saída

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(X, y, epochs=500, verbose=0)

print("Previsões:")
print(model.predict(X))
