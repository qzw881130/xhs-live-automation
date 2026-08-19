# 窗口名称
WINDOW_NAME = "直播助手-直播页"

# 平台配置
# 坐标以窗口右下角为基准：x = rect.right - right_offset, y = rect.bottom - bottom_offset
PLATFORMS = {
    "xhs": {
        "name": "小红书",
        "window_keywords": ["直播助手"],
        "window_class": "Chrome_WidgetWin_1",
        "send_interval": {"min": 900, "max": 1200},
        "comments": [
            "欢迎来到直播间，祝您阅读愉快～",
            "欢迎新朋友来到直播间～",
            "喜欢有声小说的朋友欢迎一起听书～",
            "点点赞、点点关注，支持一下主播呀～",
            "感谢来到直播间，一起品读经典～",
            "点点赞点点关注支持一下主播呀～",
            "欢迎各位听友进直播间，共品有声小说",
            "点关注不迷路~ 下次开播有通知！随时下播，随时开播",
        ],
        "comment_box": {"right_offset": 487, "bottom_offset": 88},
        "send_button": {"right_offset": 75, "bottom_offset": 77},
    },
    "dy": {
        "name": "抖音",
        "window_keywords": ["直播伴侣"],
        "window_class": None,
        "send_interval": {"min": 60, "max": 120},
        "comments": [
            "这段讲得挺有画面感",
            "听着很舒服",
            "这个情节有意思",
            "声音很适合听故事",
            "刚进来，先听一会儿",
            "这一段节奏不错",
            "故事慢慢展开了",
            "适合边听边放松",
        ],
        # 如果抖音助手窗口布局变化，只改下面 4 个数值
        "comment_box": {"right_offset": 409, "bottom_offset": 98},
        "send_button": {"right_offset": 97, "bottom_offset": 81},
    },
    "bili": {
        "name": "哔哩哔哩",
        "window_keywords": ["直播姬"],
        "window_class": None,
        "send_interval": {"min": 120, "max": 240},
        "comments": [
            "欢迎来到直播间，祝您阅读愉快～",
            "欢迎新朋友来到直播间～",
            "喜欢有声小说的朋友欢迎一起听书～",
            "点点赞、点点关注，支持一下主播呀～",
            "感谢来到直播间，一起品读经典～",
            "点点赞点点关注支持一下主播呀～",
            "欢迎各位听友进直播间，共品有声小说",
            "点关注不迷路~ 下次开播有通知！随时下播，随时开播",
        ],
        # 如果哔哩哔哩直播姬窗口布局变化，只改下面 4 个数值
        "comment_box": {"right_offset": 502, "bottom_offset": 96},
        "send_button": {"right_offset": 97, "bottom_offset": 94},
    },
}

# 是否打印调试信息
DEBUG = False

# 发送失败重试次数
MAX_RETRY = 3
