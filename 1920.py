"""
Đổi nhanh độ phân giải sang 1080x1080 @ 100Hz (Windows only).
Yêu cầu: pip install pywin32
"""

import win32api
import win32con

WIDTH = 1920
HEIGHT = 1080
REFRESH_RATE = 100


def change_resolution(width, height, refresh_rate):
    devmode = win32api.EnumDisplaySettings(None, win32con.ENUM_CURRENT_SETTINGS)
    devmode.PelsWidth = width
    devmode.PelsHeight = height
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


if __name__ == "__main__":
    result, msg = change_resolution(WIDTH, HEIGHT, REFRESH_RATE)
    print(f"Đổi sang {WIDTH}x{HEIGHT} @ {REFRESH_RATE}Hz -> {msg}")