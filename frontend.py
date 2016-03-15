from tkinter import ttk as ttk
import tkinter as tk
import tkinter.scrolledtext as ScrolledText
import time
from chatterbot import ChatBot
import win32com.client
 
speaker = win32com.client.Dispatch("SAPI.SpVoice")
chatbot = ChatBot('Eve',
    logic_adapters=[
    "chatterbot.adapters.logic.EvaluateMathematically",
    "chatterbot.adapters.logic.TimeLogicAdapter",
    "chatterbot.adapters.logic.ClosestMatchAdapter",
    "chatterbot.adapters.logic.ClosestMeaningAdapter"
    ])


chatbot.train("chatterbot.corpus.english")

class TkinterGUI(tk.Tk):
    

    def __init__( self, *args, **kwargs ):
        '''
        Create & set window variables.
        '''
        tk.Tk.__init__( self, *args, **kwargs )
        self.chatbot = chatbot

        self.title( "Eve 0.0.2" )

        self.initialize()


    def initialize( self ):
        '''
        Set window layout.
        '''
        self.grid()

        self.conversation = ScrolledText.ScrolledText( self, state='disabled')
        self.conversation.grid(column=0, row=0, columnspan=1, sticky='n', padx=0, pady=0)
        
        self.respond = ttk.Button(self, text='>', command=self.get_response)
        self.respond.grid(column=0, row=1, sticky='e', padx=0, pady=0)
        
        self.usr_input = ttk.Entry(self, state='normal')
        self.usr_input.grid(column=0, row=1, sticky='ew', padx=0, pady=0)
    def get_response( self ):
        '''
        Get a response from the chatbot &
        display it.
        '''
        user_input = self.usr_input.get()
        self.usr_input.delete( 0, tk.END )

        response = self.chatbot.get_response( user_input )

        self.conversation['state'] = 'normal'
        self.conversation.insert( tk.END, ">" + user_input + "\n" + ">>" + str( response ) + "\n" )
        self.conversation['state'] = 'disabled'

        time.sleep( 0.5 )

gui_example = TkinterGUI()
gui_example.mainloop()