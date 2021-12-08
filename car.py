Python 3.10.1 (tags/v3.10.1:2cd268a, Dec  6 2021, 19:10:37) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import os
import telebot


bot = telebot.Telebot("API KEY")


@bot.message_handler(commands=["start"])
def send_welcome(message):
bot.reply_to(message, "Hello! I'm Uvindu Bro Chat Bot")


@bot.message_handler(commands=["how"])
def send_message(message)
bot.send_message(message, "https://youtube.com/c/Uvindubro")


bot.polling() 
 1  requirements.txt 