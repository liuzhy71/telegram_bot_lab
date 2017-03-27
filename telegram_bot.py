from telegram.ext import Updater,CommandHandler,MessageHandler,Filters;
from telegram import ChatAction;
from gtts import gTTS;

def start(bot,update):
    #reply with hello
    update.message.reply_text('hello');
    #update.message.

def echo(bot,update):
    bot.sendChatAction(update.message.chat_id, ChatAction.UPLOAD_AUDIO)
    repeat_text = update.message.text;

    #update.message.reply_text(repeat_text);
    tts = gTTS(text=repeat_text,lang='en')
    tts.save("echo.mp3")
    bot.sendVoice(chat_id=update.message.chat_id,voice=open("echo.mp3",'rb'))

def main():
    updater = Updater('340779334:AAHz3xwTWZy-1Nw9jDlb5labgj9bMy3UUow');
    dp = updater.dispatcher;
    dp.add_handler(CommandHandler('start',start));
    dp.add_handler(MessageHandler(Filters.text,echo));
    updater.start_polling();    #continusely ask do you have somthing
    updater.idle();              #run forever or exterminate

if __name__ == '__main__':
    main();
