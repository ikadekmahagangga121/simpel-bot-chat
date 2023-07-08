from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from nltk.chat.util import Chat, reflections

bot = ChatBot('MyBot')

trainer = ChatterBotCorpusTrainer(bot)
trainer.train('chatterbot.corpus.indonesia')

def format_response(response):
    if response:
        return response.text
    else:
        return "Maaf, saya tidak mengerti. Bisa Anda jelaskan lebih lanjut?"
pairs = [
    [
        r"hai|halo|hei",
        ["Halo!", "Hai!", "Ada yang bisa saya bantu?"]
    ],
    [
        r"bagaimana kabarmu?",
        ["Terima kasih sudah bertanya. Saya adalah bot, jadi saya tidak punya perasaan. Bagaimana dengan Anda?"]
    ],
    [
        r"siapa (saya|nama kamu)?",
        ["Anda adalah siapa?", "Bagaimana saya bisa tahu siapa Anda?"]
    ],
    [
        r"apakah kamu manusia?",
        ["Saya adalah bot AI, bukan manusia. Tetapi saya bisa membantu Anda dengan pertanyaan dan permasalahan Anda."]
    ],
    [
        r"selesai|bye",
        ["Terima kasih telah berbicara dengan saya. Sampai jumpa!", "Sampai jumpa! Semoga harimu menyenangkan."]
    ]
]

chatbot = Chat(pairs, reflections)
print("Halo! Saya adalah bot AI. Silakan ajukan pertanyaan atau sampaikan sesuatu kepada saya.")
while True:
    user_input = input("Anda: ")
    if user_input.lower() == "bye" or user_input.lower() == "selesai":
        print("Bot: Sampai jumpa! Terima kasih telah berinteraksi dengan saya.")
        break
    else:
        bot_response = bot.get_response(user_input)
        print("Bot:", format_response(bot_response))

        # Jika bot tidak memberikan respons yang memadai, menggunakan Chat objek
        if bot_response.confidence < 0.6:
            chat_response = chatbot.respond(user_input)
            print("Bot:", chat_response)
