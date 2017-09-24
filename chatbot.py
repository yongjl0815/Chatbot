#!/usr/bin/python                                                                     

from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer


# Create a new instance of a ChatBot                                                        
chatterbot = ChatBot(
    "Sofia", #name of bot                                                                   
    preprocessors=[ #modify the input statement                                             
        'chatterbot.preprocessors.clean_whitespace', #Remove any consecutive whitespace characters                                                                                     
        'chatterbot.preprocessors.unescape_html', #Convert escaped html characters into unescaped html characters                                                                      
        'chatterbot.preprocessors.convert_to_ascii' #Converts unicode characters to ASCII character                                                                                    
    ],
    storage_adapter='chatterbot.storage.SQLStorageAdapter', #allows the chat bot to connect to SQL databases                                                                           
    input_adapter='chatterbot.input.TerminalAdapter', #allows user to usetheir terminal to communicate with the chat bot                                                               
    output_adapter='chatterbot.output.TerminalAdapter', #allows user to use their terminal to communicate with the chat bot                                                            
    filters=["chatterbot.filters.RepetitiveResponseFilter"], #eliminates possibly repetitive responses                                                                                 
    logic_adapters=[ #choose how to response to input                                       
        'chatterbot.logic.BestMatch', #returns a response based on known responses to the closest matches to the input statement                                                       
        'chatterbot.logic.MathematicalEvaluation', #respond to questions about basic math   
        'chatterbot.logic.TimeLogicAdapter', #repond to questions about current time        
        #{                                                                                  
        #    'import_path': 'chatterbot.logic.LowConfidenceAdapter',                        
        #    'threshold': 0.65,                                                             
        #    'default_response': 'I am sorry, but I do not understand.'                     
        #},                                                                                 
        { #give a specific response to a specific question                                  
            'import_path': 'chatterbot.logic.SpecificResponseAdapter',
            'input_text': 'Help me',
            'output_text': 'Call 911'
        }
    ],
    database='./database.sqlite3' #database that we'll use                                  
)
chatterbot.set_trainer(ChatterBotCorpusTrainer)

chatterbot.train( #use a corpus data to train bot                                           
    "chatterbot.corpus.english"
)
	
while True: #allow communication                                                            
    try:                                                                                    
     chatterbot_input = chatterbot.get_response(None)                                       
                                                                                            
    except(KeyboardInterrupt, EOFError, SystemExit):                                        
        break 