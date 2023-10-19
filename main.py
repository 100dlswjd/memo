import sys
import os

from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout
from PySide6.QtCore import QPropertyAnimation, QRect, Slot, Qt, QTimer
from PySide6.QtGui import QMouseEvent

from ui.main_form import Ui_MainWindow
from ui.main_widget_form import Ui_Form



class MainwindowWidget(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # frame 7, 10, 500, 380 -> 520, 10, 40, 40
        cwd = os.getcwd().replace("\\", "/")
        self.show_btn_img_path = cwd + "/img/memo_4.png"
        self.close_btn_img_path = cwd + "/img/X.png"
        self.pushButton_show.setStyleSheet(u"QPushButton{\n"
"border:3px solid #ffffff;\n"
"border-radius:20px;\n"
"padding:10px;\n"
"background-color:#00da3e;\n"
f"image:url(\"{self.show_btn_img_path}\");\n"
"}\n"
"QPushButton:hover{\n"
"background-color:#00c538;\n"
"}\n"
"QPushButton:Pressed{\n"
"background-color:#00a72f;\n"
"}")
        self.pushButton_close.setStyleSheet(u"QPushButton{\n"
"border:3px solid #ffffff;\n"
"border-radius:20px;\n"
"padding:10px;\n"
"background-color:#00da3e;\n"
f"image:url(\"{self.close_btn_img_path}\");\n"
"}\n"
"QPushButton:hover{\n"
"background-color:#00c538;\n"
"}\n"
"QPushButton:Pressed{\n"
"background-color:#00a72f;\n"
"}")

        self.show_flag = False
        self.use_check = 0

        self.pushButton_show.clicked.connect(self.btn_show_click_handler)
        self.textEdit_memo.textChanged.connect(self.textEdit_memo_changed_handler)

        self.timer = QTimer()
        self.timer.timeout.connect(self.timeout_handler)
        self.timer.start(1000)
    
    @Slot()
    def textEdit_memo_changed_handler(self):
        self.use_check = 0

    @Slot()
    def btn_show_click_handler(self):
        self.use_check = 0
        self.show_flag = not self.show_flag
        self.frame_animation = QPropertyAnimation(self.frame, b"geometry")
        self.frame_animation.setDuration(200)        
        self.frame_animation.setStartValue(self.frame.geometry())
        if self.show_flag:
            self.frame_animation.setEndValue(QRect(7, 10, 500, 380))
        else:
            self.frame_animation.setEndValue(QRect(520, 10, 40, 40))
        self.frame_animation.start()

    @Slot()
    def timeout_handler(self):
        self.use_check += 1
        if self.use_check >= 10 and self.show_flag and self.checkBox_auto.checkState() == Qt.CheckState.Checked:
            self.pushButton_show.click()

class Mainwindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.menuBar().hide()
        self.statusBar().hide()
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.setWindowFlag(Qt.WindowType.WindowStaysOnTopHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        
        self.mainwidget = MainwindowWidget()
        self.vboxlayout = QVBoxLayout()
        self.vboxlayout.addWidget(self.mainwidget)
        self.frame.setLayout(self.vboxlayout)

        self.frame.setContentsMargins(0, 0, 0, 0)

        self.mainwidget.pushButton_close.clicked.connect(self.close)

    def mousePressEvent(self, event: QMouseEvent) -> None:
        self.mainwidget.use_check = 0
        try:
            self.dragPos = event.globalPosition().toPoint()            
        except:
            pass

    def mouseMoveEvent(self, event: QMouseEvent) -> None:
        self.mainwidget.use_check = 0
        try:
            self.move(self.pos() + event.globalPosition().toPoint() - self.dragPos)
            self.dragPos = event.globalPosition().toPoint()
        except:
            pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Mainwindow()
    window.show()
    app.exec()