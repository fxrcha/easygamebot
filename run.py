from src.bot import EasyGameBot
from src.webserver import app
from src.utils import get_config
import asyncio
import os


if __name__ == "__main__":
    config = get_config()
    bot = EasyGameBot()
    app.bot = bot

    if not os.path.isdir("logs"):
        os.mkdir("logs")

    loop = asyncio.get_event_loop()

    BotFuture = asyncio.ensure_future(bot.start(config["bot"]["token"]))
    WebFuture = asyncio.ensure_future(
        app.create_server(
            host=config["admin_tool"]["host"],
            port=config["admin_tool"]["port"],
            return_asyncio_server=True,
            access_log=False,
        )
    )

    loop.run_forever()
