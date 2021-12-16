# Copyright (C) 2020-2021 by Xdenvil@Github, < https://github.com/xdenvil >.
#
# This file is part of < https://github.com/Anieteam/Aniebots> project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/Anieteam/Aniebots/blob/master/LICENSE >
#
# All rights reserved.

import logging
import sys
import time
from pyrogram import Client, errors
from config import API_HASH, API_ID, SESSION
import logging

import logging

logging.basicConfig(
    filename="app.txt",
    level=logging.ERROR,
    format="%(asctime)s %(levelname)s %(name)s %(message)s",
)
LOGGER = logging.getLogger(__name__)

HELP = {}
CMD_HELP = {}

StartTime = time.time()

API_ID = API_ID
API_HASH = API_HASH
SESSION = SESSION

app = Client(SESSION, api_id=API_ID, api_hash=API_HASH)
