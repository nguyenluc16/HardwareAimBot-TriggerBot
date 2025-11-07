@echo off
REM run.bat — mở circle.py trong cửa sổ mới, chạy main.py trong cửa sổ hiện tại

REM Thư mục script
SET SCRIPT_DIR=%~dp0

REM Mở cửa sổ mới chạy circle.py (giữ cửa sổ mở khi xong)
start "CircleWindow" cmd /k py "%SCRIPT_DIR%circle.py"

REM Chạy main.py trong cửa sổ hiện tại (chờ khi hoàn tất)
py "%SCRIPT_DIR%main.py"

REM Khi main.py kết thúc, script này kết thúc
