import argparse
import time

import win32api

from config import PLATFORMS
from sender import find_window


def parse_args():
    parser = argparse.ArgumentParser(description="交互式检查鼠标坐标和窗口相对偏移")
    parser.add_argument(
        "-p",
        "--platform",
        choices=PLATFORMS.keys(),
        default="xhs",
        help="平台：xhs=小红书，dy=抖音",
    )
    return parser.parse_args()


def get_click_offset(platform: str, prompt: str):
    was_left_down = win32api.GetKeyState(0x01) < 0
    print(prompt)

    while True:
        win = find_window(platform)

        if not win:
            print("\r未找到直播客户端窗口，请确认窗口已打开   ", end="", flush=True)
            time.sleep(0.2)
            continue

        x, y = win32api.GetCursorPos()
        is_left_down = win32api.GetKeyState(0x01) < 0
        rect = win.BoundingRectangle
        is_in_window = rect.left <= x <= rect.right and rect.top <= y <= rect.bottom
        right_offset = rect.right - x
        bottom_offset = rect.bottom - y

        print(
            "\r"
            f"mouse=({x}, {y}) | "
            f"right_offset={right_offset}, bottom_offset={bottom_offset}   ",
            end="",
            flush=True,
        )

        if is_left_down and not was_left_down:
            if is_in_window:
                print(
                    "\n"
                    f"已记录：mouse=({x}, {y}) | "
                    f"right_offset={right_offset}, bottom_offset={bottom_offset}"
                )
                return {"right_offset": right_offset, "bottom_offset": bottom_offset}

            print("\n点击不在直播客户端窗口内，请重新点击")
            print(prompt)

        was_left_down = is_left_down
        time.sleep(0.05)


def main():
    args = parse_args()
    platform_config = PLATFORMS[args.platform]

    print(f"当前平台：{platform_config['name']} ({args.platform})")
    print("按 Ctrl+C 退出")

    comment_box = get_click_offset(args.platform, "请点击评论框")
    send_button = get_click_offset(args.platform, "请点击发送按钮")

    print("\n可复制到 config.py：")
    print(f'"comment_box": {comment_box},')
    print(f'"send_button": {send_button},')


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n已退出")
