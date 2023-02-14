from telebot import *
import telebot,os
from telegram import *
from telegram.ext import *
from pyhtml2pdf import converter


tokan = "6080025228:AAE9UCEetuYi4wwr_PVStKAT6EnTVaFANXo"

bot = telebot.TeleBot(tokan, parse_mode=None)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    print("============= send_welcome ==============")
    bot.reply_to(
        message, f"Hello {message.from_user.full_name}, Welcome to the Vnsgu_Sem5_result Bot.Please write /help to see the commands available.")


@bot.message_handler(commands=['help'])
def help_message(message):
    print("============= help_message ==============")
    bot.reply_to(message, '''
		** Enter Your Set Number for Sem 5 Examination (4 digit),
        *** Test for Send also use /hello Or /Bye     
	''')


@bot.message_handler(content_types=['sticker'])
def custom_message(message):
    print("============= Custom ==============")
    bot.reply_to(message, "Send Only Digit Number")

@bot.message_handler(content_types=['photo'])
def custom_message(message):
    print("============= Custom ==============")
    bot.reply_to(message, "Send Only Digit Number")


@bot.message_handler(commands=['hello','Hello'])
def send_welcome(message):
    print("============= hello_welcome ==============")
    bot.reply_to(message, f"Hello {message.from_user.full_name}. More Option /hello  /bye.")
    
@bot.message_handler(commands=['bye','Bye'])
def send_welcome(message):
    print("============= bye_welcome ==============")
    bot.reply_to(message, f"Bye, {message.from_user.full_name}. More Option /hello  /bye.")


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.isnumeric() and len(message.text) == 4:
        setnumber = message.text
        bot.send_message(message.chat.id, "Just A Second.....")
        send_pdf(message.chat.id, setnumber)
    else:
        send_message = 'Send Only Digit Number and len of digit is 4..'
        bot.send_message(message.chat.id, send_message.title())


def send_pdf(id,setnumber):
    download_path='E:/kishan/Telegram_Bot/telegrambot/AllPdf/{}.pdf'.format(setnumber)
    converter.convert('https://ums.vnsgu.net/Result/StudentResultDisplay.aspx?HtmlURL=3104,{}'.format(setnumber), download_path)
    bot.send_document(id,document=open(download_path,'rb'))
    bot.send_message(id, "Thank You......")
    os.remove(download_path)

bot.polling(none_stop=True)
