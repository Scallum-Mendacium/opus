from rich import print
import interactions
from auth import get_token

# from db import teams, users
from tasks import Task, TeamTask

bot = interactions.Client(token=get_token())


# @bot.command()
# @interactions.option()
# async def tasklist(ctx: interactions.CommandContext, team: str = None):
#     """Lists all the current tasks (private/assigned to you)
#     Args:
#         channel (interactions.CommandContext): _description_
#     """
#     await ctx.send(get_tasks(team) if team else get_tasks(ctx.author.name))


if __name__ == "__main__":
    bot.start()
