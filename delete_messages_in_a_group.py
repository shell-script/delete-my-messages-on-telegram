#!/usr/bin/env python3
#-*-coding:utf-8-*-

from pyrogram import Client
app = Client('pyrogram', api_id='', api_hash='')

@app.on_message()
def command_handler(client, message):
	if (message.text == "delmymsg") and (message.from_user.id == app.get_me().id):
		message_ids = []
		for i in app.search_messages(chat_id=message.chat.id, from_user=message.from_user.id):
			message_ids.append(i.message_id)
			if len(message_ids) > 99:
				app.delete_messages(message.chat.id, message_ids)
				message_ids = []
		app.delete_messages(message.chat.id, message_ids)
app.run()
