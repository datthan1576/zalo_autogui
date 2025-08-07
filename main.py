import os
import time
import pyautogui
import pyperclip
from autogui import move_cursor_by_image

def click_and_paste_text(text, delay=0.5):
    pyperclip.copy(text)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(delay)

if __name__ == "__main__":

    zalo_icon_path = "data/zalo/zalo_icon.png"  
    search_bar_path = "data/zalo/zalo_search_bar.png"
    receiver_names = ["Chân Đì", "Lân Đàn"]
    message = "Test message"

    # --- Bước 1: Mở Zalo ---
    result = move_cursor_by_image(zalo_icon_path)
    if result:
        pyautogui.click()
        time.sleep(1)
    else:
        print("Không tìm thấy biểu tượng Zalo.")
        exit()

    # --- Bước 2: Xác định vị trí thanh tìm kiếm (1 lần duy nhất) ---
    search_bar_location = move_cursor_by_image(search_bar_path)
    if not search_bar_location:
        print("Không tìm thấy thanh tìm kiếm.")
        exit()

    # --- Bước 3: Gửi tin nhắn cho từng người ---
    for i, receiver_name in enumerate(receiver_names):
        # Di chuyển tới thanh tìm kiếm (dùng tọa độ đã lưu)
        pyautogui.moveTo(search_bar_location)
        pyautogui.click()
        time.sleep(0.5)

        # Gõ tên người nhận
        click_and_paste_text(receiver_name)
        pyautogui.press('enter')
        time.sleep(1)  # đợi mở khung chat

        # Gửi tin nhắn
        click_and_paste_text(message)
        pyautogui.press('enter')
        time.sleep(0.5)
