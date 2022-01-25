from utils import detection, argparser

args = argparser()
detection(args["image"], args["confidence"], args["detect"])
