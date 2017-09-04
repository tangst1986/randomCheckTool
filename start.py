'''
@author: m1tang
'''
import sys
from PyQt4.QtGui import QApplication
from mainWindow import Ui_MainWindow
import pythoncom
import pyHook
from PyQt4.QtCore import QThread
import wx
from wx.lib.flashwin_old import FlashWindow
import os

class myThread(QThread):
    def __init__(self, app):
        super(myThread, self).__init__()
        self.app = app

    def onMouseEvent(self, event):
        self.app.ExitMainLoop()
        self.terminate()
        return True
    
    def run(self):
        hm = pyHook.HookManager()
        hm.MouseAllButtonsDown = self.onMouseEvent
        hm.HookMouse()
        pythoncom.PumpMessages() 
        return


class CGui(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, 101, "fire", size = (800, 600), style = wx.FRAME_SHAPED)
        self.flash = FlashWindow(self) 
        
        swf_path = os.path.join(os.getcwd(), 'resource', 'fire.swf')
        try:
            self.flash.LoadMovie(0, swf_path) 
        except Exception as e:
            print e
            return
        
        self.flash.SetSize((800, 600))
        self.flash._set_Loop(False)

def startGui():
    try:
        app = QApplication(sys.argv)
        ui_window = Ui_MainWindow()
        ui_window.show()
    
        app.exec_()
    except Exception as e:
        print e

if __name__ == '__main__':
    app1 = wx.App()
    test = CGui()
    test.Center()
    test.Show(True)
    my_thread = myThread(app1)
    my_thread.start()
    app1.MainLoop()
    test.Hide()
    startGui()
