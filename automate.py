from telegram import Bot
from telegram.error import TelegramError

BOT_TOKEN = "7939472927:AAGX6VYKvuKrKiDvjXvn9hSeJi5IVYCQHgM"
CHAT_ID = "@MyNanaBotRecess" 

def post_to_telegram(message):
    bot = Bot(token=BOT_TOKEN)
    try:
        bot.send_message(chat_id=CHAT_ID, text=message)
        print(" Message posted successfully!")
    except TelegramError as e:
        print(f" Failed to send message: {e}")

if __name__ == "__main__":
    message = input("Enter the message to post on Telegram:\n")
    post_to_telegram(message)
