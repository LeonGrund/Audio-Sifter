import os
import argparse

import sys
import numpy as np
import madmom
from madmom.features.beats import RNNBeatProcessor
from madmom.features.beats import detect_beats
from madmom.features.beats import CRFBeatDetectionProcessor
import wave
from pydub import AudioSegment




if __name__ == '__main__':
    #print("This only executes when %s is executed rather than imported" % __file__)
    #print "hello world!!"
    #data, samplerate = sf.read('DrakeFireIce.wav')


    #generate
    proc = CRFBeatDetectionProcessor(fps=100)
    proc
    act = RNNBeatProcessor()(sys.argv[1])
    beatSeconds = proc(act)



    #Make file to hold all clips of soundfile
    if not os.path.exists('CutUpSoundFiles'):
        os.makedirs('CutUpSoundFiles')

    #Start at beginning of beat detection
    totalBeats = beatSeconds.size - 1
    halfPoint = totalBeats / 2
    quarterPoint = halfPoint / 2
    threeQuarterPoint = quarterPoint * 3
    areasToSplit = [0, quarterPoint, halfPoint, threeQuarterPoint, totalBeats]
    print areasToSplit
    for x in range ( 0, len(areasToSplit)-1):
        t1 = (beatSeconds[areasToSplit[x]]*1000)
        print 't1 is ' + str(t1)
        t2 = (beatSeconds[areasToSplit[x+1]]*1000)
        print 't2 is ' + str(t2)
        newAudio = AudioSegment.from_wav(sys.argv[1])
        newAudio = newAudio[t1:t2]


        newAudio.export('CutUpSoundFiles/newerSong%(number)03d.wav' % {"number": x}, format="wav")
    #proc(file_name) returns probability of beat at freqeuncy of 100 samples per second
