import os
import telebot


TOKEN = os.environ.get('TELEGRAM_TOKEN')
bot = telebot.TeleBot(TOKEN)

LANG_DATA = {
    'en': "Welcome! Matrix TV is back after 7 years. Proven legacy of 5M users. Watch our journey: https://youtu.be/stMOpwab6gM | Download: https://matrixandroidtv.wordpress.com/",
    'ar': "أهلاً بك! ماتريكس تي في يعود بعد 7 سنوات. إرث 5 مليون مستخدم. شاهد رحلتنا: https://youtu.be/stMOpwab6gM | التحميل: https://matrixandroidtv.wordpress.com/",
    'es': "¡Bienvenido! Matrix TV ha vuelto tras 7 años. Legado de 5M de usuarios. Mira nuestra historia: https://youtu.be/stMOpwab6gM | Descarga: https://matrixandroidtv.wordpress.com/",
    'pt': "Bem-vindo! Matrix TV está de volta após 7 anos. Legado de 5M de usuários. Veja nossa jornada: https://youtu.be/stMOpwab6gM | Baixe: https://matrixandroidtv.wordpress.com/",
    'fr': "Bienvenue ! Matrix TV est de retour après 7 ans. 5 millions d'utilisateurs. Regardez notre histoire : https://youtu.be/stMOpwab6gM | Téléchargement : https://matrixandroidtv.com/",
    'de': "Willkommen! Matrix TV ist nach 7 Jahren zurück. 5 Mio. Nutzer vertrauen uns. Unsere Reise: https://youtu.be/stMOpwab6gM | Download: https://matrixandroidtv.wordpress.com/",
    'it': "Benvenuto! Matrix TV è tornato dopo 7 anni. 5 milioni di utenti. Guarda la nostra storia: https://youtu.be/stMOpwab6gM | Scarica: https://matrixandroidtv.wordpress.com/",
    'ru': "Добро пожаловать! Matrix TV вернулся спустя 7 лет. 5 млн пользователей. Наша история: https://youtu.be/stMOpwab6gM | Скачать: https://matrixandroidtv.wordpress.com/",
    'tr': "Hoş geldin! Matrix TV 7 yıl sonra geri döndü. 5 milyon kullanıcı. Yolculuğumuzu izle: https://youtu.be/stMOpwab6gM | İndir: https://matrixandroidtv.wordpress.com/",
    'hi': "स्वागत है! Matrix TV 7 साल बाद वापस आ गया है। 5 मिलियन उपयोगकर्ताओं का भरोसा। हमारा इतिहास: https://youtu.be/stMOpwab6gM | डाउनलोड: https://matrixandroidtv.wordpress.com/",
    'zh': "欢迎！Matrix TV 时隔 7 年回归。500 万用户信赖。观看我们的历程：https://youtu.be/stMOpwab6gM | 下载：https://matrixandroidtv.wordpress.com/",
    'ja': "ようこそ！Matrix TVが7年ぶりに復活。500万人のユーザー実績。私たちの軌跡：https://youtu.be/stMOpwab6gM | ダウンロード：https://matrixandroidtv.wordpress.com/",
    'ko': "환영합니다! Matrix TV가 7년 만에 돌아왔습니다. 500만 사용자의 선택. 우리의 여정: https://youtu.be/stMOpwab6gM | 다운로드: https://matrixandroidtv.wordpress.com/",
    'id': "Selamat datang! Matrix TV kembali setelah 7 tahun. 5 juta pengguna. Lihat perjalanan kami: https://youtu.be/stMOpwab6gM | Unduh: https://matrixandroidtv.wordpress.com/",
    'nl': "Welkom! Matrix TV is terug na 7 jaar. 5 miljoen gebruikers. Bekijk onze reis: https://youtu.be/stMOpwab6gM | Download: https://matrixandroidtv.wordpress.com/"
}


@bot.message_handler(commands=['start'])
def send_welcome(message):
    try:

        lang_commands = " ".join([f"/{lang}" for lang in LANG_DATA.keys()])
        welcome_text = (
            "🌍 Matrix TV PRO: The Legend Returns! | أسطورة ماتريكس تعود!\n\n"
            f"Choose your language | اختر لغتك:\n{lang_commands}\n\n"
            "🎥 Watch our history: https://youtu.be/stMOpwab6gM?si=HgpszDERCo2uwwYT"
        )
        bot.reply_to(message, welcome_text)
    except Exception as e:
        print(f"Error in start command: {e}")


@bot.message_handler(commands=list(LANG_DATA.keys()))
def lang_reply(message):
    try:
        lang_code = message.text[1:] 
        bot.reply_to(message, LANG_DATA.get(lang_code, "Language not found."))
    except Exception as e:
        print(f"Error in lang handler: {e}")


@bot.message_handler(func=lambda message: True)
def default_reply(message):
    bot.reply_to(message, "Welcome! Please use /start to see the menu. | مرحباً! استخدم /start لرؤية القائمة.")

if __name__ == "__main__":
    print("Matrix Bot is running...")
    
    while True:
        try:
            bot.polling(none_stop=True)
        except Exception as e:
            print(f"Bot crashed: {e}. Restarting in 5 seconds...")
            import time
            time.sleep(5)
