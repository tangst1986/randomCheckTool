import py2exe
from distutils.core import setup

setup(windows = [{"script" : "start.py", "icon_resources" : [(1, './resource/myico.ico')]}],
      options = { "py2exe":{"compressed" : 1, "optimize" : 2, "bundle_files" : 1, "includes":["sip"]}},
      zipfile = None,
      data_files = [("resource", ["./resource/bg.png", "./resource/fire.swf", "./resource/bg2.png", "./resource/bg3.png", "./resource/logo.png"])]
      )