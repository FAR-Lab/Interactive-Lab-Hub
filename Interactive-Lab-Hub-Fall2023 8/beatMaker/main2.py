import pygame
from pygame import mixer
import os

pygame.init()
pygame.display.init()
pygame.display.set_mode((1,1))


black = (0, 0, 0)
white = (255, 255, 255)
gray = (128, 128, 128)
dark_gray = (50, 50, 50)
light_gray = (170, 170, 170)
blue = (0, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
gold = (212, 175, 55)
WIDTH = 1400
HEIGHT = 800
active_length = 0
active_beat = 0

# sounds
'''
hi_hat = mixer.Sound('sounds\kit2\hi hat.wav')
snare = mixer.Sound('sounds\kit2\snare.wav')
kick = mixer.Sound('sounds\kit2\kick.wav')
crash = mixer.Sound('sounds\kit2\crash.wav')
clap = mixer.Sound('sounds\kit2\clap.wav')
tom = mixer.Sound("sounds\kit2\\tom.wav")
'''
hi_hat = mixer.Sound('sounds/hi hat.wav')
snare = mixer.Sound('sounds/snare.wav')
kick = mixer.Sound('sounds/kick.wav')
crash = mixer.Sound('sounds/crash.wav')
clap = mixer.Sound('sounds/clap.wav')
tom = mixer.Sound("sounds/tom.wav")

beat_changed = True
timer = pygame.time.Clock()
fps = 60
beats = 8
bpm = 240
instruments = 6
playing = True
clicked = [[-1 for _ in range(beats)] for _ in range(instruments)]
active_list = [1 for _ in range(instruments)]

pygame.mixer.set_num_channels(instruments * 3)



def play_notes():
    for i in range(len(clicked)):
        if clicked[i][active_beat] == 1 and active_list[i] == 1:
            if i == 0:
                hi_hat.play()
            if i == 1:
                snare.play()
            if i == 2:
                kick.play()
            if i == 3:
                crash.play()
            if i == 4:
                clap.play()
            if i == 5:
                tom.play()

run = True
while run:
    timer.tick(fps)
    if beat_changed:
        play_notes()
        beat_changed = False

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                hi_hat.play()
                clicked[0][active_beat] = 1
            elif event.key == pygame.K_2:
                snare.play()
                clicked[1][active_beat] = 1
            elif event.key == pygame.K_3:
                kick.play()
                clicked[2][active_beat] = 1
            elif event.key == pygame.K_4:
                crash.play()
                clicked[3][active_beat] = 1
            elif event.key == pygame.K_5:
                clap.play()
                clicked[4][active_beat] = 1
            elif event.key == pygame.K_6:
                tom.play()
                clicked[5][active_beat] = 1

    beat_length = 3600 // bpm

    if playing:
        print(active_length, beat_length, active_beat, beat_changed)
        if active_length < beat_length: # measure time for a beat to play. This means the current beat is still playing.
            active_length += 1
        else:
            active_length = 0
            if active_beat < beats - 1:
                active_beat += 1
                beat_changed = True
            else:
                active_beat = 0
                beat_changed = True

pygame.quit()
