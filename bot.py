import os
import telebot

TOKEN = os.environ.get('TELEGRAM_TOKEN')
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    welcome_text = (
        "🌍 Welcome to Matrix TV PRO! | مرحباً بك في ماتريكس تي في\n\n"
        "EN: Choose your language: /en\n"
        "ES: Elige tu idioma: /es\n"
        "PT: Escolha seu idioma: /pt\n"
        "AR: اختر لغتك: /ar\n\n"
        "🎥 Watch our history: https://youtu.be/stMOpwab6gM?si=HgpszDERCo2uwwYT"
    )
    bot.reply_to(message, welcome_text)

@bot.message_handler(commands=['ar'])
def ar_reply(message):
    bot.reply_to(message, "أهلاً بك في عائلتنا! ماتريكس تي في يعود بعد 7 سنوات من التميز. تفقد تاريخنا في الفيديو، وحمل أحدث نسخة من موقعنا: https://matrixandroidtv.wordpress.com/")

@bot.message_handler(commands=['en'])
def en_reply(message):
    bot.reply_to(message, "Welcome! Matrix TV is back after 7 years of history. Check our journey in the video, and download the app here: https://matrixandroidtv.wordpress.com/")

@bot.message_handler(commands=['es'])
def es_reply(message):
    bot.reply_to(message, "¡Bienvenido! Matrix TV ha vuelto tras 7 años de historia. Mira nuestro video y descarga la app aquí: https://matrixandroidtv.wordpress.com/")

@bot.message_handler(commands=['pt'])
def pt_reply(message):
    bot.reply_to(message, "Bem-vindo! Matrix TV está de volta após 7 anos de história. Assista ao nosso vídeo e baixe o app aqui: https://matrixandroidtv.wordpress.com/")

@bot.message_handler(func=lambda message: True)
def default_reply(message):
    bot.reply_to(message, "Welcome! Please use /start to see the menu. | مرحباً! استخدم /start لرؤية القائمة.")

bot.polling(none_stop=True)
