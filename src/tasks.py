from datetime import datetime


class Task:
    def __init__(
        self,
        task_name: str,
        description: str,
        author: str,
        created_on: datetime = datetime.now(),
        due_date: datetime = datetime(1, 1, 1),
        notes: list[str] = ["No notes"],
    ) -> None:
        self.task_name = task_name
        self.description = description
        self.author = author
        self.created_on = str(created_on)
        self.due_date = str(due_date)
        self.notes = notes

    def get_task(self) -> dict:
        task = {
            "description": self.description,
            "created_on": self.created_on,
            "due_date": self.due_date,
            "notes": self.notes,
        }

        return task

    def to_team(self, team_name):
        return TeamTask(
            self.task_name,
            team_name,
            self.description,
            self.author,
            created_on=self.created_on,
            due_date=self.due_date,
            notes=self.notes,
        )

    def format(self) -> str:
        return f"Task Name : {self.task_name}\nDescription : {self.description}\nCreated On : {self.created_on}\nDue Date : {self.due_date}\nAdditional Notes : {str(self.notes)}"

    def __repr__(self) -> str:
        return f"{self.task_name} : {self.get_task()}"


class TeamTask(Task):
    def __init__(
        self,
        task_name: str,
        team_name: str,
        description: str,
        author: str,
        assignees: list[str] = ["No assignees"],
        created_on: datetime = datetime.now(),
        due_date: datetime = datetime(1, 1, 1),
        notes: list[str] = ["No notes"],
    ) -> None:
        super().__init__(
            task_name=task_name,
            description=description,
            author=author,
            created_on=created_on,
            due_date=due_date,
            notes=notes,
        )
        self.team_name = team_name
        self.assignees = assignees

    def get_task(self) -> dict:
        task = {
            "description": self.description,
            "author": self.author,
            "assignees": self.assignees,
            "created_on": self.created_on,
            "due_date": self.due_date,
            "notes": self.notes,
        }

        return task

    def assign(self, assignee: str) -> None:
        if assignee != self.author:
            if assignee not in self.assignees:
                self.assignees.append(assignee)
                if self.assignees[0] == "No assignees":
                    self.assignees.pop(0)

    def unassign(self, assignee: str) -> None:
        if assignee in self.assignees:
            self.assignees.remove(assignee)

    def set_team_name(self, team_name: str) -> None:
        self.team_name = team_name

    def to_user(self, author: str) -> Task:
        return Task(
            self.task_name,
            self.description,
            author,
            self.created_on,
            self.due_date,
            self.notes,
        )

    def format(self) -> str:
        return f"Task Name : {self.task_name}\nDescription : {self.description}\nAuthor : {self.author}\nAssigned To : {self.assignees}\nCreated On : {self.created_on}\nDue Date : {self.due_date}\nAdditional Notes : {str(self.notes)}"


def compile_format(tasklist: list[Task]) -> str:
    return (
        "```yaml\n"
        + "\n\n".join(
            [f"{index+1}. " + task.format() for index, task in enumerate(tasklist)]
        )
        + "```"
    )


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
