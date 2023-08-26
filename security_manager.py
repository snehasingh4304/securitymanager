import subprocess
import pyautogui
import time
import os
subprocess.run("reg add HKLM\SYSTEM\CurrentControlSet\Services\USBSTOR /v Start /t REG_DWORD /d 4 /f", shell=True)
pyautogui.hotkey("win", "s")
time.sleep(1)
pyautogui.write("Bluetooth settings")
time.sleep(1)
pyautogui.press("enter")
websites_to_block = ["example.com", "example2.com"]
with open("C:\\Windows\\System32\\drivers\\etc\\hosts", "a") as hosts_file:
    for website in websites_to_block:
        hosts_file.write(f"127.0.0.1 {website}\n")
if os.name != 'nt' or os.getuid() != 0:
    print("This script requires administrative privileges.")
    exit(1)
reg_content = """
Windows Registry Editor Version 5.00

[HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\System]
"DisableCMD"=dword:00000002
"""
reg_file_path = "disable_cmd.reg"
with open(reg_file_path, "w") as reg_file:
    reg_file.write(reg_content)
os.system(f'reg import "{reg_file_path}"')

print("Command Prompt has been disabled.")
os.remove(reg_file_path)
