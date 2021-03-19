import sys
from iothub_med_normal_temp import *
from iothub_med_high_temp import *


if __name__ == '__main__':
    # print("IoT - Simulated medical device")
    # print("Press Ctrl-C to exit")
    if sys.argv[1].lower() == "normaltemp":
        iothub_med_normal_temp()
    elif sys.argv[1].lower() == "hightemp":
        iothub_med_high_temp()
    else:
        print("Please provide one of the values 'normaltemp or hightemp' as parameters")