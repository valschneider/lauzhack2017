#!usr/bin/env python  
#coding=utf-8  

import pyaudio  
import wave  
import numpy

#define stream chunk   
chunk = 1024  

#open a wav format music  
f = wave.open(r"crash_cymbal.wav","rb")
snare = wave.open(r"snare.wav","rb")
bass_drum = wave.open(r"bass_drum.wav","rb")
crash_cymbal = wave.open(r"crash_cymbal.wav","rb")
bell = wave.open(r"bell.wav","rb")

data1 = snare.readframes(chunk)
data2 = bell.readframes(chunk)
data3 = bell.readframes(chunk)
decodeddata1 = numpy.fromstring(data1, numpy.int16)
decodeddata2 = numpy.fromstring(data2, numpy.int16)
decodeddata3 = numpy.fromstring(data3, numpy.int16)
#newdata = (decodeddata1 * 0.5 + decodeddata2* 0.5).astype(numpy.int16)
newdata = (decodeddata1 *0.3+ decodeddata2*0.3 + decodeddata3*0.3).astype(numpy.int16)


#instantiate PyAudio  
p = pyaudio.PyAudio()  
#open stream  
stream = p.open(format = p.get_format_from_width(f.getsampwidth()),  
                channels = f.getnchannels(),  
                rate = f.getframerate(),  
                output = True)  
#read data  
#data = f.readframes(chunk)  

#play stream  
while newdata[1]:  
    stream.write(newdata)  
    newdata = newdata.readframes(chunk)  

#stop stream  
stream.stop_stream()  
stream.close()  

#close PyAudio  
p.terminate()  