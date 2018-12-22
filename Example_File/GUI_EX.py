# -*- coding: utf-8 -*-
from Tkinter import *
import os, sys, inspect
src_dir = os.path.dirname(inspect.getfile(inspect.currentframe()))
arch_dir = '../lib/x64' if sys.maxsize > 2**32 else '../lib/x86'
sys.path.insert(0, os.path.abspath(os.path.join(src_dir, arch_dir)))
import Leap
import time
import numpy as np
from keras.models import Sequential
from keras.layers.core import Activation, Dense
from keras.utils import np_utils
from keras.models import model_from_json
from hangul_utils import split_syllables, join_jamos
import json
from operator import eq




class TouchPointListener(Leap.Listener):
    one=0
    two=0
    three=0
    four = 0
    five = 0
    six = 0
    seven = 0
    eight = 0
    nine = 0
    ten = 0
    S11=0
    S12 = 0
    S13 = 0
    S14 = 0
    S15 = 0
    S16 = 0
    S17 = 0
    S18 = 0
    S19 = 0
    S20 = 0
    S21 = 0
    S22 = 0
    S23 = 0
    S24 = 0
    S25 = 0
    S26 = 0
    S27 = 0
    S28 = 0
    S29 = 0
    S30 = 0
    S31 = 0

    clear_var = 0
    clear=3
    mingamdo=20
    predict_data = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])  # 적용 데이터
    direction_index = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # 손 그리기 위한 방향 배열 만든 후 삽입
    wrist_index = [0, 0, 0]  # 손목 방향 pitch,yaw,roll
    static_value = [""]

    def on_init(self, controller):
        print "Initialized"


    def labelUP(self):
        restored_text = join_jamos(self.static_value)
        print(restored_text)
        # self.v2 = StringVar(value=json.dumps(self.static_value, ensure_ascii=False))
        self.v2 = StringVar(value=restored_text)
        self.txt = Entry(textvariable=self.v2)
        self.txt.grid(row=0, column=1)

    def initializeVal(self):
        self.one=0
        self.two=0
        self.three=0
        self.four=0
        self.five = 0
        self.six = 0
        self.seven = 0
        self.eight = 0
        self.nine = 0
        self.ten = 0
        self.S11 = 0
        self.S12 = 0
        self.S13 = 0
        self.S14 = 0
        self.S15 = 0
        self.S16 = 0
        self.S17 = 0
        self.S18 = 0
        self.S19 = 0
        self.S20 = 0
        self.S21 = 0
        self.S22 = 0
        self.S23 = 0
        self.S24 = 0
        self.S25 = 0
        self.S26 = 0
        self.S27 = 0
        self.S28 = 0
        self.S29 = 0
        self.S30 = 0
        self.S31 = 0

    def on_connect(self, controller):
        print "Connected"

    def on_frame(self, controller):
        time.sleep(0.03)
        #self.paintCanvas.delete("all")

        frame = controller.frame()

        self.paintCanvas.delete("all")

        interactionBox = frame.interaction_box
        j = 0
        for pointable in frame.pointables:
            direction = pointable.direction  # 손가락 마다의 방향 지시
            if j % 5 == 0:
                thumb = float(direction[0] * Leap.RAD_TO_DEG)
                predict_data[0][3] = float(thumb / 180)
                thumb2 = float(direction[1] * Leap.RAD_TO_DEG)
                predict_data[0][4] = float(thumb2 / 180)
                thumb3 = float(direction[2] * Leap.RAD_TO_DEG)
                predict_data[0][5] = float(thumb3 / 180)
            if j % 5 == 1:
                Index = float(direction[0] * Leap.RAD_TO_DEG)
                predict_data[0][6] = float(Index / 180)
                Index2 =float( direction[1] * Leap.RAD_TO_DEG)
                predict_data[0][7] = float(Index2 / 180)
                Index3 = float(direction[2] * Leap.RAD_TO_DEG)
                predict_data[0][8] = float(Index3 / 180)
            if j % 5 == 2:
                Middle = float(direction[0] * Leap.RAD_TO_DEG)
                predict_data[0][9] =float(Middle / 180)
                Middle2 = float(direction[1] * Leap.RAD_TO_DEG)
                predict_data[0][10] = float(Middle2 / 180)
                Middle3 = float(direction[2] * Leap.RAD_TO_DEG)
                predict_data[0][11] =float(Middle3 / 180)
            if j % 5 == 3:
                Ring = float(direction[0] * Leap.RAD_TO_DEG)
                predict_data[0][12] =float (Ring / 180)
                Ring2 = float(direction[1] * Leap.RAD_TO_DEG)
                predict_data[0][13] =float (Ring2 / 180)
                Ring3 = float(direction[2] * Leap.RAD_TO_DEG)
                predict_data[0][14] = float(Ring3 / 180)
            if j % 5 == 4:
                Pinky = float(direction[0] * Leap.RAD_TO_DEG)
                predict_data[0][15] = float(Pinky / 180)
                Pinky2 = float(direction[1] * Leap.RAD_TO_DEG)
                predict_data[0][16] = float(Pinky2 / 180)
                Pinky3 = float(direction[2] * Leap.RAD_TO_DEG)
                predict_data[0][17] = float(Pinky3 / 180)

            #print pointable.id
            #print direction[0] * Leap.RAD_TO_DEG / 180
            #print direction[1] * Leap.RAD_TO_DEG / 180
            #print direction[2] * Leap.RAD_TO_DEG / 180
            j += 1

        # Get hands
        for hand in frame.hands:
            handType = "Left hand" if hand.is_left else "Right hand"

           # print "  %s, id %d, position: %s" % (
            #    handType, hand.id, hand.palm_position)
            # Get the hand's normal vector and direction
            normal = hand.palm_normal
            direction = hand.direction

            # Calculate the hand's pitch, roll, and yaw angles
            #print "  pitch: %f degrees, roll: %f degrees, yaw: %f degrees" % (
            #    direction.pitch * Leap.RAD_TO_DEG,
            #    normal.roll * Leap.RAD_TO_DEG,
             #   direction.yaw * Leap.RAD_TO_DEG)
            pitch = float(direction.pitch * Leap.RAD_TO_DEG)
            predict_data[0][0] = float(float(pitch) / float(180))
            roll = float(normal.roll * Leap.RAD_TO_DEG)
            predict_data[0][1] = float(roll / 180)
            yaw = float(direction.yaw * Leap.RAD_TO_DEG)
            predict_data[0][2] = float(yaw / 180)

        #print float(model.predict(predict_data)[0][0])
        #print float(model.predict(predict_data)[0][1])
        #print float(model.predict(predict_data)[0][2])
            print (model.predict(predict_data)[0][0])
            if handType=="Right hand" and len(frame.hands)==1:
                print predict_data
                try:
                    if not len(frame.hands) == 0:

                        if model.predict_classes(predict_data) == [0] and model.predict(predict_data)[0][0]>0.6:
                            if self.one==self.mingamdo:
                                print model.predict_classes(predict_data, verbose=0)
                                print "ㄱ 저장완료"
                                self.static_value.append(u"ㄱ")
                                self.paintCanvas.configure(background='yellow')
                                time.sleep(0.5)
                                self.paintCanvas.configure(background='white')
                                self.initializeVal()
                                self.labelUP()
                            self.one+=1
                            print self.one
                        if model.predict_classes(predict_data) == [1] and model.predict(predict_data)[0][1]>0.6:

                            if self.two==self.mingamdo:
                                print model.predict_classes(predict_data, verbose=0)

                                print "ㄴ 저장완료"
                                self.static_value.append(u"ㄴ")
                                self.paintCanvas.configure(background='yellow')
                                time.sleep(1)
                                self.paintCanvas.configure(background='white')
                                self.initializeVal()
                                self.labelUP()
                            self.two+=1
                            print self.w
                        if model.predict_classes(predict_data) == [2] and model.predict(predict_data)[0][2]>0.6:
                            if self.three == self.mingamdo:
                                print model.predict_classes(predict_data, verbose=0)
                                print "ㄷ 저장완료"
                                self.static_value.append(u"ㄷ")
                                self.paintCanvas.configure(background='yellow')
                                time.sleep(1)
                                self.paintCanvas.configure(background='white')
                                self.labelUP()
                                self.initializeVal()
                            self.three+=1
                            print self.three
                        if model.predict_classes(predict_data) == [3] and model.predict(predict_data)[0][3]>0.6:
                            if self.four == self.mingamdo:
                                print model.predict_classes(predict_data, verbose=0)

                                print "ㄹ 저장완료"
                                self.static_value.append(u"ㄹ")
                                self.paintCanvas.configure(background='yellow')
                                time.sleep(1)
                                self.paintCanvas.configure(background='white')
                                self.initializeVal()
                                self.labelUP()
                            self.four+=1
                            print self.four
                        if model.predict_classes(predict_data) == [4] and model.predict(predict_data)[0][4]>0.6:
                            if self.five == self.mingamdo:
                                print model.predict_classes(predict_data, verbose=0)

                                print "ㅁ 저장완료"
                                self.static_value.append(u"ㅁ")
                                self.paintCanvas.configure(background='yellow')
                                time.sleep(1)
                                self.paintCanvas.configure(background='white')
                                self.initializeVal()
                                self.labelUP()
                            self.five+=1
                            print self.four
                        if model.predict_classes(predict_data) == [5] and model.predict(predict_data)[0][5]>0.6:
                            if self.six == self.mingamdo:
                                print model.predict_classes(predict_data, verbose=0)

                                print "ㅂ 저장완료"
                                self.static_value.append(u"ㅂ")
                                self.paintCanvas.configure(background='yellow')
                                time.sleep(1)
                                self.paintCanvas.configure(background='white')
                                self.initializeVal()
                                self.labelUP()
                            self.six+=1
                            print self.six
                        if model.predict_classes(predict_data) == [6] and model.predict(predict_data)[0][6]>0.6:
                            if self.seven == self.mingamdo:
                                print model.predict_classes(predict_data, verbose=0)

                                print "ㅅ 저장완료"
                                self.static_value.append(u"ㅅ")
                                self.paintCanvas.configure(background='yellow')
                                time.sleep(1)
                                self.paintCanvas.configure(background='white')
                                self.initializeVal()
                                self.labelUP()
                            self.seven+=1
                            print self.seven
                        if model.predict_classes(predict_data) == [7] and model.predict(predict_data)[0][7]>0.6:
                            if self.eight == self.mingamdo:
                                print model.predict_classes(predict_data, verbose=0)

                                print "ㅇ 저장완료"
                                self.static_value.append(u"ㅇ")
                                self.paintCanvas.configure(background='yellow')
                                time.sleep(1)
                                self.paintCanvas.configure(background='white')
                                self.initializeVal()
                                self.labelUP()
                            self.eight+=1
                            print self.eight
                        if model.predict_classes(predict_data) == [8] and model.predict(predict_data)[0][8]>0.6:
                            if self.nine == self.mingamdo:
                                print model.predict_classes(predict_data, verbose=0)

                                print "ㅈ 저장완료"
                                self.static_value.append(u"ㅈ")
                                self.paintCanvas.configure(background='yellow')
                                time.sleep(1)
                                self.paintCanvas.configure(background='white')
                                self.initializeVal()
                                self.labelUP()
                            self.nine+=1
                            print self.nine
                        if model.predict_classes(predict_data) == [9] and model.predict(predict_data)[0][9]>0.6:
                            if self.ten == self.mingamdo:
                                print model.predict_classes(predict_data, verbose=0)
                                print "ㅊ 저장완료"
                                self.static_value.append(u"ㅊ")
                                self.paintCanvas.configure(background='yellow')
                                time.sleep(1)
                                self.paintCanvas.configure(background='white')
                                self.initializeVal()
                                self.labelUP()
                            self.ten+=1
                            print self.ten
                        if model.predict_classes(predict_data) == [10] and model.predict(predict_data)[0][10]>0.6:
                            if self.S11 == self.mingamdo:
                                print model.predict_classes(predict_data, verbose=0)
                                print "ㅋ 저장완료"
                                self.static_value.append(u"ㅋ")
                                self.paintCanvas.configure(background='yellow')
                                time.sleep(1)
                                self.paintCanvas.configure(background='white')
                                self.initializeVal()
                                self.labelUP()
                            self.S11+=1
                            print self.ten
                        if model.predict_classes(predict_data) == [11] and model.predict(predict_data)[0][11]>0.6:
                            if self.S12 == self.mingamdo:
                                print model.predict_classes(predict_data, verbose=0)
                                print "ㅌ 저장완료"
                                self.static_value.append(u"ㅌ")
                                self.paintCanvas.configure(background='yellow')
                                time.sleep(1)
                                self.paintCanvas.configure(background='white')
                                self.initializeVal()
                                self.labelUP()
                            self.S12+=1
                            print self.ten
                        if model.predict_classes(predict_data) == [12] and model.predict(predict_data)[0][12]>0.6:
                            if self.S13 == self.mingamdo:
                                print model.predict_classes(predict_data, verbose=0)
                                print "ㅍ 저장완료"
                                self.static_value.append(u"ㅍ")
                                self.paintCanvas.configure(background='yellow')
                                time.sleep(1)
                                self.paintCanvas.configure(background='white')
                                self.initializeVal()
                                self.labelUP()
                            self.S13+=1
                            print self.ten
                        if model.predict_classes(predict_data) == [13] and model.predict(predict_data)[0][13]>0.6:
                            if self.S14 == self.mingamdo:
                                print model.predict_classes(predict_data, verbose=0)
                                print "ㅎ 저장완료"
                                self.static_value.append(u"ㅎ")
                                self.paintCanvas.configure(background='yellow')
                                time.sleep(1)
                                self.paintCanvas.configure(background='white')
                                self.initializeVal()
                                self.labelUP()
                            self.S14+=1
                            print self.ten
                        if model.predict_classes(predict_data) == [14] and model.predict(predict_data)[0][14]>0.6:
                            if self.S15 == self.mingamdo:
                                print model.predict_classes(predict_data, verbose=0)
                                print "ㅏ 저장완료"
                                self.static_value.append(u"ㅏ")
                                self.paintCanvas.configure(background='yellow')
                                time.sleep(1)
                                self.paintCanvas.configure(background='white')
                                self.initializeVal()
                                self.labelUP()
                            self.S15+=1
                            print self.ten
                        if model.predict_classes(predict_data) == [15] and model.predict(predict_data)[0][15]>0.6:
                            if self.S16 == self.mingamdo:
                                print model.predict_classes(predict_data, verbose=0)
                                print "ㅑ 저장완료"
                                self.static_value.append(u"ㅑ")
                                self.paintCanvas.configure(background='yellow')
                                time.sleep(1)
                                self.paintCanvas.configure(background='white')
                                self.initializeVal()
                                self.labelUP()
                            self.S16+=1
                            print self.ten
                        if model.predict_classes(predict_data) == [16] and model.predict(predict_data)[0][16]>0.6:
                            if self.S17 == self.mingamdo:
                                print model.predict_classes(predict_data, verbose=0)
                                print "ㅓ 저장완료"
                                self.static_value.append(u"ㅓ")
                                self.paintCanvas.configure(background='yellow')
                                time.sleep(1)
                                self.paintCanvas.configure(background='white')
                                self.initializeVal()
                                self.labelUP()
                            self.S17+=1
                            print self.ten
                        if model.predict_classes(predict_data) == [17] and model.predict(predict_data)[0][17]>0.6:
                            if self.S18 == self.mingamdo:
                                print model.predict_classes(predict_data, verbose=0)
                                print "ㅕ 저장완료"
                                self.static_value.append(u"ㅕ")
                                self.paintCanvas.configure(background='yellow')
                                time.sleep(1)
                                self.paintCanvas.configure(background='white')
                                self.initializeVal()
                                self.labelUP()
                            self.S18+=1
                            print self.ten
                        if model.predict_classes(predict_data) == [18] and model.predict(predict_data)[0][18]>0.6:
                            if self.S19 == self.mingamdo:
                                print model.predict_classes(predict_data, verbose=0)
                                print "ㅗ 저장완료"
                                self.static_value.append(u"ㅗ")
                                self.paintCanvas.configure(background='yellow')
                                time.sleep(1)
                                self.paintCanvas.configure(background='white')
                                self.initializeVal()
                                self.labelUP()
                            self.S19+=1
                            print self.ten
                        if model.predict_classes(predict_data) == [19] and model.predict(predict_data)[0][19]>0.6:
                            if self.S20 == self.mingamdo:
                                print model.predict_classes(predict_data, verbose=0)
                                print "ㅛ 저장완료"
                                self.static_value.append(u"ㅛ")
                                self.paintCanvas.configure(background='yellow')
                                time.sleep(1)
                                self.paintCanvas.configure(background='white')
                                self.initializeVal()
                                self.labelUP()
                            self.S20+=1
                            print self.ten
                        if model.predict_classes(predict_data) == [20] and model.predict(predict_data)[0][20]>0.6:
                            if self.S21 == self.mingamdo:
                                print model.predict_classes(predict_data, verbose=0)
                                print "ㅜ 저장완료"
                                self.static_value.append(u"ㅜ")
                                self.paintCanvas.configure(background='yellow')
                                time.sleep(1)
                                self.paintCanvas.configure(background='white')
                                self.initializeVal()
                                self.labelUP()
                            self.S21+=1
                            print self.ten
                        if model.predict_classes(predict_data) == [21] and model.predict(predict_data)[0][21]>0.6:
                            if self.S22 == self.mingamdo:
                                print model.predict_classes(predict_data, verbose=0)
                                print "ㅠ 저장완료"
                                self.static_value.append(u"ㅠ")
                                self.paintCanvas.configure(background='yellow')
                                time.sleep(1)
                                self.paintCanvas.configure(background='white')
                                self.initializeVal()
                                self.labelUP()
                            self.S22+=1
                            print self.ten
                        if model.predict_classes(predict_data) == [22] and model.predict(predict_data)[0][22]>0.6:
                            if self.S23 == self.mingamdo:
                                print model.predict_classes(predict_data, verbose=0)
                                print "ㅡ 저장완료"
                                self.static_value.append(u"ㅡ")
                                self.paintCanvas.configure(background='yellow')
                                time.sleep(1)
                                self.paintCanvas.configure(background='white')
                                self.initializeVal()
                                self.labelUP()
                            self.S23+=1
                            print self.ten
                        if model.predict_classes(predict_data) == [23] and model.predict(predict_data)[0][23]>0.6:
                            if self.S24 == self.mingamdo:
                                print model.predict_classes(predict_data, verbose=0)
                                print "ㅣ 저장완료"
                                self.static_value.append(u"ㅣ")
                                self.paintCanvas.configure(background='yellow')
                                time.sleep(1)
                                self.paintCanvas.configure(background='white')
                                self.initializeVal()
                                self.labelUP()
                            self.S24+=1
                            print self.ten
                        if model.predict_classes(predict_data) == [24] and model.predict(predict_data)[0][24]>0.6:
                            if self.S25 == self.mingamdo:
                                print model.predict_classes(predict_data, verbose=0)
                                print "ㅐ 저장완료"
                                self.static_value.append(u"ㅐ")
                                self.paintCanvas.configure(background='yellow')
                                time.sleep(1)
                                self.paintCanvas.configure(background='white')
                                self.initializeVal()
                                self.labelUP()
                            self.S25+=1
                            print self.ten
                        if model.predict_classes(predict_data) == [25] and model.predict(predict_data)[0][25]>0.6:
                            if self.S26 == self.mingamdo:
                                print model.predict_classes(predict_data, verbose=0)
                                print "ㅒ 저장완료"
                                self.static_value.append(u"ㅒ")
                                self.paintCanvas.configure(background='yellow')
                                time.sleep(1)
                                self.paintCanvas.configure(background='white')
                                self.initializeVal()
                                self.labelUP()
                            self.S26+=1
                            print self.ten
                        if model.predict_classes(predict_data) == [26] and model.predict(predict_data)[0][26]>0.6:
                            if self.S27 == self.mingamdo:
                                print model.predict_classes(predict_data, verbose=0)
                                print "ㅔ 저장완료"
                                self.static_value.append(u"ㅔ")
                                self.paintCanvas.configure(background='yellow')
                                time.sleep(1)
                                self.paintCanvas.configure(background='white')
                                self.initializeVal()
                                self.labelUP()
                            self.S27+=1
                            print self.ten
                        if model.predict_classes(predict_data) == [27] and model.predict(predict_data)[0][27]>0.6:
                            if self.S28 == self.mingamdo:
                                print model.predict_classes(predict_data, verbose=0)
                                print "ㅖ 저장완료"
                                self.static_value.append(u"ㅖ")
                                self.paintCanvas.configure(background='yellow')
                                time.sleep(1)
                                self.paintCanvas.configure(background='white')
                                self.initializeVal()
                                self.labelUP()
                            self.S28+=1
                            print self.ten
                        if model.predict_classes(predict_data) == [28] and model.predict(predict_data)[0][28]>0.6:
                            if self.S29 == self.mingamdo:
                                print model.predict_classes(predict_data, verbose=0)
                                print "ㅚ 저장완료"
                                self.static_value.append(u"ㅚ")
                                self.paintCanvas.configure(background='yellow')
                                time.sleep(1)
                                self.paintCanvas.configure(background='white')
                                self.initializeVal()
                                self.labelUP()
                            self.S29+=1
                            print self.ten
                        if model.predict_classes(predict_data) == [29] and model.predict(predict_data)[0][29]>0.6:
                            if self.S30 == self.mingamdo:
                                print model.predict_classes(predict_data, verbose=0)
                                print "ㅟ 저장완료"
                                self.static_value.append(u"ㅟ")
                                self.paintCanvas.configure(background='yellow')
                                time.sleep(1)
                                self.paintCanvas.configure(background='white')
                                self.initializeVal()
                                self.labelUP()
                            self.S30+=1
                            print self.ten
                        if model.predict_classes(predict_data) == [30] and model.predict(predict_data)[0][30]>0.6:
                                if self.S31 == self.mingamdo:
                                    print model.predict_classes(predict_data, verbose=0)
                                    print "ㅢ 저장완료"
                                    self.static_value.append(u"ㅢ")
                                    self.paintCanvas.configure(background='yellow')
                                    time.sleep(1)
                                    self.paintCanvas.configure(background='white')
                                    self.initializeVal()
                                    self.labelUP()
                                self.S31 += 1
                                print self.ten

                        if self.static_value[-1] == self.static_value[-2]:
                                if eq(self.static_value[-1],u"ㄱ"):
                                    self.static_value.pop()
                                    self.static_value.pop()
                                    self.static_value.append(u"ㄲ")

                except:
                    pass
            elif len(frame.hands)==2:
                print "hands two!!!!!!!!!"


        char_to_ix = {ch: i for i, ch in enumerate(self.static_value)}
        ix_to_char = {i: ch for i, ch in enumerate(self.static_value)}
        #print(char_to_ix)
        jamo_numbers = [char_to_ix[x] for x in self.static_value]
        #print(jamo_numbers)
        restored_jamo = ''.join([ix_to_char[x] for x in jamo_numbers])



        i = 0
        for hand in frame.hands:

            arm = hand.arm
            self.wrist_index[0] = interactionBox.normalize_point(arm.wrist_position)
            # self.drawPoint(self.wrist_index[0].x * 600, 400 - self.wrist_index[0].y * 400, 20, 20, color)
            for finger in hand.fingers:
                for b in range(0, 4):
                    bone = finger.bone(b)
                    if b == 1 and i == 0:
                        self.direction_index[0] = interactionBox.normalize_point(bone.next_joint)
                    elif b == 0 and i == 0:
                        self.direction_index[1] = interactionBox.normalize_point(bone.next_joint)
                    elif b == 0 and i == 1:
                        self.direction_index[2] = interactionBox.normalize_point(bone.next_joint)
                    elif b == 0 and i == 2:
                        self.direction_index[3] = interactionBox.normalize_point(bone.next_joint)
                    elif b == 0 and i == 3:
                        self.direction_index[4] = interactionBox.normalize_point(bone.next_joint)
                    elif b == 0 and i == 4:
                        self.direction_index[5] = interactionBox.normalize_point(bone.next_joint)
                        self.drawRect(self.direction_index[0].x * 600, 400 - self.direction_index[0].y * 400,
                                      self.direction_index[1].x * 600, 400 - self.direction_index[1].y * 400,
                                      self.direction_index[2].x * 600, 400 - self.direction_index[2].y * 400,
                                      self.direction_index[3].x * 600, 400 - self.direction_index[3].y * 400,
                                      self.direction_index[4].x * 600, 400 - self.direction_index[4].y * 400,
                                      self.direction_index[5].x * 600,
                                      400 - self.direction_index[5].y * 400, self.wrist_index[0].x * 600,
                                      400 - self.wrist_index[0].y * 400)  # 손바닥 그리기
                    if b == 1 and i == 5:
                        self.direction_index[6] = interactionBox.normalize_point(bone.next_joint)
                    elif b == 0 and i == 5:
                        self.direction_index[7] = interactionBox.normalize_point(bone.next_joint)
                    elif b == 0 and i == 6:
                        self.direction_index[8] = interactionBox.normalize_point(bone.next_joint)
                    elif b == 0 and i == 7:
                        self.direction_index[9] = interactionBox.normalize_point(bone.next_joint)
                    elif b == 0 and i == 8:
                        self.direction_index[10] = interactionBox.normalize_point(bone.next_joint)
                    elif b == 0 and i == 9:
                        self.direction_index[11] = interactionBox.normalize_point(bone.next_joint)
                        self.drawRect(self.direction_index[6].x * 600, 400 - self.direction_index[6].y * 400,
                                      self.direction_index[7].x * 600, 400 - self.direction_index[7].y * 400,
                                      self.direction_index[8].x * 600, 400 - self.direction_index[8].y * 400,
                                      self.direction_index[9].x * 600, 400 - self.direction_index[9].y * 400,
                                      self.direction_index[10].x * 600, 400 - self.direction_index[10].y * 400,
                                      self.direction_index[11].x * 600,
                                      400 - self.direction_index[11].y * 400, self.wrist_index[0].x * 600,
                                      400 - self.wrist_index[0].y * 400)

                    normalbone = interactionBox.normalize_point(bone.prev_joint)
                    normalbone2 = interactionBox.normalize_point(bone.next_joint)

                    # self.drawPoint(normalbone.x * 600, 400 - normalbone.y * 400, 20, 20, color)
                    if not b == 0:
                        self.drawLine(normalbone.x * 600, 400 - normalbone.y * 400, normalbone2.x * 600,
                                      400 - normalbone2.y * 400)
                i += 1



    def drawPoint(self, x, y, width, height, color):
        self.paintCanvas.create_oval(x, y, x + width, y + height, fill="black",
                                     outline="")  # 손가락 마디마다의 점 그리기 //현재 사용 안함

    def drawLine(self, x, y, x2, y2):
        self.paintCanvas.create_line(x, y, x2, y2, fill="black", width=10)  # 손가락 관절 사이사이 그리기


    def drawRect(self, x, y, x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6):  # 손바닥 그리기 함수
        self.paintCanvas.create_polygon(x, y, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6, x1, y1, fill="BLUE")

    def set_canvas(self, canvas):
        self.paintCanvas = canvas

    def rgb_to_hex(self, rgb):
        return '#%02x%02x%02x' % rgb


class PaintBox(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.leap = Leap.Controller()
        self.painter = TouchPointListener()
        self.leap.add_listener(self.painter)
        self.grid(row=0, column=0)


        self.master.title("Touch Points")
        self.master.geometry("1200x900")

        # create Canvas component
        self.paintCanvas = Canvas(self, width="600", height="500")
        self.paintCanvas.pack()
        self.painter.set_canvas(self.paintCanvas)


def main():
    PaintBox().mainloop()


if __name__ == "__main__":

    predict_data = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],"float32")  # 적용 데이터

    # load json and create model
    json_file = open('model.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    model = model_from_json(loaded_model_json)
    # load weights into new model
    model.load_weights("model.h5")
    print("Loaded model from disk")

    # evaluate loaded model on test data
    model.compile(loss='mean_squared_error',
                  optimizer='adam',
                  metrics=['accuracy'])



    main()
