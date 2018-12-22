# -*- coding: utf-8 -*-

def drawPoint(self, x, y, width, height):
    self.paintCanvas.create_oval(x, y, x + width, y + height, fill="black")  # 손가락 마디마다의 점 그리기 //현재 사용 안함


def drawLine(self,x, y, x2, y2):
    linecolor = '#%02x%02x%02x' % (217, 217, 217)
    self.paintCanvas.create_line(x, y, x2, y2, fill=linecolor, width=13)  # 손가락 관절 사이사이 그리기


def drawRect(self, x, y, x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6):  # 손바닥 그리기 함수
    rectcolor = '#%02x%02x%02x' % (166 ,166, 166)
    self.paintCanvas.create_polygon(x, y, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6, x1, y1, fill=rectcolor)


def drawRect2(self, x, y, x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6):  # 손바닥 그리기 함수
    self.paintCanvas.create_polygon(x - 0.1, y - 0.1, x2 - 0.1, y2 - 0.1, x3 - 0.1, y3 - 0.1, x4 - 0.1, y4 - 0.1,
                                    x5 - 0.1, y5 - 0.1, x6 - 0.1, y6 - 0.1, x1 - 0.1, y1 - 0.1, fill="black")