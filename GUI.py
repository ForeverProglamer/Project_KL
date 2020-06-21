from tkinter import *
import tkinter.messagebox
from PIL import Image, ImageTk


class Main:
    background_color = '#002451'
    front_color = '#E8E8E7'
    button_color = '#FF8C00'
    active_background_color = '#284C79'
    entry_background = '#002475'

    def __init__(self, main):
        self.main = root

        # main_menu = Menu(root)
        # elements_of_menu = Menu(main_menu, tearoff=0)
        # main_menu.add_cascade(label="Menu", menu=elements_of_menu)
        # elements_of_menu.add_command(label="Лабораторна робота №1")
        # elements_of_menu.add_command(label="Лабораторна робота №2")
        # elements_of_menu.add_command(label="Лабораторна робота №3")
        # elements_of_menu.add_command(label="Лабораторна робота №4")
        # root.config(menu=main_menu)

        left_side = Frame(root, bg=self.background_color)
        right_side = Frame(root, bg=self.background_color)
        left_side.pack(side=LEFT)
        right_side.pack(side=RIGHT)

        # LEFT SIDE
        img = ImageTk.PhotoImage(Image.open(r"Photo\rb.png"))
        label = Label(left_side, image=img)
        label.pack()

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
                                       activebackground=self.active_background_color, relief=GROOVE)
        button_division = Button(left_part, width=21, text="Ділення", font=("Arial", 12), bg=self.button_color,
                                 activebackground=self.active_background_color, relief=GROOVE)
        button_addition = Button(left_part, width=21, text="Додавання", font=("Arial", 12), bg=self.button_color,
                                 activebackground=self.active_background_color, relief=GROOVE)

        button_sqrt = Button(left_part, width=21, text="Корінь", font=("Arial", 12), bg=self.button_color,
                             activebackground=self.active_background_color, relief=GROOVE)

        button_number_conversion = Button(left_part, width=21, text="Перетворення чисел", font=("Arial", 12), bg=self.button_color,
                                          activebackground=self.active_background_color, relief=GROOVE)

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


root = Tk()
root.configure(background='#002451')
root.title("Комп'ютерна арифметика")
root.resizable(width=False, height=False)
program = Main(root)
root.mainloop()
