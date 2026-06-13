# list_windows.py

import uiautomation as auto

for w in auto.GetRootControl().GetChildren():
    try:
        print(
            f"{w.ControlTypeName} | "
            f"Name='{w.Name}' | "
            f"Class='{w.ClassName}'"
        )
    except:
        pass