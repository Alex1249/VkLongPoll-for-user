import vk_api, traceback, time
from datetime import datetime
from vk_api.longpoll import VkEventType, VkLongPoll

token='' # токен

_vk_=vk_api.VkApi(token=token)
vk=_vk_.get_api()
longpoll=VkLongPoll(_vk_)

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
					vk.messages.edit(peer_id=peer_id, message=pong, message_id=message_id)
	except:
		print('Я падаю.')
		traceback.print_exc()
		time.sleep(5)
# Written with love. By Alexey Kuznetsov.
