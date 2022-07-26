
from telegram import ReplyKeyboardRemove, Update
from telegram.ext import Updater,CommandHandler,MessageHandler


def main():
    updater = Updater("5513870466:AAGiiE7YfD3_W4LXcERJSQ2gy_PSytXabN0")
    dp = updater.dispatcher
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    
    main()