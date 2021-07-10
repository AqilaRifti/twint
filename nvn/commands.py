from config import config
from watch import watch
import os
import console
import json


def project_input(message):
    return f'{input(message + ": ")}'


def init(args=""):
    project = {}
    project["name"] = project_input("name")
    project["version"] = project_input("version")
    with open("nvn.json", "w") as file:
        file.write(json.dumps(project, sort_keys=True, indent=4))
        file.close()


def check_command(args):
    for i in config["command"].keys():
        if i == args:
            return config["command"][i]


def run(args, opts=None, flag=None):
    opts = args["command_opts"]
    if opts != None:
        for i in range(int(opts)):
            os.system(check_command(args["command_args"]))
    else:
        os.system(check_command(args["command_args"]))


def info(args):
    console.info(f"NAME: {config['name']}")
    console.info(f"VERSION: {config['version']}")
    console.info(f"COMMAND_LIST: \n{config['command']}")


command_flag = ["-c", "-t", "-h", "--timer", "--clear", "--help"]
command_list = {
    "init": init,
    "run": run,
    "info": info,
    "watch": watch
}
