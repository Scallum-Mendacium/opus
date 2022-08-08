import firebase_admin
from firebase_admin import credentials, db
from tasks import Task, TeamTask
from datetime import datetime
from rich import print

cred = credentials.Certificate("src/serviceAccountKey.json")
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
