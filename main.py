import sys
import win32api
import win32con

REFRESH_RATE = 100

# 2 option cố định: (width, height)
RESOLUTIONS = [
    (1280, 882),
    (1080, 1080),
]


def get_current_resolution():
    settings = win32api.EnumDisplaySettings(None, win32con.ENUM_CURRENT_SETTINGS)
    return settings.PelsWidth, settings.PelsHeight, settings.DisplayFrequency


def change_resolution(width, height, refresh_rate=None):
    devmode = win32api.EnumDisplaySettings(None, win32con.ENUM_CURRENT_SETTINGS)
    devmode.PelsWidth = width
    devmode.PelsHeight = height
    if refresh_rate:
        devmode.DisplayFrequency = refresh_rate

    result = win32api.ChangeDisplaySettings(devmode, 0)

    codes = {
        win32con.DISP_CHANGE_SUCCESSFUL: "Thành công",
        win32con.DISP_CHANGE_RESTART: "Cần restart để áp dụng",
        win32con.DISP_CHANGE_FAILED: "Thất bại (driver từ chối)",
        win32con.DISP_CHANGE_BADMODE: "Mode không hợp lệ",
        win32con.DISP_CHANGE_NOTUPDATED: "Không lưu vào registry được",
        win32con.DISP_CHANGE_BADFLAGS: "Flags không hợp lệ",
        win32con.DISP_CHANGE_BADPARAM: "Tham số không hợp lệ",
    }
    return result, codes.get(result, f"Mã lỗi không xác định: {result}")


def main():
    cw, ch, cf = get_current_resolution()
    print(f"Độ phân giải hiện tại: {cw}x{ch} @ {cf}Hz\n")

    print("Chọn độ phân giải:")
    for idx, (w, h) in enumerate(RESOLUTIONS):
        marker = "  <- hiện tại" if (w, h) == (cw, ch) else ""
        print(f"  [{idx}] {w}x{h} @ {REFRESH_RATE}Hz{marker}")

    choice = input("\nChọn số thứ tự muốn đổi sang (Enter để hủy): ").strip()
    if not choice:
        print("Đã hủy.")
        return

    try:
        idx = int(choice)
        w, h = RESOLUTIONS[idx]
    except (ValueError, IndexError):
        print("Lựa chọn không hợp lệ.")
        sys.exit(1)

    result, msg = change_resolution(w, h, REFRESH_RATE)
    print(f"\nĐổi sang {w}x{h} @ {REFRESH_RATE}Hz -> {msg}")


if __name__ == "__main__":
    main()