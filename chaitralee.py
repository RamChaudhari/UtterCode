# Module - Speech Recognition
import speech_recognition as sr

# Sub-Module - Recognizer
r = sr.Recognizer()

# Class
class MasterClass :
    pass



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

def if_else(a):
    idx = unilist.index(a)
    CodeFile.write("if (")
    CodeFile.write(unilist[idx +1], unilist[idx+2], unilist[idx+3], unilist[idx+4])
    
    

        

# Dictionary
# FILE REQ FOR DICTIONARY
dict1 = { 'input' : input_f, 'print' : print_f, 'if' : if_else}
dict2 = { "less" : "<", "greater" : ">", "more" : ">", "equal" : "=", "add" : "+", "sum" : "+", "plus" : "+", "subtract" : "-", 
"multiply" : "*", "product" : "*", "divide" : "/", "floor" : "//", "remainder" : "%", "power" : "**", "raised" : "**",
"x" : "x", "10" : "10", "y" : "y", "5" : "5"}

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
    if i in dict2:
       print(dict2[i])

# myInputString = Input('string')
# myInputInt = Input('int')