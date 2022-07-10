#!/usr/bin/env python3
#-*-coding:utf-8-*-

from pyrogram import Client
app = Client('pyrogram', api_id='', api_hash='')

import logging
logging.basicConfig(level=logging.WARN)

@app.on_message(filters.me & filters.regex('delmymsg'))
async def delmymsg_handler(client, message):
	if message.text == "delmymsg":
		await message.delete()
		# Require admin privileges
		# await app.delete_user_history(message.chat.id,
		# 	(message.from_user and message.from_user.id or message.sender_chat.id))

		message_ids = []
		# async for i in app.search_messages(chat_id=message.chat.id, from_user=user_id):
		async for i in app.search_messages(chat_id=message.chat.id, from_user='me'):
			message_ids.append(i.id)
			if len(message_ids) > 99:
				await app.delete_messages(message.chat.id, message_ids)
				message_ids = []
		await app.delete_messages(message.chat.id, message_ids)
app.run()
