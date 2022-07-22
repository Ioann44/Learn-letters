import tkinter as tk
from questModule import AnswerBtnPressed


class ExchButton(tk.Button):
    def __init__(self, id):
        tk.Button.__init__(
            self,
            text="0",
            font="Times 100",
            width=2,
            height=1,
            command=lambda: AnswerBtnPressed(id),
        )
        self.id = id