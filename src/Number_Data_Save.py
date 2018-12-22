# -*- coding: utf-8 -*-
from Tkinter import *
import os, sys, inspect

import numpy as np
from keras.models import Sequential
from keras.layers.core import Activation, Dense
from keras.utils import np_utils

from Number_Data import num1,num2,num3,num4,num5,num6,num7,num8,num9,num0


np.random.seed(1339)

Train_Data_Count=100
append1 = np.reshape(np.append(num1.num1, num2.num2), (Train_Data_Count*2, 18))
append2 = np.reshape(np.append(append1, num3.num3), (Train_Data_Count*3, 18))
append3 = np.reshape(np.append(append2, num4.num4), (Train_Data_Count*4, 18))
append4 = np.reshape(np.append(append3, num5.num5), (Train_Data_Count*5, 18))
append5 = np.reshape(np.append(append4, num6.num6), (Train_Data_Count*6, 18))
append6 = np.reshape(np.append(append5, num7.num7), (Train_Data_Count*7, 18))
append7 = np.reshape(np.append(append6, num8.num8), (Train_Data_Count*8, 18))
append8 = np.reshape(np.append(append7, num9.num9), (Train_Data_Count*9, 18))
append9 = np.reshape(np.append(append8, num0.num0), (Train_Data_Count*10, 18))


training_data = append9

training_data = training_data / 180
predict_data = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]], "float32")  # 적용 데이터

# the four expected results in the same order
class_1 = np.ones((Train_Data_Count, 1), dtype=np.int) * 0
class_2 = np.ones((Train_Data_Count, 1), dtype=np.int) * 1
class_3 = np.ones((Train_Data_Count, 1), dtype=np.int) * 2
class_4 = np.ones((Train_Data_Count, 1), dtype=np.int) * 3
class_5 = np.ones((Train_Data_Count, 1), dtype=np.int) * 4
class_6 = np.ones((Train_Data_Count, 1), dtype=np.int) * 5
class_7 = np.ones((Train_Data_Count, 1), dtype=np.int) * 6
class_8 = np.ones((Train_Data_Count, 1), dtype=np.int) * 7
class_9 = np.ones((Train_Data_Count, 1), dtype=np.int) * 8
class_10 = np.ones((Train_Data_Count, 1), dtype=np.int) * 9


append1 = np.reshape(np.append(class_1, class_2), (Train_Data_Count*2, 1))
append2 = np.reshape(np.append(append1, class_3), (Train_Data_Count*3, 1))
append3 = np.reshape(np.append(append2, class_4), (Train_Data_Count*4, 1))
append4 = np.reshape(np.append(append3, class_5), (Train_Data_Count*5, 1))
append5 = np.reshape(np.append(append4, class_6), (Train_Data_Count*6, 1))
append6 = np.reshape(np.append(append5, class_7), (Train_Data_Count*7, 1))
append7 = np.reshape(np.append(append6, class_8), (Train_Data_Count*8, 1))
append8 = np.reshape(np.append(append7, class_9), (Train_Data_Count*9, 1))
append9 = np.reshape(np.append(append8, class_10), (Train_Data_Count*10, 1))


target_data = append9
Y_train = np_utils.to_categorical(target_data, 10)

model = Sequential()
model.add(Dense(256, input_dim=18, activation='relu'))
model.add(Dense(256, input_dim=18, activation='relu'))
model.add(Dense(10, activation='softmax'))

model.compile(loss='categorical_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

#mean_squared_error
model.fit(training_data, Y_train, batch_size=Train_Data_Count, nb_epoch=20, verbose=1)

model_json = model.to_json()
with open("Number_model.json", "w") as json_file:
    json_file.write(model_json)
# serialize weights to HDF5
model.save_weights("Number_model.h5")
print("Saved model to disk")
