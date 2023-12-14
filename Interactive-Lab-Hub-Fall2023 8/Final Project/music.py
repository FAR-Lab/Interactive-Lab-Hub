import time
import qwiic_button
import sys
import vlc

import board
from adafruit_seesaw import seesaw, rotaryio, digitalio
from adafruit_neokey.neokey1x4 import NeoKey1x4

i2c = board.I2C()  # uses board.SCL and board.SDA
# i2c = board.STEMMA_I2C()  # For using the built-in STEMMA QT connector on a microcontroller
seesaw = seesaw.Seesaw(i2c, addr=0x36)
neokey = NeoKey1x4(i2c, addr=0x30)

seesaw_product = (seesaw.get_version() >> 16) & 0xFFFF
print("Found product {}".format(seesaw_product))
if seesaw_product != 4991:
    print("Wrong firmware loaded?  Expected 4991")

# Configure seesaw pin used to read knob button presses
# The internal pull up is enabled to prevent floating input
seesaw.pin_mode(24, seesaw.INPUT_PULLUP)
button = digitalio.DigitalIO(seesaw, 24)

beats = ["hi-hat.wav", "Acoustic Sticks 01.wav", "snare-drum.wav", "Acoustic Snare 29.wav"]

def play_beat(index, volume):
    instance = vlc.Instance()
    p = instance.media_player_new()
    m = instance.media_new(beats[index]) 
    p.set_media(m)
    vlc.libvlc_audio_set_volume(p, volume)
    p.play()

def run_example():
    my_button = qwiic_button.QwiicButton()
    instance = vlc.Instance('--aout=alsa')
    p = instance.media_player_new()
    m = instance.media_new('drum.wav') 
    instance.vlm_set_loop("drum", True)
    # print(instance.vlm_set_loop('drum.wav', True))
    p.set_media(m)
    p.play()
    is_playing = True
    is_paused = False
    last_position = None
    button_held = False
    encoder = rotaryio.IncrementalEncoder(seesaw)
    initial_volume = 100
    volume = 100

    while True: 
        if my_button.is_button_pressed() == True:
            p.pause()
            is_playing = False
            is_paused = not is_paused
            time.sleep(0.2)

        elif not is_playing and not is_paused:    
            p.play()
            is_playing = True

        # negate the position to make clockwise rotation positive
        position = -encoder.position

        if position != last_position:
            last_position = position
            print("Position: {}".format(position))
            if -20 <= position and position <= 20:
                volume = initial_volume + position * 5
                vlc.libvlc_audio_set_volume(p, volume)
                print("Volume: {}".format(volume))

        if not button.value and not button_held:
            button_held = True
            print("Button pressed")

        if button.value and button_held:
            button_held = False
            print("Button released")

        if neokey[0]:
            play_beat(0, volume)
            neokey.pixels[0] = 0xFF0000
            time.sleep(0.2)
        else:
            neokey.pixels[0] = 0x0

        if neokey[1]:
            play_beat(1, volume)
            neokey.pixels[1] = 0xFFFF00
            time.sleep(0.2)
        else:
            neokey.pixels[1] = 0x0

        if neokey[2]:
            play_beat(2, volume)
            neokey.pixels[2] = 0x00FF00
            time.sleep(0.2)
        else:
            neokey.pixels[2] = 0x0

        if neokey[3]:
            play_beat(3, volume)
            neokey.pixels[3] = 0x00FFFF
            time.sleep(0.2)
        else:
            neokey.pixels[3] = 0x0
        
        
if __name__ == '__main__':
    try:
        run_example()
    except (KeyboardInterrupt, SystemExit) as exErr:
        sys.exit(0)