# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_widget_form_2.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QTabWidget, QVBoxLayout, QWidget)

class Ui_MainWidget(object):
    def setupUi(self, MainWidget):
        if not MainWidget.objectName():
            MainWidget.setObjectName(u"MainWidget")
        MainWidget.resize(600, 400)
        MainWidget.setMinimumSize(QSize(600, 400))
        MainWidget.setStyleSheet(u"")
        self.pushButton_show = QPushButton(MainWidget)
        self.pushButton_show.setObjectName(u"pushButton_show")
        self.pushButton_show.setGeometry(QRect(520, 10, 70, 80))
        self.pushButton_show.setStyleSheet(u"QPushButton{\n"
"border:3px solid #ffffff;\n"
"border-radius:20px;\n"
"padding:10px;\n"
"background-color:#00da3e;\n"
"image:url(\"D:/git/100dlswjd/memo/img/memo_4.png\");\n"
"}\n"
"QPushButton:hover{\n"
"background-color:#00c538;\n"
"}\n"
"QPushButton:Pressed{\n"
"background-color:#00a72f;\n"
"}")
        self.label_move = QLabel(MainWidget)
        self.label_move.setObjectName(u"label_move")
        self.label_move.setGeometry(QRect(520, 80, 70, 22))
        self.label_move.setStyleSheet(u"QLabel{\n"
"border:3px solid #ffffff;\n"
"border-radius:8px;\n"
"background-color:qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(0, 218, 62, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}")
        self.frame_main = QFrame(MainWidget)
        self.frame_main.setObjectName(u"frame_main")
        self.frame_main.setEnabled(True)
        self.frame_main.setGeometry(QRect(7, 10, 500, 380))
        self.frame_main.setMinimumSize(QSize(0, 0))
        self.frame_main.setStyleSheet(u"QFrame{\n"
"background-color:qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:1, stop:0 rgba(0, 237, 69, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border:3px solid #ffffff;\n"
"border-radius:20px;\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(self.frame_main)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(4, 4, 4, 4)
        self.tabWidget_memo = QTabWidget(self.frame_main)
        self.tabWidget_memo.setObjectName(u"tabWidget_memo")
        self.tabWidget_memo.setStyleSheet(u"QTabBar:tab{\n"
"border:2px solid #ffffff;\n"
"border-radius:10px;\n"
"width:80px;\n"
"height:20px;\n"
"background-color:#47f279;\n"
"}\n"
"QTabBar:tab:hover{\n"
"background-color:#3dd167;\n"
"}\n"
"QTabBar:tab:Pressed{\n"
"background-color:#35b85a;\n"
"}\n"
"QTabWidget:pane {\n"
"border:none;\n"
"border-radius:none;\n"
"padding:0px\n"
"}")

        self.verticalLayout.addWidget(self.tabWidget_memo)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(4, 4, 4, 4)
        self.label_error = QLabel(self.frame_main)
        self.label_error.setObjectName(u"label_error")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_error.sizePolicy().hasHeightForWidth())
        self.label_error.setSizePolicy(sizePolicy)
        self.label_error.setStyleSheet(u"QLabel{\n"
"border:none;\n"
"background-color:none;\n"
"color:rgb(0, 218, 62)\n"
"}\n"
"QLabel:hover{\n"
"color:#000000;\n"
"}")

        self.horizontalLayout.addWidget(self.label_error)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.checkBox_auto = QCheckBox(self.frame_main)
        self.checkBox_auto.setObjectName(u"checkBox_auto")
        sizePolicy.setHeightForWidth(self.checkBox_auto.sizePolicy().hasHeightForWidth())
        self.checkBox_auto.setSizePolicy(sizePolicy)
        self.checkBox_auto.setStyleSheet(u"QCheckBox{\n"
"color:#409047;\n"
"}\n"
"QCheckBox:indicator{\n"
"border:2px solid #72ff7e;\n"
"border-radius:6px;\n"
"}\n"
"QCheckBox:indicator:checked{\n"
"border:1px solid #72ff7e;\n"
"padding:2px;\n"
"background-color:#58c561;\n"
"}")
        self.checkBox_auto.setCheckable(True)
        self.checkBox_auto.setChecked(False)

        self.horizontalLayout.addWidget(self.checkBox_auto)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.pushButton_close = QPushButton(MainWidget)
        self.pushButton_close.setObjectName(u"pushButton_close")
        self.pushButton_close.setGeometry(QRect(520, 110, 70, 40))
        self.pushButton_close.setStyleSheet(u"QPushButton{\n"
"border:3px solid #ffffff;\n"
"border-radius:20px;\n"
"padding:10px;\n"
"background-color:#00da3e;\n"
"image:url(\"D:/git/100dlswjd/memo/img/X.png\");\n"
"}\n"
"QPushButton:hover{\n"
"background-color:#00c538;\n"
"}\n"
"QPushButton:Pressed{\n"
"background-color:#00a72f;\n"
"}")
        self.frame_main.raise_()
        self.pushButton_show.raise_()
        self.label_move.raise_()
        self.pushButton_close.raise_()

        self.retranslateUi(MainWidget)

        self.tabWidget_memo.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(MainWidget)
    # setupUi

    def retranslateUi(self, MainWidget):
        MainWidget.setWindowTitle(QCoreApplication.translate("MainWidget", u"Form", None))
        self.pushButton_show.setText("")
        self.label_move.setText("")
        self.label_error.setText(QCoreApplication.translate("MainWidget", u"\ubc84\uadf8 \ubb38\uc758\ub294 \ub543\uc950\uc5d0\uac8c", None))
        self.checkBox_auto.setText(QCoreApplication.translate("MainWidget", u"\uc790\ub3d9 \ucd95\uc18c", None))
        self.pushButton_close.setText("")
    # retranslateUi
