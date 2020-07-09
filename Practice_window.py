from tkinter import *
import tkinter.messagebox
import multiplication
import memory_buffer


class PracticeWindow:
    background_color = '#00171f'
    front_color = '#65ffff'
    button_color = '#1b4d4c'
    active_background_color = '#284C79'
    entry_background = '#1b4d4c'

    def window_for_practice(self, root):

        def on_up(event):
            current_focus = self.practice_window.focus_get().winfo_id()
            if current_focus == self.entry_for_sign_x.winfo_id():
                self.entry_for_order_x.focus()
            elif current_focus == self.entry_for_mantissa_x.winfo_id():
                self.entry_for_sign_x.focus()
            elif current_focus == self.entry_for_order_y.winfo_id():
                self.entry_for_mantissa_x.focus()
            elif current_focus == self.entry_for_sign_y.winfo_id():
                self.entry_for_order_y.focus()
            elif current_focus == self.entry_for_mantissa_y.winfo_id():
                self.entry_for_sign_y.focus()

        def on_down(event):
            current_focus = self.practice_window.focus_get().winfo_id()
            if current_focus == self.entry_for_order_x.winfo_id():
                self.entry_for_sign_x.focus()
            elif current_focus == self.entry_for_sign_x.winfo_id():
                self.entry_for_mantissa_x.focus()
            elif current_focus == self.entry_for_mantissa_x.winfo_id():
                self.entry_for_order_y.focus()
            elif current_focus == self.entry_for_order_y.winfo_id():
                self.entry_for_sign_y.focus()
            elif current_focus == self.entry_for_sign_y.winfo_id():
                self.entry_for_mantissa_y.focus()

        def focus_out(event):
            if event.widget.winfo_id() == self.entry_for_sign_x.winfo_id():
                pass

        self.practice_window = Toplevel(root)
        self.practice_window.configure(background=self.background_color)
        # self.practice_window.resizable(width=False, height=False)

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

        self.option_variable = StringVar(frame_x)
        self.option_variable.set("1")

        self.option_menu = OptionMenu(frame_x, self.option_variable, "1", "2", "3", "4", )
        self.option_menu["background"] = self.entry_background
        self.option_menu["justify"] = "center"
        self.option_menu["activebackground"] = self.active_background_color
        self.option_menu["fg"] = self.front_color
        self.option_menu['highlightthickness'] = 1
        self.option_menu["borderwidth"] = 0
        self.option_menu["indicatoron"] = 0
        self.option_menu["relief"]: FLAT
        self.option_menu["anchor"] = "c"

        self.method_of_operation = Label(frame_x, width=21, text="Спосіб операції", font=("Arial", 12), fg=self.front_color, bg=self.entry_background,
                                         relief=FLAT)
        order_x = Label(frame_x, width=21, text="Порядок X", font=("Arial", 12), fg=self.front_color, bg=self.entry_background,
                        relief=FLAT)
        self.entry_for_order_x = Entry(frame_x, bg=self.entry_background, fg=self.front_color, width=7, font=("", 13), justify=CENTER, relief=FLAT)
        sign_x = Label(frame_x, width=21, text="Знак X", font=("Arial", 12), fg=self.front_color, bg=self.entry_background,
                       relief=FLAT)
        self.entry_for_sign_x = Entry(frame_x, bg=self.entry_background, fg=self.front_color, width=7, font=("", 13), justify=CENTER, relief=FLAT)

        mantissa_x = Label(frame_x, width=21, text="Мантиса X", font=("Arial", 12), fg=self.front_color, bg=self.entry_background,
                           relief=FLAT)
        self.entry_for_mantissa_x = Entry(frame_x, bg=self.entry_background, fg=self.front_color, width=7, font=("", 13), justify=CENTER, relief=FLAT)

        order_y = Label(frame_y, width=21, text="Порядок Y", font=("Arial", 12), fg=self.front_color, bg=self.entry_background,
                        relief=FLAT)
        self.entry_for_order_y = Entry(frame_y, bg=self.entry_background, fg=self.front_color, width=7, font=("", 13), justify=CENTER, relief=FLAT)
        sign_y = Label(frame_y, width=21, text="Знак Y", font=("Arial", 12), fg=self.front_color, bg=self.entry_background,
                       relief=FLAT)
        self.entry_for_sign_y = Entry(frame_y, bg=self.entry_background, fg=self.front_color, width=7, font=("", 13), justify=CENTER, relief=FLAT)

        mantissa_y = Label(frame_y, width=21, text="Мантиса Y", font=("Arial", 12), fg=self.front_color, bg=self.entry_background,
                           relief=FLAT)
        self.entry_for_mantissa_y = Entry(frame_y, bg=self.entry_background, fg=self.front_color, width=7, font=("", 13), justify=CENTER, relief=FLAT)

        self.method_of_operation.grid(row=0, column=0, padx=8, pady=20)
        self.option_menu.grid(row=0, column=1, padx=8, pady=10, sticky=W)
        order_x.grid(row=1, column=0, padx=8, pady=10)
        self.entry_for_order_x.grid(row=1, column=1, padx=8, pady=10)
        sign_x.grid(row=2, column=0, padx=8, pady=10)
        self.entry_for_sign_x.grid(row=2, column=1, padx=8, pady=10)
        mantissa_x.grid(row=3, column=0, padx=8, pady=10)
        self.entry_for_mantissa_x.grid(row=3, column=1, padx=8, pady=10)

        order_y.grid(row=0, column=0, padx=8, pady=10)
        self.entry_for_order_y.grid(row=0, column=1, padx=8, pady=10)
        sign_y.grid(row=1, column=0, padx=8, pady=5)
        self.entry_for_sign_y.grid(row=1, column=1, padx=8, pady=10)
        mantissa_y.grid(row=2, column=0, padx=8, pady=5)
        self.entry_for_mantissa_y.grid(row=2, column=1, padx=8, pady=10)

        self.confirm_button = Button(left_part, width=11, text="Порахувати", font=("Arial", 12), bg=self.button_color,
                                     activebackground=self.active_background_color, relief=GROOVE)
        self.confirm_button.pack()

        # right part
        frame_for_label = Frame(right_part, bg=self.background_color)
        frame_for_label.pack(side=TOP, fill=BOTH)
        self.label_of_current_operation = Label(frame_for_label, bg='#1b4d4c', fg="#65ffff", font=("Ubuntu", 20), text="CURRENT OPERATION")
        self.label_of_current_operation.pack(side=TOP, fill=X)

        self.frame_for_text = Frame(right_part, bg=self.background_color)
        self.frame_for_text.pack(fill=BOTH, pady=30)

        # text = Text(self.frame_for_text, width=75, height=20, font=("Times", 15), wrap=WORD, bg='#284C79', fg='#A9B7C6', relief=FLAT, yscrollcommand=set())
        # scrollb_y = Scrollbar(self.frame_for_text, command=text.yview)
        # text['yscrollcommand'] = scrollb_y.set
        # scrollb_y.pack(fill=Y, side=RIGHT)
        # text.pack(side=LEFT, fill=BOTH)

        frame_for_logo = Frame(right_part, bg='#1b4d4c')
        frame_for_logo.pack(pady=10, side=BOTTOM, fill=BOTH)
        logo = Label(frame_for_logo, font=('Ubuntu', 15), text="LOGO", bg='#002451', fg='#65ffff')
        logo.pack(side=RIGHT)

        #  binding
        self.entry_for_order_x.bind("<Down>", on_down)
        self.entry_for_sign_x.bind("<Down>", on_down)
        self.entry_for_mantissa_x.bind("<Down>", on_down)
        self.entry_for_order_y.bind("<Down>", on_down)
        self.entry_for_sign_y.bind("<Down>", on_down)
        self.entry_for_mantissa_y.bind("<Down>", on_down)

        self.entry_for_order_x.bind("<Up>", on_up)
        self.entry_for_sign_x.bind("<Up>", on_up)
        self.entry_for_mantissa_x.bind("<Up>", on_up)
        self.entry_for_order_y.bind("<Up>", on_up)
        self.entry_for_sign_y.bind("<Up>", on_up)
        self.entry_for_mantissa_y.bind("<Up>", on_up)

        self.entry_for_order_x.bind("<FocusOut>", focus_out)
        self.entry_for_sign_x.bind("<FocusOut>", focus_out)
        self.entry_for_mantissa_x.bind("<FocusOut>", focus_out)
        self.entry_for_order_y.bind("<FocusOut>", focus_out)
        self.entry_for_sign_y.bind("<FocusOut>", focus_out)
        self.entry_for_mantissa_y.bind("<FocusOut>", focus_out)

    def multiplication_window(self, root):
        def multiply():
            self.destroy_labels()
            self.check_all_entry()
            multiplication.calculate((int(self.option_variable.get()) - 1),
                                     self.entry_for_order_x.get(),
                                     self.entry_for_order_y.get(),
                                     self.entry_for_sign_x.get(),
                                     self.entry_for_sign_y.get(),
                                     self.entry_for_mantissa_x.get(),
                                     self.entry_for_mantissa_y.get())

            for i in range(len(memory_buffer.memory[0])):
                for j in range(len(memory_buffer.memory[0][i])):
                    display_label = Label(self.frame_for_text, text="\n", bg="#1b4d4c", fg='#65ffff', font=("times", 20), justify=CENTER,
                                          relief=FLAT)
                    display_label["text"] = memory_buffer.memory[0][i][j]
                    display_label.grid(row=i + 1, column=j + 1, padx=3, pady=4)
                    self.result_labels.append(display_label)
            self.check_all_entry()
            (int(self.option_variable.get()) - 1)

        self.check_existence_of_window(root)

        self.result_labels = []
        self.practice_window.title("Операція множення")
        self.label_of_current_operation["text"] = "Множення двійкових чисел"
        self.confirm_button["command"] = multiply
        self.method_of_operation["text"] = "Спосіб множення"

        self.reset_table()
        self.practice_window.protocol("WM_DELETE_WINDOW", self.on_closing_practice_window)

    def division_window(self, root):
        self.check_existence_of_window(root)

        self.practice_window.title("Операція ділення")
        self.label_of_current_operation["text"] = "Ділення двійкових чисел"

        self.reset_table()
        self.practice_window.protocol("WM_DELETE_WINDOW", self.on_closing_practice_window)

    def addition_window(self, root):
        self.check_existence_of_window(root)

        self.practice_window.title("Операція додавання")
        self.label_of_current_operation["text"] = "Додавання двійкових чисел"

        self.reset_table()
        self.practice_window.protocol("WM_DELETE_WINDOW", self.on_closing_practice_window)

    def sqrt_window(self, root):
        self.check_existence_of_window(root)

        self.practice_window.title("Операція добування корення")
        self.label_of_current_operation["text"] = "Добування корення"

        self.reset_table()
        self.practice_window.protocol("WM_DELETE_WINDOW", self.on_closing_practice_window)

    def convert_window(self, root):
        self.check_existence_of_window(root)

        self.practice_window.title("Операція перетворення чисел")
        self.label_of_current_operation["text"] = "Перетворення двійкових чисел"

        self.reset_table()
        self.practice_window.protocol("WM_DELETE_WINDOW", self.on_closing_practice_window)

    def check_existence_of_window(self, root):
        try:
            if self.practice_window.winfo_exists():
                pass
        except AttributeError:
            self.window_for_practice(root)

    def check_all_entry(self):
        errors = 0
        if not self.entry_for_order_x.get() or not self.entry_for_sign_x.get() or not self.entry_for_mantissa_x.get():
            tkinter.messagebox.showwarning("Empty(ies) is(are) entry", "Input your data", parent=self.practice_window)
            errors += 1
        elif not self.entry_for_order_x.get().isdigit():
            tkinter.messagebox.showwarning("Input error", "Wrong order", parent=self.practice_window)
            errors += 1

        elif not self.entry_for_sign_x.get().isdigit():
            tkinter.messagebox.showwarning("Input error", "Wrong sign", parent=self.practice_window)
            errors += 1

        elif not self.entry_for_mantissa_x.get().isdigit():
            tkinter.messagebox.showwarning("Input error", "Wrong mantissa", parent=self.practice_window)
            errors += 1

    def reset_table(self):
        width_of_label = [2, 7, 6, 7, 3, 14]
        names_of_columns = ['№', 'RG1', 'RG2', 'RG3', 'CT', 'Операції']
        for column in range(6):
            name_label = Label(self.frame_for_text, text=names_of_columns[column], bg="#1b4d4c", fg='#65ffff', width=width_of_label[column], font=("times", 20),
                               justify=CENTER, relief=FLAT)
            name_label.grid(row=0, column=column + 1, padx=3, pady=4)
        self.list_of_labels = []
        for row in range(6):
            for column in range(6):
                display_label = Label(self.frame_for_text, text="\n", bg="#1b4d4c", fg='#65ffff', width=width_of_label[column], font=("times", 20), justify=CENTER,
                                      relief=FLAT)
                display_label.grid(row=row + 1, column=column + 1, padx=3, pady=4)
                self.list_of_labels.append(display_label)

    def destroy_labels(self):
        for el in self.list_of_labels:
            el.destroy()

        if self.result_labels:
            for el in self.result_labels:
                el.destroy()

        self.list_of_labels.clear()
        self.result_labels.clear()

    def on_closing_practice_window(self):
        self.practice_window.destroy()
        del self.practice_window
