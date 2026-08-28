#!/usr/bin/python3
"""Export an employee's TODO list to CSV format."""

import csv
import json
import sys
from urllib.request import urlopen


def main():
    """Export an employee's TODO list to a CSV file."""
    employee_id = int(sys.argv[1])

    user_url = (
        "https://jsonplaceholder.typicode.com/users/{}"
        .format(employee_id)
    )
    todos_url = (
        "https://jsonplaceholder.typicode.com/users/{}/todos"
        .format(employee_id)
    )

    user = json.loads(urlopen(user_url).read().decode("utf-8"))
    todos = json.loads(urlopen(todos_url).read().decode("utf-8"))

    username = user.get("username")

    filename = "{}.csv".format(employee_id)

    with open(filename, "w", newline="") as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)

        for task in todos:
            writer.writerow([
                employee_id,
                username,
                task.get("completed"),
                task.get("title")
            ])


if __name__ == "__main__":
    main()