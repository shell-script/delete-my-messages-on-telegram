#!/usr/bin/env python3
#-*-coding:utf-8-*-

from telethon.sync import TelegramClient
client = TelegramClient('telethon', api_id='', api_hash='')
client.start()

if input('Are you sure you want to delete your *every outgoing message* in *every group*? (y/N): ') != 'y':
	exit(0)

message_ids = []
counter = 0

for dialog in client.get_dialogs():
	if dialog.is_group:
		for message in client.iter_messages(dialog.entity, from_user=client.get_me()):
			message_ids.append(message.id)
			counter +=1
			print('Message ID: %d, Chat ID: %d, Chat Title: %s' % (message.id, dialog.id, dialog.title))
			if len(message_ids) > 99:
				client.delete_messages(client.get_entity(entity), message_ids)
				print('%d messages were deleted.' % len(message_ids))
				message_ids=[]
		client.delete_messages(client.get_entity(entity), message_ids)

print('Total %d messages were deleted.' % counter)
print('Done! (Please run the script two to three times to clean every message. If you run once only, some messages may won\'t be deleted.)')
print('Some service messages(user joined group and so on) can only be deleted by admins, so the counter will stay the same and it\'s normal.')
