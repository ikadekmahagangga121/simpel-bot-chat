print("Halo! Saya adalah Bot AI sederhana. Silakan ajukan pertanyaan atau sampaikan sesuatu kepada saya.")

while True:
    user_input = input("Anda: ")
    if user_input.lower() == "bye" or user_input.lower() == "selesai":
        print("Bot: Sampai jumpa! Terima kasih telah berinteraksi dengan saya.")
        break
    else:
        print("Bot: Terima kasih atas pertanyaan atau pernyataannya. Saya adalah bot AI sederhana dan belum bisa memberikan jawaban yang lengkap. Mohon maaf atas keterbatasan saya.")
