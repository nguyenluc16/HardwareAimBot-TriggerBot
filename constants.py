# ==========================
# constants.py — dùng chung cho toàn project
# ==========================

# Serial Port Settings
FIXED_SERIAL_PORT = "COM3"
SPEED_MULTIPLIER = 1.2

# Hotkey Config
TOGGLE_KEY = "F1"
VK_A = 0x41
VK_D = 0x44

# FOV / Resolution Defaults
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
FOV = 70

import numpy as np

# ==========================
# Colorant Configuration
# ==========================

# Màu tím (Purple)
COLOR_PURPLE_LOWER = np.array([140, 110, 150])
COLOR_PURPLE_UPPER = np.array([150, 195, 255])

# Màu đỏ (Red)
COLOR_RED_LOWER = np.array([0, 150, 150])
COLOR_RED_UPPER = np.array([10, 255, 255])

# Màu vàng (Yellow)
COLOR_YELLOW_LOWER = np.array([20, 100, 150])
COLOR_YELLOW_UPPER = np.array([35, 255, 255])

# Mặc định đang dùng màu tím
ACTIVE_COLOR_LOWER = COLOR_PURPLE_LOWER
ACTIVE_COLOR_UPPER = COLOR_PURPLE_UPPER

# Ngưỡng xử lý ảnh
COLORANT_THRESHOLD = 60
