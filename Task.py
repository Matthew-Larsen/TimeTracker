import json

from dateutil import parser


class TaskList:
    def __init__(self, tasks):
        self.tasks = tasks

    def copy_task_list(self, task_list):
        self.tasks = task_list.tasks

    def import_json(self):
        output = TaskList([])
        try:
            with open("tasks.json", "r") as jsonFile:
                data = json.load(jsonFile)
                output = TaskList(self.get_tasks_from_json(data))
        except:
            raise Exception("No file to load")

        return output

    def get_tasks_from_json(self, data):
        output_list = []
        for task in data['tasks']:
            output_list.append(Task(task["name"], self.get_usage_data_from_json(task)))
        return output_list

    def get_usage_data_from_json(self, task):
        usage_data = []
        for entry in task['usage_data']:
            usage_data.append(
                Use(parser.parse(entry["start_time"]),
                    parser.parse(entry["end_time"])))
        return usage_data

    def serialize(self):
        list_of_tasks = []
        for task in self.tasks:
            list_of_tasks.append(task.serialize())

        return {
            "tasks": list_of_tasks
        }


class Task:

    def __init__(self, name, usage_data):
        self.name = name
        self.usage_data = usage_data

    def serialize(self):
        return {
            'name': self.name,
            'usage_data': self.convert_uses_to_json()
        }

    def convert_uses_to_json(self):
        use_list = []
        for use in self.usage_data:
            use_list.append(use.serialize())
        return use_list


class Use:

    def __init__(self, start_time, end_time):
        self.start_time = start_time
        self.end_time = end_time
        self.elapsed_time = end_time - start_time
        self.calculate_elapsed()

    def calculate_elapsed(self):
        self.days = self.elapsed_time.days
        self.seconds = self.elapsed_time.seconds
        self.hours = self.seconds // 3600
        self.minutes = (self.seconds % 3600) // 60
        self.seconds = self.seconds % 60

    def serialize(self):
        return {
            "start_time": self.start_time.strftime("%Y-%m-%d %H:%M:%S"),
            "end_time": self.end_time.strftime("%Y-%m-%d %H:%M:%S"),
            "days": self.days,
            "hours": self.hours,
            "minutes": self.minutes,
            "seconds": self.seconds
        }
