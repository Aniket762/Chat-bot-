from chatterbot import ChatBot 
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot('basic')
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train('chatterbot.corpous.english')

while True:
    query = str(input(">>"))
    print(chatbot.get_response(query))
    if "exit" in query:
        break