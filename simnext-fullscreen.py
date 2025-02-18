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
            center_x, center_y = window.left + window.width // 2, window.top + window.height // 2
            pyautogui.click(center_x, center_y, button='right')
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

