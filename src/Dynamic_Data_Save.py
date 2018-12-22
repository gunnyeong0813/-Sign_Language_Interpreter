# -*- coding: utf-8 -*-
import inspect
import os
import sys

src_dir = os.path.dirname(inspect.getfile(inspect.currentframe()))
arch_dir = '../lib/x64' if sys.maxsize > 2**32 else '../lib/x86'
sys.path.insert(0, os.path.abspath(os.path.join(src_dir, arch_dir)))
import numpy as np
from keras.models import Sequential
from keras.layers.core import Dense
from keras.utils import np_utils
from Dynamic_Data import _1_meet,_2_funny,_3_sorry,_4_hungry,_5_thank,_5_thank2,\
    _6_hello,_7_regretful,_8_do,_9_donot,_10_connect,_11_nicetomeet,_12_no,_13_now,_14_byebye,\
    _15_time,_16_is,_17_eat,_18_rank,_19_team,_20_senior,_21_junior,_22_well,_23_dokdo,\
    _24_grand,_25_evaluate,_26_coach,_27_sir,_28_front,_29_buy,_29_buy2,_30_weather,\
    _30_weather2,_31_today,_32_different,_33_please,_34_because,_22_well2,_35_support,\
    _36_receive,_37_cellphone,_38_clap,_42_signlang,_43_teach,_45_hard,_46_happy,_47_baseball,_48_eman,_17_eat2

np.random.seed(1337)

Train_Data_Count=50
append1 = np.reshape(np.append(_1_meet.meet, _2_funny.funny), (Train_Data_Count * 2, 36))
append2 = np.reshape(np.append(append1, _3_sorry.sorry), (Train_Data_Count * 3, 36))
append3 = np.reshape(np.append(append2, _4_hungry.hungry), (Train_Data_Count * 4, 36))
append4 = np.reshape(np.append(append3, _5_thank.thank), (Train_Data_Count * 5, 36))
append5 = np.reshape(np.append(append4, _6_hello.hello), (Train_Data_Count * 6, 36))
append6 = np.reshape(np.append(append5, _7_regretful.regretful), (Train_Data_Count * 7, 36))
append7 = np.reshape(np.append(append6, _8_do.do), (Train_Data_Count * 8, 36))
append8 = np.reshape(np.append(append7, _9_donot.donot), (Train_Data_Count * 9, 36))
append9 = np.reshape(np.append(append8, _10_connect.connect), (Train_Data_Count * 10, 36))
append10 = np.reshape(np.append(append9, _11_nicetomeet.nicetomeet), (Train_Data_Count * 11, 36))
append11 = np.reshape(np.append(append10, _12_no.no), (Train_Data_Count * 12, 36))
append12 = np.reshape(np.append(append11, _13_now.now), (Train_Data_Count * 13, 36))
append13 = np.reshape(np.append(append12, _14_byebye.byebye), (Train_Data_Count * 14, 36))
append14 = np.reshape(np.append(append13, _15_time.time), (Train_Data_Count * 15, 36))
append15 = np.reshape(np.append(append14, _16_is.is_16), (Train_Data_Count * 16, 36))
append16 = np.reshape(np.append(append15, _17_eat.eat), (Train_Data_Count * 17, 36))
append17 = np.reshape(np.append(append16, _18_rank.rank), (Train_Data_Count * 18, 36))
append18 = np.reshape(np.append(append17, _19_team.team), (Train_Data_Count * 19, 36))
append19 = np.reshape(np.append(append18, _20_senior.senior), (Train_Data_Count * 20, 36))
append20 = np.reshape(np.append(append19, _21_junior.junior), (Train_Data_Count * 21, 36))
append21 = np.reshape(np.append(append20, _22_well.well), (Train_Data_Count * 22, 36))
append22 = np.reshape(np.append(append21, _23_dokdo.dokdo), (Train_Data_Count * 23, 36))
append23 = np.reshape(np.append(append22, _24_grand.grand), (Train_Data_Count * 24, 36))
append24 = np.reshape(np.append(append23, _25_evaluate.evaluate), (Train_Data_Count * 25, 36))
append25 = np.reshape(np.append(append24, _26_coach.coach), (Train_Data_Count * 26, 36))
append26 = np.reshape(np.append(append25, _27_sir.sir), (Train_Data_Count * 27, 36))
append27 = np.reshape(np.append(append26, _28_front.front), (Train_Data_Count * 28, 36))
append28 = np.reshape(np.append(append27, _5_thank2.thank2), (Train_Data_Count * 29, 36))
append29 = np.reshape(np.append(append28, _29_buy.buy), (Train_Data_Count * 30, 36))
append30 = np.reshape(np.append(append29, _29_buy2.buy2), (Train_Data_Count * 31, 36))
append31 = np.reshape(np.append(append30, _30_weather.weather), (Train_Data_Count * 32, 36))
append32 = np.reshape(np.append(append31, _30_weather2.weather2), (Train_Data_Count * 33, 36))
append33 = np.reshape(np.append(append32, _31_today.today), (Train_Data_Count * 34, 36))
append34 = np.reshape(np.append(append33, _32_different.different), (Train_Data_Count * 35, 36))
append35 = np.reshape(np.append(append34, _33_please.please), (Train_Data_Count * 36, 36))
append36 = np.reshape(np.append(append35, _34_because.because), (Train_Data_Count * 37, 36))
append37 = np.reshape(np.append(append36, _22_well2.well2), (Train_Data_Count * 38, 36))
append38 = np.reshape(np.append(append37, _35_support.support), (Train_Data_Count * 39, 36))
append39 = np.reshape(np.append(append38, _36_receive.receive), (Train_Data_Count * 40, 36))
append40 = np.reshape(np.append(append39, _37_cellphone.cellphone), (Train_Data_Count * 41, 36))
append41 = np.reshape(np.append(append40, _38_clap.clap), (Train_Data_Count * 42, 36))
append42 = np.reshape(np.append(append41, _42_signlang.signlang), (Train_Data_Count * 43, 36))
append43 = np.reshape(np.append(append42, _43_teach.teach), (Train_Data_Count * 44, 36))
append44 = np.reshape(np.append(append43, _45_hard.hard), (Train_Data_Count * 45, 36))
append45 = np.reshape(np.append(append44, _46_happy.happy), (Train_Data_Count * 46, 36))
append46 = np.reshape(np.append(append45, _47_baseball.baseball), (Train_Data_Count * 47, 36))
append47 = np.reshape(np.append(append46, _48_eman.eman), (Train_Data_Count * 48, 36))
append48 = np.reshape(np.append(append47, _17_eat2.eat2), (Train_Data_Count * 49, 36))

training_data = append48

training_data = training_data / 180
predict_data = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]], "float32")  # 적용 데이터

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
class_34 = np.ones((Train_Data_Count, 1), dtype=np.int) * 33
class_35 = np.ones((Train_Data_Count, 1), dtype=np.int) * 34
class_36 = np.ones((Train_Data_Count, 1), dtype=np.int) * 35
class_37 = np.ones((Train_Data_Count, 1), dtype=np.int) * 36
class_38 = np.ones((Train_Data_Count, 1), dtype=np.int) * 37
class_39 = np.ones((Train_Data_Count, 1), dtype=np.int) * 38
class_40 = np.ones((Train_Data_Count, 1), dtype=np.int) * 39
class_41 = np.ones((Train_Data_Count, 1), dtype=np.int) * 40
class_42 = np.ones((Train_Data_Count, 1), dtype=np.int) * 41
class_43 = np.ones((Train_Data_Count, 1), dtype=np.int) * 42
class_44 = np.ones((Train_Data_Count, 1), dtype=np.int) * 43
class_45 = np.ones((Train_Data_Count, 1), dtype=np.int) * 44
class_46 = np.ones((Train_Data_Count, 1), dtype=np.int) * 45
class_47 = np.ones((Train_Data_Count, 1), dtype=np.int) * 46
class_48 = np.ones((Train_Data_Count, 1), dtype=np.int) * 47
class_49 = np.ones((Train_Data_Count, 1), dtype=np.int) * 48



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
append33 = np.reshape(np.append(append32, class_34), (Train_Data_Count*34, 1))
append34 = np.reshape(np.append(append33, class_35), (Train_Data_Count*35, 1))
append35 = np.reshape(np.append(append34, class_36), (Train_Data_Count*36, 1))
append36 = np.reshape(np.append(append35, class_37), (Train_Data_Count*37, 1))
append37 = np.reshape(np.append(append36, class_38), (Train_Data_Count*38, 1))
append38 = np.reshape(np.append(append37, class_39), (Train_Data_Count*39, 1))
append39 = np.reshape(np.append(append38, class_40), (Train_Data_Count*40, 1))
append40 = np.reshape(np.append(append39, class_41), (Train_Data_Count*41, 1))
append41 = np.reshape(np.append(append40, class_42), (Train_Data_Count*42, 1))
append42 = np.reshape(np.append(append41, class_43), (Train_Data_Count*43, 1))
append43 = np.reshape(np.append(append42, class_44), (Train_Data_Count*44, 1))
append44 = np.reshape(np.append(append43, class_45), (Train_Data_Count*45, 1))
append45 = np.reshape(np.append(append44, class_46), (Train_Data_Count*46, 1))
append46 = np.reshape(np.append(append45, class_47), (Train_Data_Count*47, 1))
append47 = np.reshape(np.append(append46, class_48), (Train_Data_Count*48, 1))
append48 = np.reshape(np.append(append47, class_49), (Train_Data_Count*49, 1))



target_data = append48
Y_train = np_utils.to_categorical(target_data, 49)

model = Sequential()
model.add(Dense(98, input_dim=36, activation='linear'))
model.add(Dense(98, input_dim=36, activation='linear'))
model.add(Dense(98, input_dim=36, activation='linear'))
model.add(Dense(49, activation='softmax'))

model.compile(loss='categorical_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

#mean_squared_error
model.fit(training_data, Y_train, batch_size=Train_Data_Count, nb_epoch=20, verbose=1)

model_json = model.to_json()
with open("Dynamic_model.json", "w") as json_file:
    json_file.write(model_json)
# serialize weights to HDF5
model.save_weights("Dynamic_model.h5")
print("Saved model to disk")
