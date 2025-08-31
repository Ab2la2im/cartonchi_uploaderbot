from aiogram import types
from aiogram.filters import Command
from bot import dp

@dp.message(Command("start"))
async def start_handler(message: types.Message):
    await message.answer("سلام! ربات با موفقیت بالا آمد.")