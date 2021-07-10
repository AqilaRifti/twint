import json
import console

config = {}
try:
    with open("nvn.json", "r") as file:
        config = json.loads(
            file.read()
        )
        file.close()

except FileNotFoundError:
    console.error("No Config File Found")
