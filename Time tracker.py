import time
from datetime import datetime

import uiautomation
import win32gui

from Task import *


task_list = TaskList([]).import_json()


past_window = win32gui.GetWindowText(win32gui.GetForegroundWindow())
start_time = datetime.now()

task_name = ""


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


while True:
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
