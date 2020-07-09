from tkinter import *

from PIL import Image, ImageTk


class HiTech_Button():

    def __init__(self, root, frame, text, funk=None):
        self.button = PhotoImage(file=r"Photo/button.png")
        self.button_active = PhotoImage(master=root, file=(r"Photo/button_active.png"))
        self.button_hover = PhotoImage(master=root, file=(r"Photo/button_hover.png"))
        self.btn = Label(frame, text=text, image=self.button, bg="#00171f", compound=CENTER, fg="#4bdddd", font=("", 10), bd=0)
        self.btn.bind('<ButtonPress-1>', self.on_press)
        self.btn.bind('<ButtonRelease-1>', self.on_rel)
        self.btn.bind('<Enter>', self.on_enter)
        self.btn.bind('<Leave>', self.on_leave)
        self.funk = funk

    def on_press(self, event):
        self.btn.configure(fg="#3fa0eb", image=self.button_active)
        if self.funk != None:
            self.funk()

    def on_rel(self, event):
        self.btn.configure(fg="#4bdddd", image=self.button)

    def on_enter(self, event):
        self.btn.configure(image=self.button_hover)

    def on_leave(self, event):
        self.btn.configure(image=self.button)


class HiTech_Question():

    def __init__(self, root, frame, funk=None):
        self.button = PhotoImage(file=r"Photo/question.png")
        self.button_active = PhotoImage(master=root, file=(r"Photo/question_active.png"))
        self.button_hover = PhotoImage(master=root, file=(r"Photo/question_hover.png"))
        self.btn = Label(frame, image=self.button, bg="#00171f", compound=CENTER, bd=0)
        self.btn.bind('<ButtonPress-1>', self.on_press)
        self.btn.bind('<ButtonRelease-1>', self.on_rel)
        self.btn.bind('<Enter>', self.on_enter)
        self.btn.bind('<Leave>', self.on_leave)
        self.funk = funk

    def on_press(self, event):
        self.btn.configure(image=self.button_active)
        if self.funk != None:
            self.funk()

    def on_rel(self, event):
        self.btn.configure(image=self.button)

    def on_enter(self, event):
        self.btn.configure(image=self.button_hover)

    def on_leave(self, event):
        self.btn.configure(image=self.button)


class HiTech_Label():

    def __init__(self, frame, text, type):
        self.label_l = ImageTk.PhotoImage(Image.open(r"Photo/label_left.png"))
        self.label_r = ImageTk.PhotoImage(Image.open(r"Photo/label_right.png"))
        if type == 1:
            self.lbl = Label(frame, text=text, image=self.label_l, bg="#00171f", compound=CENTER, fg="#4bdddd", font=("", 10), bd=0)
            self.lbl.image = self.label_l
        else:
            self.lbl = Label(frame, text=text, image=self.label_r, bg="#00171f", compound=CENTER, fg="#4bdddd", font=("", 10), bd=0)
            self.lbl.image = self.label_r
