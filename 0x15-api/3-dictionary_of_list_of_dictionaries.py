#!/usr/bin/python3
"""Exports to-do of all employees to JSON format."""
import requests
import csv
import json
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


def export_to_json(all_tasks):
    json_filename = "todo_all_employees.json"
    with open(json_filename, mode='w') as file:
        json.dump(all_tasks, file, indent=4)
    print(f"Data exported to {json_filename}")


if __name__ == '__main__':
    all_tasks = {}

    try:
        for user_id in range(1, 11):  # Assuming user IDs range from 1 to 10
            user_data = fetch_user_data(user_id)
            user_name = user_data['name']
            todos = fetch_user_todos(user_id)

            tasks = []
            for task in todos:
                tasks.append({"username": user_name,
                              "task": task['title'],
                              "completed": task['completed']})

            all_tasks[user_id] = tasks

        export_to_json(all_tasks)
    except requests.RequestException as e:
        print("Error:", e)
        sys.exit(1)
