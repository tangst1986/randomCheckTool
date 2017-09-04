# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created: Mon Sep 14 10:18:34 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QMainWindow, QFileDialog, QIcon, QMessageBox,\
    QGraphicsOpacityEffect
from PyQt4.QtCore import QTextCodec
import os
from dialog2 import Ui_dialog2
import subprocess

excel_file = r''

QTextCodec.setCodecForTr(QTextCodec.codecForName("utf-8")) 
QTextCodec.setCodecForCStrings(QTextCodec.codecForName("GBK"))
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

class Ui_MainWindow(QMainWindow):
    def __init__(self):
        super(Ui_MainWindow,self).__init__()
        MainWindow = self
        
        self.setBgPic()
        self.setupUi(MainWindow)
 
        self.excel_file = r''
        
        self.setIcon()
        self.setBtnConnect()
        
    def setupUi(self, window1):
        window1.setObjectName(_fromUtf8("window1"))
        window1.resize(734, 422)
        self.setFixedSize(734, 422)
        self.centralwidget = QtGui.QWidget(window1)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
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
        self.menubar.setGeometry(QtCore.QRect(0, 0, 801, 26))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        window1.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(window1)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        window1.setStatusBar(self.statusbar)

        self.retranslateUi(window1)
        QtCore.QMetaObject.connectSlotsByName(window1)

    def retranslateUi(self, window1):
        window1.setWindowTitle(_translate("window1", "消防监督抽查系统", None))
        self.importBtn.setText(_translate("window1", "导入数据", None))
        self.selectBtn.setText(_translate("window1", "编辑数据", None))
        self.startBtn.setText(_translate("window1", "开始抽查", None))
    
    def setBgPic(self):
        pl = QtGui.QPalette(self)
        pic_path = os.path.join(os.getcwd(), r'./resource/bg.png')
        brush = QtGui.QBrush(QtGui.QPixmap(pic_path))
        
        pl.setBrush(QtGui.QPalette.Background, brush)
        self.setPalette(pl)
        self.setAutoFillBackground(True)
    
        self.opacity = QGraphicsOpacityEffect()
        self.opacity.setOpacity(0.5)
        self.setGraphicsEffect(self.opacity)
        
    def setIcon(self):
        self.setWindowIcon(QIcon('./resource/logo.png'))
        
    def setBtnConnect(self):
        self.importBtn.clicked.connect(self.clickImportBtn)
        self.selectBtn.clicked.connect(self.clickSelectBtn)
        self.startBtn.clicked.connect(self.clickStartBtn)
     
    def clickImportBtn(self):
        self.excel_file = QFileDialog.getOpenFileName(None, self.tr('请选择导入数据'), r'/')
        if self.excel_file == r'':
            return
        QMessageBox.about(self, self.tr('导入文件成功'), self.tr(self.excel_file.toUtf8()))
        self.excel_file = str(self.excel_file.toUtf8()).decode('utf-8').encode('gb2312')
        
    def clickSelectBtn(self):
        if self.excel_file == r'':
            QMessageBox.about(self, self.tr('提示'), self.tr('你还没有导入数据文件'))
            return 
        try:
            subprocess.check_output(self.excel_file, shell=True)
        except subprocess.CalledProcessError as e:
            QMessageBox.about(self, self.tr('提示'), self.tr('%s' % e.output))
            
    def clickStartBtn(self):
        if not self.excel_file or self.excel_file == r'':
            QMessageBox.about(self, self.tr('提示'), self.tr('你还没有导入数据文件'))
            return
                    
        self.dlg2 = Ui_dialog2(self.excel_file)
        self.dlg2.show()


