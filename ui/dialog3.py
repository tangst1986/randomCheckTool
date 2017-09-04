# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog3.ui'
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

class Ui_dialog3(object):
    def setupUi(self, dialog3):
        dialog3.setObjectName(_fromUtf8("dialog3"))
        dialog3.resize(739, 377)
        self.centralwidget = QtGui.QWidget(dialog3)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.firstBtn = QtGui.QPushButton(self.centralwidget)
        self.firstBtn.setGeometry(QtCore.QRect(300, 110, 81, 41))
        self.firstBtn.setStyleSheet(_fromUtf8("font: 10pt \"微软雅黑\";"))
        self.firstBtn.setObjectName(_fromUtf8("firstBtn"))
        self.secondBtn = QtGui.QPushButton(self.centralwidget)
        self.secondBtn.setGeometry(QtCore.QRect(420, 110, 81, 41))
        self.secondBtn.setStyleSheet(_fromUtf8("font: 10pt \"微软雅黑\";"))
        self.secondBtn.setObjectName(_fromUtf8("secondBtn"))
        self.thirdBtn = QtGui.QPushButton(self.centralwidget)
        self.thirdBtn.setGeometry(QtCore.QRect(530, 110, 81, 41))
        self.thirdBtn.setStyleSheet(_fromUtf8("font: 10pt \"微软雅黑\";"))
        self.thirdBtn.setObjectName(_fromUtf8("thirdBtn"))
        self.fourthBtn = QtGui.QPushButton(self.centralwidget)
        self.fourthBtn.setGeometry(QtCore.QRect(640, 110, 81, 41))
        self.fourthBtn.setStyleSheet(_fromUtf8("font: 10pt \"微软雅黑\";"))
        self.fourthBtn.setObjectName(_fromUtf8("fourthBtn"))
        self.exportBtn = QtGui.QPushButton(self.centralwidget)
        self.exportBtn.setGeometry(QtCore.QRect(440, 180, 131, 41))
        self.exportBtn.setStyleSheet(_fromUtf8("font: 10pt \"微软雅黑\";"))
        self.exportBtn.setObjectName(_fromUtf8("exportBtn"))
        dialog3.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(dialog3)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 739, 26))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        dialog3.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(dialog3)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        dialog3.setStatusBar(self.statusbar)

        self.retranslateUi(dialog3)
        QtCore.QMetaObject.connectSlotsByName(dialog3)

    def retranslateUi(self, dialog3):
        dialog3.setWindowTitle(_translate("dialog3", "消防监督抽查系统", None))
        self.firstBtn.setText(_translate("dialog3", "第一季度", None))
        self.secondBtn.setText(_translate("dialog3", "第二季度", None))
        self.thirdBtn.setText(_translate("dialog3", "第三季度", None))
        self.fourthBtn.setText(_translate("dialog3", "第四季度", None))
        self.exportBtn.setText(_translate("dialog3", "导出数据", None))

