import pygame.mixer

music = pygame.mixer.music
import time

pygame.mixer.init()
# music.set_volume(1)
music.load("alphabet.mp3")


def playSound(letter):
    music.rewind()
    music.play(start=1 + myOrd(letter) - ord("А"))
    time.sleep(1)
    music.stop()


def playFullSound(letter):
    music.rewind()
    music.play()
    time.sleep(1)
    music.stop()
    playSound(letter)


def test():
    music.play(start=0)
    music.stop()
    for i in range(0, 34):
        music.play(start=i)
        time.sleep(1)
        music.stop()


def myOrd(letter):
    ordVal = ord(letter)
    if ordVal == 1025:
        return 1046
    elif ordVal > 1045:
        return ordVal + 1
    else:
        return ordVal