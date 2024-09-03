import pyautogui
import time

print("Posicione o cursor sobre o elemento desejado.")
time.sleep(5)
x, y = pyautogui.position()
print(f"As coordenadas são: X={x}, Y={y}")