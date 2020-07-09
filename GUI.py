from tkinter import *
from PIL import Image, ImageTk
from Practice_window import PracticeWindow
from disign_for_GUI import HiTech_Button, HiTech_Question, HiTech_Label

root = Tk()
hexagon = PhotoImage(file=r"Photo/Animation/hexagon/43.gif")
hexagon_frame_counter = 43
load = PhotoImage(file=r"Photo/Animation/load/0.gif")
load_frame_counter = 0
radar = PhotoImage(file=r"Photo/Animation/radar/radar000.png")
radar_frame_counter = 0
logo = PhotoImage(file=r"Photo\Animation\DNA\0.gif")
logo_frame_counter = 0
connecting = PhotoImage(file=r"Photo\Animation\connecting\0.gif")
connecting_frame_counter = 0
binary = PhotoImage(file=r"Photo\Animation\binary\0.gif")
binary_frame_counter = 0


class Main:
    background_color = '#000f16'
    front_color = '#E8E8E7'
    button_color = '#FF8C00'
    active_background_color = '#284C79'
    entry_background = '#002475'
    frame_right = PhotoImage(file=r"Photo/frame1.png")
    frame_bottom = PhotoImage(file=r"Photo/frame3.png")
    frame_left = ImageTk.PhotoImage(Image.open(r"Photo/frame2.png"))
    # bottom_logo = PhotoImage(file=(r"Photo/bottom_logo.png"))
    question = ImageTk.PhotoImage(Image.open(r"Photo/question.png"))
    load_logo = PhotoImage(file=r"Photo/Animation/load/load_logo.png")
    bg_image = PhotoImage(file=r"Photo/background.png")

    def __init__(self):
        global hexagon, hexagon_animation, radar, radar_animation, logo, DNA_animation, load, load_animation, connecting, connecting_animation, binary, binary_animation

        hexagon_animation()
        radar_animation()
        DNA_animation()
        load_animation()
        connecting_animation()
        binary_animation()

        left_side = Frame(root, bg=self.background_color)
        right_side = Frame(root, bg=self.background_color)
        center_side = Frame(root, bg=self.background_color)
        canvas = Canvas(center_side, width=1200, height=580, bd=0, highlightthickness=0, bg=self.background_color)
        canvas.pack()
        left_side.pack(side=LEFT)
        # right_side.pack(side=RIGHT)
        center_side.pack(side=RIGHT, padx=10, pady=20)

        # LEFT SIDE
        # self.img_main = ImageTk.PhotoImage(Image.open(r"Photo/rbr.png"))
        # label = Label(left_side, image=self.img_main, bg=self.background_color)
        # label.pack()
        # root.wm_attributes("-transparentcolor", self.background_color)
        hexagon_label = Label(center_side, image=hexagon, bg="#00171f", compound=CENTER, fg="#4bdddd", font=("", 10), bd=0)

        # RIGHT SIDE

        right_part = Frame(right_side, bg=self.background_color)
        left_part = Frame(right_side, bg=self.background_color)
        right_part.pack(side=RIGHT)
        left_part.pack(side=LEFT)

        canvas.create_image(0, 99, image=binary, anchor=NW)
        canvas.create_image(460, 300, image=connecting, anchor=NW)
        canvas.create_image(678, 370, image=load, anchor=NW)
        canvas.create_image(459, 121, image=logo, anchor=NW)
        canvas.create_image(641, 121, image=self.bg_image, anchor=NW)
        canvas.create_image(0, 0, image=self.frame_left, anchor=NW)
        canvas.create_image(481, 405, image=hexagon, anchor=NW)
        canvas.create_image(38, 90, image=radar, anchor=NW)
        canvas.create_image(670, 0, image=self.frame_right, anchor=NW)
        canvas.create_image(670, 380, image=self.frame_bottom, anchor=NW)
        # canvas.create_image(783, 475, image=self.load_logo, anchor=NW)

        label1 = HiTech_Label(center_side, "Теорія", 1)
        button1 = HiTech_Button(root, center_side, "Лабораторна робота №1")
        button2 = HiTech_Button(root, center_side, "Лабораторна робота №2")
        button3 = HiTech_Button(root, center_side, "Лабораторна робота №3")
        button4 = HiTech_Button(root, center_side, "Лабораторна робота №4")
        button5 = HiTech_Button(root, center_side, "Лабораторна робота №5")
        question = HiTech_Question(root, center_side)

        lbl1 = canvas.create_window(700, 50, anchor=NW, window=label1.lbl)
        btn1 = canvas.create_window(700, 90, anchor=NW, window=button1.btn)
        btn2 = canvas.create_window(700, 140, anchor=NW, window=button2.btn)
        btn3 = canvas.create_window(700, 190, anchor=NW, window=button3.btn)
        btn4 = canvas.create_window(700, 240, anchor=NW, window=button4.btn)
        btn5 = canvas.create_window(700, 290, anchor=NW, window=button5.btn)
        quest = canvas.create_window(982, 420, anchor=NW, window=question.btn)

        label2 = HiTech_Label(center_side, "Практика", 2)
        button6 = HiTech_Button(root, center_side, "Множення", lambda: practice_window.multiplication_window(root))
        button7 = HiTech_Button(root, center_side, "Ділення", lambda: practice_window.division_window(root))
        button8 = HiTech_Button(root, center_side, "Додавання", lambda: practice_window.addition_window(root))
        button9 = HiTech_Button(root, center_side, "Корінь", lambda: practice_window.sqrt_window(root))
        button10 = HiTech_Button(root, center_side, "Перетворення чисел", lambda: practice_window.convert_window(root))

        lbl1 = canvas.create_window(920, 50, anchor=NW, window=label2.lbl)
        btn6 = canvas.create_window(928, 90, anchor=NW, window=button6.btn)
        btn7 = canvas.create_window(928, 140, anchor=NW, window=button7.btn)
        btn8 = canvas.create_window(928, 190, anchor=NW, window=button8.btn)
        btn9 = canvas.create_window(928, 240, anchor=NW, window=button9.btn)
        btn10 = canvas.create_window(928, 290, anchor=NW, window=button10.btn)

        label1 = Label(left_part, width=21, text="Теорія", font=("Arial", 12), fg=self.front_color, bg=self.entry_background,
                       relief=FLAT)
        button_lab1 = Button(left_part, width=21, text="Лабораторна робота №1", font=("Arial", 12), bg=self.button_color,
                             activebackground=self.active_background_color, relief=GROOVE)
        button_lab2 = Button(left_part, width=21, text="Лабораторна робота №2", font=("Arial", 12), bg=self.button_color,
                             activebackground=self.active_background_color, relief=GROOVE)
        button_lab3 = Button(left_part, width=21, text="Лабораторна робота №3", font=("Arial", 12), bg=self.button_color,
                             activebackground=self.active_background_color, relief=GROOVE)
        button_lab4 = Button(left_part, width=21, text="Лабораторна робота №4", font=("Arial", 12), bg=self.button_color,
                             activebackground=self.active_background_color, relief=GROOVE)
        button_lab5 = Button(left_part, width=21, text="Лабораторна робота №5", font=("Arial", 12), bg=self.button_color,
                             activebackground=self.active_background_color, relief=GROOVE)

        label2 = Label(left_part, width=21, text="Практика", font=("Arial", 12), fg=self.front_color, bg=self.entry_background,
                       relief=FLAT)
        button_multiplication = Button(left_part, width=21, text="Множення", font=("Arial", 12), bg=self.button_color,
                                       activebackground=self.active_background_color, relief=GROOVE, command=lambda: practice_window.multiplication_window(root))
        button_division = Button(left_part, width=21, text="Ділення", font=("Arial", 12), bg=self.button_color,
                                 activebackground=self.active_background_color, relief=GROOVE, command=lambda: practice_window.division_window(root))
        button_addition = Button(left_part, width=21, text="Додавання", font=("Arial", 12), bg=self.button_color,
                                 activebackground=self.active_background_color, relief=GROOVE, command=lambda: practice_window.addition_window(root))
        button_sqrt = Button(left_part, width=21, text="Корінь", font=("Arial", 12), bg=self.button_color,
                             activebackground=self.active_background_color, relief=GROOVE, command=lambda: practice_window.sqrt_window(root))
        button_number_conversion = Button(left_part, width=21, text="Перетворення чисел", font=("Arial", 12), bg=self.button_color,
                                          activebackground=self.active_background_color, relief=GROOVE, command=lambda: practice_window.convert_window(root))
        label1.grid(row=0, column=0, padx=15, pady=10)
        button_lab1.grid(row=1, column=0, padx=15, pady=10)
        button_lab2.grid(row=2, column=0, padx=15, pady=10)
        button_lab3.grid(row=3, column=0, padx=15, pady=10)
        button_lab4.grid(row=4, column=0, padx=15, pady=10)
        button_lab5.grid(row=5, column=0, padx=15, pady=10)

        label2.grid(row=0, column=1, padx=15, pady=10)
        button_multiplication.grid(row=1, column=1, padx=15, pady=10)
        button_division.grid(row=2, column=1, padx=15, pady=10)
        button_addition.grid(row=3, column=1, padx=15, pady=10)
        button_sqrt.grid(row=4, column=1, padx=15, pady=10)
        button_number_conversion.grid(row=5, column=1, padx=15, pady=10)


# def on_closing():
#     if tkinter.messagebox.askokcancel("Quit", "Do you want to quit?"):
#         root.destroy()
def hexagon_animation():
    global hexagon, hexagon_frame_counter
    hexagon_frame_counter += 1

    if hexagon_frame_counter == 93:
        hexagon_frame_counter = 43
    hexagon["file"] = "Photo\\Animation\\hexagon\\" + str(hexagon_frame_counter) + ".gif"
    root.after(25, hexagon_animation)


def load_animation():
    global load, load_frame_counter
    load_frame_counter += 1
    if load_frame_counter == 59:
        load_frame_counter = 0
    load["file"] = "Photo\\Animation\\load\\" + str(load_frame_counter) + ".gif"
    root.after(25, load_animation)


def radar_animation():
    global radar, radar_frame_counter
    radar_frame_counter += 1

    if radar_frame_counter == 80:
        radar_frame_counter = 0
    radar["file"] = "Photo\\Animation\\radar\\radar00" + str(radar_frame_counter) + ".png"
    root.after(25, radar_animation)


def DNA_animation():
    global logo, logo_frame_counter
    logo_frame_counter += 1
    if logo_frame_counter == 59:
        logo_frame_counter = 0
    logo["file"] = "Photo\\Animation\\DNA\\" + str(logo_frame_counter) + ".gif"
    root.after(25, DNA_animation)


def connecting_animation():
    global connecting, connecting_frame_counter
    connecting_frame_counter += 1
    if connecting_frame_counter == 59:
        connecting_frame_counter = 0
    connecting["file"] = "Photo\\Animation\\connecting\\" + str(connecting_frame_counter) + ".gif"
    root.after(55, connecting_animation)


def binary_animation():
    global binary, binary_frame_counter
    binary_frame_counter += 1
    if binary_frame_counter == 11:
        binary_frame_counter = 0
    binary["file"] = "Photo\\Animation\\binary\\" + str(binary_frame_counter) + ".gif"
    root.after(95, binary_animation)


# root.protocol("WM_DELETE_WINDOW", on_closing)


root.configure(background='#000f16')
root.title("Комп'ютерна арифметика")
root.resizable(width=False, height=False)
practice_window = PracticeWindow()

program = Main()
root.mainloop()
