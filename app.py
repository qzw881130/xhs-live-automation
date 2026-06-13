import random
import time
import ctypes
import sys

from holo import generate_comment
from sender import send_comment
from config import SEND_INTERVAL_MIN, SEND_INTERVAL_MAX


def disable_quick_edit():
    kernel32 = ctypes.windll.kernel32
    h_stdin = kernel32.GetStdHandle(-10)

    mode = ctypes.c_uint()
    kernel32.GetConsoleMode(h_stdin, ctypes.byref(mode))

    new_mode = mode.value & ~0x0040
    kernel32.SetConsoleMode(h_stdin, new_mode)


def countdown(seconds):
    while seconds > 0:
        m, s = divmod(seconds, 60)
        sys.stdout.write(f"\r⏳ 下次检查/发送：{m:02d}:{s:02d}   ")
        sys.stdout.flush()
        time.sleep(1)
        seconds -= 1

    sys.stdout.write("\r" + " " * 40 + "\r")
    sys.stdout.flush()


disable_quick_edit()

while True:
    comment = generate_comment()
    ok = send_comment(comment)

    wait = random.randint(SEND_INTERVAL_MIN, SEND_INTERVAL_MAX)

    if ok:
        print(f"已发送，{wait} 秒后再次检查")
    else:
        print(f"未发送，{wait} 秒后再次检查")

    countdown(wait)