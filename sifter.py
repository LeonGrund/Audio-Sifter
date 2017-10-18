import os
import sys
import numpy as np
import madmom
from madmom.features.beats import RNNBeatProcessor
from madmom.features.beats import detect_beats
from madmom.features.beats import CRFBeatDetectionProcessor
import wave
from pydub import AudioSegment


#GENERATES file 'CutUpSoundFiles' in current directory, which contains 4 .wav files of the audio split up 
def cutUpQuarters(fileName):
        #generate
    proc = CRFBeatDetectionProcessor(fps=100)
    proc
    act = RNNBeatProcessor()(fileName)
    beatSeconds = proc(act)



    #Make file to hold all clips of soundfile
    if not os.path.exists('CutUpSoundFiles'):
        os.makedirs('CutUpSoundFiles')

    #Generate 
    totalBeats = beatSeconds.size - 1
    halfPoint = totalBeats / 2
    quarterPoint = halfPoint / 2
    threeQuarterPoint = quarterPoint * 3

    #Start at beginning of beat detection
    areasToSplit = [0, quarterPoint, halfPoint, threeQuarterPoint, totalBeats]


    for x in range ( 0, len(areasToSplit)-1):
        t1 = (beatSeconds[areasToSplit[x]]*1000)
        t2 = (beatSeconds[areasToSplit[x+1]]*1000)
        
        newAudio = AudioSegment.from_wav(fileName)
        newAudio = newAudio[t1:t2]


        newAudio.export('CutUpSoundFiles/newerSong%(number)03d.wav' % {"number": x}, format="wav")




if __name__ == '__main__':
    cutUpQuarters(sys.argv[1])

    
