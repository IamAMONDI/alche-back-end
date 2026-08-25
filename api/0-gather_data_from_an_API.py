#!/usr/bin/python3
"""Gather an employee's TODO list progress from a REST API."""

import requests
import sys


def main():
    """Display an employee's completed TODO tasks."""
    employee_id = int(sys.argv[1])

    user_url = (
        "https://jsonplaceholder.typicode.com/users/{}"
        .format(employee_id)
    )
    todos_url = (
        "https://jsonplaceholder.typicode.com/users/{}/todos"
        .format(employee_id)
    )

    user = requests.get(user_url).json()
    todos = requests.get(todos_url).json()

    employee_name = user.get("name")
    completed_tasks = [
        task for task in todos if task.get("completed")
    ]

    print(
        "Employee {} is done with tasks({}/{}):"
        .format(employee_name, len(completed_tasks), len(todos))
    )

    for task in completed_tasks:
        print("\t {}".format(task.get("title")))


if __name__ == "__main__":
    main()