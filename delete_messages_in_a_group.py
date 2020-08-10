#!/usr/bin/env python3
#-*-coding:utf-8-*-

from telethon import TelegramClient, events
client = TelegramClient('telethon', api_id='', api_hash='')

@client.on(events.NewMessage)
async def handler(event):
	if (event.message.message == "delmymsg") and (event.message.from_id == (await client.get_me()).id):
		message_ids = []
		async for message in client.iter_messages(event.message.to_id.channel_id, from_user=event.message.from_id):
			message_ids.append(message.id)
		await client.delete_messages(event.message.to_id.channel_id, message_ids)

client.start()
client.loop.run_forever()
