from Task import *

task_list = TaskList([])


def load():
    global task_list
    task_list = TaskList([]).import_json()


def get_data():
    global task_list
    return TaskList([]).copy_task_list(task_list)
