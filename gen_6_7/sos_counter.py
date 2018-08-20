import curses
import struct
import time

from citra import Citra

SM = 1
USUM = 2

# Change this value to your desired game
current_game = USUM

# -----------------------------------------------------------------------------

def get_sos_count_address():
    if SM == current_game:
        return 0x3003960D   # SM 1.0
    elif USUM == current_game:
        return 0x300397F9   # USUM 1.0 to 1.2
    return 0

def read_sos_count(c):
    read_address = get_sos_count_address()
    data = c.read_memory(read_address, 1)
    value = struct.unpack("B", data)[0]
    return value

def run():
    win = curses.initscr()

    try:
        c = Citra()
        if c.is_connected():
            while True:
                value = read_sos_count(c)
                win.clear()
                win.addstr("PokeStreamer-Tools SOS Counter Tool\n\n")
                win.addstr("SOS count: %d" % (value))
                win.refresh()

                with open("sos_count.txt", "w") as f:
                    f.write(str(value))

                time.sleep(1)
        else:
            print("Failed to connect to Citra RPC Server")
    finally:
        curses.endwin()

if "__main__" == __name__:
    run()
