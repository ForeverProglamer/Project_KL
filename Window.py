from tkinter import *
import multiplication, memory_buffer

root = Tk()
name_sign_1 = Label(text="Порядок Х")
name_sign_1.pack()
entry_1 = Entry()
entry_1.pack()
name_sign_2 = Label(text="Знак Х")
name_sign_2.pack()
entry_2 = Entry()
entry_2.pack()
name_sign_3 = Label(text="Мантиса Х")
name_sign_3.pack()
entry_3 = Entry()
entry_3.pack()
name_sign_4 = Label(text="Порядок Y")
name_sign_4.pack()
entry_4 = Entry()
entry_4.pack()
name_sign_5 = Label(text="Знак Y")
name_sign_5.pack()
entry_5 = Entry()
entry_5.pack()
name_sign_6 = Label(text="Мантиса Y")
name_sign_6.pack()
entry_6 = Entry()
entry_6.pack()
name_sign_7 = Label(text="Номер операції")
name_sign_7.pack()
entry_7 = Entry()
entry_7.pack()


def for_command():
    multiplication.calculate(entry_7.get(),
                             entry_1.get(),
                             entry_4.get(),
                             entry_2.get(),
                             entry_5.get(),
                             entry_3.get(),
                             entry_6.get())
    print("Cтан пам'яті операцій:\n", memory_buffer.memory,
          "\nCтан пам'яті порядку:\n", memory_buffer.orders_memory,
          "\nCтан пам'яті відповіді:\n", memory_buffer.answers_memory)


button = Button(text="Обчислити", command=for_command)
button.pack()
root.mainloop()
