import telegram
import requests
from GetConfigData import GetTelegramToken
from GetConfigData import GetTelegramGroupChatID
def SendPhoto(photourl):
    
    token=GetTelegramToken()
    bot = telegram.Bot(token=token)
    

    GroupChatID=GetTelegramGroupChatID()
    bot.send_photo(chat_id=GroupChatID, photo=photourl)

# bot.send_message(chat_id=chat_id, 
#                  text='<b>bold</b> <i>italic</i>http://www.speedtest.net/result/9519600887.png.', 
#                  parse_mode=telegram.ParseMode.HTML)

# def telegram_bot_sendtext(bot_message):

#     bot_token = token
#     bot_chatID = '751099792'
#     send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

#     response = requests.get(send_text)

#     return response.json()
    

