import vk_api, traceback, random, time
from datetime import datetime
from vk_api.longpoll import VkEventType, VkLongPoll

token='token'

vk=vk_api.VkApi(token=token)#авторизовываем админа
longpoll=VkLongPoll(vk)

def sms(peer_id=int, message=str, attachments=None, sticker_id=None, peer_ids=None, reply_to=None, forward_messages=None, pyload=None, disable_mentions=None):
	vk.method('messages.send',
	{'peer_id': peer_id,
	'peer_ids': peer_ids,
	'message': message,
	'attachmets': attachments,
	'sticker_id': sticker_id,
	'reply_to': reply_to,
	'forward_messages': forward_messages,
	'pyload': pyload,
	'disable_mentions': disable_mentions,
	'random_id': random.randint(10, 10**6)}
	)
	
def  sms_edit(peer_id=int, message=str, message_id=int, attachments=None, keep_forward_messages=None):
	r=vk.method('messages.edit',
	{'peer_id': peer_id,
	'message': message,
	'message_id': message_id,
	'attachments': attachments,
	'keep_forward_messages': keep_forward_messages,
	})
	return r
	
	
while True:
	try:
		for event in longpoll.listen():
			if event.type == VkEventType.MESSAGE_NEW and event.from_me:
				text=event.text.lower()
				peer_id=event.peer_id
				time_=event.raw[4]
				message_id=event.message_id
				if text=='.пинг':
					pong=f'Понг лп: {abs(round(datetime.now().timestamp()-time_, 3))}'
					sms_edit(peer_id=peer_id, message=pong, message_id=message_id)
	except:
		print('Я падаю.')
		traceback.print_exc()
		time.sleep(5)
	
