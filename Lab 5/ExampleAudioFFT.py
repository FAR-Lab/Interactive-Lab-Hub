import pyaudio
import numpy as np
import scipy
from numpy_ringbuffer import RingBuffer

import queue
import time

DEVICE_INDEX = 1

UPDATE_RATE = 1.0
SAMPLING_RATE = 44100

### Things you probably dont need to change
FORMAT=np.float32



def main():
    audioQueue = queue.Queue()
    pyaudio_instance = pyaudio.PyAudio()
    print("Setting up callback")
    def _callback(in_data, frame_count, time_info, status):
        audioQueue.put(in_data)
        
        return None, pyaudio.paContinue

    stream = pyaudio_instance.open(input=True,start=False,format=pyaudio.paFloat32,channels=1,rate=SAMPLING_RATE,frames_per_buffer=int(SAMPLING_RATE/2),stream_callback=_callback,input_device_index=DEVICE_INDEX)
    AudioBuffer = RingBuffer(capacity=SAMPLING_RATE*1, dtype=FORMAT) # 1 second long buffer.
    VolumeHistory = RingBuffer(capacity=int(20/UPDATE_RATE), dtype=FORMAT) ## This is how you can compute a history to record changes over time
    ###
    nextTimeStamp = time.time()
    stream.start_stream()
    try:
        while True:
            frames = audioQueue.get()
            if not frames:
                continue
            framesData = np.fromstring(frames, dtype=FORMAT)
            AudioBuffer.extend(framesData[0::1]) ## here we are picking only one of the 6 channels 
            
            if(AudioBuffer.is_full and audioQueue.qsize()<2 and time.time()>nextTimeStamp): ## We want to make sure that the queue of new audio does not get too long.
                print("Will process data now")
                buffer  = np.array(AudioBuffer)
                volume = np.rint(np.sqrt(np.mean(buffer**2))*10000)
                VolumeHistory.append(volume)
                volumneSlow = volume
                volumechange = 0.0
                print("Ok more analysis")
                if VolumeHistory.is_full:
                    length = int(np.round(VolumeHistory.maxlen/2))
                    vnew = np.array(VolumeHistory)[length:].mean()
                    vold = np.array(VolumeHistory)[:VolumeHistory.maxlen-length].mean()
                    volumechange =vnew-vold
                    volumneSlow = np.array(VolumeHistory).mean()
                
                print("RMS volume "+ str(volumneSlow)+', Volume Change:'+ str(volumechange))
                nextTimeStamp = UPDATE_RATE+time.time()
    except:
        print("Something happend with the audio example. Stopping!") 

if __name__ == '__main__':
    print("Befor Main")
    main()
    print("After Main")

