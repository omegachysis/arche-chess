#!/usr/bin/env python3

import subprocess, time

engine = subprocess.Popen(
    'stockfish-dd-64-modern.exe',
    universal_newlines=True,
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
)

def put(command):
    print('\nyou:\n\t'+command)
    engine.stdin.write(command+'\n')

def get():
    # using the 'isready' command (engine has to answer 'readyok')
    # to indicate current last line of stdout
    engine.stdin.write('isready\n')
    print('\nengine:')
    while True:
        text = engine.stdout.readline().strip()
        if text == 'readyok':
            break
        if text !='':
            print('\t'+text)

get()
put('uci')
get()
put('setoption name Hash value 128')
get()
put('ucinewgame')
get()
put('position startpos')
get()
put('go depth 12')
get()
time.sleep(1)
get()

input()
