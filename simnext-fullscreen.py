import pygetwindow as gw
import pyautogui
import time
import ctypes

def find_and_focus_window(window_title):
    windows = gw.getWindowsWithTitle(window_title)
    if not windows:
        ctypes.windll.user32.MessageBoxW(0, "A tela 'SIM Next' não foi encontrada.", "Erro", 0)
        return

    for window in windows:
        window.activate()
        time.sleep(1)  
        if window.isMinimized:
            window.restore()
        window.maximize()

        time.sleep(1)  
        center_x, center_y = window.left + window.width // 2, window.top + window.height // 2
        pyautogui.click(center_x, center_y, button='right')
        time.sleep(0.5)  

        # while not pyautogui.locateOnScreen('./item_tela_cheia.png', confidence=0.6):
        for _ in range(21):
            pyautogui.press('down')
            time.sleep(0.2) 

        pyautogui.press('enter')
        

if __name__ == "__main__":
    find_and_focus_window("SIM Next")

