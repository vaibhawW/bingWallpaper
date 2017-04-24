import os
import shutil
#making the file
f=open("main.py.desktop","w+")
string="""[Desktop Entry]
Type=Application
Exec=python """+os.getcwd()+"""/main.py
Hidden=false
NoDisplay=false
X-GNOME-Autostart-enabled=true
Name[en_IN]=bingWallpaper
Name=bingWallpaper
Comment[en_IN]=sets desktop wallpaper
Comment=sets desktop wallpaper"""
f.write(string)
f.close()

#finding the startup location
dest=os.popen("echo $HOME").read()[:-1]+"/.config/autostart/main.py.desktop"

#copying startup file
shutil.copyfile("main.py.desktop",dest)

#deleting temp files
os.remove("main.py.desktop")
