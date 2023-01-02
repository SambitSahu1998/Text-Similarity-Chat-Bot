from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from playsound import playsound

import random
import webbrowser
import os

user1=['How are you','how are you']
user2=['good morning','morning','good evening','evening','good afternoon','afternoon','good night','night']
user3=['hi','hai','hey','hello']
user4=['who is your developer','who is the developer']
user5=['java developer','am a java developer']
mybot1=['I\'m good waiting for you, dear']
mybot2=['Same to you dear.']
mybot3=['Hi Dear.']
mybot4=['My developer is Master Chiranjib Parida and Master Sambit Kumar Sahu.']
mybot5=['so what am python bot i don''t know who are you Glad to meet you']
random_reply1=random.choice(mybot1)
random_reply2=random.choice(mybot2)
random_reply3=random.choice(mybot3)
random_reply4=random.choice(mybot4)
random_reply5=random.choice(mybot5)


bot = ChatBot(
'Norman',
storage_adapter='chatterbot.storage.SQLStorageAdapter',
logic_adapters=[
                {
                 'import_path': 'chatterbot.logic.MathematicalEvaluation'
                 },
                {
                 'import_path': 'chatterbot.logic.BestMatch',
                 'threshold': 0.70,
                 'default_response': 'I am sorry, but I do not understand.'
                 }
    ],
database_url='sqlite:///database.sqlite3'
)
trainer=ListTrainer(bot)


for files in os.listdir('C:/Users/SAMBIT/chatterbot-corpus-master/chatterbot_corpus/data/english/'):
    data = open('C:/Users/SAMBIT/chatterbot-corpus-master/chatterbot_corpus/data/english/' + files,'r').readlines() 
    trainer.train(data)
    
while True:
     message = input('You: ')
     if 'open Google Webpage' in message:
             url = 'https://www.google.com/'
             webbrowser.open(url)
     elif 'play a Song for me' in message:
             playsound("MagentaRiddimFBCOMTHEEDMLOVERSRingtone.mp3")
     elif 'open Calculator' in message:
             os.system('%windir%\system32\calc.exe')
     elif 'open Paint' in message:
             os.system('%windir%\system32\mspaint.exe')        
     elif message in user1:
             print('ChatBot :',random_reply1)
     elif message in user2:
             print('ChatBot :',random_reply2)
     elif message in user3:
             print('ChatBot :',random_reply3)
     elif message in user4:
             print('ChatBot :',random_reply4)
     elif message in user5:
             print('ChatBot :',random_reply5)
     elif message.strip() != 'Bye':
             reply = bot.get_response(message)
             print('ChatBot :',reply)
     elif message.strip() == 'Bye':
             print('ChatBot: Nice to meet you. Bye')
             break

