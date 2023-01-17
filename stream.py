"""

By Allen Tao
Created at 2023/01/17 14:04
"""
import pyautogui
import io


def gen_stream():
    while True:
        frame = io.BytesIO()
        screenshot = pyautogui.screenshot()
        screenshot.save(frame, format="JPEG")
        yield b'--frame\r\nContent-Type: image/jpeg\r\n\r\n' + frame.getvalue()
