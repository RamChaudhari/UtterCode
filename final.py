# Module - Speech Recognition
import speech_recognition as sr

# Sub-Module - Recognizer
r = sr.Recognizer()



# Global Text File
# FILE REQ FOR TEXT
global text

# Mic is source 
def mic():
    with sr.Microphone() as source:
        print('Speak anything: ')
        # Audio from source
        audio = r.listen(source)
        # Audio conv to Text - Google SubModule
        global text
        text = r.recognize_google(audio)
        # O/p - text
        try:
            print('You said: {}', format(text))
        except:
            print('Sorry could not recognize your voice.')

    # text conv to lower case, words separated, universal list printed
    text = text.lower()
    global unilist
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
    

def input_f(a) :
    idx = unilist.index(a)
    if unilist[idx+1] == 'string' :
        print(unilist[idx-2], unilist[idx-1],"input("+"'Enter a String :'"+")")
        CodeFile.write(unilist[idx-2])
        CodeFile.write(unilist[idx-1])
        CodeFile.write("input("+"'Enter a String :'"+")\n")
    elif unilist[idx+1] == 'integer' :
        print(unilist[idx-2], unilist[idx-1],"int(input("+"'Enter an integer :'"+"))\n")
        CodeFile.write(unilist[idx-2])
        CodeFile.write(unilist[idx-1])
        CodeFile.write("int(input("+"'Enter an integer :'"+"))")
    return


def print_f(a) :
    idx = unilist.index(a)
    print("print('", end=" ")
    CodeFile.write("print(' ")
    temp = idx+1
    while(unilist[temp] != "break") :
        print(unilist[temp], end=" ")
        CodeFile.write(unilist[temp])
        CodeFile.write(" ")
        temp = temp+1
    print("')", end=" ")
    CodeFile.write("')")

def forloop(a):
    idx = unilist.index(a)
    if unilist[idx] == "repeat":
        CodeFile.write("\n")
        CodeFile.write('for i in ')
        CodeFile.write("range(")
        CodeFile.write("0,")
        CodeFile.write(unilist[idx+1])
        CodeFile.write("): \n")
        CodeFile.write("    ")
        CodeFile.write("x")
    return
        
def comment(a):
    idx = unilist.index(a)
    if unilist[idx] == "comment":
        CodeFile.write("# ")
        temp = idx+1
        while(unilist[temp] != "break") :
            print(unilist[temp], end=" ")
            CodeFile.write(unilist[temp])
            CodeFile.write(" ")
            temp = temp+1
    return

def whileloop(a):
    idx = unilist.index(a)
    if unilist[idx] == 'until':
        CodeFile.write('while')
        mic()
    return


# Dictionary
# FILE REQ FOR DICTIONARY
dict1 = { 'input' : input_f, 'print' : print_f, 'repeat' : forloop, 'comment' : comment, 'until' : whileloop}

# FILE REQ FOR O/P
CodeFile = open('CodeFile.py', 'a+')


# myInputString = Input('string')
# myInputInt = Input('int')
mic()