import PIL.ImageTk, PIL.Image
import tkinter as tk
from buttonModule import ExchButton
import questModule as qm

if __name__ == "__main__":
    root = tk.Tk()
    image = PIL.Image.open("soundPic.png")
    image = image.resize([100, 100])
    soundPic = PIL.ImageTk.PhotoImage(image)

    btn_play = tk.Button(
        image=soundPic,
        bg="#F5FFB7",
        activebackground="#F5FFB7",
        command=qm.ListenBtnPressed,
    )
    btn_play.pack(fill=tk.X)

    qm.btns = [ExchButton(i) for i in range(4)]
    for btn in qm.btns:
        btn.pack(side=tk.LEFT)

    qm.tk_update = root.update
    qm.getLetters()
    root.mainloop()