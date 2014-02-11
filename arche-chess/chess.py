#!/usr/bin/env python3

from arche import engine
from arche import debug

import subprocess

log = debug.log("game chess")

def main():
    game = engine.Game(1024, 768, False)
    game.startApp(Chess())
    game.run()

class Player(object):
    app = None

class PlayerHuman(Player):
    def __init__(self):
        pass
    
    def move(self, board):
        move = None
        while True:
            move = input("Your move: ")
            if board.isMoveLegal(move):
                break
            else:
                print("Not a legal move!")
        return move
    
class PlayerComputer(Player):
    def __init__(self, depth=12):
        self.depth = depth

    def move(self, board):
        move = None
        self.app.enginePut("go depth {}".format(self.depth))
        while True:
            r = self.app.engineGet()
            if "bestmove" in r:
                results = r[r.index("bestmove") + 9:].split(" ")
                move = results[0]
                pondermove = results[2]
                break
        board.move(move)

class Board(object):
    moves = []
    app = None
    def __init__(self):
        pass
    def move(self, move):
        moves.append(move)
    def isMoveLegal(self, move):
        pass

class Chess(engine.Application):
    playerWhite = None
    playerBlack = None
    def __init__(self, playerWhite, playerBlack):
        super(Chess, self).__init__()

        self.backgroundColor = (80,0,0)

        self.playerWhite = playerWhite
        self.playerBlack = playerBlack

        log.info("Starting stockfish")
        self.engine = subprocess.Popen(
            "chess/stockfish-dd-64-modern.exe",
            universal_newlines = True,
            stdin = subprocess.PIPE,
            stdout = subprocess.PIPE,
            )

        Player.app = self
        Board.app = self

        self.enginePut("uci")

    def enginePut(self, command):
        self.engine.stdin.write(command + "\n")
    def engineGet(self):
        data = ""
        engine.stdin.write('isready\n')
        while True:
            text = engine.stdout.readline().strip()
            if text == 'readyok':
                break
            if text !='':
                data += text
        return data

    def gameStart(self):
        pass

if __name__ == "__main__":
    debug.test(main)
