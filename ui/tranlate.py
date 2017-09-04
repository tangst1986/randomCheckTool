'''
@author: m1tang
'''
import os

if __name__ == '__main__':
    cmd = r'pyuic4 -o dialog1.py dialog1.ui'
    os.system(cmd)
    
    cmd = r'pyuic4 -o dialog2.py dialog2.ui'
    os.system(cmd)
    
    cmd = r'pyuic4 -o dialog3.py dialog3.ui'
    os.system(cmd)    
