from GUI_EX0413 import TouchPointListener

TouchPointListener.sensitive=TouchPointListener.sensitive
def Sense_Up(event):
    TouchPointListener.sensitive += 2
    print (TouchPointListener.sensitive)

    TouchPointListener.sensitive = TouchPointListener.sensitive



def Sense_Down(event):
    if not TouchPointListener.sensitive == 0:
        TouchPointListener.sensitive -= 2
        print (TouchPointListener.sensitive)
        TouchPointListener.sensitive=TouchPointListener.sensitive
    elif TouchPointListener.sensitive == 0:
        print (TouchPointListener.sensitive)
        print ("nothing nothing")
        TouchPointListener.sensitive=TouchPointListener.sensitive