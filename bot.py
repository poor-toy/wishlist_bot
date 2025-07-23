from aiogram import Bot, Dispatcher, executor, types
import logging

API_TOKEN = "7709077183:AAHpoUtefyEFbw9LL62nQmqZXEmR2wVlWpE"  # <-- Вставь сюда свой токен

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

WEBAPP_URL = "https://profound-cascaron-aa3bbf.netlify.app"

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    kb = types.InlineKeyboardMarkup()
    btn_friends = types.InlineKeyboardButton("Открыть вишлист 🎁", url=WEBAPP_URL)
    btn_admin = types.InlineKeyboardButton("Админ-версия 👑", url=f"{WEBAPP_URL}?admin=1")
    kb.add(btn_friends)
    kb.add(btn_admin)
    await message.answer("Выбери версию вишлиста:", reply_markup=kb)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
