import time
from aiogram import Dispatcher , Bot , types , executor
import speech_recognition
import openai
from pydub import AudioSegment
from pathlib import Path
import json
import aiofiles
from text_to_speech import speech_to_text , text_to_speech



token_info = '6447462209:AAENNuT2ZRFPOqHiE5tC7rTxvn9UhO8pqc0'
bot = Bot(token = token_info)
db = Dispatcher(bot)


gpt_key = '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'
openai.api_key = gpt_key

sr = speech_recognition.Recognizer()
sr.pause_threshold = 0.6


@db.message_handler(commands='start')
async def hello(message : types.Message):
    await message.answer('Привет это чат gpt 3 , ты уже можешь задавать мне вопросы ')


@db.message_handler(commands=['speach'])
async def func(message : types.Message):
    text = ''.join(message.text[7:])
    text_to_speech(text)
    with open('text_to_speech.mp3' , 'rb') as f:
        await bot.send_audio(message.chat.id, f)


@db.message_handler(content_types=['text'])
async def func(message : types.Message):
    response = openai.Completion.create(
        prompt = message.text,
        engine = 'text-davinci-003',
        max_tokens = 1000,
        temperature = 0.3,
        n = 1,
        stop = None,
        timeout=15
    )
    await message.answer(response['choices'][0]['text'])

    


@db.message_handler(content_types=['voice'])
async def func(message : types.Message):
    # file_info = await bot.get_file(message.voice.file_id)
    # downloaded_file = await bot.download_file(file_info.file_path)
    # with open("voice_message.wav", "wb") as audio_file:
    #     audio_file.write(downloaded_file.read())
    #     print('qq')
    # with speech_recognition.AudioFile() as mic:
    #     audio = sr.record(source=mic)
    #     query = sr.recognize_google(audio_data=audio, language='ru-RU').lower()
    #     print(query)
    file = await bot.get_file(message.voice.file_id)
    bytes = await bot.download_file(file.file_path)
    async with aiofiles.open('voice.ogg' , 'wb') as f:
        await f.write(bytes.read())

    text = speech_to_text()

    response = openai.Completion.create(
        prompt = text,
        engine = 'text-davinci-003',
        max_tokens = 1000,
        temperature = 0.3,
        n = 1,
        stop = None,
        timeout=15
    )
    await message.answer(response['choices'][0]['text'])




def main():
    executor.start_polling(db , skip_updates=True)



if __name__ == '__main__':
    main()




