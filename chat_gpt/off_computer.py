import os
import time
import speech_recognition
import webbrowser
import subprocess
import keyboard



def func():
    sr = speech_recognition.Recognizer()
    sr.pause_threshold = 0.5
    while True:
        try:
            with speech_recognition.Microphone() as mic:
                sr.adjust_for_ambient_noise(source=mic, duration=0.5)
                audio = sr.listen(source=mic)
                query = sr.recognize_google(audio_data=audio, language='ru-RU').lower().replace('админ' , 'admin')
                with open('a.mp3' , 'w') as f:
                    f.write(query)
                print(query)
            if 'admin выключи мой компьютер' in query:
                if 'через' in query:
                    text = query.split()
                    ind = text.index('через')
                    res = ' '.join(text[ind+1:ind+2])
                    print(res)
                    time.sleep(int(res)*60)
                # os.system('shutdown /s /t 0')
                print('Комп офнут)')
            elif 'admin открой' in query:
                if 'youtube' in query:
                    text = query.split()
                    ind = text.index('youtube')
                    res = ' '.join(text[ind+1:])
                    webbrowser.open(f'https://www.youtube.com/results?search_query={res}')
                elif 'twitch' in query:
                    webbrowser.open(f'https://www.twitch.tv/')
                elif 'гугл' in query or 'google' in query:
                    text = query.split()
                    ind = text.index('открой')
                    res = ' '.join(text[ind+2:])
                    webbrowser.open(f'https://www.google.com/search?q={res}')
                elif 'telegram' in query or 'tg' in query or 'тг' in query:
                    subprocess.Popen('C:\\Users\\Xeon\\AppData\\Roaming\\Telegram Desktop\\Telegram.exe')
                elif 'dota' in query:
                    subprocess.Popen('D:\\steam\\steamapps\\common\\dota 2 beta\\game\\bin\\win64\\dota2.exe')
                elif 'кс' in query:
                    subprocess.Popen('D:\\steam\\steamapps\\common\\Counter-Strike Global Offensive\\csgo.exe')
                elif 'discord' in query or 'дс' in query or 'ds' in query:
                    subprocess.Popen('C:\\Users\\Xeon\\AppData\\Local\\Discord\\app-1.0.9017\\Discord.exe')
            elif 'admin напиши сообщение' in query:
                text = query.split()
                ind = text.index('сообщение')
                res = ' '.join(text[ind+1:])
                keyboard.write(res)
                keyboard.press_and_release('enter')
            elif 'admin очистить строку' in query:
                keyboard.press('ctrl+backspace')
            else:
                continue
        except Exception:
            return func()



def main():
    func()



if __name__ == '__main__':
    main()