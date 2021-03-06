import logging
import sys
import discord

FORMATTER = logging.Formatter(
    "[%(asctime)s] [%(filename)s] [%(name)s:%(module)s] [%(levelname)s]: %(message)s"
)

SANIC_CONFIG = dict(
    version=1,
    disable_existing_loggers=False,
    loggers={
        "sanic.root": {"level": "INFO", "handlers": ["console", "file_generic"]},
        "sanic.error": {
            "level": "INFO",
            "handlers": ["error_console", "file_generic"],
            "propagate": True,
            "qualname": "sanic.error",
        },
        "sanic.access": {
            "level": "INFO",
            "handlers": ["access_console", "file_access"],
            "propagate": True,
            "qualname": "sanic.access",
        },
    },
    handlers={
        "file_generic": {
            "class": "logging.FileHandler",
            "formatter": "generic",
            "filename": "logs/sanic_generic.txt",
        },
        "file_access": {
            "class": "logging.FileHandler",
            "formatter": "access",
            "filename": "logs/sanic_access.txt",
        },
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "generic",
            "stream": sys.stdout,
        },
        "error_console": {
            "class": "logging.StreamHandler",
            "formatter": "generic",
            "stream": sys.stderr,
        },
        "access_console": {
            "class": "logging.StreamHandler",
            "formatter": "access",
            "stream": sys.stdout,
        },
    },
    formatters={
        "generic": {
            "format": "[%(asctime)s] [%(filename)s] [%(name)s:%(module)s] [%(levelname)s]: %(message)s",
            "class": "logging.Formatter",
        },
        "access": {
            "format": "[%(asctime)s] [%(filename)s] [%(name)s:%(module)s] [%(levelname)s]: "
            + "%(request)s %(message)s %(status)d %(byte)d",
            "class": "logging.Formatter",
        },
    },
)


class Logger:
    @staticmethod
    def cogLogger(cog) -> logging.Logger:
        name = cog.__class__.__qualname__
        logger = logging.getLogger(name)
        logger.setLevel(logging.INFO)

        if not logger.hasHandlers():
            streamhandler = logging.StreamHandler()
            streamhandler.setFormatter(FORMATTER)
            filehandler = logging.FileHandler(f"logs/{name}.txt", "a")
            filehandler.setFormatter(FORMATTER)
            logger.addHandler(streamhandler)
            logger.addHandler(filehandler)

        logger.info(f"{name} Loaded.")
        return logger

    @staticmethod
    def defaultLogger(name) -> logging.Logger:
        log = logging.getLogger(name)
        log.setLevel(logging.INFO)

        if not log.hasHandlers():
            stream_handler = logging.StreamHandler()
            filehandler = logging.FileHandler("logs/{}.txt".format(name), "a")
            stream_handler.setFormatter(FORMATTER)
            filehandler.setFormatter(FORMATTER)
            log.addHandler(filehandler)
            log.addHandler(stream_handler)

        log.info(f"{name} Loaded.")
        return log

    @staticmethod
    def discordLogger() -> logging.Logger:
        logger = logging.getLogger("discord")
        logger.setLevel(logging.INFO)
        logger.handlers.clear()
        streamhandler = logging.StreamHandler()
        streamhandler.setFormatter(FORMATTER)
        filehandler = logging.FileHandler(f"logs/discord.txt", "a")
        filehandler.setFormatter(FORMATTER)
        logger.addHandler(streamhandler)
        logger.addHandler(filehandler)
        return logger
