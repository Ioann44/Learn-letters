import sys
import random
import time
from collections import defaultdict
from _thread import start_new_thread
import soundModule as sm

START_VALUE = 3
IF_RIGHT = -3
IF_WRONG = 1

alphabet = list("АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ")
data = defaultdict(int)
for letter in alphabet:
    data[letter] = START_VALUE
answer = None
btns = None
tk_update = None


def getLetters():
    global answer

    if len(data) == 0:
        print("Letters are gone!")
        input()
        sys.exit()

    answer = random.choice(list(data.keys()))
    letters = random.choices(alphabet, k=4)
    if not answer in letters:
        letters[random.randint(0, 3)] = answer
    for btn, letter in zip(btns, letters):
        btn["text"] = letter

    tk_update()
    start_new_thread(sm.playFullSound, (answer,))


def AnswerBtnPressed(id):
    if btns[id]["text"] == answer:
        data[answer] += IF_RIGHT
        if data[answer] <= 0:
            del data[answer]
            print(len(data), "букв осталось изучить")
    else:
        btns[id]["bg"] = "red"
        data[answer] += IF_WRONG
        data[btns[id]["text"]] += IF_WRONG

    for btn in btns:
        if btn["text"] == answer:
            btn["bg"] = "green"

    tk_update()
    time.sleep(2)
    for btn in btns:
        btn["bg"] = "SystemButtonFace"

    tk_update()
    getLetters()


def ListenBtnPressed():
    start_new_thread(sm.playSound, (answer,))
