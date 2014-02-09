
import traceback
import logging
from logging import *
import sys

formatLogging = "%(lineno)4d | %(asctime)s | %(levelname)8s | %(name)s |: %(message)s"
levelGameConsole = INFO
levelSystemConsole = INFO
levelLogFile = INFO

exec(open("config/debug.cfg").read())

log = logging.getLogger("R") # "R" stands for 'root'
log.setLevel(levelGameConsole)

console = logging.StreamHandler()
console.setLevel(levelSystemConsole)

logfile = logging.FileHandler("error.log")
logfile.setLevel(levelLogFile)

formatter = logging.Formatter(formatLogging)

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
