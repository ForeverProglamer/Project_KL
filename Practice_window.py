from tkinter import *


class PracticeWindow:
    background_color = '#002451'
    front_color = '#E8E8E7'
    button_color = '#FF8C00'
    active_background_color = '#284C79'
    entry_background = '#002475'

    def window_for_practice(self, root):
        self.practice_window = Toplevel(root)
        self.practice_window.configure(background=self.background_color)
        self.practice_window.resizable(width=False, height=False)

        main_menu = Menu(self.practice_window)
        main_menu.add_command(label="Головне меню")
        main_menu.add_command(label="Перейти до теорії")
        main_menu.add_command(label="Зберегти у файл")
        self.practice_window.config(menu=main_menu)

        left_part = Frame(self.practice_window, bg=self.background_color)
        right_part = Frame(self.practice_window, bg=self.background_color)
        left_part.pack(side=LEFT)
        right_part.pack(fill=BOTH)

        #  Left part
        frame_x = Frame(left_part, bg=self.background_color)
        frame_x.pack(pady=5)
        frame_y = Frame(left_part, bg=self.background_color)
        frame_y.pack(pady=5)
        frame_for_button = Frame(left_part, bg=self.background_color)
        frame_for_button.pack(pady=10)

        order_x = Label(frame_x, width=21, text="Порядок X", font=("Arial", 12), fg=self.front_color, bg=self.entry_background,
                        relief=FLAT)
        entry_for_poryadok_x = Entry(frame_x, bg=self.entry_background, fg=self.front_color, width=7, font=("", 13), justify=CENTER, relief=FLAT)
        sign_x = Label(frame_x, width=21, text="Занак X", font=("Arial", 12), fg=self.front_color, bg=self.entry_background,
                       relief=FLAT)
        entry_for_sign_x = Entry(frame_x, bg=self.entry_background, fg=self.front_color, width=7, font=("", 13), justify=CENTER, relief=FLAT)

        mantissa_x = Label(frame_x, width=21, text="Мантиса X", font=("Arial", 12), fg=self.front_color, bg=self.entry_background,
                           relief=FLAT)
        entry_for_mantissa_x = Entry(frame_x, bg=self.entry_background, fg=self.front_color, width=7, font=("", 13), justify=CENTER, relief=FLAT)

        order_y = Label(frame_y, width=21, text="Порядок Y", font=("Arial", 12), fg=self.front_color, bg=self.entry_background,
                        relief=FLAT)
        entry_for_poradok_y = Entry(frame_y, bg=self.entry_background, fg=self.front_color, width=7, font=("", 13), justify=CENTER, relief=FLAT)
        sign_y = Label(frame_y, width=21, text="Занак Y", font=("Arial", 12), fg=self.front_color, bg=self.entry_background,
                       relief=FLAT)
        entry_for_sign_y = Entry(frame_y, bg=self.entry_background, fg=self.front_color, width=7, font=("", 13), justify=CENTER, relief=FLAT)

        mantissa_y = Label(frame_y, width=21, text="Мантиса Y", font=("Arial", 12), fg=self.front_color, bg=self.entry_background,
                           relief=FLAT)
        entry_for_mantissa_y = Entry(frame_y, bg=self.entry_background, fg=self.front_color, width=7, font=("", 13), justify=CENTER, relief=FLAT)

        order_x.grid(row=0, column=0, padx=8, pady=10)
        entry_for_poryadok_x.grid(row=0, column=1, padx=8, pady=10)
        sign_x.grid(row=1, column=0, padx=8, pady=10)
        entry_for_sign_x.grid(row=1, column=1, padx=8, pady=10)
        mantissa_x.grid(row=2, column=0, padx=8, pady=10)
        entry_for_mantissa_x.grid(row=2, column=1, padx=8, pady=10)

        order_y.grid(row=0, column=0, padx=8, pady=10)
        entry_for_poradok_y.grid(row=0, column=1, padx=8, pady=10)
        sign_y.grid(row=1, column=0, padx=8, pady=5)
        entry_for_sign_y.grid(row=1, column=1, padx=8, pady=10)
        mantissa_y.grid(row=2, column=0, padx=8, pady=5)
        entry_for_mantissa_y.grid(row=2, column=1, padx=8, pady=10)

        confirm_button = Button(left_part, width=11, text="Порахувати", font=("Arial", 12), bg=self.button_color,
                                activebackground=self.active_background_color, relief=GROOVE)
        confirm_button.pack()

        # right part
        frame_for_label = Frame(right_part, bg=self.background_color)
        frame_for_label.pack(side=TOP, fill=BOTH)
        self.label_of_current_operation = Label(frame_for_label, bg='#A9B7C6', fg="#141781", font=("Ubuntu", 20), text="CURRENT OPERATION")
        self.label_of_current_operation.pack(side=TOP, fill=X)

        frame_for_text = Frame(right_part, bg=self.background_color)
        frame_for_text.pack(fill=BOTH)

        text = Text(frame_for_text, width=75, height=20, font=("Times", 15), wrap=WORD, bg='#284C79', fg='#A9B7C6', relief=FLAT, yscrollcommand=set())
        scrollb_y = Scrollbar(frame_for_text, command=text.yview)
        text['yscrollcommand'] = scrollb_y.set
        scrollb_y.pack(fill=Y, side=RIGHT)
        text.pack(side=LEFT, fill=BOTH)

        frame_for_logo = Frame(right_part, bg='#002451')
        frame_for_logo.pack(pady=10, side=BOTTOM, fill=BOTH)
        logo = Label(frame_for_logo, font=('Ubuntu', 15), text="LOGO", bg='#002451', fg='#A9B7C6')
        logo.pack(side=RIGHT)

    def multiplication_window(self, root):
        try:
            if self.practice_window.winfo_viewable():
                print("Window for practice exists")
        except AttributeError:
            print("Window not exists")
            self.window_for_practice(root)

        self.practice_window.title("Операція множення")
        self.label_of_current_operation["text"] = "Множення двійкових чисел"
        self.practice_window.protocol("WM_DELETE_WINDOW", self.on_closing_practice_window)

    def division_window(self, root):
        try:
            if self.practice_window.winfo_exists():
                print('Window for practice exists')

        except AttributeError:
            print("Window not exists")
            self.window_for_practice(root)

        self.practice_window.title("Операція ділення")
        self.label_of_current_operation["text"] = "Ділення двійкових чисел"
        self.practice_window.protocol("WM_DELETE_WINDOW", self.on_closing_practice_window)

    def addition_window(self, root):
        try:
            if self.practice_window.winfo_exists():
                print('Window for practice exists')
        except AttributeError:
            print("Window not exists")
            self.window_for_practice(root)

        self.practice_window.title("Операція додавання")
        self.label_of_current_operation["text"] = "Додавання двійкових чисел"
        self.practice_window.protocol("WM_DELETE_WINDOW", self.on_closing_practice_window)

    def sqrt_window(self, root):
        try:
            if self.practice_window.winfo_exists():
                print('Window for practice exists')
        except AttributeError:
            print("Window not exists")
            self.window_for_practice(root)

        self.practice_window.title("Операція добування корення")
        self.label_of_current_operation["text"] = "Добування корення"
        self.practice_window.protocol("WM_DELETE_WINDOW", self.on_closing_practice_window)

    def convert_window(self, root):
        try:
            if self.practice_window.winfo_exists():
                print('Window for practice exists')
        except AttributeError:
            print("Window not exists yet")
            self.window_for_practice(root)

        self.practice_window.title("Операція перетворення чисел")
        self.label_of_current_operation["text"] = "Перетворення двійкових чисел"
        self.practice_window.protocol("WM_DELETE_WINDOW", self.on_closing_practice_window)

    def on_closing_practice_window(self):
        self.practice_window.destroy()
        del self.practice_window
