import speech_recognition as sr
import pyaudio

r = sr.Recognizer()

with sr.Microphone() as source:
    print('질문해주세요:')
    audio = r.listen(source)
    
    try:
        text = r.recognize_google(audio, language='ko-KR')
        print('당신의 질문은 : {}입니다.'.format(text))
    except:
        print('목소리를 인식할 수 없습니다.')