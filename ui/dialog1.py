# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog1.ui'
#
# Created: Thu Sep 24 21:06:59 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_window1(object):
    def setupUi(self, window1):
        window1.setObjectName(_fromUtf8("window1"))
        window1.resize(734, 422)
        self.centralwidget = QtGui.QWidget(window1)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(290, 80, 421, 131))
        self.label.setObjectName(_fromUtf8("label"))
        self.importBtn = QtGui.QPushButton(self.centralwidget)
        self.importBtn.setGeometry(QtCore.QRect(320, 240, 101, 51))
        self.importBtn.setStyleSheet(_fromUtf8("font: 10pt \"MS Shell Dlg 2\";"))
        self.importBtn.setObjectName(_fromUtf8("importBtn"))
        self.selectBtn = QtGui.QPushButton(self.centralwidget)
        self.selectBtn.setGeometry(QtCore.QRect(460, 240, 101, 51))
        self.selectBtn.setStyleSheet(_fromUtf8("font: 10pt \"MS Shell Dlg 2\";"))
        self.selectBtn.setObjectName(_fromUtf8("selectBtn"))
        self.startBtn = QtGui.QPushButton(self.centralwidget)
        self.startBtn.setGeometry(QtCore.QRect(600, 240, 101, 51))
        self.startBtn.setStyleSheet(_fromUtf8("font: 10pt \"MS Shell Dlg 2\";"))
        self.startBtn.setObjectName(_fromUtf8("startBtn"))
        window1.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(window1)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 734, 26))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        window1.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(window1)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        window1.setStatusBar(self.statusbar)

        self.retranslateUi(window1)
        QtCore.QMetaObject.connectSlotsByName(window1)

    def retranslateUi(self, window1):
        window1.setWindowTitle(_translate("window1", "消防监督抽查系统", None))
        self.label.setText(_translate("window1", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:600;\">消防监督抽查系统</span></p></body></html>", None))
        self.importBtn.setText(_translate("window1", "导入数据", None))
        self.selectBtn.setText(_translate("window1", "编辑数据", None))
        self.startBtn.setText(_translate("window1", "开始抽查", None))

