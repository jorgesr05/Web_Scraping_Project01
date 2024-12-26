import requests
from webscraping_aru import floatFirstPrice


def telegram_bot_sendtext(bot_message):

    bot_token = 'put your token'
    bot_chatID = 'put your chatID'
    send_text = 'https://api.telegram.org/bot' + bot_token + \
        '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text, timeout=10)

    return response.json()


objectPrice = 300

if floatFirstPrice < objectPrice:
    test = telegram_bot_sendtext(
        f"Good luck Mi Lic ❤️! There is an offer on your favorite product. The new price is: S/. {floatFirstPrice:.2f} \n The web page: https://www.aruma.pe/serum-effaclar-ultra-concentrado-30ml-la-roche-posay/p")
else:
    test = telegram_bot_sendtext("Regular price 🥲")
