from datetime import datetime

import interactions
from auth import get_token

bot = interactions.Client(token=get_token())


def get_tasks():
    return {
        "Teams": {
            "Make opus bot": {
                "Description": "Finish making a bot that can handle group/personal tasks on discord, easily and elegantly",
                "Assignee": ["Utshaan#9092", "PananaBants78#9226"],
                "Creator": "PananaBants78#9226",
                "Deadline": datetime(year=2022, month=8, 9, 23, 59, 59),
                "Created": datetime(2022, 8, 4, 15, 23, 32),
            },
        }
    }


@bot.command()
async def tasklist(channel: interactions.CommandContext):
    """Lists all the current tasks (private/assigned to you)

    Args:
        channel (interactions.CommandContext): _description_
    """
    await channel.send(get_tasks())


if __name__ == "__main__":
    bot.start()
