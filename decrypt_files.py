""" A script which pretends to decrypt files. """
import random
import time
import curses
import sys

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def generate_encrypted_filename():
    begin = random.choice([
        'bitcoin',
        'cia',
        'nuclear_silo',
        'whitehouse'
        'ufo'
    ])

    middle = random.choice([
        'ledger',
        'sighting_log',
        'communique',
        'log',
    ])

    end = random.choice([
        'alpha',
        'tango',
        'defcon_0',
        'top_secret',
    ])
    
    suffix = int(random.random()*999)

    filetype = random.choice(['jpg', 'zip', 'tar.gz', 'txt', 'html', 'png', 'pdf'])

    return f"{begin}_{middle}_{end}_{suffix:03d}.{filetype}"

def decrypt_file(loc, filename, time_delay, scr, message_history):
    encrypted = '*'*len(filename)
    indices = [i for i in range(len(filename))]
    file_number = int(random.random() * 100000)

    counter = 1

    scr.addstr(loc+0, 0, f"Starting decryption subroutine on unknown file {file_number:07d}")
    toggle = True
    while len(indices) > 0:
        idx = random.choice(indices)
        del indices[indices.index(idx)]
        
        filename = list(filename)
        encrypted = list(encrypted)
        counter = 1 if counter > 3 else counter
        periods = '.' * counter
        periods = f'{periods: <3}'
        encrypted[idx] = filename[idx]
        encrypted = ''.join(encrypted)
        scr.addstr(loc+1, 4, f"DECRYPTING{periods}")
        if len(indices) == 0:
            scr.addstr(loc+2, 8, f"{encrypted}", curses.color_pair(4))
        else:
            scr.addstr(loc+2, 8, f"{encrypted}", curses.color_pair(3))
        if toggle:
            scr.addstr(loc+3, 4, f"STATUS: FAILURE")
        else:
            scr.addstr(loc+3, 4, f"STATUS: FAILURE", curses.color_pair(1))
        toggle = toggle is False
        time.sleep(time_delay)
        counter += 1
        scr.refresh()
    scr.addstr(loc+3, 4, "DECRYPTION SUCCESSFUL", curses.color_pair(2))
    time.sleep(1)

if __name__ == '__main__':
    screen = curses.initscr()
    curses.start_color()
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_RED)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.noecho()
    curses.cbreak()
    try:
        screen_location = 0
        while True:
            decrypt_file(loc=screen_location, filename=generate_encrypted_filename(), time_delay = 0.3, scr=screen, message_history='')
            screen_location += 5
    except KeyboardInterrupt:
        curses.echo()
        curses.nocbreak()
        curses.endwin()
        sys.exit(0)
    finally:
        curses.echo()
        curses.nocbreak()
        curses.endwin()

