""" A script which pretends to decrypt files. """
import random
import time
import curses
import sys


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
    try:
        scr.addstr(loc+0, 0, f"Starting decryption subroutine on unknown file {file_number:07d}")
    except curses.error:
        pass
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
        try:
            scr.addstr(loc+1, 4, f"DECRYPTING{periods}")
        except curses.error:
            pass
        if len(indices) == 0:
            try:
                scr.addstr(loc+2, 8, f"{encrypted}", curses.color_pair(4))
            except curses.error:
                pass
        else:
            try:
                scr.addstr(loc+2, 8, f"{encrypted}", curses.color_pair(3))
            except curses.error:
                pass
        if toggle:
            try:
                scr.addstr(loc+3, 4, f"STATUS: FAILURE")
            except curses.error:
                pass
        else:
            try:
                scr.addstr(loc+3, 4, f"STATUS: FAILURE", curses.color_pair(1))
            except curses.error:
                pass
        toggle = toggle is False
        time.sleep(time_delay)
        counter += 1
        scr.refresh()
    try:
        scr.addstr(loc+3, 4, "DECRYPTION SUCCESSFUL", curses.color_pair(2))
    except curses.error:
        pass
if __name__ == '__main__':
    screen = curses.initscr()
    screen.scrollok(True)
    curses.start_color()
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_RED)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.noecho()
    curses.cbreak()
    try:
        cursor_start = 0
        while True:
            rows, cols = screen.getmaxyx()
            decrypt_file(loc=cursor_start, filename=generate_encrypted_filename(), time_delay = 0.1, scr=screen, message_history='')
            if rows - cursor_start < 5:
                screen.scroll(rows)
                cursor_start = 0
            else:
                cursor_start += 5

    except KeyboardInterrupt:
        curses.echo()
        curses.nocbreak()
        curses.endwin()
        sys.exit(0)
    finally:
        curses.echo()
        curses.nocbreak()
        curses.endwin()

