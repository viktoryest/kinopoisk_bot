import os
from dotenv import load_dotenv
from kinopoisk.movie import Movie
import logging
from aiogram import Bot, Dispatcher, executor, types

load_dotenv()

API_TOKEN = os.getenv('token')

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Отправьте название фильма")


@dp.message_handler()
async def echo(message: types.Message):
    movie_list = Movie.objects.search(message)
    answer = f'Нашлись следующие фильмы:\n'
    for movie in movie_list:
        answer += str(movie) + '\n'

    await message.answer(answer)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
