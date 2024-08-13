import pyautogui
print(pyautogui.size())

width, height = pyautogui.size()
print(width)
print(height)

print(pyautogui.position())

pyautogui.moveTo(10,10)
pyautogui.moveTo(1000,1000, duration = 2)

pyautogui.moveRel(200,0,duration = 2)