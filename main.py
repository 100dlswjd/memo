import sys
import os
import json
import ctypes

from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton
from PySide6.QtCore import QPropertyAnimation, QRect, Slot, Qt, QTimer, QObject, Signal
from PySide6.QtGui import QMouseEvent, QPixmap

from ui.main_form import Ui_MainWindow
from ui.main_widget_form import Ui_MainWidget
from ui.memo_widget import Ui_memo

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

class MemoSignal(QObject):
    MemoTitleChanged = Signal(list)

class MemoWidget(QWidget, Ui_memo):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setStyleSheet(u"QWidget{\n"
"border:0px;\n"
"}")    
        self.frame_memo.setStyleSheet(u"QFrame{\n"
"border:none;\n"
"\n"
"}")
        self.plainTextEdit_memo.setStyleSheet(u"QPlainTextEdit{\n"
"border:3px solid #ffffff;\n"
"border-radius:16px;\n"
"background-color:#ffffff;\n"
"padding:5px 10px 5px 10px;\n"
"}\n"
"QAbstractScrollArea{\n"
"background-color:#ffffff;\n"
"}\n"
"QScrollBar{\n"
"background-color:#ffffff;\n"
"}\n"
"QScrollBar:sub-line{\n"
"border:none;\n"
"background-color:none;\n"
"}\n"
"QScrollBar:add-line{\n"
"border:none;\n"
"background-color:none;\n"
"}\n"
"QScrollBar:handle{\n"
"background-color:#7af69e;\n"
"border:1px solid #f3f3f3;\n"
"border-radius:8px;\n"
"}\n"
"QScrollBar:handle:Pressed{\n"
"background-color:#6ddd8d;\n"
"}\n"
"")
        self.memo = MemoSignal()
        self.index = 0
        self.plainTextEdit_memo.textChanged.connect(self.plainTextEdit_memo_text_changed_handler)
        
    @Slot()
    def plainTextEdit_memo_text_changed_handler(self):
        title = self.plainTextEdit_memo.toPlainText().replace("\n", "    ")[:4]
        self.memo.MemoTitleChanged.emit([self.index, title])

class MainwindowWidget(QWidget, Ui_MainWidget):
    def __init__(self, default_tab : bool):
        super().__init__()
        self.setupUi(self)
        # frame 7, 10, 500, 380 -> 520, 10, 40, 40
        self.show_btn_img_path = resource_path("img/memo_4.png").replace("\\", "/")
        self.x_btn_img_path = resource_path("img/X.png").replace("\\", "/")        
        self.close_btn_img_path = resource_path("img/close.png").replace("\\", "/")
        self.up_btn_img_path = resource_path("img/up.png").replace("\\", "/")
        self.down_btn_img_path = resource_path("img/down.png").replace("\\", "/")
        self.up_hover_btn_img_path = resource_path("img/up_hover.png").replace("\\", "/")
        self.down_hover_btn_img_path = resource_path("img/down_hover.png").replace("\\", "/")

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
f"image:url(\"{self.x_btn_img_path}\");\n"
"}\n"
"QPushButton:hover{\n"
"background-color:#00c538;\n"
"}\n"
"QPushButton:Pressed{\n"
"background-color:#00a72f;\n"
"}")
        self.plus_btn_img_path = resource_path("img/+.png").replace("\\", "/")
        self.pushButton_add_tab = QPushButton()
        self.pushButton_add_tab.setStyleSheet(u"QPushButton{"
"background-color:#40f274;"
"border:2px solid #ffffff;"
"border-radius:10px;"
f"image:url(\"{self.plus_btn_img_path}\");"
"width:20;"
"height:20;"
"}"
"QPushButton:hover{"
"background-color:#37d364;"
"}"
"QPushButton:Pressed{"
"background-color:#2caa50;"
"}")        
        
        self.tabWidget_memo.setStyleSheet(u"QTabBar:tab{"
"border:2px solid #ffffff;"
"border-radius:10px;"
"width:80px;"
"height:20px;"
"background-color:#47f279;"
"}"
"QTabBar:tab:hover{"
"background-color:#3dd167;"
"}"
"QTabBar:tab:Pressed{"
"background-color:#35b85a;"
"}"
"QTabWidget:pane {"
"border:none;"
"border-radius:none;"
"padding:0px"
"}"
"QTabBar:tab:selected{"
"background-color:#00a72f;"
"color:#ffffff;"
"}"
"QTabBar:close-button{"
f"image:url(\"{self.close_btn_img_path}\");"
"}"
"QTabBar:scroller{"
"width:0px;"
"}")

        self.spinBox_auto_time.setEnabled(False)
        self.spinBox_auto_time.setMinimum(10)
        self.spinBox_auto_time.setStyleSheet(u"QSpinBox{\n"
"border:2px solid #ffffff;\n"
"border-radius:6px;\n"
"background-color:#8ef7ad;\n"
"color:#409047;\n"
"}\n"
"QSpinBox:up-button{\n"
"border:0px;\n"
f"image:url(\"{self.up_btn_img_path}\");\n"
"}\n"
"QSpinBox:up-button:hover{\n"
f"image:url(\"{self.up_hover_btn_img_path}\");\n"
"}\n"
"QSpinBox:down-button{\n"
"border:0px;\n"
f"image:url(\"{self.down_btn_img_path}\");\n"
"}\n"
"QSpinBox:down-button:hover{\n"
f"image:url(\"{self.down_hover_btn_img_path}\");\n"
"}")

        self.show_flag = False
        self.use_check = 0
        self.tab_list = []

        self.tabWidget_memo.setTabsClosable(False)
        self.tabWidget_memo.setCornerWidget(self.pushButton_add_tab)

        self.checkBox_auto.stateChanged.connect(self.checkBox_auto_handler)        

        self.tabWidget_memo.tabCloseRequested.connect(self.tabWidget_memo_close_handler)
        self.pushButton_show.clicked.connect(self.btn_show_click_handler)
        self.pushButton_add_tab.clicked.connect(self.btn_add_click_handler)

        if default_tab:
            self.pushButton_add_tab.click()

        self.timer = QTimer()
        self.timer.timeout.connect(self.timeout_handler)
        self.timer.start(1000)

        self.memo_1 = ""
        self.memo_2 = ""
        self.memo_3 = ""
        self.memo_4 = ""
        self.memo_5 = ""
        self.text_changed = False

    @Slot()
    def checkBox_auto_handler(self):
        if self.checkBox_auto.checkState() == Qt.CheckState.Checked:
            self.spinBox_auto_time.setEnabled(True)
        else:
            self.spinBox_auto_time.setEnabled(False)

    def tabWidget_memo_close_handler(self, index):
        self.tabWidget_memo.removeTab(index)
        self.tab_list.pop(index)
        if self.tabWidget_memo.count() == 1:
            self.tabWidget_memo.setTabsClosable(False)
        
        if self.tabWidget_memo.count() < 5:
            self.pushButton_add_tab.show()
            
    @Slot()
    def btn_add_click_handler(self):
        tab = MemoWidget()
        self.tabWidget_memo.addTab(tab, "Memo")
        self.tab_list.append(tab)
        index = 0
        for memo in self.tab_list:
            memo.index = index
            memo.memo.MemoTitleChanged.connect(self.memo_title_changed_handler)
            index += 1

        if self.tabWidget_memo.count() > 1:
            self.tabWidget_memo.setTabsClosable(True)
        if self.tabWidget_memo.count() >= 5:
            self.pushButton_add_tab.hide()
    
    @Slot(list)
    def memo_title_changed_handler(self, data : list):
        index = data[0]
        title = data[1]
        self.tabWidget_memo.setTabText(index, title)
        self.text_changed = True

    @Slot()
    def btn_show_click_handler(self):
        self.use_check = 0
        self.show_flag = not self.show_flag
        self.frame_animation = QPropertyAnimation(self.frame_main, b"geometry")
        self.frame_animation.setDuration(200)        
        self.frame_animation.setStartValue(self.frame_main.geometry())
        if self.show_flag:
            self.frame_animation.setEndValue(QRect(7, 10, 500, 380))
        else:
            self.frame_animation.setEndValue(QRect(520, 10, 40, 40))
        self.frame_animation.start()

    @Slot()
    def timeout_handler(self):
        self.use_check += 1
        if self.use_check >= self.spinBox_auto_time.value() and self.show_flag and self.checkBox_auto.checkState() == Qt.CheckState.Checked:
            self.pushButton_show.click()
        
        if self.text_changed:
            self.save()
            self.text_changed = False

    def save(self):
        try:
            self.memo_1 = self.tab_list[0].plainTextEdit_memo.toPlainText()
            if self.memo_1 == "":
                self.memo_1 = " "
        except:
            self.memo_1 = ""
        try:
            self.memo_2 = self.tab_list[1].plainTextEdit_memo.toPlainText()
            if self.memo_2 == "":
                self.memo_2 = " "
        except:
            self.memo_2 = ""

        try:
            self.memo_3 = self.tab_list[2].plainTextEdit_memo.toPlainText()
            if self.memo_3 == "":
                self.memo_3 = " "
        except:
            self.memo_3 = ""

        try:        
            self.memo_4 = self.tab_list[3].plainTextEdit_memo.toPlainText()
            if self.memo_4 == "":
                self.memo_4 = " "
        except:
            self.memo_4 = ""

        try:
            self.memo_5 = self.tab_list[4].plainTextEdit_memo.toPlainText()
            if self.memo_5 == "":
                self.memo_5 = " "
        except:
            self.memo_5 = ""

        self.memo_data = {"memo_1":self.memo_1,"memo_2":self.memo_2,"memo_3":self.memo_3,"memo_4":self.memo_4,"memo_5":self.memo_5}
        self.memo_path = os.path.join(os.path.expandvars("%userprofile%"),"documents","ddatg","memo.json")
        with open(self.memo_path,"w") as f:
            f.write(json.dumps(self.memo_data)+"\n")
            f.close()

class Mainwindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.menuBar().hide()
        self.statusBar().hide()
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        myappid = 'ddatg memo' # arbitrary string
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)


        self.document_path = os.path.join(os.path.expandvars("%userprofile%"),"documents")
        self.memo_path = os.path.join(os.path.expandvars("%userprofile%"),"documents","ddatg","memo.json")        

        self.memo_data = ""
            
        try:
            with open(self.memo_path,"r") as f:
                self.memo_data = json.load(f)
                f.close()
        except:
            try:
                os.mkdir(os.path.join(self.document_path,"ddatg"))
                with open(self.memo_path,"w") as f:
                    f.close()
            except:
                pass

        self.mainwidget = MainwindowWidget(not bool(self.memo_data))
        self.vboxlayout = QVBoxLayout()
        self.vboxlayout.addWidget(self.mainwidget)
        self.frame.setLayout(self.vboxlayout)
        try:
            if self.memo_data:
                self.memo_1 = self.memo_data["memo_1"]
                self.memo_2 = self.memo_data["memo_2"]
                self.memo_3 = self.memo_data["memo_3"]
                self.memo_4 = self.memo_data["memo_4"]
                self.memo_5 = self.memo_data["memo_5"]
                if self.memo_1:
                    self.mainwidget.pushButton_add_tab.click()
                    self.mainwidget.tab_list[0].plainTextEdit_memo.setPlainText(self.memo_1)
                if self.memo_2:
                    self.mainwidget.pushButton_add_tab.click()
                    self.mainwidget.tab_list[1].plainTextEdit_memo.setPlainText(self.memo_2)
                if self.memo_3:
                    self.mainwidget.pushButton_add_tab.click()
                    self.mainwidget.tab_list[2].plainTextEdit_memo.setPlainText(self.memo_3)
                if self.memo_4:
                    self.mainwidget.pushButton_add_tab.click()
                    self.mainwidget.tab_list[3].plainTextEdit_memo.setPlainText(self.memo_4)
                if self.memo_5:
                    self.mainwidget.pushButton_add_tab.click()
                    self.mainwidget.tab_list[4].plainTextEdit_memo.setPlainText(self.memo_5)
        except Exception as e:
            print(e)

        self.frame.setContentsMargins(0, 0, 0, 0)

        self.mainwidget.pushButton_close.clicked.connect(self.close_btn_handler)
        self.mainwidget.checkBox_floating.stateChanged.connect(self.checkBox_floating_state_changed_handler)

    @Slot()
    def close_btn_handler(self):
        self.mainwidget.save()
        self.close()

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

    @Slot()
    def checkBox_floating_state_changed_handler(self):
        if self.mainwidget.checkBox_floating.checkState() == Qt.CheckState.Checked:
            self.setWindowFlag(Qt.WindowType.WindowStaysOnTopHint, True)
        else:
            self.setWindowFlag(Qt.WindowType.WindowStaysOnTopHint, False)

        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Mainwindow()
    window.show()
    ico = resource_path("img/memo_3.png")
    app.setWindowIcon(QPixmap(ico))
    app.exec()