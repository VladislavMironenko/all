import gtts
from pydub import AudioSegment
import speech_recognition
import soundfile as sf



def text_to_speech(msg):
    tts = gtts.gTTS(msg , lang='ru')
    tts.save('text_to_speech.mp3')

def ogg2wav(ofn):
    wfn = ofn.replace('.ogg' , '.wav')
    print(wfn)
    data, sample_rate = sf.read(ofn)
    print(ofn)
    print(data , 'ййй' , sample_rate)
    sf.write(wfn, data, sample_rate)

def speech_to_text():
    ogg2wav('voice.ogg')
    r = speech_recognition.Recognizer()
    print(r)
    with speech_recognition.AudioFile('voice.wav') as source:
        audio = r.record(source)
        text = r.recognize_google(audio_data=audio , language='ru')
        print(text)
        return text