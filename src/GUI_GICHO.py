#-*-coding: utf-8 -*-
from Tkinter import *
import os, sys, inspect
src_dir = os.path.dirname(inspect.getfile(inspect.currentframe()))
arch_dir = '../lib/x64' if sys.maxsize > 2**32 else '../lib/x86'
sys.path.insert(0, os.path.abspath(os.path.join(src_dir, arch_dir)))
import Leap
from PIL import Image, ImageTk


class TouchPointListener(Leap.Listener):
    middle_font = ('Verdana', 18)
    LB = Listbox(width=30, height=13)
    SB = Scrollbar(orient=VERTICAL)
    LB.config(yscrollcommand=SB.set, font=middle_font)
    SB.config(command=LB.yview)
    SB.pack(side=RIGHT, fill=Y)
    LB.pack(side=LEFT, fill=BOTH, expand=Y)
    SB.place(x=1170, y=50)
    LB.place(x=700, y=50)
    def on_init(self, controller):
        print "Initialized"

    def on_connect(self, controller):
        print "Connected"

    def on_frame(self, controller):
        self.paintCanvas.delete("all")
        frame = controller.frame()

        interactionBox = frame.interaction_box

        for pointable in frame.pointables:
            width = pointable.width
            print width
            print len(frame.pointables)
            direction = pointable.direction
            normalizedPosition = interactionBox.normalize_point(pointable.tip_position)
            if (pointable.touch_distance > 0 and pointable.touch_zone != Leap.Pointable.ZONE_NONE):
                color = self.rgb_to_hex((0, 255 - 255 * pointable.touch_distance, 0))

            elif (pointable.touch_distance <= 0):
                color = self.rgb_to_hex((-255 * pointable.touch_distance, 0, 0))
                # color = self.rgb_to_hex((255,0,0))

            else:
                color = self.rgb_to_hex((0, 0, 200))

            self.draw(normalizedPosition.x * 800, 600 - normalizedPosition.y * 600, 40, 40, color)

    def draw(self, x, y, width, height, color):
        self.paintCanvas.create_oval(x, y, x + width, y + height, fill=color, outline="")
        #self.create_oval.attributes('-alpha', 0.3)

    def set_canvas(self, canvas):
        self.paintCanvas = canvas

    def rgb_to_hex(self, rgb):
        return '#%02x%02x%02x' % rgb


class PaintBox(Frame):
    middle_font = ('Verdana', 18)
    large_font = ('Verdana', 25)

    paintCanvas = Canvas(width="600", height="450")

    def hide_me(self,event):
        event.widget.pack_forget()


    def button1Click(self, event):
        if self.button1["background"] == "green":
            self.button1["background"] = "yellow"
        else:
            self.button1["background"] = "green"

    def button2Click(self, event):
        self.myParent.destroy()

    def show_label(self, event=None):
        self.label.place_forget()

    def hide_label(self, event=None):
        self.label.place_forget()


    def __init__(self):
        Frame.__init__(self)
        self.frame = Frame(self)
        self.frame.pack(side="top", fill="both", expand=True)

        self.label = Label(text="Hello, world")
        self.button1 = Button(text="Click to hide label",
                            command=self.hide_label)

        self.button2 = Button( text="Click to show label",
                            command=self.show_label)
        self.label.pack(in_=self.frame)
        self.button1.pack(in_=self.frame)
        self.button2.pack(in_=self.frame)
        self.pack(in_=self.frame)
        self.frame.place(x=1150, y=400)


        self.leap = Leap.Controller()
        self.painter = TouchPointListener()
        self.leap.add_listener(self.painter)
        self.grid(row=0, column=0)

        self.master.title("HandsTalk")
        self.master.geometry("1300x550")
        self.master.configure(background='light cyan')

        # create Canvas component

        self.paintCanvas.configure(background='white')
        self.paintCanvas.pack(padx=45, pady=45)
        self.paintCanvas.place(x=45, y=45)

        self.painter.set_canvas(self.paintCanvas)

        self.Send_Button = Button(text="OK", borderwidth=0)
        self.send_image = PhotoImage(file="../image/send.gif")
        self.Send_Button.config(image=self.send_image)
        self.Send_Button.pack()

        self.Send_Button.place(x=1150, y=470)

        self.ST_Button = Button(text="인식속도 ↓", background="salmon")
        self.ST_Button.pack()

        self.ST_Button.place(x=1000, y=20)

        self.ST_Button2 = Button(text="인식속도 ↑", background="salmon")
        self.ST_Button2.pack()

        self.ST_Button2.place(x=1070, y=20)

        self.SWITCH_Button = Button(text="수화 하기", background="white", height=80, width=80)
        self.Hand_Image = PhotoImage(file="../image/Two_Hands.gif")
        self.SWITCH_Button.config(image=self.Hand_Image)
        self.SWITCH_Button.pack()

        self.SWITCH_Button.place(x=1150, y=150)

        self.SWITCH_Button2 = Button(text="지화 하기", background="white", height=80, width=80)
        self.Hand_Image2 = PhotoImage(file="../image/One_Hand.gif")
        self.SWITCH_Button2.config(image=self.Hand_Image2)
        self.SWITCH_Button2.pack()

        self.SWITCH_Button2.place(x=1150, y=230)

        self.SWITCH_Button3 = Button(text="숫자 쓰기", background="white", height=80, width=80)
        self.Num_Image = PhotoImage(file="../image/Number.gif")
        self.SWITCH_Button3.config(image=self.Num_Image)
        self.SWITCH_Button3.pack()

        self.SWITCH_Button3.place(x=1150, y=310)




        self.v2 = StringVar(value="")
        self.txt = Entry(textvariable=self.v2, font=self.large_font)

        self.txt.place(x=700, y=480)

        self.link = Label(text="HandsTalk HomePage", fg="blue", cursor="hand2", bg="light cyan")
        self.link.pack()

        self.link.place(x=700, y=20)

        self.Mode = Label(text="지화 MODE", bg="light cyan")
        self.Mode.pack()
        self.Mode.place(x=850, y=20)


def main():
    PaintBox().mainloop()


if __name__ == "__main__":
    main()