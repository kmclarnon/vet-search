import os
import sys
import glob

# import required modules below

parent_folder_path = os.path.abspath(os.path.dirname(__file__))
sys.path.append(parent_folder_path)
sys.path.append(os.path.join(parent_folder_path, "lib"))
sys.path.append(os.path.join(parent_folder_path, "plugin"))

# these have to come after we modify the system path
from flowlauncher import FlowLauncher
import pyperclip


class VetSearch(FlowLauncher):
    def query(self, query):
        with open(os.path.join(os.getcwd(), "search.path"), "r") as f:
            search_path = f.read()
        results = []
        for f in glob.glob(f"{search_path}{query}*"):
            results.append(
                {
                    "Title": os.path.splitext(os.path.basename(f))[0],
                    "IcoPath": "images/app.png",
                    "JsonRPCAction": {
                        "method": "copy_file",
                        "parameters": [f],
                    },
                }
            )
        return results

    def context_menu(self, data):
        return []

    def copy_file(self, file):
        with open(file, "r") as f:
            pyperclip.copy(f.read())


if __name__ == "__main__":
    VetSearch()
