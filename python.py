import pyautogui
import time


pyautogui.PAUSE = 2


time.sleep(3)  
pyautogui.click(1145, 426) 
pyautogui.write('Joao da Silva')
time.sleep(2)
pyautogui.click(1143, 500)  
pyautogui.write('joao.silva@email.com')
time.sleep(2)
pyautogui.click(1140, 576) 
pyautogui.write('81999999999')
time.sleep(2)
pyautogui.click(1139, 651) 
pyautogui.write('01/01/1988')
time.sleep(2) 
pyautogui.click(1139, 725)  
pyautogui.write('12345678900')
time.sleep(2)
print("Formulário preenchido com sucesso!")
