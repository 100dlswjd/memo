# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'memo_widget.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QSizePolicy,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_memo(object):
    def setupUi(self, memo):
        if not memo.objectName():
            memo.setObjectName(u"memo")
        memo.resize(469, 299)
        memo.setStyleSheet(u"QWidget{\n"
"border:0px;\n"
"}")
        self.verticalLayout = QVBoxLayout(memo)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_memo = QFrame(memo)
        self.frame_memo.setObjectName(u"frame_memo")
        self.frame_memo.setStyleSheet(u"QFrame{\n"
"border:none;\n"
"\n"
"}")
        self.frame_memo.setFrameShape(QFrame.StyledPanel)
        self.frame_memo.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_memo)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.textEdit_memo = QTextEdit(self.frame_memo)
        self.textEdit_memo.setObjectName(u"textEdit_memo")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit_memo.sizePolicy().hasHeightForWidth())
        self.textEdit_memo.setSizePolicy(sizePolicy)
        self.textEdit_memo.setStyleSheet(u"QTextEdit{\n"
"border:3px solid #ffffff;\n"
"border-radius:16px;\n"
"background-color:#ffffff;\n"
"padding:5px 10px 5px 10px;\n"
"}")

        self.horizontalLayout_2.addWidget(self.textEdit_memo)


        self.verticalLayout.addWidget(self.frame_memo)


        self.retranslateUi(memo)

        QMetaObject.connectSlotsByName(memo)
    # setupUi

    def retranslateUi(self, memo):
        memo.setWindowTitle(QCoreApplication.translate("memo", u"Form", None))
    # retranslateUi

