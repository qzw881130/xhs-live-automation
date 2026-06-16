# 评论发送间隔（秒）
SEND_INTERVAL_MIN = 900
SEND_INTERVAL_MAX = 1200

# 窗口名称
WINDOW_NAME = "直播助手-直播页"

# 平台配置
# 坐标以窗口右下角为基准：x = rect.right - right_offset, y = rect.bottom - bottom_offset
PLATFORMS = {
    "xhs": {
        "name": "小红书",
        "window_keywords": ["直播助手"],
        "window_class": "Chrome_WidgetWin_1",
        "comment_box": {"right_offset": 487, "bottom_offset": 88},
        "send_button": {"right_offset": 75, "bottom_offset": 77},
    },
    "dy": {
        "name": "抖音",
        "window_keywords": ["直播伴侣"],
        "window_class": None,
        # 如果抖音助手窗口布局变化，只改下面 4 个数值
        "comment_box": {"right_offset": 409, "bottom_offset": 98},
        "send_button": {"right_offset": 97, "bottom_offset": 81},
    },
}

# 是否打印调试信息
DEBUG = False

# 发送失败重试次数
MAX_RETRY = 3
