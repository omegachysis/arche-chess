
import traceback
import logging
from logging import *
import sys

exec(open("config/debug.cfg").read())

log = logging.getLogger("R") # "R" stands for 'root'
log.setLevel(logging.DEBUG)

console = logging.StreamHandler()
console.setLevel(levelSystemConsole)

logfile = logging.FileHandler("error.log")
logfile.setLevel(levelLogFile)

formatter = logging.Formatter(
    "%(lineno)4d | %(asctime)s | %(levelname)8s | %(name)s |: %(message)s")

console.setFormatter(formatter)
logfile.setFormatter(formatter)

log.addHandler(console)
log.addHandler(logfile)

def test(main):
    log.info("starting tests")
    try:
        main()
    except:
        log.critical(traceback.format_exc())
