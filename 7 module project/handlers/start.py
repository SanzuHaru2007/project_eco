from aiogram import F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
import random

from keyboards.keyboards import main_keyboard

def register_start_handlers(dp):
    @dp.message(Command("start"))
    async def start_handler(message: Message):
        await message.answer(
            "🕵️‍♀️ Добро пожаловать в штаб-квартиру расследований.\n"
            "Ты получил доступ к закрытым базам ООН. Здесь не будет скучных лекций. Только дела, факты и твоя логика.\n"
            "Что тебя ждёт:\n"
            "🌍 Три реальных экопреступления (нефтяные субсидии, разливы, уничтожение лесов)\n"
            "🔍 Выбор из трёх подозреваемых в каждом деле",
            reply_markup=main_keyboard
        )