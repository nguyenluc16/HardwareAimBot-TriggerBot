import sys
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtWidgets import QApplication, QWidget

from constants import FOV


class CircleOverlayWidget(QWidget):
    def __init__(self):
        super().__init__()

        # Thiết lập cửa sổ không viền, trong suốt
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        # Cửa sổ hiển thị nhỏ trên màn hình
        self.setGeometry(0, 0, 400, 400)  # Kích thước cửa sổ
        self.setWindowOpacity(0.8)  # Độ mờ của cửa sổ overlay (tùy chỉnh)

    def paintEvent(self, event):
        # Vẽ hình tròn
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)  # Bật chế độ làm mịn

        # Thiết lập bút vẽ viền trắng
        pen = QPen(QColor(255, 255, 255))  # Viền trắng
        pen.setWidth(2)  # Độ dày viền
        painter.setPen(pen)
        painter.setBrush(Qt.NoBrush)  # Không tô màu bên trong hình tròn

        # Vị trí trung tâm màn hình
        center_x = self.width() // 2
        center_y = self.height() // 2
        radius = FOV/2  # Bán kính hình tròn

        # Vẽ hình tròn
        painter.drawEllipse(
            int(center_x - radius),
            int(center_y - radius),
            int(radius * 2),
            int(radius * 2)
        )


        # Kết thúc việc vẽ
        painter.end()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CircleOverlayWidget()

    # Đặt cửa sổ overlay ở giữa màn hình
    screen_geometry = app.desktop().screenGeometry()
    window.move((screen_geometry.width() - window.width()) // 2, (screen_geometry.height() - window.height()) // 2)

    window.show()
    sys.exit(app.exec_())
