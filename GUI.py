from tkinter import *
from PIL import Image, ImageTk
from Practice_window import PracticeWindow
from Theory_window import TheoryWindow

class Main:
    background_color = '#002451'
    front_color = '#E8E8E7'
    button_color = '#FF8C00'
    active_background_color = '#284C79'
    entry_background = '#002475'

    def __init__(self):
        left_side = Frame(root, bg=self.background_color)
        right_side = Frame(root, bg=self.background_color)
        left_side.pack(side=LEFT)
        right_side.pack(side=RIGHT)

        # LEFT SIDE
        self.img_main = ImageTk.PhotoImage(Image.open(r"Photo/rbr.png"))
        label = Label(left_side, image=self.img_main, bg=self.background_color)
        label.pack()
        # root.wm_attributes("-transparentcolor", self.background_color)

        # RIGHT SIDE
        right_part = Frame(right_side, bg=self.background_color)
        left_part = Frame(right_side, bg=self.background_color)
        right_part.pack(side=RIGHT)
        left_part.pack(side=LEFT)

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


root = Tk()
# root.protocol("WM_DELETE_WINDOW", on_closing)

root.configure(background='#002451')
root.title("Комп'ютерна арифметика")
root.resizable(width=False, height=False)
practice_window = PracticeWindow()
theory_window = TheoryWindow()
program = Main()
root.mainloop()
