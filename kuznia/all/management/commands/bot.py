import datetime
from django.conf import settings
from aiogram import types, Bot, Dispatcher, executor
from django.core.management.base import BaseCommand

import random
from all.models import Categories , Test , Product , Image
from django.core.management.base import BaseCommand
from aiogram import Bot, Dispatcher, types
from aiogram import executor
from django.conf import settings
from asgiref.sync import sync_to_async
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from django.core.files.base import ContentFile


class Command(BaseCommand):
    help = 'Run the Telegram bot'



    def handle(self, *args, **options):
        bot = Bot(token=settings.TOKEN)
        storage = MemoryStorage()
        dp = Dispatcher(bot , storage = storage)


        class Form(StatesGroup):
            Name = State()
            Price = State()
            Image = State()
            Description = State()

        @sync_to_async
        def fgg(name , price , image ,  description):
            cat = Categories.objects.get(categories = 'Калибры')
            # with image as i:
            #     res_photo = i
            image_obj = Image()
            image_obj.image.save('1.jpg', ContentFile(image.read()), save=True)
            # with open('1.jpg', 'rb') as f:
            b = Image.objects.create(name = name, image = image_obj.image)
            product = Product.objects.create(categories = cat , name = name , price = price, data = datetime.datetime.now() , description = description)
            product.images.set([image_obj])

        # @dp.message_handler(content_types=['photo'])
        # async def price(message: types.Message):
        #     data = await bot.get_file(message.photo[-1].file_id)
        #     with open(f'{data}.jpg' , 'wb') as f:
        #         await message.answer(f.write(data))

        # @dp.message_handler(content_types=['photo'])
        # async def price(message: types.Message):
        #     file_data = await bot.get_file(message.photo[-1].file_id)
        #     downloaded_file = await bot.download_file(file_data.file_path)
        #     await message.answer_photo(downloaded_file)

            # with open(photo_path, 'wb') as f:
            #     f.write(downloaded_file.read())
            #
            # with open(photo_path, 'rb') as f:
            #     await message.answer_photo(downloaded_file)

        #
        # @dp.message_handler(commands='start')
        # async def start(message: types.Message):
        #     await message.answer('Напишите (Создать)')

        @dp.message_handler(content_types=['text'], state=None)
        async def start_handler(message: types.Message):
            await message.answer("Введите ваше имя:")
            await Form.Name.set()

        @dp.message_handler(state=Form.Name)
        async def name(message: types.Message, state: FSMContext):
            async with state.proxy() as data:
                data['Name'] = message.text
            await message.answer("Введите цену:")
            await Form.Price.set()

        @dp.message_handler(state=Form.Price)
        async def price(message: types.Message, state: FSMContext):
            async with state.proxy() as data:
                data['Price'] = message.text
            await message.answer(f"Закиньте фотографию:")
            await Form.Image.set()

        @dp.message_handler(content_types=['photo'] , state=Form.Image)
        async def image(message: types.Message, state: FSMContext):
            async with state.proxy() as data:
                file_data = await bot.get_file(message.photo[-1].file_id)
                data['Image'] = await bot.download_file(file_data.file_path)
            # with open('1.jpg' , 'wb') as f:
            #     f.write(m.read())
            await message.answer(f"Введите описание:")
            await Form.Description.set()


        @dp.message_handler(state=Form.Description)
        async def description(message: types.Message, state: FSMContext):
            async with state.proxy() as data:
                data['Description'] = message.text
            await state.finish()
            await fgg(
                name=data.get('Name'),
                price=data.get('Price'),
                image = data.get('Image'),
                description=data.get('Description')
            )
            await message.answer(f"Вы завершили ввод. Данные сохранены.")

        executor.start_polling(dp, skip_updates=True)



