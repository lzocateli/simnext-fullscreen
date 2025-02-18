import pygetwindow as gw
import pyautogui
import time
import ctypes
import sys

def find_and_focus_window(window_title, num_down_presses):
    windows = gw.getWindowsWithTitle(window_title)
    if not windows:
        ctypes.windll.user32.MessageBoxW(0, f"A tela '{window_title}' não foi encontrada.", "Erro", 0)
        return

    for window in windows:
        try:
            window.activate()
            time.sleep(1)  
            if window.isMinimized:
                window.restore()
            window.maximize()

            time.sleep(1)  
            # center_x, center_y = window.left + window.width // 2, window.top + window.height // 2
            

            # Obter o identificador da janela ativa
            active_window = ctypes.windll.user32.GetForegroundWindow()

            # Obter as coordenadas e o tamanho da janela ativa
            rect = ctypes.wintypes.RECT()
            ctypes.windll.user32.GetWindowRect(active_window, ctypes.pointer(rect))

            # Calcular o centro da janela ativa
            center_x = (rect.left + rect.right) // 2
            center_y = (rect.top + rect.bottom) // 2

            # # Mover o cursor do mouse para o centro da janela ativa
            # pyautogui.moveTo(center_x, center_y)

            
            pyautogui.click(center_x -100, center_y - 200, button='right')
            time.sleep(0.5)  

            for _ in range(num_down_presses):
                pyautogui.press('down')
                time.sleep(0.2) 

            pyautogui.press('enter')
            break  # Exit the loop if successful
        except gw.PyGetWindowException as e:
            print(f"Erro ao ativar a janela: {e}")
            continue  # Try the next window

if __name__ == "__main__": 
    if len(sys.argv) != 3:
        print("Uso: python simnext-fullscreen.py <window_title> <num_down_presses>")
        sys.exit(1)

    window_title = sys.argv[1]
    num_down_presses = int(sys.argv[2])
    find_and_focus_window(window_title, num_down_presses)

