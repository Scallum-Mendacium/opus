import firebase_admin
from firebase_admin import credentials, db
from tasks import Task, TeamTask
from datetime import datetime
import os

CRED = {
    "auth_provider_x509_cert_url": os.environ.get("auth_provider_x509_cert_url"),
    "auth_uri": os.environ.get("auth_uri"),
    "client_email": os.environ.get("client_email"),
    "client_id": os.environ.get("client_id"),
    "client_x509_cert_url": os.environ.get("client_x509_cert_url"),
    "private_key": os.environ.get("private_key"),
    "private_key_id": os.environ.get("private_key_id"),
    "project_id": os.environ.get("project_id"),
    "token_uri": os.environ.get("token_uri"),
    "type": os.environ.get("type"),
}

cred = credentials.Certificate(CRED)
app = firebase_admin.initialize_app(
    cred,
    {
        "databaseURL": "https://opus-db287-default-rtdb.asia-southeast1.firebasedatabase.app/"
    },
)

teams = db.reference("Teams")
users = db.reference("Users")


def add_team_task(team_task: TeamTask) -> None:
    teams.child(team_task.team_name).update({team_task.task_name: team_task.get_task()})


def add_user_task(task: Task) -> None:
    users.child(task.author).update({task.task_name: task.get_task()})


def delete_user_task_implicit(task: Task) -> None:
    users.child(f"{task.author}/{task.task_name}").delete()


def delete_user_task_explicit(author: str, task_name: str) -> None:
    users.child(f"{author}/{task_name}").delete()


def delete_team_task_implicit(team_task: TeamTask) -> None:
    teams.child(f"{team_task.team_name}/{team_task.task_name}").delete()


def delete_team_task_explicit(team_name: str, task_name: str) -> None:
    teams.child(f"{team_name}/{task_name}").delete()


def get_user_tasks(author: str) -> list:
    return [
        Task(
            task_name,
            data["description"],
            author,
            datetime.strptime(data["created_on"], "%Y-%m-%d %H:%M:%S.%f"),
            datetime.strptime(data["due_date"], "%Y-%m-%d %H:%M:%S"),
            data["notes"],
        )
        for task_name, data in users.child(author).get().items()
    ]


def get_team_tasks(team_name: str) -> dict:
    return [
        TeamTask(
            task_name,
            team_name,
            data["description"],
            data["author"],
            data["assignees"],
            datetime.strptime(data["created_on"], "%Y-%m-%d %H:%M:%S.%f"),
            datetime.strptime(data["due_date"], "%Y-%m-%d %H:%M:%S"),
            data["notes"],
        )
        for task_name, data in teams.child(team_name).get().items()
    ]


# 1. Edit task
# 2. Complete task
