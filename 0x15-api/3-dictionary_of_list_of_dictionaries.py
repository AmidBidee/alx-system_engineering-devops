#!/usr/bin/python3
"""
Extend the python script from exercise 0 to export data in JSON format.

Records all completed tasks from all employees.
Format must be: {"USER_ID": [ {"task": TASK_TITLE,
                               "completed": TASK_COMPLETED_STATUS,
                               "username": USERNAME"},
                               {...}
                            ]
File name must be: todo_all_employees.json
"""
import json
import requests

if __name__ == "__main__":
    users = requests.get("http://jsonplaceholder.typicode.com/users").json()
    tasks = requests.get("http://jsonplaceholder.typicode.com/todos").json()
    all_user_tasks = {}

    for user in users:
        eid = user.get("id")
        username = user.get("username")
        all_tasks = []

        for task in tasks:
            if (task.get("userId") == eid):
                temp = {}
                temp["username"] = username
                temp["task"] = task.get("title")
                temp["completed"] = task.get("completed")
                all_tasks.append(temp)

        all_user_tasks[eid] = all_tasks

    with open('todo_all_employees.json', 'w+') as jsonfile:
        jsonfile.write(json.dumps(all_user_tasks))
