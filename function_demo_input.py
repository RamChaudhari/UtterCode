# Module - Speech Recognition
import speech_recognition as sr

# Sub-Module - Recognizer
r = sr.Recognizer()

# Class
class MasterClass :
    pass


def next_key_after_input(idx) :
    if (unilist[idx+2] == "terminate") :
        return
    i = unilist[idx+2]
    if i in dict1:
        a = i
        dict1[i](a)
    return

def input_f(a) :
    idx = unilist.index(a)
    if unilist[idx+1] == 'string' :
        print("input("+"'Enter a String :'"+")")
        CodeFile.write("input("+"'Enter a String :'"+")")
    elif unilist[idx+1] == 'integer' :
        print("int(input("+"'Enter an integer :'"+")'")
        CodeFile.write("input("+"'Enter an integer :'"+")")
    next_key_after_input(idx)
    return

def x() :

    print("x")

# Dictionary
# FILE REQ FOR DICTIONARY
dict1 = { 'input' : input_f,'ram' : x}

# FILE REQ FOR O/P
CodeFile = open('CodeFile.py', 'a+')

class Output(MasterClass):
    pass
class Condition(MasterClass):
    pass
class Loop(MasterClass):
    pass
class Operators(MasterClass):
    pass


# Global Text File
# FILE REQ FOR TEXT
global text

# Mic is source 
with sr.Microphone() as source:
    print('Speak anything: ')
    # Audio from source
    audio = r.listen(source)
    # Audio conv to Text - Google SubModule
    text = r.recognize_google(audio)
    # O/p - text
    try:
        print('You said: {}', format(text))
    except:
        print('Sorry could not recognize your voice.')

# text conv to lower case, words separated, universal list printed
text = text.lower()
unilist = text.split()
# FILE REQ FOR UNILIST
InputText = open('InputText', 'a+')
InputText.write(text)
print(unilist)

# Check for keyword and perform req operation
for i in unilist:
    if i in dict1:
        a = i
        dict1[i](a)
    

# myInputString = Input('string')
# myInputInt = Input('int')
