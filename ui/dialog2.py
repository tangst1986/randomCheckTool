# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog2.ui'
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

class Ui_dialog2(object):
    def setupUi(self, dialog2):
        dialog2.setObjectName(_fromUtf8("dialog2"))
        dialog2.setEnabled(True)
        dialog2.resize(708, 439)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(dialog2.sizePolicy().hasHeightForWidth())
        dialog2.setSizePolicy(sizePolicy)
        dialog2.setMinimumSize(QtCore.QSize(0, 0))
        self.centralwidget = QtGui.QWidget(dialog2)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 60, 71, 41))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 130, 71, 41))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 210, 71, 41))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(40, 280, 71, 31))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.firstImPercent = QtGui.QTextEdit(self.centralwidget)
        self.firstImPercent.setGeometry(QtCore.QRect(130, 70, 91, 30))
        self.firstImPercent.setObjectName(_fromUtf8("firstImPercent"))
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(130, 20, 111, 41))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(280, 20, 111, 41))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.firstCoPercent = QtGui.QTextEdit(self.centralwidget)
        self.firstCoPercent.setGeometry(QtCore.QRect(280, 70, 91, 30))
        self.firstCoPercent.setObjectName(_fromUtf8("firstCoPercent"))
        self.secondImPercent = QtGui.QTextEdit(self.centralwidget)
        self.secondImPercent.setGeometry(QtCore.QRect(130, 140, 91, 30))
        self.secondImPercent.setObjectName(_fromUtf8("secondImPercent"))
        self.threeImPercent = QtGui.QTextEdit(self.centralwidget)
        self.threeImPercent.setGeometry(QtCore.QRect(130, 210, 91, 30))
        self.threeImPercent.setObjectName(_fromUtf8("threeImPercent"))
        self.fourImPercent = QtGui.QTextEdit(self.centralwidget)
        self.fourImPercent.setGeometry(QtCore.QRect(130, 280, 91, 30))
        self.fourImPercent.setObjectName(_fromUtf8("fourImPercent"))
        self.secondCoPercent = QtGui.QTextEdit(self.centralwidget)
        self.secondCoPercent.setGeometry(QtCore.QRect(280, 140, 91, 30))
        self.secondCoPercent.setObjectName(_fromUtf8("secondCoPercent"))
        self.threeCoPercent = QtGui.QTextEdit(self.centralwidget)
        self.threeCoPercent.setGeometry(QtCore.QRect(280, 210, 91, 30))
        self.threeCoPercent.setObjectName(_fromUtf8("threeCoPercent"))
        self.fourCoPercent = QtGui.QTextEdit(self.centralwidget)
        self.fourCoPercent.setGeometry(QtCore.QRect(280, 280, 91, 30))
        self.fourCoPercent.setObjectName(_fromUtf8("fourCoPercent"))
        self.exportFileBtn = QtGui.QPushButton(self.centralwidget)
        self.exportFileBtn.setGeometry(QtCore.QRect(240, 330, 251, 51))
        self.exportFileBtn.setStyleSheet(_fromUtf8("font: 75 16pt \"MS Shell Dlg 2\";"))
        self.exportFileBtn.setObjectName(_fromUtf8("exportFileBtn"))
        self.firstLotPercent = QtGui.QTextEdit(self.centralwidget)
        self.firstLotPercent.setGeometry(QtCore.QRect(490, 70, 111, 30))
        self.firstLotPercent.setObjectName(_fromUtf8("firstLotPercent"))
        self.secondLotPercent = QtGui.QTextEdit(self.centralwidget)
        self.secondLotPercent.setGeometry(QtCore.QRect(490, 140, 111, 30))
        self.secondLotPercent.setObjectName(_fromUtf8("secondLotPercent"))
        self.threeLotPercent = QtGui.QTextEdit(self.centralwidget)
        self.threeLotPercent.setGeometry(QtCore.QRect(490, 210, 111, 30))
        self.threeLotPercent.setObjectName(_fromUtf8("threeLotPercent"))
        self.fourLotPercent = QtGui.QTextEdit(self.centralwidget)
        self.fourLotPercent.setGeometry(QtCore.QRect(490, 280, 111, 30))
        self.fourLotPercent.setObjectName(_fromUtf8("fourLotPercent"))
        self.typeComBox = QtGui.QComboBox(self.centralwidget)
        self.typeComBox.setGeometry(QtCore.QRect(430, 30, 240, 31))
        self.typeComBox.setStyleSheet(_fromUtf8("font: 75 10pt \"MS Shell Dlg 2\";"))
        self.typeComBox.setObjectName(_fromUtf8("typeComBox"))
        dialog2.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(dialog2)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 708, 26))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        dialog2.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(dialog2)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        dialog2.setStatusBar(self.statusbar)

        self.retranslateUi(dialog2)
        QtCore.QMetaObject.connectSlotsByName(dialog2)

    def retranslateUi(self, dialog2):
        dialog2.setWindowTitle(_translate("dialog2", "消防监督抽查系统", None))
        self.label.setText(_translate("dialog2", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">第一季度</span></p></body></html>", None))
        self.label_2.setText(_translate("dialog2", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">第二季度</span></p></body></html>", None))
        self.label_3.setText(_translate("dialog2", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">第三季度</span></p></body></html>", None))
        self.label_4.setText(_translate("dialog2", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">第四季度</span></p></body></html>", None))
        self.label_5.setText(_translate("dialog2", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">重点单位(%)</span></p></body></html>", None))
        self.label_6.setText(_translate("dialog2", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">一般单位(%)</span></p></body></html>", None))
        self.exportFileBtn.setText(_translate("dialog2", "生成数据", None))

