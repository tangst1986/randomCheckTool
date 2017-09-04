'''
@author: m1tang
'''
import os
import wx
from wx.lib.flashwin_old import FlashWindow
from PyQt4.QtCore import QThread
import pythoncom
import pyHook

class myThread(QThread):
    def __init__(self, app):
        super(myThread, self).__init__()
        self.app = app
    def onMouseEvent(self, event):
        print event.WindowName
        print event.Position
        
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
    
if __name__ == '__main__':
    app = wx.App()
    test = CGui()
    test.Center()
    test.Show(True)
    my_thread = myThread(app)
    my_thread.start()
    app.MainLoop()
    