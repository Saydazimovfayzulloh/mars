from aiogram import types, Bot, executor, Dispatcher
from data import Api_token
import logging
from buttons import menuMain
from inline_buttons import meneProducts, meneCourses
from aiogram.types import CallbackQuery

bot = Bot(token=Api_token)
dp = Dispatcher(bot)

logging.basicConfig(level=logging.INFO)

@dp.message_handler(commands=["start"])
async def start(message:types.Message):
    username = message.from_user.full_name
    await message.answer(f"Salom {username} Botimizga xush kelib siz.\nKerakli bo'limni tanlang", reply_markup=menuMain)

@dp.message_handler(text="Mahsulotlar")
async def start(message:types.Message):
    await message.answer("Kerakli bo'limnini tanlang", reply_markup=meneProducts)

@dp.callback_query_handler(text="courses")
async def courses(call: CallbackQuery):
    await call.message.answer("Bizning kurslarimisiz", reply_markup=meneCourses)






if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)


