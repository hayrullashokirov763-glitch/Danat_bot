import asyncio
import logging
from aiogram import Bot, Dispatcher, F, types
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import database as db
from states import DonateState

# ----------------- SOZLAMALAR -----------------
TOKEN = "8239144356:AAFcWdPNt-oY_RkPPodHGjull6TonE_oNlk"
ADMIN_GROUP_ID = -1004251107671  # Cheklar boradigan guruh ID-si
ADMIN_ID = 7261837291             # O'zingizning shaxsiy Telegram ID-ingiz
CARD_NUMBER = "5440810301878483 (Shokirov Xayrulla)"
# ----------------------------------------------

bot = Bot(token=TOKEN)
dp = Dispatcher()
