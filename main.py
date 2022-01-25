from projekt.utils import detection
from projekt.utils import argparser

args = argparser()
detection(args["image"], args["confidence"], args["detect"])
