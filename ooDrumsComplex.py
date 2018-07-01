# amy alexander 6/22/2018
# Slightly more complex demo to argue "limb independence" in traditional drum kit performance/pedagogy
# as inherently "object-oriented."  it's not meant to emulate a human performer,
# and it's certainly a monotonous, mechanical, player. it just illustrates that most of us
# learn to play kit in an "object-oriented" way without realizing it.
# Unlike the "basic" demo, this one implements independent counting for every limb.
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


    def __init__(self, counts, voice, timbre, countmillis, countincrements):
        self.counts = counts
        self.pitch = voice
        self.timbre = timbre
        self.countmillis = countmillis
        self.countincrements = countincrements

        self.lastmetrotime = millis()
        self.lastmetroname = 0.0
        self.lastmetrocount = ""

    def maybeplay (self, whatcount):
        # counting is now within each limb/instrument/instance.
        if (millis() > self.lastmetrotime + self.countmillis):

            self.lastmetroname = (self.lastmetroname % 4) + self.countincrements #count by countincrements notes
            self.lastmetrocount = self.lastmetroname + (1.00 - self.countincrements) #offset because musical counting starts with 1, but programming starts with 0 (or 0.5 for practical purposes.)

            if whatcount in self.counts:
                commandline = "/usr/bin/say -r 300 -v '" + self.pitch + "' " + self.timbre + " &"
                print ("playing: " + commandline)
                os.system(commandline)


            self.lastmetrotime = millis()

############

def millis():
    # what time is it
    now = int(round(time.time() * 1000))
    return now


############### main #####################
print("\n######### Ctrl-C to quit #########\n\n\n")

snarecounts = [1.75, 3.75]  # confusing because of the different timing below
basscounts = [1.0, 2.5, 3.0, 4.5]
ridecounts = [1.0, 1.75, 2.0, 2.75, 3.0, 3.75, 4.0, 4.75]
hihatfootcounts = [2.0, 4.0]


# Here we have independent timing and counting for each limb/instrument
# It's not really counted anything like traditional notation,
# as implementing triplets, dotted sixteenths, etc. in millesconds is beyond
# where I'd planned to get off this train. It is
# just meant to basically show "limb independence,"" since
# post-novice players learn to cope with competing triplets, duplets, etc.
snare = Instrument(snarecounts, "Alex", "choo", 200, 0.125)
bass = Instrument(basscounts, "Bruce", "thump", 300, 0.25)
ride = Instrument(ridecounts, "Bells", "sting", 300, 0.25)
hihat = Instrument(hihatfootcounts, "Princess", "clip", 300, 0.25)


while True:
    # player decides whether to play
    snare.maybeplay(snare.lastmetrocount)
    bass.maybeplay (bass.lastmetrocount)
    ride.maybeplay (ride.lastmetrocount)
    hihat.maybeplay (hihat.lastmetrocount)
