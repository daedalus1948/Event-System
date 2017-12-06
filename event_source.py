# start these scripts via a pipe as a "python3 event_source.py | python3 event_system.py"

# this source script only produces random data and sends it (via a pipe) to the other process (event_system.py)
# This script exists as a convenience to test receiving data from various /dev/ ttys/usb/input files
# in this case the script supplies for dev/input/mice (on linux)
# the data format is custom and does not follow any real specification
# for testing purposes only, not intended for production!
import time
import random
import sys


def produce_data():

    events = ['click:10:20:', 'hover:5:2:', 'hover:99:99:', 'close:7:3:',
              'open:10:20:', 'open:5:2:', 'hover:7:3:', 'click:7:3:', 'click:99:99:']

    chosen_event = events[random.randint(0, len(events)-1)]

    return chosen_event


while 1:
    print(produce_data())
    sys.stdout.flush()
    time.sleep(1)
