from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.layers import Embedding
from keras.layers import Conv1D, GlobalAveragePooling1D, MaxPooling1D
seq_length=100
import numpy as np

x_train = np.array([[0,0],[0,1],[1,0],[1,1]], "float32")
y_train = np.array([[0],[1],[1],[0]], "float32")
x_test = np.array([[0,0],[0,1],[1,0],[1,1]], "float32")
y_test = np.array([[0],[1],[1],[0]], "float32")


model = Sequential()
model.add(Conv1D(64, 3, activation='relu', input_shape=(seq_length, 100)))
model.add(Conv1D(64, 3, activation='relu'))
model.add(MaxPooling1D(3))
model.add(Conv1D(128, 3, activation='relu'))
model.add(Conv1D(128, 3, activation='relu'))
model.add(GlobalAveragePooling1D())
model.add(Dropout(0.5))
model.add(Dense(1, activation='sigmoid'))

model.compile(loss='binary_crossentropy',
              optimizer='rmsprop',
              metrics=['accuracy'])

model.fit(x_train, y_train, batch_size=16, epochs=100)
score = model.evaluate(x_test, y_test, batch_size=16)