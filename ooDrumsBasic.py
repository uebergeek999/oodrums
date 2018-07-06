#  amy alexander 6/22/2018
# simple demo to argue traditional basic drum kit "limb independence" in performance/pedagogy
# as inherently "object-oriented."  it's not meant to emulate a human performer,
# and it's certainly a monotonous, mechanical, player. it just illustrates that most of us
# learn to play kit in an "object-oriented" way without realizing it.
#
# uses osx speech synthesizer. can be modified for other platforms/speech synths.
# but note that some synths don't start up fast enough to keep the timing.

import os
import time


#############
class Instrument(object):

    # class to represent any drum or cymbal... but could also be thought of as
    # "Limb." Each drum has a pitch (speech synth voice), timbre (what the voice
    #  says), and most importantly, count (the player plays it on specific counts.)

    def __init__(self, counts, voice, timbre):
        self.counts = counts
        self.pitch = voice
        self.timbre = timbre

    def maybeplay (self, whatcount):
        if whatcount in self.counts:
            # player decides: do i play this eighth note with this limb?
            commandline = "/usr/bin/say -r 300 -v '" + self.pitch + "' " + self.timbre + " &"
            print ("playing: " + commandline)
            os.system(commandline)


############

def millis():
    # what time is it
    now = int(round(time.time() * 1000))
    return now


############### main #####################
print("\n######### Ctrl-C to quit #########\n\n\n")
# here's a simple rock groove, as a beginning player might learn to count it.

snarecounts = [2.0, 4.0]
basscounts = [1.0, 2.5, 3.0, 4.5]
ridecounts = [1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5]
hihatfootcounts = [2.0, 4.0]


snare = Instrument(snarecounts, "Alex", "choo" )
bass = Instrument(basscounts, "Bruce", "thump")
ride = Instrument(ridecounts, "Bells", "ting")
hihat = Instrument(hihatfootcounts, "Princess", "clip")


lastmetrotime = millis();
lastmetroname = 0.0;
eighthmillis = 700; # however many milliseconds you want an eighth note to be. smaller numbers play faster


while True:
    # this part represents the performer continually counting eigth notes.
    # ("1 and, 2 and,"" etc.)
    if (millis() > lastmetrotime + eighthmillis):

        lastmetroname = (lastmetroname % 4) + 0.5 #count by eighth notes
        lastmetrocount = lastmetroname + 0.5 #offset because musical counting starts with 1, but programming starts with 0 (or 0.5 for practical purposes.)
        print (lastmetrocount)

        # the "maybeplay" commands for each instrument only actually play when the count is appropriate
        # for that limb/instrument.
        # this represents the decision the player makes at every eighth note they count.
        snare.maybeplay (lastmetrocount)
        bass.maybeplay (lastmetrocount)
        ride.maybeplay (lastmetrocount)
        hihat.maybeplay (lastmetrocount)

        lastmetrotime = millis()
