from rich import print
# import interactions
from auth import get_token
# from db import teams, users
from tasks import Task, TeamTask

# bot = interactions.Client(token=get_token())


def get_tasks(name: str, users=None, teams=None, type: str = "user"):
    if type == "user":
        data = users.get()
        if name in data.keys():
            return data[name]
        else:
            raise Exception("User not found in database")
    elif type == "team":
        data = teams.get()
        if name in data.keys():
            return data[name]
        else:
            raise Exception("Team name not found in database")


# @bot.command()
# @interactions.option()
# async def tasklist(ctx: interactions.CommandContext, team: str = None):
#     """Lists all the current tasks (private/assigned to you)
#     Args:
#         channel (interactions.CommandContext): _description_
#     """
#     await ctx.send(get_tasks(team) if team else get_tasks(ctx.author.name))


def test_tasks():
    task = Task(
        "Nice", "AAAAAAA", "Utkarsh", due_date="Random thing", notes=["hmm", "hmmmm"]
    )
    print(task.get_data())
    task = task.to_team("Epic team moment")
    print(task.get_data())
    task.assign("Praneeth")
    task.assign("Utkarsh")
    print(task.get_data())
    task.unassign("Utkarsh")
    print(task.get_data())
    task.unassign("Praneeth")
    print(task.get_data())
    task = task.to_user("Utkarsh")
    print(task.get_data())


if __name__ == "__main__":
    test_tasks()
