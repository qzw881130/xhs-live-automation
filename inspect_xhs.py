import uiautomation as auto


def print_tree(control, depth=0, max_depth=12):
    if depth > max_depth:
        return

    try:
        print(
            "  " * depth +
            f"{control.ControlTypeName} | "
            f"Name='{control.Name}' | "
            f"Class='{control.ClassName}'"
        )
    except Exception:
        return

    try:
        for child in control.GetChildren():
            print_tree(child, depth + 1, max_depth)
    except Exception:
        pass


win = auto.PaneControl(searchDepth=1, Name="直播助手-直播页")

if not win.Exists(5):
    print("找不到直播助手 Pane")
    exit()

print("找到直播助手：", win.Name)
print("=" * 80)

print_tree(win)