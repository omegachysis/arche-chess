#!/usr/bin/env python3

import Engine
import Debug

import logging

log = logging.getLogger("R.Main")

def main():
    log.info("starting main")

    game = Engine.Game(1024, 768, False)

    game.run()

if __name__ == "__main__":
    Debug.test(main)
