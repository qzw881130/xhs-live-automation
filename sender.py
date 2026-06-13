import time
import pyperclip
import uiautomation as auto
import win32gui


WINDOW_NAME = "直播助手-直播页"


def find_window():
    root = auto.GetRootControl()

    for win in root.GetChildren():
        try:
            name = win.Name or ""
            class_name = win.ClassName or ""

            if "直播助手" in name and class_name == "Chrome_WidgetWin_1":
                return win
        except Exception:
            pass

    return None


def is_foreground_xhs() -> bool:
    hwnd = win32gui.GetForegroundWindow()
    title = win32gui.GetWindowText(hwnd)
    class_name = win32gui.GetClassName(hwnd)

    print(f"当前前台窗口: {title} | {class_name}")

    return "直播助手" in title or class_name == "Chrome_WidgetWin_1" and "直播助手" in title


def send_comment(text: str) -> bool:
    win = find_window()

    if not win:
        print("[跳过] 当前屏幕没有直播助手窗口")
        return False

    if not is_foreground_xhs():
        print("[跳过] 直播助手不是前台窗口，不发送")
        return False

    rect = win.BoundingRectangle

    comment_x = rect.right - 487
    comment_y = rect.bottom - 88

    send_x = rect.right - 75
    send_y = rect.bottom - 77

    print("=" * 50)
    print("窗口:", rect.left, rect.top, rect.right, rect.bottom)
    print("输入框:", comment_x, comment_y)
    print("发送:", send_x, send_y)
    print("=" * 50)

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