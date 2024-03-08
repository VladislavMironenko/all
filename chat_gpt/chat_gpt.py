import time
import speech_recognition
import openai
from parcer_chat_gpt import lst


gpt_key = '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'
openai.api_key = gpt_key

sr = speech_recognition.Recognizer()
sr.pause_threshold = 1

def func(text):
    response = openai.Completion.create(
        prompt = text,
        engine = 'text-davinci-003',
        max_tokens = 100,
        temperature = 0.3,
        n = 1,
        stop = None,
        timeout=15
    )

    if response:
        print(response.choices[0].text.strip())
    else:
        print('Uppssss sry')


def audio_func():
    print('Можете говорить')
    with speech_recognition.Microphone() as mic:
        sr.adjust_for_ambient_noise(source=mic , duration=0.5)
        audio = sr.listen(source=mic)
        query = sr.recognize_google(audio_data=audio , language='ru-RU').lower()
        print(query)
        func(query)

def main():
    audio_func()


if __name__ == '__main__':
    main()