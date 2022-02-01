#!/usr/bin/python3
"""
Extend the python script from exercise 0 to export data in CSV format.
Record all tasks that are owned by the employee.
Format must be: "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
File name must be: USER_ID.csv
"""
import json
import requests
import sys

if __name__ == "__main__":
    eid = sys.argv[1]
    username = requests.get("http://jsonplaceholder.typicode.com/users/{}"
                            .format(eid)).json().get("username")
    all_user_tasks = {}
    tasks = []
    r = requests.get("http://jsonplaceholder.typicode.com/todos").json()

    for task in r:
        if (task.get("userId") == int(eid)):
            temp = {}
            temp['task'] = task.get("title") 
            temp['completed'] = task.get("completed")
            temp['username'] = username
            tasks.append(temp)

    all_user_tasks['{}'.format(eid)] = tasks
        

    with open('{}.json'.format(eid), 'w+') as jsonfile:
         jsonfile.write(json.dumps(all_user_tasks))