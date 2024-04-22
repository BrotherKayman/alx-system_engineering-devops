#!/usr/bin/python3
"""returns information about employee's TODO list progress"""
import requests
import sys


def fetch_user_data(user_id):
    endpoint = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)
    response = requests.get(endpoint)
    response.raise_for_status()
    return response.json()


def fetch_user_todos(user_id):
    endpoint = "https://jsonplaceholder.typicode.com/todos"
    params = {'userId': user_id}
    response = requests.get(endpoint, params=params)
    response.raise_for_status()
    return response.json()


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <user_id>")
        sys.exit(1)

    user_id = sys.argv[1]

    try:
        user_data = fetch_user_data(user_id)
        user_name = user_data['name']
        todos = fetch_user_todos(user_id)

        completed_tasks = [task['title']
                           for task in todos if task['completed']]
        total_tasks = len(todos)

        print(
            f"Employee {user_name} has completed {len(completed_tasks)} out of {total_tasks} tasks:")
        for task in completed_tasks:
            print(f"\t{task}")
    except requests.RequestException as e:
        print("Error:", e)
        sys.exit(1)
    except KeyError:
        print("Invalid user ID or data format")
        sys.exit(1)
