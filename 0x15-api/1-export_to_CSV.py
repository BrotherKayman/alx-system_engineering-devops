#!/usr/bin/python3
"""Exports employee to-do list data to CSV format."""
import requests
import csv
import sys


def fetch_user_data(user_id):
    endpoint = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    response = requests.get(endpoint)
    response.raise_for_status()
    return response.json()


def fetch_user_todos(user_id):
    endpoint = "https://jsonplaceholder.typicode.com/todos"
    params = {'userId': user_id}
    response = requests.get(endpoint, params=params)
    response.raise_for_status()
    return response.json()


def export_to_csv(user_id, user_name, completed_tasks):
    csv_filename = f"{user_id}.csv"
    with open(csv_filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(
            ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        writer.writerows(completed_tasks)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit(1)

    user_id = sys.argv[1]

    try:
        user_data = fetch_user_data(user_id)
        user_name = user_data['name']
        todos = fetch_user_todos(user_id)

        completed_tasks = [
            (user_id,
             user_name,
             task['completed'],
                task['title']) for task in todos]

        export_to_csv(user_id, user_name, completed_tasks)
    except requests.RequestException as e:
        sys.exit(1)
    except KeyError:
        sys.exit(1)
