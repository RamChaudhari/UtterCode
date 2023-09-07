import speech_recognition as sr

r = sr.Recognizer()
global text
with sr.Microphone() as source:
    print('Speak Anything:')
    audio = r.listen(source)
    text = r.recognize_google(audio)
    try:
        print('You said : {}', format(text))
    except:
        print('Sorry could not recongize your voice.')
text = text.lower()
unilist = list(text.split())

#uni_dict = {'has':'=', }
# print(unilist)