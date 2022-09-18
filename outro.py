#import the stuff i need
import time
import datetime
import timeit
import os
from pygame import mixer

#load the song
mixer.init()
mixer.music.load('fat.mp3')
mixer.music.play()

#the countdown timer
def countdown_timer(x):
    while x >= 0 :
        x -= 1
        print(format(str(datetime.timedelta(seconds=x))),"UNTIL COMPUTER SHUTDOWN")
        print("\n")
        time.sleep(1)
        
if __name__ == '__main__':
    print(timeit.timeit(lambda:countdown_timer(18), number=1))
