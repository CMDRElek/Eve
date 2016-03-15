import sys
import stor
import datetime
from chatterbot import ChatBot
import win32com.client
'''
Imports in order of appearance:
System
Eve's Storage
Date and Time
Base code for Eve
Eve's Voice (from Windows)
'''
speaker = win32com.client.Dispatch("SAPI.SpVoice")
chatbot = ChatBot('Eve',
    logic_adapters=[
    "chatterbot.adapters.logic.EvaluateMathematically",
    "chatterbot.adapters.logic.TimeLogicAdapter",
    "chatterbot.adapters.logic.ClosestMatchAdapter",
    "chatterbot.adapters.logic.ClosestMeaningAdapter"
    ])
#initializes the voice and language systems

#creates variable for user's command and Eve's response
cmd = ''
response = ''
thetime= datetime.datetime.now().replace(second=0, microsecond=0)
#trims seconds and microseconds from the time command for readability
active = 1
#simple on/off switch
chatbot.train("chatterbot.corpus.english")
#tells Eve to record all I/O messages to better learn English and sentence structure.


class geninput():
    def usrinput(self):
        global cmd
        cmd = input('>')
        cmd.lower
        return cmd
#takes command and turns it into variable cmd        
#makes it all lowercase for future command queries and simplicity   

class calcinput():
    def query():
        global cmd
        global cmdtrigger
        cmdtrigger = 0
        speaker.Speak(chatbot.get_response(cmd))
        cmd = ''
            
        return cmd
        return cmdtrigger
        
'''
SEARCH COMMAND DEPRECATED: TODO
        elif 'search' in cmd:
            Google.search(query=cmd, num=5, start=2, country_code="en")
            cmd = ''
            cmdtrigger = 1

        elif 'define' in cmd:
            print()
            cmd = ''
'''

class response():
    global response
    global cmd
# listener that flips the cmd back to unused state to get another query
while active == 1:
    geninput.usrinput(cmd)
    calcinput.query()
    if cmd == 'exit':
        active = 0
        cmd = ''
        sys.exit("Successfully terminated.")
        
