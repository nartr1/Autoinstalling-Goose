#! /usr/bin/python3
import urllib.request
import base64
from io import BytesIO
import zipfile
import subprocess
import platform
import os

cwd = os.getcwd()

def run_win_cmd(cmd):
    result = []
    process = subprocess.Popen(cmd,
                               shell=True,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
    for line in process.stdout:
        result.append(line)
    errcode = process.returncode
    for line in result:
        print(line)
    if errcode is not None:
        raise Exception('cmd %s failed, see above for details', cmd)


if "Windows" in platform.platform():
	is_windows = True
else:
	is_windows = False


goose_url = "https://raw.githubusercontent.com/nartr1/Autoinstalling-Goose/master/goose64"
page = urllib.request.urlopen(goose_url)

#print(page.read())

files_needed_zipped = base64.b64decode(page.read())

f = open(".hidden_goose", "wb")

f.write(files_needed_zipped)

with zipfile.ZipFile(".hidden_goose", 'r') as zip_ref:
	zip_ref.extractall(".")

if is_windows:
	run_win_cmd("DesktopGoose v0.3/GooseDesktop.exe")
else:
	#subprocess.run("wine "+cwd+"/DesktopGoose\ v0.3/GooseDesktop.exe")
	os.system("wine "+cwd+"/DesktopGoose\ v0.3/GooseDesktop.exe")