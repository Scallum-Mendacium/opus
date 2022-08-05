from datetime import datetime
from rich import print

import interactions
from auth import get_token
from db import teams, users

bot = interactions.Client(token=get_token())


class TeamTasks:
    def __init__(
        self,
        name: str,
        team: str,
        description: str,
        author: str,
        assignees: list = None,
        due_date: str(datetime) = None,
        notes: str = None,
    ) -> None:
        self.name = name
        self.team = team
        self.description = description
        self.author = author
        self.assignees = assignees
        self.due_date = due_date
        self.notes = notes
        self.data = self.create()

    def create(self) -> dict:
        task = {
            self.name: {
                "description": self.description,
                "created_on": str(datetime.now()),
                "due_date": self.due_date,
                "notes": self.notes,
            }
        }
        if self.team:
            task[self.name]["team"] = self.team
            task[self.name]["author"] = self.author
            task[self.name]["assignees"] = self.assignees

        return task

    def change_team(self, team):
        if self.team:
            self.team = team
            self.data = self.create()

    def to_private(self):
        if self.team:
            self.team = None
            self.data = self.create()


class Tasks(TeamTasks):
    def __init__(
        self,
        name: str,
        description: str,
        author: str,
        due_date: str(datetime) = None,
        notes: str = None,
    ) -> None:
        super().__init__(
            name=name,
            team=None,
            description=description,
            author=author,
            assignees=None,
            due_date=due_date,
            notes=notes,
        )

    def to_team(self, team):
        self.team = team
        self.data = self.create()


def get_tasks(name: str, type: str = "user"):
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


@bot.command()
@interactions.option()
async def tasklist(ctx: interactions.CommandContext, team: str = None):
    """Lists all the current tasks (private/assigned to you)

    Args:
        channel (interactions.CommandContext): _description_
    """
    await ctx.send(get_tasks(team) if team else get_tasks(ctx.author.name))


if __name__ == "__main__":
    bot.start()
