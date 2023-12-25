import os
import sys
import time
try:
  import pyautogui
except:
 os. system('pip install pyautogui')
 import pyautogui
def clean():
	if os.name == 'nt':
		os.system('cls')
	else:
		os.system('clear')
clean()
def banner():
	print("""
 _____ _     ____  _  __   _____  _    _____    _  _      ____  ____ ___  _  
/    // \ /\/   _\/ |/ /  /__ __\/ \ /|\__  \  / \/ \  /|/  _ \/  _ \\  \//  
|  __\| | |||  /  |   /     / \  | |_||  /  |  | || |\ ||| | //| / \| \  /   
| |   | \_/||  \_ |   \     | |  | | || _\  |  | || | \||| |_\\| \_/| /  \   
\_/   \____/\____/\_|\_\    \_/  \_/ \|/____/  \_/\_/  \|\____/\____//__/\\
									By @th3wantedboy
Telegram : @th3wantedboy
Facebook : @th3wantedboy
Twitter  : @th3wantedboy
Github   : @th3wantedboy
""")
banner()
x = input('Enter Your Message: ')
t = int(input('Thread: '))
print('Start In 3 Second...')
time.sleep(3)
while t > 0:
	pyautogui.typewrite(x)
	pyautogui.press('enter')
	time.sleep(0.2)
	clean()
	print('Remaining sent : ',t)
	t = t - 1
if t == 0:
	clean()
	banner()
	print('Done')
