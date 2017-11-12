import time
import random
import string
import pyaudio 
import wave
import numpy
import threading
from utils.abstract_keyboard import *
from utils.abstract_keyboard_display import *

basepath = os.path.dirname(os.path.abspath(__file__))
basepath = os.path.abspath(os.path.join(basepath, os.pardir))

sys.path.append(basepath)
from utils import PhysicalKeyboard
from utils import Colours

kbd = PhysicalKeyboard()

music_loop = [[False for x in xrange(10)] for y in xrange(4)] 
mesure = 0

def start_loop(delay):
    global mesure 
    mesure = mesure + 1
    print(mesure)
    #time.sleep(delay)

def welcome():
    print("welcome to the synthe demo !")
    print("1) bell")
    print("2) snare")
    print("3) crash cymbal")
    print("4) drum")
    print("enter to start the loop")

def user_input():
    #melodie_keys = raw_input("please enter the melody :")
    melodie_keys = "yaswcerfvthn."
    x = y = 0
    for idx, row in kbd.layout["rows"].iteritems():
        if idx > 0 and idx <= 4:
            y = 0
            for key in row:
                #print(idx,x,y)
                if y < 11:
                    if(key in melodie_keys.upper() ):
                        #print("keys founds")
                        music_loop[x][y-1] = True
                    else:
                        music_loop[x][y-1] = False
                else:
                    break
                y = y+1
            x = x+1

    line = ""
    for idx in range(4):
        for idy in range(10):
            if music_loop[idx][idy] == True:
                line = line + "1"
            else:
                line = line + "0"
        print(line)
        line = ""

def audio_thread(audio, file):
    CHUNK = 1024

    sound = wave.open(file, 'rb')

    # open stream (2)
    stream = audio.open(format=audio.get_format_from_width(sound.getsampwidth()),
                channels=sound.getnchannels(),
                rate=sound.getframerate(),
                output=True)

    # read data
    data = sound.readframes(CHUNK)

    # play stream (3)
    while len(data) > 0:
        stream.write(data)
        data = sound.readframes(CHUNK)

    # stop stream (4)
    stream.stop_stream()
    stream.close()

def audio_threading():
    # instantiate PyAudio (1)
    p = pyaudio.PyAudio()

    if music_loop[0][mesure] == True:
        threading.Thread(target=audio_thread(p,"audio/snare.wav")).start()
        #t1 = threading.Thread(target=audio_thread, args=("audio/snare.wav",), kwargs={'rate':44100})
        #t1.start()
    if music_loop[1][mesure] == True:
        threading.Thread(target=audio_thread(p,"audio/bass_drum.wav")).start()
        #t2 = threading.Thread(target=audio_thread, args=("audio/bass_drum.wav",), kwargs={'rate':44100})
        #t2.start()
    if music_loop[2][mesure] == True:
        threading.Thread(target=audio_thread(p,"audio/crash_cymbal.wav")).start()
        #t3 = threading.Thread(target=audio_thread, args=(sound,), kwargs={'rate':44100})
        #t3.start()
    if music_loop[3][mesure] == True:
        threading.Thread(target=audio_thread(p,"audio/bell.wav")).start()
        #t4 = threading.Thread(target=audio_thread, args=(sound,), kwargs={'rate':44100})
        #t4.start()

    # close PyAudio (5)
    p.terminate()

def audio_blocking():
    CHUNK = 1024

    sound1 = wave.open("audio/bell.wav", 'rb')
    sound2 = wave.open("audio/snare.wav", 'rb')
    sound3 = wave.open("audio/crash_cymbal.wav", 'rb')
    sound4 = wave.open("audio/bass_drum.wav", 'rb')

    # instantiate PyAudio (1)
    p = pyaudio.PyAudio()

    # open stream (2)
    stream = p.open(format=p.get_format_from_width(sound1.getsampwidth()),
                    channels=sound1.getnchannels(),
                    rate=sound1.getframerate(),
                    output=True)

    # read data
    data = sound1.readframes(CHUNK)

    data1 = sound1.readframes(CHUNK)
    data2 = sound2.readframes(CHUNK)
    data3 = sound3.readframes(CHUNK)
    data4 = sound4.readframes(CHUNK)
    decodeddata1 = numpy.fromstring(data1, numpy.int16)
    decodeddata2 = numpy.fromstring(data2, numpy.int16)
    decodeddata3 = numpy.fromstring(data3, numpy.int16)
    decodeddata4 = numpy.fromstring(data4, numpy.int16)


    sound_debug = ""
    if music_loop[0][mesure] == True:
        decodeddata = decodeddata1
        sound_debug = "1"
    else:
        if music_loop[1][mesure] == True:
            decodeddata = decodeddata2
            sound_debug = "2"
        else:
            if music_loop[2][mesure] == True:
                decodeddata = decodeddata3
                sound_debug = "3"
            else:
                if music_loop[3][mesure] == True:
                    decodeddata = decodeddata4
                    sound_debug = "4"
                else:
                    return

    if music_loop[1][mesure] == True:
            decodeddata = decodeddata + decodeddata2
            sound_debug = sound_debug + "2"
    if music_loop[2][mesure] == True:
            decodeddata = decodeddata + decodeddata3
            sound_debug = sound_debug + "3"
    if music_loop[3][mesure] == True:
            decodeddata = decodeddata + decodeddata4
            sound_debug = sound_debug +  "4"

    print(sound_debug)
    newdata = (decodeddata).astype(numpy.int16)

    #newdata = (decodeddata1 * 0.25 + decodeddata2* 0.25 + decodeddata3 * 0.25 + decodeddata4* 0.25).astype(numpy.int16)

    # play stream (3)
    while len(newdata) > 0:
        stream.write(newdata)
        newdata = sound2.readframes(CHUNK)

    # stop stream (4)
    stream.stop_stream()
    stream.close()

    # close PyAudio (5)
    p.terminate()

def audio_callback():
        # instantiate PyAudio (1)
    p = pyaudio.PyAudio()

    # define callback (2)
    #def callback(in_data, frame_count, time_info, status):
    #    data1 = sound1.readframes(frame_count)
    #    data2 = sound2.readframes(frame_count)
    #    decodeddata1 = numpy.fromstring(data1, numpy.int16)
    #    decodeddata2 = numpy.fromstring(data2, numpy.int16)
    #    newdata = (decodeddata1 * 0.5 + decodeddata2* 0.5).astype(numpy.int16)
    #    return (result.tostring(), pyaudio.paContinue)
    def callback(in_data, frame_count, time_info, status):
        data1 = sound1.readframes(frame_count)
        data2 = sound2.readframes(frame_count)
        data3 = sound3.readframes(frame_count)
        data4 = sound4.readframes(frame_count)
        decodeddata1 = numpy.fromstring(data1, numpy.int16)
        decodeddata2 = numpy.fromstring(data2, numpy.int16)
        decodeddata3 = numpy.fromstring(data3, numpy.int16)
        decodeddata4 = numpy.fromstring(data4, numpy.int16)


        if music_loop[0][mesure] == True:
            decodeddata = decodeddata1
        else:
            if music_loop[1][mesure] == True:
                decodeddata = decodeddata2
            else:
                if music_loop[2][mesure] == True:
                    decodeddata = decodeddata3
                else:
                    if music_loop[3][mesure] == True:
                        decodeddata = decodeddata2
                    else:
                        return

        if music_loop[1][mesure] == True:
                decodeddata = decodeddata + decodeddata2
        if music_loop[2][mesure] == True:
                decodeddata = decodeddata + decodeddata3
        if music_loop[3][mesure] == True:
                decodeddata = decodeddata + decodeddata4

        newdata = (decodeddata).astype(numpy.int16)

        #newdata = (decodeddata1 * 0.25 + decodeddata2* 0.25 + decodeddata3 * 0.25 + decodeddata4* 0.25).astype(numpy.int16)
        return (newdata, pyaudio.paContinue)

    # open stream using callback (3)
    stream = p.open(format=p.get_format_from_width(sound1.getsampwidth()),
                    channels=sound1.getnchannels(),
                    rate=sound1.getframerate(),
                    output=True,
                    stream_callback=callback)

    # start the stream (4)
    stream.start_stream()

    # wait for stream to finish (5)
    while stream.is_active():
        time.sleep(0.1)

    # stop stream (6)
    stream.stop_stream()

def main():
    # game logic
    welcome()
    user_input()

    while True:

        audio_threading()
        start_loop(2)
        if mesure == 10:
            break

    stream.close()
    sound1.close()

    # close PyAudio (7)
    p.terminate()

main()