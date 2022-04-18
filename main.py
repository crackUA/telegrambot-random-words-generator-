from distutils import text_file
from email import message
import telebot
from telebot import types
import random
from distutils import text_file
import config
token='YOUR TOKEN'

bot=telebot.TeleBot(token)
@bot.message_handler(commands=['hi'])#Creating command /hi.
def send_message(message):#Bot sends message.
          bot.send_message(message.chat.id,config.random_message2)#We call method config.random_message2.
@bot.message_handler(commands=['gr'])#Creating command /gr 
def generate_message(message):
          bot.send_message(message.chat.id,config.random_message)#We call method config.random_message.
if __name__ == '__main__':
     bot.polling(none_stop=True)#Finish our program. 
