import random
import time
import ctypes
import sys
import argparse

from holo import generate_comment
from sender import send_comment
from config import PLATFORMS, SEND_INTERVAL_MIN, SEND_INTERVAL_MAX


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


def parse_args():
    parser = argparse.ArgumentParser(description="自动发送直播评论")
    parser.add_argument(
        "-p",
        "--platform",
        choices=PLATFORMS.keys(),
        default="xhs",
        help="平台：xhs=小红书，dy=抖音",
    )
    return parser.parse_args()


disable_quick_edit()
args = parse_args()
platform_name = PLATFORMS[args.platform]["name"]
print(f"当前平台：{platform_name} ({args.platform})")

while True:
    comment = generate_comment()
    ok = send_comment(comment, args.platform)

    wait = random.randint(SEND_INTERVAL_MIN, SEND_INTERVAL_MAX)

    if ok:
        print(f"已发送，{wait} 秒后再次检查")
    else:
        print(f"未发送，{wait} 秒后再次检查")

    countdown(wait)
