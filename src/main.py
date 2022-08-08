import interactions
from auth import get_token
from tasks import Task, TeamTask
import db

bot = interactions.Client(token=get_token())

if __name__ == "__main__":
    bot.start()
