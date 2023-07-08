from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

bot = ChatBot('MyBot')
trainer = ChatterBotCorpusTrainer(bot)
trainer.train('chatterbot.corpus.indonesia')
print("Halo! Saya adalah bot AI. Silakan ajukan pertanyaan atau sampaikan sesuatu kepada saya.")

while True:
    user_input = input("Anda: ")
    if user_input.lower() == "bye" or user_input.lower() == "selesai":
        print("Bot: Sampai jumpa! Terima kasih telah berinteraksi dengan saya.")
        break
    else:
        bot_response = bot.get_response(user_input)
        print("Bot:", bot_response)
