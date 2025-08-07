import pyautogui
import os

def move_cursor_by_image(image_path, threshold=0.8, move_duration=0.5):
    """
    Tìm ảnh trên màn hình và di chuyển chuột tới đó.

    Args:
        image_path (str): Đường dẫn tuyệt đối tới file ảnh mẫu (.png, .jpg, ...)
        threshold (float): Mức độ khớp (0.0 đến 1.0). Mặc định là 0.8
        move_duration (float): Thời gian di chuyển chuột (giây)

    Returns:
        tuple: Tọa độ (x, y) nếu tìm thấy, hoặc None nếu không tìm thấy
    """
    # Kiểm tra ảnh có tồn tại không
    if not os.path.exists(image_path):
        print(f"[LỖI] Không tìm thấy file ảnh: {image_path}")
        return None

    try:
        # Tìm vị trí ảnh trên màn hình
        location = pyautogui.locateOnScreen(image_path, confidence=threshold)

        if location:
            center = pyautogui.center(location)
            pyautogui.moveTo(center.x, center.y, duration=move_duration)
            print(f"[✓] Đã di chuyển chuột tới: {center}")
            return (center.x, center.y)
        else:
            print("[!] Không tìm thấy ảnh trên màn hình.")
            return None

    except Exception as e:
        print(f"[LỖI] Xảy ra lỗi khi xử lý ảnh: {e}")
        return None
