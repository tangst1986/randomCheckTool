# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog3.ui'
#
# Created: Wed Sep 23 13:32:43 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QMainWindow, QIcon, QMessageBox, QFileDialog
import os
from PyQt4.QtCore import QTextCodec
import shutil
from business import cleanup
import subprocess


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

class Ui_dialog3(QMainWindow):
    def __init__(self, excel_file):
        super(Ui_dialog3,self).__init__()
        MainWindow = self
        self.setupUi(MainWindow)
        
        self.excel_file = excel_file
        self.export_path = r''
        self.setBg()
        self.setIcon()
        self.setConnectBtn()
    
    def setupUi(self, dialog3):
        dialog3.setObjectName(_fromUtf8("dialog3"))
        dialog3.resize(739, 377)
        self.setFixedSize(739, 377)
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
        
    def setBg(self):
        pl = QtGui.QPalette(self)
        pic_path = os.path.join(os.getcwd(), r'./resource/bg3.png')
        brush = QtGui.QBrush(QtGui.QPixmap(pic_path))
        
        pl.setBrush(QtGui.QPalette.Background, brush)
        self.setPalette(pl)
        self.setAutoFillBackground(True)
    
    def setIcon(self):
        self.setWindowIcon(QIcon('./resource/logo.png'))
    
    def setConnectBtn(self):
        self.firstBtn.clicked.connect(self.clickFirstBtn)
        self.secondBtn.clicked.connect(self.clickSecondBtn)
        self.thirdBtn.clicked.connect(self.clickThirdBtn)
        self.fourthBtn.clicked.connect(self.clickFourthBtn)
        self.exportBtn.clicked.connect(self.clickExportBtn)
        
    def clickFirstBtn(self):
        self.clickBtn(1)
    
    def clickSecondBtn(self):
        self.clickBtn(2)
        
    def clickThirdBtn(self):
        self.clickBtn(3)
        
    def clickFourthBtn(self):
        self.clickBtn(4)
        
    def clickBtn(self, quarter_index):
        file_dir = os.path.dirname(self.excel_file)
        file_path = os.path.join(file_dir, '%d.csv' % quarter_index)
        try:
            subprocess.check_output(file_path, shell=True)
        except subprocess.CalledProcessError as e:
            QMessageBox.about(self, self.tr('错误'), self.tr('%s' % e.output))
    
    def clickExportBtn(self):
        export_dir = QFileDialog.getExistingDirectory(self, self.tr('请选择保存路径'), '/')
        src_file = os.path.join(os.path.dirname(self.excel_file), 'result.xls')
        
        if export_dir == r'':
            return
        
        export_dir = str(export_dir.toUtf8()).decode('utf-8').encode('gb2312')
        self.export_path = export_dir
        
        if os.path.abspath(export_dir) == os.path.abspath(os.path.dirname(self.excel_file)):
            QMessageBox.about(self, self.tr('提示'), self.tr('导出成功'))
            return
        
        if os.path.exists(os.path.join(export_dir, 'result.xls')):
            os.remove(os.path.join(export_dir, 'result.xls'))
        
        try:
            shutil.move(src_file, export_dir)
        except Exception as e:
            QMessageBox.about(self, self.tr('提示'), self.tr('%s' % e))
            return
       
        QMessageBox.about(self, self.tr('提示'), self.tr('导出成功'))
        
    def closeEvent(self, *args, **kwargs):
        if os.path.abspath(self.export_path) == os.path.abspath(os.path.dirname(self.excel_file)):
            file_dir = os.path.dirname(self.excel_file)
            for ele in os.listdir(file_dir):
                if ele == '1.csv':
                    os.remove(os.path.join(file_dir, ele))
                elif ele == '2.csv':
                    os.remove(os.path.join(file_dir, ele))
                elif ele == '3.csv':
                    os.remove(os.path.join(file_dir, ele))
                elif ele == '4.csv':
                    os.remove(os.path.join(file_dir, ele))       
        else:
            cleanup(os.path.dirname(self.excel_file))
        return