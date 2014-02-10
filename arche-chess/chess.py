#!/usr/bin/env python3

import subprocess
import time

def start():
    engine = subprocess.Popen(
        "chess/stockfish-dd-64-modern.exe",
        universal_newlines = True,
        stdin = subprocess.PIPE,
        stdout = subprocess.PIPE,
        )

    return engine

def put(engine, command):
    engine.stdin.write(command + "\n")

def get(engine):
    data = ""
    engine.stdin.write('isready\n')
    while True:
        text = engine.stdout.readline().strip()
        if text == 'readyok':
            break
        if text !='':
            data += text
    if data:
        print(data)
    return data

def checkLegal(engine, move):
    put(engine, "go depth 5 searchmoves " + move)
    while True:
        r = get(engine)
        if "bestmove" in r:
            results = r[r.index("bestmove") + 9:].split(" ")
            testmove = results[0]
            print(r)
            pondermove = results[2]
            break
    return testmove != "(none)"

def setPosition(engine, moves):
    put(engine, "position startpos moves " + ' '.join(moves))
    get(engine)

if __name__ == "__main__":
    print("Let's play CHESS!")
    engine = start()
    get(engine)
    put(engine, "uci")
    get(engine)
    put(engine, "ucinewgame")
    get(engine)
    
    moves = []
    
    while True:
        setPosition(engine, moves)

        print("")
        print("-----------------------------")
        while True:
            print("What is your move? ")
            whitemove = input(" :: ")
            if checkLegal(engine, whitemove):
                break
            else:
                print("That is not a legal move!")
        print("-----------------------------")
        print("")
        moves.append(whitemove)

        setPosition(engine, moves)

        put(engine, "go depth 12")
        while True:
            r = get(engine)
            if "bestmove" in r:
                results = r[r.index("bestmove") + 9:].split(" ")
                blackmove = results[0]
                moves.append(blackmove)
                print(r)
                pondermove = results[2]
                break

        print("")
        print("==========================")
        print("BLACK PLAYS: ")
        print(blackmove)
        print("==========================")
        print("")
        
        
