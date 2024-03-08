import speech_recognition


sr = speech_recognition.Recognizer()
sr.pause_threshold = 0.5
def audio_func():
    while True:
        try:
            with speech_recognition.Microphone() as mic:
                sr.adjust_for_ambient_noise(source=mic , duration=0.5)
                audio = sr.listen(source=mic)
                query = sr.recognize_google(audio_data=audio , language='ru-RU').lower()
                if query == 'выйти':
                    break
                else:
                    print(query)
        except Exception:
            continue

def main():
    audio_func()


if __name__ == '__main__':
    main()