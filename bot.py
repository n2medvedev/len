
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
       
def talk_to_me(bot, update):
    #print(update.message.text)
    bot.sendMessage(update.message.chat_id, "получил "+update.message.text)
def show_error(bot, update, error):
    print(error)
def greet_user(bot, update):
    print(bot)
    print(update)
    print('вызван Старт')
    bot.sendMessage(update.message.chat_id, text='Давай общаться!')
def main():
    updater = Updater("350203777:AAFM5aYBNc2WpHlt-t8VZMCS0Wz49MjokAA")
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("Hello", greet_user))
    dp.add_handler(MessageHandler([Filters.text], talk_to_me))
    dp.add_error_handler(show_error)
    updater.start_polling()
    updater.idle()

main()