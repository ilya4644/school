import random
import tkinter as tk


class App:

    def __init__(self):
        self.root = tk.Tk()
        self.text = tk.StringVar()
        self.text.set("")
        self.label = tk.Label(self.root, textvariable=self.text)
        self.message_entry = tk.Entry(self.root)
        self.button = tk.Button(self.root, text="Go!", command=self.change_text)
        self.message_entry.pack()
        self.button.pack()
        self.label.pack()
        self.root.geometry("250x100")
        self.root.mainloop()

    def change_text(self):
        number = random.randint(1, 10)
        numb = int(self.message_entry.get())
        if numb == number:
            self.text.set("Числа совпали! \n Вы победили!")
        else:
            self.text.set(f"Числа не совпали, вот правильное число:{number}")


app = App()