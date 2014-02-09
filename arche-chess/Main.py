#!/usr/bin/env python3

from arche import engine
from arche import debug

import logging

log = logging.getLogger("R.Main")

def main():
    log.info("starting main")

    game = engine.Game(1024, 768, False)

    game.run()

if __name__ == "__main__":
    debug.test(main)
