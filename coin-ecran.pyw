import pyautogui, keyboard, time

while True:
	if pyautogui.position() == pyautogui.Point(x=0, y=0):
		#print("i____i", i)
		keyboard.send('windows+tab')
		"""print(pyautogui.position())
		print(pyautogui.size())"""
		time.sleep(0.7)