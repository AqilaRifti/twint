import sys
import console
import commands

def ask():
    command = {
        "command_name": None,
        "command_args": None,
        "command_opts": None,
        "command_flag": None,
    }
    command_index = [j for j in command]

    if len(sys.argv) < 2:
        console.error("to few argument")
    
    for i in range(len(sys.argv)):
        try:
            command[command_index[i]] = sys.argv[i + 1]
        except IndexError:
            break

    return command

def execute():
    command = ask()
    for i in commands.command_list.keys():
        if i == command["command_name"]:
            commands.command_list[i](command)
            break