import random

from config import PLATFORMS


def generate_comment(platform: str = "xhs"):
    comments = PLATFORMS[platform]["comments"]
    return random.choice(comments)
