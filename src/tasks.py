from datetime import datetime


class Task:
    def __init__(
        self,
        name: str,
        description: str,
        author: str,
        created_on: datetime = datetime.now(),
        due_date: datetime | None = None,
        notes: list[str] = [],
    ) -> None:
        self.name = name
        self.description = description
        self.author = author
        self.created_on = str(created_on)
        self.due_date = str(due_date)
        self.notes = notes

    def get_data(self) -> dict:
        data = {
            self.name: {
                "description": self.description,
                "created_on": self.created_on,
                "due_date": self.due_date,
                "notes": self.notes,
            }
        }

        return data

    def to_team(self, team_name):
        return TeamTask(
            self.name,
            team_name,
            self.description,
            self.author,
            created_on=self.created_on,
            due_date=self.due_date,
            notes=self.notes,
        )


class TeamTask(Task):
    def __init__(
        self,
        name: str,
        team_name: str,
        description: str,
        author: str,
        assignees: list[str] = [],
        created_on: datetime = datetime.now(),
        due_date: datetime | None = None,
        notes: list[str] = [],
    ) -> None:
        super().__init__(
            name=name,
            description=description,
            author=author,
            created_on=created_on,
            due_date=due_date,
            notes=notes,
        )
        self.team_name = team_name
        self.assignees = assignees

    def get_data(self) -> dict:
        data = {
            self.name: {
                "description": self.description,
                "author": self.author,
                "assignees": self.assignees,
                "created_on": self.created_on,
                "due_date": self.due_date,
                "notes": self.notes,
            }
        }

        return data

    def assign(self, assignee: str) -> None:
        (
            (assignee not in self.assignees) and (assignee != self.author)
        ) and self.assignees.append(assignee)

    def unassign(self, assignee: str) -> None:
        (assignee in self.assignees) and self.assignees.remove(assignee)

    def set_team_name(self, team_name: str) -> None:
        self.team_name = team_name

    def to_user(self, author: str) -> Task:
        return Task(
            self.name,
            self.description,
            author,
            self.created_on,
            self.due_date,
            self.notes,
        )
