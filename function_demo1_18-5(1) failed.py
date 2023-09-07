#Python 2.x program for Speech Recognition

import speech_recognition as sr

#Sample rate is how often values are recorded
sample_rate = 48000
#Chunk is like a buffer. It stores 2048 samples (bytes of data)
#here.
#it is advisable to use powers of 2 such as 1024 or 2048
chunk_size = 2048
#Initialize the recognizer
global r
r = sr.Recognizer()

#generate a list of all audio cards/microphones
mic_list = sr.Microphone.list_microphone_names()


def input_f(a) :
    idx = unilist.index(a)
    if unilist[idx+1] == 'string' :
        print(unilist[idx-2], unilist[idx-1],"input("+"'Enter a String :'"+")")
        # CodeFile.write(unilist[idx-2])
        # CodeFile.write(unilist[idx-1])
        CodeFile.write("input("+"'Enter a String :'"+")\n")
    elif unilist[idx+1] == 'integer' :
        print(unilist[idx-2], unilist[idx-1],"int(input("+"'Enter an integer :'"+"))\n")
        # CodeFile.write(unilist[idx-2])
        # CodeFile.write(unilist[idx-1])
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
    newline()
    CodeFile.write("if ")
    CodeFile.write(dict2[unilist[idx +1]])
    CodeFile.write(dict2[unilist[idx +2]])
    #CodeFile.write(dict2[unilist[idx +3]])
    CodeFile.write(dict2[unilist[idx +4]])
    CodeFile.write(dict2[unilist[idx +6]])
    CodeFile.write(":\n")
    CodeFile.write("    ")
    mic()


def forloop(a):
    idx = unilist.index(a)
    print("In for loop")
    CodeFile.write("for i in range(")
    print("for i in range(", end='')
    CodeFile.write(unilist[idx+1])
    CodeFile.write("):")
    print(str(unilist[idx+1]))
    print("\n")
    CodeFile.write("\n  ")
    print("Body of loop :")
    mic()
    
    

def newline():
    CodeFile.write("\n")


# FILE REQ FOR O/P
CodeFile = open('CodeFile.py', 'a+')





dict1 = { 'input' : input_f, 'print' : print_f, 'if' : if_else}
dict2 = { "less" : "<", "greater" : ">", "more" : ">", "equal" : "=", "add" : "+", "sum" : "+", "plus" : "+", "subtract" : "-", 
"multiply" : "*", "product" : "*", "divide" : "/", "floor" : "//", "remainder" : "%", "power" : "**", "raised" : "**",
"x" : "x", "10" : "10", "y" : "y", "5" : "5"}


# microphone
def mic():
    # Global Text File
    global text
    with sr.Microphone(sample_rate = sample_rate, chunk_size = chunk_size) as source:
	#wait for a second to let the recognizer adjust the
	#energy threshold based on the surrounding noise level
    r.adjust_for_ambient_noise(source)
	print("Say Something")
	#listens for the user's input
	audio = r.listen(source)
		
	try: 
		text = r.recognize_google(audio)
		print ("you said: " + text)
	
	#error occurs when google could not understand what was said
	
	except sr.UnknownValueError:
		print("Google Speech Recognition could not understand audio")
	
	except sr.RequestError as e:
		print("Could not request results from Google Speech Recognition service; {0}".format(e))
    # text conv to lower case, words separated, universal list printed


# FILE REQ FOR TEXT 
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
    if i in dict2:
        print(dict2[i])
        CodeFile.write(dict2[i])

mic()