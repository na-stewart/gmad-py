import json
import os
import re
import shutil
import subprocess
from sys import platform


def gmad_bin():
    if platform == "linux" or platform == "linux2":
        return "bin/gmad_linux"
    elif platform == "darwin":
        return "bin/gmad_osx"
    elif platform == "win32":
        return "bin/gmad_windows.exe"


def extract(directory):
    for f in os.listdir(directory):
        if f.endswith(".gma"):
            addon = os.path.join(directory, f)
            print(f"Extracting gma file {addon}...")
            subprocess.call([gmad_bin(), "extract", "-file", addon])


def create_addon_json(addon_json):
    possible_types = [
        "gamemode",
        "map",
        "weapon",
        "vehicle",
        "npc",
        "tool",
        "effects",
        "model",
    ]
    possible_tags = [
        "fun",
        "roleplay",
        "scenic",
        "movie",
        "realism",
        "cartoon",
        "water",
        "comic",
        "build",
    ]
    data = dict()
    data["title"] = input("What will be the name of your addon?: ")
    data["type"] = input(
        f"What will be the type of your addon? You can choose only one. ({', '.join(possible_types)}): "
    )
    if data["type"] not in possible_types:
        raise ValueError("Invalid addon type.")
    data["tags"] = re.split(
        r", | (?!.*?, )",
        input(
            f"What tags will be applied to your addon? You can choose up to two. ({', '.join(possible_tags)}): "
        ),
    )
    if 0 <= len(data["tags"]) > 2 or not bool(set(data["tags"]) & set(possible_tags)):
        raise ValueError("Invalid addon tags.")
    data["ignore"] = re.split(
        r", | (?!.*?, )",
        input(
            "List the file names of the files you want to ignore in the addon, you may use wildcards: "
        ),
    )
    with open(addon_json, "w") as f:
        f.write(json.dumps(data))


def create(directory):
    for d in os.listdir(directory):
        addon = os.path.join(directory, d)
        if os.path.isdir(addon):
            print(f"Creating gma file {addon}.gma...")
            addon_json = os.path.join(addon, "addon.json")
            if not os.path.exists(addon_json):
                if input("Could not find addon.json, do you want to generate one? (yes/no): ") != "yes":
                    continue
                create_addon_json(addon_json)
            subprocess.call(
                [
                    gmad_bin(),
                    "create",
                    "-folder",
                    addon,
                    "-out",
                    f"{addon}.gma",
                ]
            )


def main():
    print(
        """                                        
         /$$$$$$  /$$      /$$  /$$$$$$  /$$$$$$$ 
        /$$__  $$| $$$    /$$$ /$$__  $$| $$__  $$
       | $$  \__/| $$$$  /$$$$| $$  \ $$| $$  \ $$
       | $$ /$$$$| $$ $$/$$ $$| $$$$$$$$| $$  | $$
       | $$|_  $$| $$  $$$| $$| $$__  $$| $$  | $$
       | $$  \ $$| $$\  $ | $$| $$  | $$| $$  | $$
       |  $$$$$$/| $$ \/  | $$| $$  | $$| $$$$$$$/
        \______/ |__/     |__/|__/  |__/|_______/ 
       """
    )
    print("Garry's Mod Easy Addon Creator and Extractor v1.0")
    print("https://github.com/sunset-developer")
    print("---------------------------------------------------------")
    directory = input(
        "Please enter the directory that your addons are located (/home/user/example/addons): "
    )
    execution_type = input(
        "Do you want to extract or create gma files. (extract/create): "
    )
    if execution_type == "extract":
        extract(directory)
    elif execution_type == "create":
        create(directory)
    else:
        raise TypeError("Invalid execution type")
    input("Thanks for using gmad-py.")


if __name__ == "__main__":
    main()
