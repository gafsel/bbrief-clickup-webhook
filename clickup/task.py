import requests
import os

CLICKUP_BASE_PATH = os.getenv("CLICKUP_BASE_PATH")
CLICKUP_API_KEY = os.getenv("CLICKUP_API_KEY")


def get(task_id: str) -> dict:
    print(f"Getting task {task_id} data")

    resp = requests.get(
        f"{CLICKUP_BASE_PATH}/task/{task_id}",
        timeout=10,
        headers={
            "Authorization": f"{CLICKUP_API_KEY}"
        })

    if resp.status_code == 200:
        return resp.json()
    else:
        raise Exception(f"Falha ao consultar task {task_id}")