import logging

from config import *
from aiogram import Bot, Dispatcher, types, executor

# configure logging
from date_parser.date_parser import simplify_string, find_date_time_string
from number_parser.number_parser import translate_word_to_number

logging.basicConfig(level=logging.INFO)

# initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


# start
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Привет, я бот-порученец! Напиши что ты хочешь сделать и когда, а я это запомню.")


# help
@dp.message_handler(commands=['help'])
async def send_instruction(message: types.Message):
    await message.answer(
        text="*Доступные команды:*\n"
             "1. /list - показывает активные напоминания для данного чата.",
        parse_mode=types.ParseMode.MARKDOWN)


@dp.message_handler()
async def echo(message: types.Message):
    translate = translate_word_to_number(message.text)
    simple = simplify_string(translate)
    time_and_date = find_date_time_string(simple)
    answer = f'Translate: {translate}\n' \
             f'Simplify: {simple}\n' \
             f'DateTime: {time_and_date}'
    logging.info(answer)
    await message.answer(f'{message.date}\n{answer}')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
