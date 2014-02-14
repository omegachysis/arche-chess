#!/usr/bin/env python3

from arche import engine
from arche import debug

log = debug.log("game main")
def main():
    log.info("starting main")

    game = engine.Game(1024, 768, False)

    game.startApp(MainMenu())

    game.run()

class MainMenu(engine.Application):
    def __init__(self):
        super(MainMenu, self).__init__()

        self.backgroundColor = (255,255,255)


if __name__ == "__main__":
    debug.test(main)
