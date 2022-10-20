import pyaudio
import numpy as np
from scipy.fft import rfft, rfftfreq
from scipy.signal.windows import hann
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

    def _callback(in_data, frame_count, time_info, status):
        audioQueue.put(in_data)
        return None, pyaudio.paContinue

    stream = pyaudio_instance.open(input=True,start=False,format=pyaudio.paFloat32,channels=1,rate=SAMPLING_RATE,frames_per_buffer=int(SAMPLING_RATE/2),stream_callback=_callback,input_device_index=DEVICE_INDEX)
    AudioBuffer = RingBuffer(capacity=SAMPLING_RATE*1, dtype=FORMAT) # 1 second long buffer.
    VolumeHistory = RingBuffer(capacity=int(20/UPDATE_RATE), dtype=FORMAT) ## This is how you can compute a history to record changes over time
    ### Here  is a good spot to extend other buffers  aswell that keeps track of varailbes over a certain period of time. 

    nextTimeStamp = time.time()
    stream.start_stream()
    if True:
        while True:
            frames = audioQueue.get()
            if not frames:
                continue
            framesData = np.frombuffer(frames, dtype=FORMAT)
            AudioBuffer.extend(framesData[0::1]) ## here we are picking only one of the 6 channels 
            
            if(AudioBuffer.is_full and audioQueue.qsize()<2 and time.time()>nextTimeStamp): ## We want to make sure that the queue of new audio does not get too long.
                buffer  = np.array(AudioBuffer)
                volume = np.rint(np.sqrt(np.mean(buffer**2))*10000)
                VolumeHistory.append(volume)
                volumneSlow = volume
                volumechange = 0.0
                if VolumeHistory.is_full:
                    length = int(np.round(VolumeHistory.maxlen/2))
                    vnew = np.array(VolumeHistory)[length:].mean()
                    vold = np.array(VolumeHistory)[:VolumeHistory.maxlen-length].mean()
                    volumechange =vnew-vold
                    volumneSlow = np.array(VolumeHistory).mean()
                


                N = buffer.shape[0]
                window = hann(N)
                amplitudes = np.abs(rfft(buffer*window))[2:]
                frequencies = (rfftfreq(N, 1/SAMPLING_RATE)[:N//2])[2:]
               

                LoudestFrequency = frequencies[amplitudes.argmax()]
                
                print("Loudest Frqeuncy:",LoudestFrequency)
                print("RMS volume:",volumneSlow)
                print("Volume Change:",volumechange)
                nextTimeStamp = UPDATE_RATE+time.time()
    except:
        print("Something happend with the audio example. Stopping!") 

if __name__ == '__main__':
    main()

