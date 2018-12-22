# -*- coding: utf-8 -*-
from Tkinter import *
import os, sys, inspect

import numpy as np
from keras.models import Sequential
from keras.layers.core import Activation, Dense
from keras.utils import np_utils

from Static_Data import static1,static2,static3,static4,static5,static6,static7,static8,static9,static10,static11,static12,static13,static14,\
    static15,static16,static17,static18,static19,static20,static21,static22,static23,static24,static25,static26,static27,static28,static29,static30,static31,delete,send


np.random.seed(1337)

Train_Data_Count=100
append1 = np.reshape(np.append(static1.static1, static2.static2), (Train_Data_Count*2, 18))
append2 = np.reshape(np.append(append1, static3.static3), (Train_Data_Count*3, 18))
append3 = np.reshape(np.append(append2, static4.static4), (Train_Data_Count*4, 18))
append4 = np.reshape(np.append(append3, static5.static5), (Train_Data_Count*5, 18))
append5 = np.reshape(np.append(append4, static6.static6), (Train_Data_Count*6, 18))
append6 = np.reshape(np.append(append5, static7.static7), (Train_Data_Count*7, 18))
append7 = np.reshape(np.append(append6, static8.static8), (Train_Data_Count*8, 18))
append8 = np.reshape(np.append(append7, static9.static9), (Train_Data_Count*9, 18))
append9 = np.reshape(np.append(append8, static10.static10), (Train_Data_Count*10, 18))
append10 = np.reshape(np.append(append9, static11.static11), (Train_Data_Count*11, 18))
append11 = np.reshape(np.append(append10, static12.static12), (Train_Data_Count*12, 18))
append12 = np.reshape(np.append(append11, static13.static13), (Train_Data_Count*13, 18))
append13 = np.reshape(np.append(append12, static14.static14), (Train_Data_Count*14, 18))
append14 = np.reshape(np.append(append13, static15.static15), (Train_Data_Count*15, 18))
append15 = np.reshape(np.append(append14, static16.static16), (Train_Data_Count*16, 18))
append16 = np.reshape(np.append(append15, static17.static17), (Train_Data_Count*17, 18))
append17 = np.reshape(np.append(append16, static18.static18), (Train_Data_Count*18, 18))
append18 = np.reshape(np.append(append17, static19.static19), (Train_Data_Count*19, 18))
append19 = np.reshape(np.append(append18, static20.static20), (Train_Data_Count*20, 18))
append20 = np.reshape(np.append(append19, static21.static21), (Train_Data_Count*21, 18))
append21 = np.reshape(np.append(append20, static22.static22), (Train_Data_Count*22, 18))
append22 = np.reshape(np.append(append21, static23.static23), (Train_Data_Count*23, 18))
append23 = np.reshape(np.append(append22, static24.static24), (Train_Data_Count*24, 18))
append24 = np.reshape(np.append(append23, static25.static25), (Train_Data_Count*25, 18))
append25 = np.reshape(np.append(append24, static26.static26), (Train_Data_Count*26, 18))
append26 = np.reshape(np.append(append25, static27.static27), (Train_Data_Count*27, 18))
append27 = np.reshape(np.append(append26, static28.static28), (Train_Data_Count*28, 18))
append28 = np.reshape(np.append(append27, static29.static29), (Train_Data_Count*29, 18))
append29 = np.reshape(np.append(append28, static30.static30), (Train_Data_Count*30, 18))
append30 = np.reshape(np.append(append29, static31.static31), (Train_Data_Count*31, 18))
append31 = np.reshape(np.append(append30, delete.delete), (Train_Data_Count*32, 18))
append32 = np.reshape(np.append(append31, send.send), (Train_Data_Count*33, 18))

training_data = append32

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
class_11 = np.ones((Train_Data_Count, 1), dtype=np.int) * 10
class_12 = np.ones((Train_Data_Count, 1), dtype=np.int) * 11
class_13 = np.ones((Train_Data_Count, 1), dtype=np.int) * 12
class_14 = np.ones((Train_Data_Count, 1), dtype=np.int) * 13
class_15 = np.ones((Train_Data_Count, 1), dtype=np.int) * 14
class_16 = np.ones((Train_Data_Count, 1), dtype=np.int) * 15
class_17 = np.ones((Train_Data_Count, 1), dtype=np.int) * 16
class_18 = np.ones((Train_Data_Count, 1), dtype=np.int) * 17
class_19 = np.ones((Train_Data_Count, 1), dtype=np.int) * 18
class_20 = np.ones((Train_Data_Count, 1), dtype=np.int) * 19
class_21 = np.ones((Train_Data_Count, 1), dtype=np.int) * 20
class_22 = np.ones((Train_Data_Count, 1), dtype=np.int) * 21
class_23 = np.ones((Train_Data_Count, 1), dtype=np.int) * 22
class_24 = np.ones((Train_Data_Count, 1), dtype=np.int) * 23
class_25 = np.ones((Train_Data_Count, 1), dtype=np.int) * 24
class_26 = np.ones((Train_Data_Count, 1), dtype=np.int) * 25
class_27 = np.ones((Train_Data_Count, 1), dtype=np.int) * 26
class_28 = np.ones((Train_Data_Count, 1), dtype=np.int) * 27
class_29 = np.ones((Train_Data_Count, 1), dtype=np.int) * 28
class_30 = np.ones((Train_Data_Count, 1), dtype=np.int) * 29
class_31 = np.ones((Train_Data_Count, 1), dtype=np.int) * 30
class_32 = np.ones((Train_Data_Count, 1), dtype=np.int) * 31
class_33 = np.ones((Train_Data_Count, 1), dtype=np.int) * 32

append1 = np.reshape(np.append(class_1, class_2), (Train_Data_Count*2, 1))
append2 = np.reshape(np.append(append1, class_3), (Train_Data_Count*3, 1))
append3 = np.reshape(np.append(append2, class_4), (Train_Data_Count*4, 1))
append4 = np.reshape(np.append(append3, class_5), (Train_Data_Count*5, 1))
append5 = np.reshape(np.append(append4, class_6), (Train_Data_Count*6, 1))
append6 = np.reshape(np.append(append5, class_7), (Train_Data_Count*7, 1))
append7 = np.reshape(np.append(append6, class_8), (Train_Data_Count*8, 1))
append8 = np.reshape(np.append(append7, class_9), (Train_Data_Count*9, 1))
append9 = np.reshape(np.append(append8, class_10), (Train_Data_Count*10, 1))
append10 = np.reshape(np.append(append9, class_11), (Train_Data_Count*11, 1))
append11 = np.reshape(np.append(append10, class_12), (Train_Data_Count*12, 1))
append12 = np.reshape(np.append(append11, class_13), (Train_Data_Count*13, 1))
append13 = np.reshape(np.append(append12, class_14), (Train_Data_Count*14, 1))
append14 = np.reshape(np.append(append13, class_15), (Train_Data_Count*15, 1))
append15 = np.reshape(np.append(append14, class_16), (Train_Data_Count*16, 1))
append16 = np.reshape(np.append(append15, class_17), (Train_Data_Count*17, 1))
append17 = np.reshape(np.append(append16, class_18), (Train_Data_Count*18, 1))
append18 = np.reshape(np.append(append17, class_19), (Train_Data_Count*19, 1))
append19 = np.reshape(np.append(append18, class_20), (Train_Data_Count*20, 1))
append20 = np.reshape(np.append(append19, class_21), (Train_Data_Count*21, 1))
append21 = np.reshape(np.append(append20, class_22), (Train_Data_Count*22, 1))
append22 = np.reshape(np.append(append21, class_23), (Train_Data_Count*23, 1))
append23 = np.reshape(np.append(append22, class_24), (Train_Data_Count*24, 1))
append24 = np.reshape(np.append(append23, class_25), (Train_Data_Count*25, 1))
append25 = np.reshape(np.append(append24, class_26), (Train_Data_Count*26, 1))
append26 = np.reshape(np.append(append25, class_27), (Train_Data_Count*27, 1))
append27 = np.reshape(np.append(append26, class_28), (Train_Data_Count*28, 1))
append28 = np.reshape(np.append(append27, class_29), (Train_Data_Count*29, 1))
append29 = np.reshape(np.append(append28, class_30), (Train_Data_Count*30, 1))
append30 = np.reshape(np.append(append29, class_31), (Train_Data_Count*31, 1))
append31 = np.reshape(np.append(append30, class_32), (Train_Data_Count*32, 1))
append32 = np.reshape(np.append(append31, class_33), (Train_Data_Count*33, 1))


target_data = append32
Y_train = np_utils.to_categorical(target_data, 33)

model = Sequential()
model.add(Dense(330, input_dim=18, activation='relu'))
model.add(Dense(330, input_dim=18, activation='relu'))
model.add(Dense(33, activation='softmax'))

model.compile(loss='mean_squared_error',
              optimizer='adam',
              metrics=['accuracy'])

#mean_squared_error
model.fit(training_data, Y_train, batch_size=Train_Data_Count, nb_epoch=20, verbose=1)

model_json = model.to_json()
with open("model.json", "w") as json_file:
    json_file.write(model_json)
# serialize weights to HDF5
model.save_weights("model.h5")
print("Saved model to disk")
