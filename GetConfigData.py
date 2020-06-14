import configparser

config = configparser.ConfigParser()
config.read('config.ini')

def GetTelegramToken():
    return config['telegram']['token']


def GetTelegramGroupChatID():
    return config['telegram']['GroupChatID']





