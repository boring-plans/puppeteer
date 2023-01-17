"""
Keyboard and mouse events.

By Allen Tao
Created at 2023/01/17 14:05
"""
import math
from typing import Tuple

import pyautogui


def mouse_down(x: float, y: float) -> None:
    pyautogui.mouseDown(convert_pos(x, y))


def mouse_up() -> None:
    pyautogui.mouseUp()


def mouse_to(x: float, y: float) -> None:
    pyautogui.moveTo(convert_pos(x, y))


def convert_pos(x: float, y: float) -> Tuple[int, int]:
    size = pyautogui.size()
    return math.floor(size.width * x), math.floor(size.height * y)
