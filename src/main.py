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
            await ctx.send(compile_format(db.get_user_tasks(ctx.author.name)))
        else:
            await ctx.send(compile_format(db.get_user_tasks(group_name)))
    elif group.lower() == "team":
        if group_name == " ":
            await ctx.send("```Error: Please give the team name as an argument```")
        else:
            await ctx.send(compile_format(db.get_team_tasks(group_name)))

@bot.command()
@interactions.option(name="task_name", description="Name for the task", required=True)
@interactions.option(name="description", description="Describe the task", required=True)
@interactions.option(name="team_name", description="Team to add task to (leave empty for user tasks)", required=False)
@interactions.option(name="assignees", description="Name of the assignees you'd like to add (Case sensitive, separate using ':')", required=False)
@interactions.option(name="due_date", description="Due Date for the task (Year/Month/Date/Hour/Minute/Second)", required=False)
@interactions.option(name="notes", description="Additional notes for the task(use | to separate notes)", required=False)
async def new_task(ctx: interactions.CommandContext, task_name: str, description: str ,team_name: str = ' ', assignees: str = ' ', due_date: str = ' ', notes: str = ' '):
    due_date = datetime(*tuple(map(lambda x : int(x), due_date.split('/')))) if due_date != ' ' else datetime(1,1,1)
    notes = notes.split('|') if notes != ' ' else ["No notes"]
    if team_name == ' ':
        task = Task(
                task_name,
                description,
                ctx.author.name,
                due_date=due_date,
                notes=notes
            )
        db.add_user_task(task)
        await ctx.send(f"Task Added. Information about task :{compile_format([task.format()])}")
    else:
        assignees = assignees.split(':') if assignees == ' ' else ["No assignees"]
        task = TeamTask(
            task_name,
            team_name,
            description,
            ctx.author.name,  
            assignees,
            due_date=due_date,
            notes=notes
        )
        db.add_team_task(TeamTask)
        await ctx.send(f"Task Added. Information about task : {compile_format([task.format()])}")

@bot.command()
@interactions.option(name="task_name", description="Name of the task to be deleted", required=True)
@interactions.option(name="team_name", description="Team to add task to (leave empty for user tasks)", required=False)
async def remove_task(ctx: interactions.CommandContext, task_name: str, team_name: str = ' '):
    if team_name == ' ':
        db.delete_user_task_explicit(ctx.author.name, task_name)
        await ctx.send("`Task deleted`")
    else:
        db.delete_team_task_explicit(team_name, task_name)
        await ctx.send("`Task deleted`")


if __name__ == "__main__":
    bot.start()
