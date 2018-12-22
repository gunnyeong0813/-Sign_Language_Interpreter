# -*- coding: utf-8 -*-


#pip install gTTS
#pip install playsound
from gtts import gTTS

import pygame
import time
tts = gTTS(text='만나서 반갑습니다.', lang='ko')
tts.save("tts.mp3")

# p = vlc.MediaPlayer("C:\Users\Gunnyeong\Desktop\HANDST~2\speak.mp3")
# p.play()
import playsound
playsound.playsound('tts.mp3', True)
