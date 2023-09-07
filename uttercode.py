import speech_recognition as sr

r = sr.Recognizer()
global text

with sr.Microphone() as source:
    print('Speak anything: ')
    audio = r.listen(source)
    text = r.recognize_google(audio)
    try:
        print('You said: {}', format(text))
    except:
        print('Sorry could not recognize your voice.')

text = text.lower()
unilist = text.split()
print(unilist)

dict1 = {'line' : '\n',
    'ram': 'x',
 'chaitralee' : 'x',
  'shruti' : 'x',
   'ashwin' : 'x',
    'manish': 'x',
    'has' : "=",
    '10' : 10
    }

for i in unilist:
    if i in dict1:
        print(dict1.get(i), end=" ")