import requests

token = input("Telegram Bot Token:\n")
chatid = input("Chat ID\n")

msg = input("Which message do you want send?\n")

while True:
	requests.post('https://api.telegram.org/bot' + token + '/sendMessage?chat_id=' + chatid + '&text=' + msg)