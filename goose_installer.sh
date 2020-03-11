#! /bin/bash

#apt install wine winetricks -y

cat goose64 | base64 -d >> goose_zip && unzip goose_zip && rm -rf goose_zip
wine DesktopGoose\ v0.3/GooseDesktop.exe
#rm -rf DesktopGoose\ v0.3/