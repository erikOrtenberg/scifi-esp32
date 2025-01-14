from math import floor
from machine import Timer
import random

currentlyWriting = False
writingIteration = 0
strToPrint = ""

animLength = 30
animIteration = 0

output = ""
charset = "'/\\#!\"¤%&()=?<>-_*^"

def mPrint(string):
    global currentlyWriting
    global writingIteration
    global strToPrint
    global animIteration
    global output
    if(currentlyWriting): 
        return -1
    currentlyWriting = True
    writingIteration = 0
    strToPrint = string
    animIteration = 0
    output = ""
    tim = Timer(-1)
    tim.init(period=50, mode=Timer.PERIODIC, callback=mPrintHelper)
    return 0

def mPrintHelper(t):
    global currentlyWriting
    global strToPrint
    global writingIteration
    global animIteration
    global output
    if animIteration <= animLength:
        if animIteration < len(strToPrint):
            ## LOADING ANIM
            rand = random.getrandbits(8)/2**8
            char = charset[floor(rand*len(charset))]
            output = char + output
        else:
            ## DECRYPTING ANIM
            rand = random.getrandbits(8)/2**8
            char = charset[floor(rand*len(charset))]
            output = char + output[0:-1]
        animIteration = animIteration + 1
    else: 
        ## PRINTING TEXT ANIM
        text = output[0:writingIteration]
        encrypted = output[writingIteration: -1]
        output = text + strToPrint[writingIteration] + encrypted
        writingIteration = writingIteration + 1

    print("\033[H\033[J", end="")
    print("DECRYPTING . . .")
    print(output)
    if(writingIteration >= len(strToPrint)):
        t.deinit()
        currentlyWriting = False
