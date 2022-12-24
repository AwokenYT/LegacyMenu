import subprocess
import os
import subprocess
from winreg import *

import winreg

def check_key_exists(key):
  try:
    winreg.OpenKey(winreg.HKEY_CURRENT_USER, key)
  except WindowsError:
    return False
  return True

key = r"Software\Classes\CLSID\{86ca1aa0-34aa-4e8b-a509-50c905bae2a2}"
if check_key_exists(key):
    print("Disabling Legacy Right Click Menu")
    subprocess.run(["reg.exe", "delete", "HKEY_CURRENT_USER\Software\Classes\CLSID\{86ca1aa0-34aa-4e8b-a509-50c905bae2a2}", "/f"])
else:
    print("Enabling Legacy Right Click Menu")
    subprocess.run(["reg.exe", "add", "HKEY_CURRENT_USER\Software\Classes\CLSID\{86ca1aa0-34aa-4e8b-a509-50c905bae2a2}\InprocServer32", "/f", "/ve"])


os.system("taskkill /F /IM explorer.exe & start explorer")


