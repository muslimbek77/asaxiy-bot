from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from prompt_toolkit import HTML
from asaxiy import rasm_content

from config import BOT_TOKEN


bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Salom bu bot asaxiy.uz dan maxsulotlarni olib beradi.\n Botdan foydalanish uchun text yozing")


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("Напиши мне что-нибудь, и я отпрпавлю этот текст тебе в ответ!")


@dp.message_handler()
async def echo_message(message: types.Message):
    content=rasm_content(message.text)[:10]
    
    for j,i in enumerate(content):
        await message.reply_photo(f"{i[0]}",caption=f"{j+1}.Mahsulot:{i[1]}\nNarxi:{i[2]}\nBo'lib to'lash:{i[3]}")
       
    if not content:
         await message.reply("Afsuski hech narsa topilmadi!")
        
if __name__ == '__main__':
    executor.start_polling(dp)