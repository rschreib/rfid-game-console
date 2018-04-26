from tkinter import *

window = Tk()
windowWidth = 1080
windowHeight = 540
s = str(windowWidth) + 'x' + str(windowHeight) + '-5+40'
window.geometry(s)

window.configure(background="#181818")

oldtitle = window.title()
window.title('CSCI250 Final Project Game')

label_1 = Label(window, text="Username")
entry_1 = Entry(window)
label_2 = Label(window, text=" Password")
entry_2 = Entry(window)

label_1.place(x=windowWidth/2-8, y=windowHeight/2-14, anchor=E)
label_2.place(x=windowWidth/2-8, y=windowHeight/2+14, anchor=E)
entry_1.place(x=windowWidth/2, y=windowHeight/2-13, anchor=W)
entry_2.place(x=windowWidth/2, y=windowHeight/2+13, anchor=W)

window.mainloop()

# orange - #D86D03  