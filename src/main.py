from rich import print
from datetime import datetime

import interactions
from auth import get_token
from tasks import Task, TeamTask, compile_format
import db

bot = interactions.Client(token=get_token())


@bot.command()
@interactions.option(str, name="group", description="User/Team", required=False)
@interactions.option(
    str, name="group_name", description="name of the team", required=False
)
async def tasklist(
    ctx: interactions.CommandContext, group: str = "user", group_name: str = " "
):
    """Returns a list of all the tasks for the given User/Team

    Args:
        ctx (interactions.CommandContext): _description_
    """
    if group.lower() == "user":
        if group_name == " ":
            try:
                tasks = db.get_user_tasks(ctx.author.name)
            except AttributeError:
                await ctx.send("`You have 0 tasks at the moment`")
                return
            await ctx.send(compile_format(tasks))
        else:
            try:
                tasks = db.get_user_tasks(group_name)
            except AttributeError:
                await ctx.send(f"`{group_name} has 0 tasks at the moment`")
                return
            await ctx.send(compile_format(tasks))
    elif group.lower() == "team":
        if group_name == " ":
            await ctx.send("```Error: Please give the team name as an argument```")
        else:
            try:
                tasks = db.get_team_tasks(group_name)
            except AttributeError:
                await ctx.send(f"`{group_name} has 0 tasks at the moment`")
                return
            await ctx.send(compile_format(tasks))


@bot.command()
@interactions.option(name="task_name", description="Name for the task", required=True)
@interactions.option(name="description", description="Describe the task", required=True)
@interactions.option(
    name="team_name",
    description="Team to add task to (leave empty for user tasks)",
    required=False,
)
@interactions.option(
    name="assignees",
    description="Name of the assignees you'd like to add (Case sensitive, separate using ':')",
    required=False,
)
@interactions.option(
    name="due_date",
    description="Due Date for the task (Year/Month/Date/Hour/Minute/Second)",
    required=False,
)
@interactions.option(
    name="notes",
    description="Additional notes for the task(use | to separate notes)",
    required=False,
)
async def new_task(
    ctx: interactions.CommandContext,
    task_name: str,
    description: str,
    team_name: str = " ",
    assignees: str = " ",
    due_date: str = " ",
    notes: str = " ",
):
    due_date = (
        datetime(*tuple(map(lambda x: int(x), due_date.split("/"))))
        if due_date != " "
        else datetime(1, 1, 1)
    )
    notes = notes.split("|") if notes != " " else ["No notes"]
    if team_name == " ":
        task = Task(
            task_name, description, ctx.author.name, due_date=due_date, notes=notes
        )
        db.add_user_task(task)
        await ctx.send(
            f"Task Added. Information about task :{compile_format([task.format()])}"
        )
    else:
        assignees = assignees.split(":") if assignees == " " else ["No assignees"]
        task = TeamTask(
            task_name,
            team_name,
            description,
            ctx.author.name,
            assignees,
            due_date=due_date,
            notes=notes,
        )
        db.add_team_task(task)
        await ctx.send(
            f"Task Added. Information about task : {compile_format([task.format()])}"
        )


@bot.command()
@interactions.option(
    name="task_name", description="Name of the task to be deleted", required=True
)
@interactions.option(
    name="team_name",
    description="Team to add task to (leave empty for user tasks)",
    required=False,
)
async def remove_task(
    ctx: interactions.CommandContext, task_name: str, team_name: str = " "
):
    if team_name == " ":
        db.delete_user_task_explicit(ctx.author.name, task_name)
    else:
        db.delete_team_task_explicit(team_name, task_name)
    
    await ctx.send("`Task deleted`")

@bot.command()
@interactions.option(name="task_name", description="Name of task", required=True)
@interactions.option(name="team_name", description="Name of team to move task to", required=True)
@interactions.option(name="source", description="Group to which the task belongs (leave empty for user tasks)", required=False)
async def move_to_team(ctx: interactions.CommandContext, task_name: str, team_name: str, source: str = " "):
    if source == " ":
        try:
            task = [task for task in db.get_user_tasks(ctx.author.name) if task.task_name == task_name][0]
        except IndexError:
            await ctx.send(f"`There are no tasks matching {task_name}`")
        db.delete_user_task_implicit(task)
        db.add_team_task(task.to_team(team_name))
    else:
        try:
            task = [task for task in db.get_team_tasks(source) if task.task_name == task_name][0]
        except AttributeError:
            await ctx.send(f"`There is no team named {team_name}`")
            return
        except IndexError:
            await ctx.send(f"`There are no tasks matching {task_name}`")
            return
        db.delete_team_task_implicit(task)
        db.add_team_task(task.to_team(team_name))
    await ctx.send(f"`Task transfered to {team_name}`")

@bot.command()
@interactions.option(name="task_name", description="Name of task", required=True)
@interactions.option(name="source", description="Team to which the task belongs", required=True)
async def move_to_self(ctx: interactions.CommandContext, task_name: str, source: str):
    try:
        task = [task for task in db.get_team_tasks(source) if task.task_name == task_name][0]
    except AttributeError:
        await ctx.send(f"`There is no task matching {task_name} in {source}`")
        return
    db.delete_team_task_implicit(task)
    db.add_user_task(task.to_user(ctx.author.name))
    await ctx.send(f"`Task added to {ctx.author.name}`")
    


if __name__ == "__main__":
    bot.start()
