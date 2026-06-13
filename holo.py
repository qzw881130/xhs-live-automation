import random

WELCOME = [
    "欢迎来到直播间，祝您阅读愉快～",
    "欢迎新朋友来到直播间～",
    "喜欢《红楼梦》的朋友欢迎一起听书～",
    "点点赞点点关注支持一下主播呀～",
    "感谢来到直播间，一起品读经典～"
]


def generate_comment():
    return random.choice(WELCOME)