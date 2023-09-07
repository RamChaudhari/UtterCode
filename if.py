#Python 2.x program for Speech Recognition

import speech_recognition as sr

# Module - Speech Recognition
# import speech_recognition as sr

# # Sub-Module - Recognizer
# global r
# r = sr.Recognizer()
# FILE REQ FOR O/P
CodeFile = open('CodeFile.py', 'a+')

def input_f(a) :
    idx = unilist.index(a)
    if "string" in unilist :
        print(unilist[idx-2], unilist[idx-1],"input("+"'Enter a String :'"+")")
        # CodeFile.write(unilist[idx-2])
        # CodeFile.write(unilist[idx-1])
        CodeFile.write("input("+"'Enter a String :'"+")")
    elif "integer" in unilist :
        print(unilist[idx-2], unilist[idx-1],"int(input("+"'Enter an integer :'"+"))")
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
    print("for i in range(" + str(unilist[idx+1]) + ")")
    CodeFile.write(unilist[idx+1])
    CodeFile.write("):")
    print("\n")
    print("Body of loop :")
    
    while (unilist[0] != "break") :
        print("\n")
        CodeFile.write("\n\t")
        mic()
       

def newline(a):
    CodeFile.write("\n")

def comment_func(a):
    
    # CodeFile.write('#')
    # CodeFile.write("\t")
    # CodeFile.writelines(['comment', 'hello'])
    # while "break" not in unilist:
    #     print("\n")
    #     CodeFile.write("\n")
    #     mic()
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


# Dictionary
# FILE REQ FOR DICTIONARY

dict1 = { 'input' : input_f, 'print' : print_f, 'if' : if_else, 'repeat' : forloop, 'line' : newline, 'comment' : comment_func}
dict2 = { "less" : "<", "greater" : ">", "more" : ">", "equal" : "=", "add" : "+", "sum" : "+", "plus" : "+", "subtract" : "-", 
"multiply" : "*", "product" : "*", "divide" : "/", "floor" : "//", "remainder" : "%", "power" : "**", "raised" : "**",
"x" : "x", "10" : "10", "y" : "y", "5" : "5"}


# microphone
def mic():
    #enter the name of usb microphone that you found
    #using lsusb
    #the following name is only used as an example
    # mic_name = "USB Device 0x46d:0x825: Audio (hw:1, 0)"  
    #Sample rate is how often values are recorded
    sample_rate = 48000
    #Chunk is like a buffer. It stores 2048 samples (bytes of data)
    #here.
    #it is advisable to use powers of 2 such as 1024 or 2048
    chunk_size = 2048
    #Initialize the recognizer
    r = sr.Recognizer()

    #generate a list of all audio cards/microphones
    mic_list = sr.Microphone.list_microphone_names()

    #the following loop aims to set the device ID of the mic that
    #we specifically want to use to avoid ambiguity.
    # for i, microphone_name in enumerate(mic_list):
    # 	if microphone_name == mic_name:
    # 		device_id = i

    #use the microphone as source for input. Here, we also specify
    #which device ID to specifically look for incase the microphone
    #is not working, an error will pop up saying "device_id undefined"
    with sr.Microphone(sample_rate = sample_rate, chunk_size = chunk_size) as source:
        #wait for a second to let the recognizer adjust the
        #energy threshold based on the surrounding noise level
        r.adjust_for_ambient_noise(source)
        print ("Say Something")
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