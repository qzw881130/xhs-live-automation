import time
import pyperclip
import uiautomation as auto
import win32gui

from config import DEBUG, PLATFORMS


def log(*args):
    if DEBUG:
        print(*args)


def get_platform_config(platform: str):
    if platform not in PLATFORMS:
        supported = ", ".join(PLATFORMS.keys())
        raise ValueError(f"不支持的平台: {platform}，支持: {supported}")

    return PLATFORMS[platform]


def find_window(platform: str):
    platform_config = get_platform_config(platform)
    keywords = platform_config.get("window_keywords", [])
    window_class = platform_config.get("window_class")
    root = auto.GetRootControl()

    if DEBUG:
        print("=" * 60)
        print(f"开始查找{platform_config['name']}窗口...")

    for win in root.GetChildren():
        try:
            name = win.Name or ""
            class_name = win.ClassName or ""
            rect = win.BoundingRectangle

            log(
                f"Name='{name}' | "
                f"Class='{class_name}' | "
                f"Rect=({rect.left},{rect.top},{rect.right},{rect.bottom})"
            )

            class_matched = not window_class or class_name == window_class
            keywords_matched = all(keyword in name for keyword in keywords)

            if keywords_matched and class_matched:
                log(f"✅ 命中{platform_config['name']}窗口")
                return win

        except Exception as e:
            log("异常:", e)

    return None


def is_foreground_platform(platform: str) -> bool:
    platform_config = get_platform_config(platform)
    hwnd = win32gui.GetForegroundWindow()
    title = win32gui.GetWindowText(hwnd)

    log(f"当前前台窗口: {title}")

    return all(keyword in title for keyword in platform_config.get("window_keywords", []))


def send_comment(text: str, platform: str = "xhs") -> bool:
    platform_config = get_platform_config(platform)
    win = find_window(platform)

    if not win:
        print(f"[跳过] 当前屏幕没有{platform_config['name']}窗口")
        return False

#    if not is_foreground_platform(platform):
#        print(f"[跳过] {platform_config['name']}不是前台窗口，不发送")
#        return False

    rect = win.BoundingRectangle
    comment_box = platform_config["comment_box"]
    send_button = platform_config["send_button"]

    comment_x = rect.right - comment_box["right_offset"]
    comment_y = rect.bottom - comment_box["bottom_offset"]

    send_x = rect.right - send_button["right_offset"]
    send_y = rect.bottom - send_button["bottom_offset"]

    log("=" * 50)
    log("平台:", platform_config["name"])
    log("窗口:", rect.left, rect.top, rect.right, rect.bottom)
    log("输入框:", comment_x, comment_y)
    log("发送:", send_x, send_y)
    log("=" * 50)

    pyperclip.copy(text)
    time.sleep(0.2)

    auto.Click(comment_x, comment_y)
    time.sleep(0.2)

    auto.SendKeys("{Ctrl}a")
    time.sleep(0.1)
    auto.SendKeys("{Delete}")
    time.sleep(0.1)

    auto.SendKeys("{Ctrl}v")
    time.sleep(0.2)

    auto.Click(send_x, send_y)
    time.sleep(0.2)

    print("[已发送]", text)
    return True
