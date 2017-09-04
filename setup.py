'''
@author: m1tang
'''
import os
import subprocess
import shutil

base_path = os.getcwd()

gui_dir = os.path.join(base_path, 'gui_exe')


def clean_build_dir():
    if os.path.exists(gui_dir):
        shutil.rmtree(gui_dir)
        
def mk_build_dir():
    if not os.path.exists(gui_dir):
        os.mkdir(gui_dir)

def build_exe(commond):
    try:
        subprocess.check_output(commond)
    except subprocess.CalledProcessError as e:
        print e.output
        print "err: build failed %s" % commond
        return False
    
    return True

def build_gui_exe():
    gui_exe_build = r'python gui_setup.py py2exe'
        
    if not build_exe(gui_exe_build):
        return False
    
    shutil.move('dist', gui_dir)
    return True

if __name__ == '__main__':
    clean_build_dir()
    mk_build_dir()
    build_gui_exe()