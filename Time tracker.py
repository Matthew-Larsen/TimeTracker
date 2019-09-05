import getpass
import os
import time
from datetime import datetime

import uiautomation
import win32gui

from Task import *

global task_list
global task_name
global past_window
global start_time
global running

running = False
task_list = None
past_window = None
start_time = None
task_name = None


def start():
    global task_list
    global task_name
    global past_window
    global start_time
    global running

    try:
        task_list = TaskList([]).import_json()
    except Exception:
        task_list = TaskList([])
    past_window = win32gui.GetWindowText(win32gui.GetForegroundWindow())
    start_time = datetime.now()
    task_name = ""
    running = True


def name_formatter(name):
    if "PyCharm" in name:
        split_by_hyphen = name.split(" - ")
        if len(split_by_hyphen) == 3 and split_by_hyphen[2] == "PyCharm":
            return split_by_hyphen[0] + " " + split_by_hyphen[2]
    elif "Google Chrome" in name:
        return url_formatter()
    return name


def url_formatter():
    window = win32gui.GetForegroundWindow()
    chrome = uiautomation.ControlFromHandle(window)
    return chrome.EditControl().GetValuePattern().Value.split("/")[0]

def add_to_startup(file_path=""):
    USER_NAME = getpass.getuser()
    if file_path == "":
        file_path = os.path.dirname(os.path.realpath(__file__))
    bat_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % USER_NAME
    with open(bat_path + '\\' + "open.bat", "w+") as bat_file:
        bat_file.write(r'start "" %s' % file_path)


if __name__ == "__main__":
    start()

while running:

    try:
        new_window = win32gui.GetWindowText(win32gui.GetForegroundWindow())
        if new_window != past_window:
            end_time = datetime.now()
            window_name = name_formatter(past_window)
            use = Use(start_time, end_time)

            used_before = False
            for task in task_list.tasks:
                if task.name == window_name:
                    used_before = True
                    task.usage_data.append(use)
            if not used_before:
                task = Task(window_name, [use])
                task_list.tasks.append(task)

            with open("tasks.json", "w") as json_file:
                json.dump(task_list.serialize(), json_file, indent=4, sort_keys=True)
            start_time = datetime.now()

        time.sleep(5)
        past_window = new_window
    except KeyboardInterrupt:
        with open("tasks.json", "w") as json_file:
            json.dump(task_list.serialize(), json_file, indent=4, sort_keys=True)


