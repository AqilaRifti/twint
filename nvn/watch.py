from watchgod import watch
import os

def watch(args):
    for changes in watch(args["command_args"]):
        os.system(args["command_opts"])
