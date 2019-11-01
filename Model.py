from Task import *

task_list = TaskList([])


def load():
    global task_list
    task_list = TaskList([]).import_json()


def get_data():
    global task_list
    return TaskList([]).copy_task_list(task_list)


def get_data_after(date):
    all_data = get_data()
    tasks_after = []
    for task in all_data.tasks:
        after_data = []
        for use in task.usage_data:
            if date_is_after(use.start_time.strftime("%Y-%m-%d %H:%M:%S"), date):
                after_data.append(use)

        new = Task(task.name, after_data, task.tags)
        tasks_after.append(new)
    return TaskList(tasks_after)


def get_data_with_tag(tag):
    all_data = get_data()
    tagged_tasks = []
    for task in all_data.tasks:
        if tag in task.tags:
            tagged_tasks.append(task)

    return TaskList(tagged_tasks)


def get_tagged_after(tag, date):
    all_data = get_data()
    tasks_after = []
    for task in all_data.tasks:
        if tag not in task.tags:
            continue
        after_data = []
        for use in task.usage_data:
            if date_is_after(use.start_time.strftime("%Y-%m-%d %H:%M:%S"), date):
                after_data.append(use)

        new = Task(task.name, after_data, task.tags)
        tasks_after.append(new)
    return TaskList(tasks_after)


def date_is_after(date, point):
    year1str, month1str, rest1 = date.split("-")
    year2str, month2str, rest2 = point.split("-")

    year1 = int(year1str)
    month1 = int(month1str)
    year2 = int(year2str)
    month2 = int(month2str)

    if year1 > year2:
        return True
    elif year1 < year2:
        return False

    if month1 > month2:
        return True
    elif month1 < month2:
        return False

    day1str, time_str1 = rest1.split(" ")
    day2str, time_str2 = rest2.split(" ")

    if int(day1str) > int(day2str):
        return True
    elif int(day1str) < int(day2str):
        return False

    hour_str1, min_str1, sec_str1 = time_str1.split(":")
    hour_str2, min_str2, sec_str2 = time_str2.split(":")

    hour1 = int(hour_str1)
    hour2 = int(hour_str2)
    min1 = int(min_str1)
    min2 = int(min_str2)
    sec1 = int(sec_str1)
    sec2 = int(sec_str2)

    if hour1 > hour2:
        return True
    elif hour1 < hour2:
        return False
    if min1 > min2:
        return True
    elif min1 < min2:
        return False
    if sec1 > sec2:
        return True
    return False

