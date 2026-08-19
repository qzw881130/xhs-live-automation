# XHS Live Agent

一个基于 Python + UIAutomation 的直播评论自动发送工具。

## 功能

- AI 自动生成直播评论
- 自动定位直播客户端窗口
- 自动输入并发送评论
- 支持小红书和抖音平台
- 支持配置不同平台的窗口匹配和按钮坐标
- 支持交互式检查评论框和发送按钮坐标

---

## 项目结构

```text
.
├── app.py                    # 主程序
├── sender.py                 # 评论发送模块
├── holo.py                   # AI 评论生成模块
├── config.py                 # 配置文件
├── check_mouse_position.py   # 坐标检查工具
├── prompts/                  # Prompt 模板
├── README.md
└── .gitignore
```

---

## 安装

创建虚拟环境：

```bash
python -m venv venv
```

激活虚拟环境：

```bash
venv\Scripts\activate
```

安装依赖：

```bash
pip install -r requirements.txt
```

或手动安装：

```bash
pip install uiautomation pyperclip openai pywin32
```

---

## 配置

平台配置在 `config.py` 的 `PLATFORMS` 中。发送间隔单位是秒，每个平台单独配置：

```python
PLATFORMS = {
    "xhs": {
        "name": "小红书",
        "window_keywords": ["直播助手"],
        "window_class": "Chrome_WidgetWin_1",
        "send_interval": {"min": 900, "max": 1200},
        "comment_box": {"right_offset": 487, "bottom_offset": 88},
        "send_button": {"right_offset": 75, "bottom_offset": 77},
    },
    "dy": {
        "name": "抖音",
        "window_keywords": ["直播伴侣"],
        "window_class": None,
        "send_interval": {"min": 60, "max": 120},
        "comment_box": {"right_offset": 409, "bottom_offset": 98},
        "send_button": {"right_offset": 97, "bottom_offset": 81},
    },
    "bili": {
        "name": "哔哩哔哩",
        "window_keywords": ["直播姬"],
        "window_class": None,
        "send_interval": {"min": 120, "max": 240},
        "comment_box": {"right_offset": 502, "bottom_offset": 96},
        "send_button": {"right_offset": 97, "bottom_offset": 94},
    },
}
```

---

## 运行

小红书：

```bash
python app.py -p xhs
```

抖音：

```bash
python app.py -p dy
```

哔哩哔哩：

```bash
python app.py -p bili
```

如果不传 `-p`，默认使用小红书：

```bash
python app.py
```

程序会：

- 生成 AI 评论
- 定位对应平台的直播客户端窗口
- 点击评论框
- 粘贴评论
- 点击发送按钮
- 等待下一次执行

---

## 坐标检查工具

`check_mouse_position.py` 用于交互式获取评论框和发送按钮坐标。

启动小红书坐标检查：

```bash
python check_mouse_position.py -p xhs
```

启动抖音坐标检查：

```bash
python check_mouse_position.py -p dy
```

启动哔哩哔哩坐标检查：

```bash
python check_mouse_position.py -p bili
```

运行后按提示操作：

1. 提示 `请点击评论框` 时，在直播客户端里点击评论输入框。
2. 程序会记录评论框的 `right_offset` 和 `bottom_offset`。
3. 提示 `请点击发送按钮` 时，在直播客户端里点击发送按钮。
4. 程序会记录发送按钮的 `right_offset` 和 `bottom_offset`。
5. 最后会输出可复制到 `config.py` 的配置内容。

输出示例：

```python
"comment_box": {"right_offset": 409, "bottom_offset": 98},
"send_button": {"right_offset": 97, "bottom_offset": 81},
```

把对应内容更新到 `config.py` 的平台配置里：

```python
"dy": {
    "name": "抖音",
    "window_keywords": ["直播伴侣"],
    "window_class": None,
    "comment_box": {"right_offset": 409, "bottom_offset": 98},
    "send_button": {"right_offset": 97, "bottom_offset": 81},
},
```

坐标计算方式：

```python
x = rect.right - right_offset
y = rect.bottom - bottom_offset
```

因此窗口大小或布局变化后，只需要重新运行 `check_mouse_position.py`，再更新对应平台的 4 个偏移值。

---

## 注意事项

- 当前工具依赖 Windows UIAutomation，只适用于 Windows。
- 运行时需要保持直播客户端窗口打开。
- 如果找不到窗口，先检查 `config.py` 中对应平台的 `window_keywords`。
- 不建议过于频繁发送评论，请合理设置发送间隔。

---

## License

MIT License
