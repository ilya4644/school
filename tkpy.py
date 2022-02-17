import tkinter as tk
import os
import sys


class App:

    def __init__(self):
        self.root = tk.Tk()

        self.square = 0.0
        self.rulon = 0

        self.mheight = tk.DoubleVar()
        self.mlength = tk.DoubleVar()
        self.mwidth = tk.DoubleVar()
        self.mrulon = tk.DoubleVar()

        self.text_length = tk.StringVar()
        self.text_length.set("Длина")
        self.text_width = tk.StringVar()
        self.text_width.set("Ширина")
        self.text_height = tk.StringVar()
        self.text_height.set("Высота")
        self.text_rulon = tk.StringVar()
        self.text_rulon.set("В рулоне")
        self.text_square = tk.StringVar()
        self.text_square.set(f"Площадь стен = {self.square} кв. м")
        self.text_rulons = tk.StringVar()
        self.text_rulons.set(f"Нужно {self.rulon} рулонов")

        self.label_length = tk.Label(self.root, textvariable=self.text_length)
        self.label_width = tk.Label(self.root, textvariable=self.text_width)
        self.label_height = tk.Label(self.root, textvariable=self.text_height)
        self.label_rulon = tk.Label(self.root, textvariable=self.text_rulon)
        self.label_square = tk.Label(self.root, textvariable=self.text_square)
        self.label_rulons = tk.Label(self.root, textvariable=self.text_rulons)

        self.message_entry_length = tk.Entry(self.root)
        self.message_entry_width = tk.Entry(self.root)
        self.message_entry_height = tk.Entry(self.root)
        self.message_entry_rulon = tk.Entry(self.root)

        self.button_save = tk.Button(self.root, text="Сохранить")
        self.button_import = tk.Button(self.root, text="Загрузить")

        self.label_length.pack()
        self.message_entry_length.pack()
        self.label_width.pack()
        self.message_entry_width.pack()
        self.label_height.pack()
        self.message_entry_height.pack()
        self.label_rulon.pack()
        self.message_entry_rulon.pack()
        self.label_square.pack()
        self.label_rulons.pack()

        self.button_save.pack()
        self.button_import.pack()

        self.mheight.trace("w", self.count())
        self.mlength.trace("w", self.count())
        self.mwidth.trace("w", self.count())
        self.mrulon.trace("w", self.count())

        self.root.mainloop()

    def count(self):
        self.square = float(self._height.get())*(2*(float(self.text_length.get())+float(self.text_width.get())))
        self.rulons = self.square // self.rulon
        if self.square % self.rulon != 0:
            self.rulons += 1


app = App()