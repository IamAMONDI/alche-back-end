#!/usr/bin/python3
"""Gather an employee's TODO list progress from a REST API."""

import json
import sys
from urllib.request import urlopen


def main():
    """Display an employee's completed TODO tasks."""
    employee_id = int(sys.argv[1])

    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = (
        f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    )

    user = json.loads(urlopen(user_url).read().decode("utf-8"))
    todos = json.loads(urlopen(todos_url).read().decode("utf-8"))

    employee_name = user.get("name")
    completed_tasks = [task for task in todos if task.get("completed")]

    print(
        f"Employee {employee_name} is done with tasks("
        f"{len(completed_tasks)}/{len(todos)}):"
    )

    for task in completed_tasks:
        print(f"\t {task.get('title')}")


if __name__ == "__main__":
    main()