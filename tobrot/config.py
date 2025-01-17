import os

class Config(object):

    # get a token from @BotFather

    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "1704140019:AAF7br57RFmDgfMTmi2MgqMjnhUKU-x3HRQ")

    # The Telegram API things

    APP_ID = int(os.environ.get("APP_ID", 4867825))

    API_HASH = os.environ.get("API_HASH", aabe3552a9471da31e974e5d455d37be))

    # Get these values from my.telegram.org

    # to store the channel ID who are authorized to use the bot

    AUTH_CHANNEL = int(os.environ.get("AUTH_CHANNEL", -1001403741622))

    # the download location, where the HTTP Server runs

    DOWNLOAD_LOCATION = "./DOWNLOADS"

    # Telegram maximum file upload size

    MAX_FILE_SIZE = 50000000

    TG_MAX_FILE_SIZE = 1572864000

    FREE_USER_MAX_FILE_SIZE = 50000000

    # chunk size that should be used with requests

    CHUNK_SIZE = int(os.environ.get("CHUNK_SIZE", 128))

    # default thumbnail to be used in the videos

    DEF_THUMB_NAIL_VID_S = os.environ.get("DEF_THUMB_NAIL_VID_S", "https://placehold.it/90x90")

    # maximum message length in Telegram

    MAX_MESSAGE_LENGTH = 4096

    # set timeout for subprocess

    PROCESS_MAX_TIMEOUT = 3600

    #

    ARIA_TWO_STARTED_PORT = int(os.environ.get("ARIA_TWO_STARTED_PORT", 6800))

    EDIT_SLEEP_TIME_OUT = int(os.environ.get("EDIT_SLEEP_TIME_OUT", 1))

    MAX_TIME_TO_WAIT_FOR_TORRENTS_TO_START = int(os.environ.get("MAX_TIME_TO_WAIT_FOR_TORRENTS_TO_START", 600))

    MAX_TG_SPLIT_FILE_SIZE = int(os.environ.get("MAX_TG_SPLIT_FILE_SIZE", 1072864000))
