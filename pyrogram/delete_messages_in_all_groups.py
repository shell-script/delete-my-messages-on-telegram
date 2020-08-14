#!/usr/bin/env python3
#-*-coding:utf-8-*-

from pyrogram import Client
app = Client('pyrogram', api_id='', api_hash='')
app.start()

if input('Are you sure you want to delete your *every outgoing message* in *every group*? (y/N): ') != 'y':
	exit(0)

message_ids = []
counter = 0

for dialog in app.iter_dialogs():
	if (dialog.chat.type == "group") or (dialog.chat.type == "supergroup"):
		for i in app.search_messages(chat_id=dialog.chat.id, from_user="me"):
			message_ids.append(i.message_id)
			counter +=1
			print('Message ID: %d, Chat ID: %d, Chat Title: %s' % (i.message_id, i.chat.id, i.chat.title))
			if len(message_ids) > 99:
				app.delete_messages(dialog.chat.id, message_ids)
				print('%d messages were deleted.' % len(message_ids))
				message_ids=[]
		app.delete_messages(dialog.chat.id, message_ids)

print('Total %d messages were deleted.' % counter)
print('Done! (Please run the script two to three times to clean every message. If you run once only, some messages may won\'t be deleted.)')
print('Some service messages(user joined group and so on) can only be deleted by admins, so the counter will stay the same and it\'s normal.')