from aiogram import Dispatcher , types , executor , Bot
from rembg import remove
from data_telegram import token

bot = Bot(token)
dp = Dispatcher(bot)

@dp.message_handler(commands='start')
async def start(message:types.Message):
    await message.answer('Hi, this is a removal and replacement bot background, upload images')


@dp.message_handler(content_types=['photo'])
async def take_images(message : types.Message):
    photo = message.photo[-1]
    file_info = await bot.get_file(photo.file_id)
    photo_url = file_info.file_path
    filename = 'input.jpg'
    await bot.download_file(photo_url , filename)
    with open('input.jpg' , 'rb') as f:
        a = f.read()
        output = remove(a)
        await bot.send_photo(message.chat.id , output)


executor.start_polling(dp , skip_updates=True)