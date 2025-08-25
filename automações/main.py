import pyautogui
import keyboard
import time

#criar uma função
def tarefa():
    time.sleep(1)
#abrir o navegador
    pyautogui.press("win")
    time.sleep(0.5)
    pyautogui.write("Opera")
    pyautogui.press("enter")
    time.sleep(1)
#entrar no meet
    pyautogui.write("https://meet.google.com/")
    pyautogui.press("enter")
    time.sleep(3)
#entrar na sala de reunião
    pyautogui.press("enter")
#associar essa função a uma combinação de teclas
keyboard.add_hotkey("ctrl+alt+a", tarefa)

keyboard.wait("esc")