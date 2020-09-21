#!/usr/bin/python3

import urllib
import requests

chat_id = 'YOUR USER OR CHAT ID'
bot_id = 'BOT ID'
telegram_api = 'https://api.telegram.org/bot'

def sendText(text):
    print('[+] Sendind message...')
    response = requests.get(telegram_api + bot_id + '/sendMessage?chat_id=' + chat_id + '&text=' + urllib.parse.quote_plus(text))
    if response.json()['ok']:
        print('[+] Message sent successfully!')
    else:
        print('[-] Message was not sent...')
        print('[!] Error code: ' + str(response.json()['error_code']))
        print('[!] ' + response.json()['description'])
    return response

if __name__ == '__main__':
    sendText('[+] Testing bot...')
