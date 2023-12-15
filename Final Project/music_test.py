import vlc
import sys


def run_example():
    instance = vlc.Instance('--aout=alsa')
    p = instance.media_player_new()
    m = instance.media_new('drum.wav') 
    p.set_media(m)
    p.play()
    while True:
        pass 
    # p.pause() 
    # volume = 50
    # vlc.libvlc_audio_set_volume(p, volume)
if __name__ == '__main__':
    try:
        run_example()
    except (KeyboardInterrupt, SystemExit) as exErr:
        sys.exit(0)